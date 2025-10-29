import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Activity(_message.Message):
    __slots__ = ("name", "creator", "type", "level", "create_time", "payload")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Activity.Type]
        MEMO_COMMENT: _ClassVar[Activity.Type]
        VERSION_UPDATE: _ClassVar[Activity.Type]
    TYPE_UNSPECIFIED: Activity.Type
    MEMO_COMMENT: Activity.Type
    VERSION_UPDATE: Activity.Type
    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LEVEL_UNSPECIFIED: _ClassVar[Activity.Level]
        INFO: _ClassVar[Activity.Level]
        WARN: _ClassVar[Activity.Level]
        ERROR: _ClassVar[Activity.Level]
    LEVEL_UNSPECIFIED: Activity.Level
    INFO: Activity.Level
    WARN: Activity.Level
    ERROR: Activity.Level
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    name: str
    creator: str
    type: Activity.Type
    level: Activity.Level
    create_time: _timestamp_pb2.Timestamp
    payload: ActivityPayload
    def __init__(self, name: _Optional[str] = ..., creator: _Optional[str] = ..., type: _Optional[_Union[Activity.Type, str]] = ..., level: _Optional[_Union[Activity.Level, str]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[ActivityPayload, _Mapping]] = ...) -> None: ...

class ActivityPayload(_message.Message):
    __slots__ = ("memo_comment",)
    MEMO_COMMENT_FIELD_NUMBER: _ClassVar[int]
    memo_comment: ActivityMemoCommentPayload
    def __init__(self, memo_comment: _Optional[_Union[ActivityMemoCommentPayload, _Mapping]] = ...) -> None: ...

class ActivityMemoCommentPayload(_message.Message):
    __slots__ = ("memo", "related_memo")
    MEMO_FIELD_NUMBER: _ClassVar[int]
    RELATED_MEMO_FIELD_NUMBER: _ClassVar[int]
    memo: str
    related_memo: str
    def __init__(self, memo: _Optional[str] = ..., related_memo: _Optional[str] = ...) -> None: ...

class ListActivitiesRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListActivitiesResponse(_message.Message):
    __slots__ = ("activities", "next_page_token")
    ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    activities: _containers.RepeatedCompositeFieldContainer[Activity]
    next_page_token: str
    def __init__(self, activities: _Optional[_Iterable[_Union[Activity, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetActivityRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
