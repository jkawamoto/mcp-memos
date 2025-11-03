#  client.py
#
#  Copyright (c) 2025 Junpei Kawamoto
#
#  This software is released under the MIT License.
#
#  http://opensource.org/licenses/mit-license.php
from collections.abc import Awaitable
from contextlib import AbstractAsyncContextManager
from types import TracebackType
from typing import Callable, Union, Self, TypeVar

from grpc.aio import UnaryUnaryClientInterceptor, ClientCallDetails, UnaryUnaryCall, insecure_channel, Channel, Metadata

from .api.v1.attachment_service_pb2 import CreateAttachmentRequest, Attachment
from .api.v1.attachment_service_pb2_grpc import AttachmentServiceStub
from .api.v1.common_pb2 import State
from .api.v1.memo_service_pb2 import Memo, Visibility, CreateMemoRequest, SetMemoAttachmentsRequest, GetMemoRequest
from .api.v1.memo_service_pb2_grpc import MemoServiceStub

RequestType = TypeVar("RequestType")
ResponseType = TypeVar("ResponseType")


class AuthInterceptor(UnaryUnaryClientInterceptor):
    token: str

    def __init__(self, token: str) -> None:
        self.token = token

    async def intercept_unary_unary(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], Awaitable[UnaryUnaryCall[RequestType, ResponseType]]],
        client_call_details: ClientCallDetails,
        request: RequestType,
    ) -> Union[UnaryUnaryCall, ResponseType]:
        if client_call_details.metadata is None:
            metadata = Metadata()
            client_call_details = client_call_details._replace(metadata=metadata)  # type: ignore
        else:
            metadata = client_call_details.metadata

        metadata.add("authorization", f"Bearer {self.token}")
        return await continuation(client_call_details, request)


class Memos(AbstractAsyncContextManager):
    _channel: Channel
    _memo_service: MemoServiceStub
    _attachment_service: AttachmentServiceStub

    def __init__(self, target: str, token: str) -> None:
        self._channel = insecure_channel(target, interceptors=[AuthInterceptor(token)])
        self._memo_service = MemoServiceStub(self._channel)
        self._attachment_service = AttachmentServiceStub(self._channel)

    async def __aenter__(self) -> Self:
        await self._channel.channel_ready()
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None, /
    ) -> None:
        await self.close()

    async def close(self) -> None:
        await self._channel.close()

    async def create_memo(self, content: str, visibility: Visibility = Visibility.VISIBILITY_UNSPECIFIED) -> Memo:
        """Create a memo."""
        memo: Memo = await self._memo_service.CreateMemo(
            CreateMemoRequest(
                memo=Memo(
                    state=State.STATE_UNSPECIFIED,
                    content=content,
                    visibility=visibility,
                )
            )
        )
        return memo

    async def attach_file(self, memo_name: str, filename: str, content: bytes, mime_type: str | None = None) -> None:
        """Attach a file to a memo."""
        attachment: Attachment = await self._attachment_service.CreateAttachment(
            CreateAttachmentRequest(
                attachment=Attachment(
                    filename=filename,
                    content=content,
                    type=mime_type or "application/octet-stream",
                )
            )
        )
        memo: Memo = await self._memo_service.GetMemo(GetMemoRequest(name=memo_name))
        memo.attachments.append(attachment)
        await self._memo_service.SetMemoAttachments(
            SetMemoAttachmentsRequest(
                name=memo.name,
                attachments=memo.attachments,
            )
        )
