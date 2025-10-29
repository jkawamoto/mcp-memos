import datetime

from mcp_memos.api.v1 import user_service_pb2 as _user_service_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCurrentSessionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentSessionResponse(_message.Message):
    __slots__ = ("user", "last_accessed_at")
    USER_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_AT_FIELD_NUMBER: _ClassVar[int]
    user: _user_service_pb2.User
    last_accessed_at: _timestamp_pb2.Timestamp
    def __init__(self, user: _Optional[_Union[_user_service_pb2.User, _Mapping]] = ..., last_accessed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("password_credentials", "sso_credentials")
    class PasswordCredentials(_message.Message):
        __slots__ = ("username", "password")
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        username: str
        password: str
        def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
    class SSOCredentials(_message.Message):
        __slots__ = ("idp_id", "code", "redirect_uri")
        IDP_ID_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
        idp_id: int
        code: str
        redirect_uri: str
        def __init__(self, idp_id: _Optional[int] = ..., code: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...
    PASSWORD_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SSO_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    password_credentials: CreateSessionRequest.PasswordCredentials
    sso_credentials: CreateSessionRequest.SSOCredentials
    def __init__(self, password_credentials: _Optional[_Union[CreateSessionRequest.PasswordCredentials, _Mapping]] = ..., sso_credentials: _Optional[_Union[CreateSessionRequest.SSOCredentials, _Mapping]] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("user", "last_accessed_at")
    USER_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_AT_FIELD_NUMBER: _ClassVar[int]
    user: _user_service_pb2.User
    last_accessed_at: _timestamp_pb2.Timestamp
    def __init__(self, user: _Optional[_Union[_user_service_pb2.User, _Mapping]] = ..., last_accessed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
