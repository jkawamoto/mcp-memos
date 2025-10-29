import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Inbox(_message.Message):
    __slots__ = ("name", "sender", "receiver", "status", "create_time", "type", "activity_id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[Inbox.Status]
        UNREAD: _ClassVar[Inbox.Status]
        ARCHIVED: _ClassVar[Inbox.Status]
    STATUS_UNSPECIFIED: Inbox.Status
    UNREAD: Inbox.Status
    ARCHIVED: Inbox.Status
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Inbox.Type]
        MEMO_COMMENT: _ClassVar[Inbox.Type]
        VERSION_UPDATE: _ClassVar[Inbox.Type]
    TYPE_UNSPECIFIED: Inbox.Type
    MEMO_COMMENT: Inbox.Type
    VERSION_UPDATE: Inbox.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    sender: str
    receiver: str
    status: Inbox.Status
    create_time: _timestamp_pb2.Timestamp
    type: Inbox.Type
    activity_id: int
    def __init__(self, name: _Optional[str] = ..., sender: _Optional[str] = ..., receiver: _Optional[str] = ..., status: _Optional[_Union[Inbox.Status, str]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[_Union[Inbox.Type, str]] = ..., activity_id: _Optional[int] = ...) -> None: ...

class ListInboxesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListInboxesResponse(_message.Message):
    __slots__ = ("inboxes", "next_page_token", "total_size")
    INBOXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    inboxes: _containers.RepeatedCompositeFieldContainer[Inbox]
    next_page_token: str
    total_size: int
    def __init__(self, inboxes: _Optional[_Iterable[_Union[Inbox, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateInboxRequest(_message.Message):
    __slots__ = ("inbox", "update_mask", "allow_missing")
    INBOX_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    inbox: Inbox
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    def __init__(self, inbox: _Optional[_Union[Inbox, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class DeleteInboxRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
