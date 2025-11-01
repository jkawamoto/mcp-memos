#  client.py
#
#  Copyright (c) 2025 Junpei Kawamoto
#
#  This software is released under the MIT License.
#
#  http://opensource.org/licenses/mit-license.php

from contextlib import AbstractAsyncContextManager
from typing import Callable, Union, Self, TypeVar

from grpc.aio import UnaryUnaryClientInterceptor, ClientCallDetails, UnaryUnaryCall, insecure_channel, Channel

from .api.v1.common_pb2 import State
from .api.v1.memo_service_pb2 import Memo, Visibility, CreateMemoRequest
from .api.v1.memo_service_pb2_grpc import MemoServiceStub

RequestType = TypeVar("RequestType")
ResponseType = TypeVar("ResponseType")


class AuthInterceptor(UnaryUnaryClientInterceptor):
    def __init__(self, token):
        self.token = token

    async def intercept_unary_unary(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], UnaryUnaryCall],
        client_call_details: ClientCallDetails,
        request: RequestType,
    ) -> Union[UnaryUnaryCall, ResponseType]:
        metadata = list(client_call_details.metadata or [])
        metadata.append(("authorization", f"Bearer {self.token}"))

        client_call_details = client_call_details._replace(metadata=metadata)
        return await continuation(client_call_details, request)


class Memos(AbstractAsyncContextManager):
    _channel: Channel
    _memo_service: MemoServiceStub

    def __init__(self, target: str, token) -> None:
        self._channel = insecure_channel(target, interceptors=[AuthInterceptor(token)])
        self._memo_service = MemoServiceStub(self._channel)

    async def __aenter__(self) -> Self:
        await self._channel.channel_ready()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback, /):
        await self.close()

    async def close(self) -> None:
        await self._channel.close()

    async def create_memo(self, content: str, visibility: Visibility = Visibility.VISIBILITY_UNSPECIFIED) -> Memo:
        """Create a memo."""
        return await self._memo_service.CreateMemo(
            CreateMemoRequest(
                memo=Memo(
                    state=State.STATE_UNSPECIFIED,
                    content=content,
                    visibility=visibility,
                )
            )
        )
