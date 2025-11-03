#  mock.py
#
#  Copyright (c) 2025 Junpei Kawamoto
#
#  This software is released under the MIT License.
#
#  http://opensource.org/licenses/mit-license.php
import threading
from collections.abc import Iterator, Callable
from concurrent import futures
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, TypeVar
from urllib.parse import urlparse, parse_qs
from uuid import uuid1

import grpc
import pytest
from google.protobuf.empty_pb2 import Empty
from grpc import ServicerContext, StatusCode, HandlerCallDetails, RpcMethodHandler

from mcp_memos.api.v1.attachment_service_pb2 import CreateAttachmentRequest, Attachment
from mcp_memos.api.v1.attachment_service_pb2_grpc import (
    AttachmentServiceServicer,
    add_AttachmentServiceServicer_to_server,
)
from mcp_memos.api.v1.memo_service_pb2 import Memo, CreateMemoRequest, GetMemoRequest, SetMemoAttachmentsRequest
from mcp_memos.api.v1.memo_service_pb2_grpc import MemoServiceServicer, add_MemoServiceServicer_to_server

API_TOKEN = "test:token"

_AUTH_HEADER_KEY = "authorization"
_AUTH_HEADER_VALUE = f"Bearer {API_TOKEN}"

RequestType = TypeVar("RequestType")
ResponseType = TypeVar("ResponseType")


def _abort(_request: Any, context: ServicerContext) -> None:
    context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid signature")


class SignatureValidationInterceptor(grpc.ServerInterceptor):
    def intercept_service(
        self,
        continuation: Callable[[HandlerCallDetails], RpcMethodHandler | None],
        handler_call_details: HandlerCallDetails,
    ) -> RpcMethodHandler | None:
        expected_metadata = (_AUTH_HEADER_KEY, _AUTH_HEADER_VALUE)
        if expected_metadata in handler_call_details.invocation_metadata:
            return continuation(handler_call_details)
        else:
            return grpc.unary_unary_rpc_method_handler(_abort)  # type: ignore


class MockServicer(AttachmentServiceServicer, MemoServiceServicer):
    endpoint: str = "localhost:50051"
    memos: dict[str, Memo] = {}
    attachments: dict[str, Attachment] = {}

    def _get_memo(self, context: ServicerContext, name: str) -> Memo:
        if name not in self.memos:
            context.abort(StatusCode.NOT_FOUND, "Requested memo not found")
        return self.memos[name]

    def CreateMemo(self, request: CreateMemoRequest, context: ServicerContext) -> Memo:
        if not request.memo.name:
            request.memo.name = f"memos/{uuid1()}"

        self.memos[request.memo.name] = request.memo
        return request.memo

    def GetMemo(self, request: GetMemoRequest, context: ServicerContext) -> Memo:
        return self._get_memo(context, request.name)

    def SetMemoAttachments(self, request: SetMemoAttachmentsRequest, context: ServicerContext) -> Empty:
        memo = self._get_memo(context, request.name)
        memo.attachments.clear()  # type: ignore
        memo.attachments.extend(request.attachments)
        return Empty()

    def CreateAttachment(self, request: CreateAttachmentRequest, context: ServicerContext) -> Attachment:
        attachment = request.attachment
        if request.attachment_id:
            attachment.name = request.attachment_id
        else:
            attachment.name = f"attachments/{uuid1()}"
        self.attachments[attachment.name] = attachment
        return attachment


@pytest.fixture(scope="module")
def memos_server() -> Iterator[MockServicer]:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=[SignatureValidationInterceptor()])
    servicer = MockServicer()
    add_AttachmentServiceServicer_to_server(servicer, server)
    add_MemoServiceServicer_to_server(servicer, server)
    server.add_insecure_port(servicer.endpoint)
    server.start()
    yield servicer
    server.stop(3)


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        ctype = parse_qs(urlparse(self.path).query).get("ctype")[0]  # type: ignore

        self.send_response(200)
        self.send_header("Content-type", ctype)
        self.end_headers()

        response_text = "Hello, this is a test server!"
        self.wfile.write(response_text.encode("utf-8"))


class MockHTTPServer:
    host: str
    port: int
    server: HTTPServer | None
    thread: threading.Thread | None

    def __init__(self, host: str = "localhost", port: int = 18000) -> None:
        self.host = host
        self.port = port
        self.server = None
        self.thread = None

    def start(self) -> None:
        self.server = HTTPServer((self.host, self.port), SimpleHandler)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.daemon = True
        self.thread.start()

    def stop(self) -> None:
        if self.server:
            self.server.shutdown()
            if self.thread:
                self.thread.join()

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"


@pytest.fixture(scope="module")
def mock_http_server() -> Iterator[MockHTTPServer]:
    httpd = MockHTTPServer()
    httpd.start()
    yield httpd
    httpd.stop()
