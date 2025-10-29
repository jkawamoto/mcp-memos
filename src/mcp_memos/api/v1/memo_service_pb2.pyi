import datetime

from mcp_memos.api.v1 import attachment_service_pb2 as _attachment_service_pb2
from mcp_memos.api.v1 import common_pb2 as _common_pb2
from mcp_memos.api.v1 import markdown_service_pb2 as _markdown_service_pb2
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

class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VISIBILITY_UNSPECIFIED: _ClassVar[Visibility]
    PRIVATE: _ClassVar[Visibility]
    PROTECTED: _ClassVar[Visibility]
    PUBLIC: _ClassVar[Visibility]
VISIBILITY_UNSPECIFIED: Visibility
PRIVATE: Visibility
PROTECTED: Visibility
PUBLIC: Visibility

class Reaction(_message.Message):
    __slots__ = ("name", "creator", "content_id", "reaction_type", "create_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    creator: str
    content_id: str
    reaction_type: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., creator: _Optional[str] = ..., content_id: _Optional[str] = ..., reaction_type: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Memo(_message.Message):
    __slots__ = ("name", "state", "creator", "create_time", "update_time", "display_time", "content", "nodes", "visibility", "tags", "pinned", "attachments", "relations", "reactions", "property", "parent", "snippet", "location")
    class Property(_message.Message):
        __slots__ = ("has_link", "has_task_list", "has_code", "has_incomplete_tasks")
        HAS_LINK_FIELD_NUMBER: _ClassVar[int]
        HAS_TASK_LIST_FIELD_NUMBER: _ClassVar[int]
        HAS_CODE_FIELD_NUMBER: _ClassVar[int]
        HAS_INCOMPLETE_TASKS_FIELD_NUMBER: _ClassVar[int]
        has_link: bool
        has_task_list: bool
        has_code: bool
        has_incomplete_tasks: bool
        def __init__(self, has_link: bool = ..., has_task_list: bool = ..., has_code: bool = ..., has_incomplete_tasks: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: _common_pb2.State
    creator: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_time: _timestamp_pb2.Timestamp
    content: str
    nodes: _containers.RepeatedCompositeFieldContainer[_markdown_service_pb2.Node]
    visibility: Visibility
    tags: _containers.RepeatedScalarFieldContainer[str]
    pinned: bool
    attachments: _containers.RepeatedCompositeFieldContainer[_attachment_service_pb2.Attachment]
    relations: _containers.RepeatedCompositeFieldContainer[MemoRelation]
    reactions: _containers.RepeatedCompositeFieldContainer[Reaction]
    property: Memo.Property
    parent: str
    snippet: str
    location: Location
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[_common_pb2.State, str]] = ..., creator: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., display_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., content: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[_markdown_service_pb2.Node, _Mapping]]] = ..., visibility: _Optional[_Union[Visibility, str]] = ..., tags: _Optional[_Iterable[str]] = ..., pinned: bool = ..., attachments: _Optional[_Iterable[_Union[_attachment_service_pb2.Attachment, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[MemoRelation, _Mapping]]] = ..., reactions: _Optional[_Iterable[_Union[Reaction, _Mapping]]] = ..., property: _Optional[_Union[Memo.Property, _Mapping]] = ..., parent: _Optional[str] = ..., snippet: _Optional[str] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("placeholder", "latitude", "longitude")
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    placeholder: str
    latitude: float
    longitude: float
    def __init__(self, placeholder: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class CreateMemoRequest(_message.Message):
    __slots__ = ("memo", "memo_id", "validate_only", "request_id")
    MEMO_FIELD_NUMBER: _ClassVar[int]
    MEMO_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    memo: Memo
    memo_id: str
    validate_only: bool
    request_id: str
    def __init__(self, memo: _Optional[_Union[Memo, _Mapping]] = ..., memo_id: _Optional[str] = ..., validate_only: bool = ..., request_id: _Optional[str] = ...) -> None: ...

class ListMemosRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "state", "order_by", "filter", "show_deleted")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    state: _common_pb2.State
    order_by: str
    filter: str
    show_deleted: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., state: _Optional[_Union[_common_pb2.State, str]] = ..., order_by: _Optional[str] = ..., filter: _Optional[str] = ..., show_deleted: bool = ...) -> None: ...

class ListMemosResponse(_message.Message):
    __slots__ = ("memos", "next_page_token", "total_size")
    MEMOS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    memos: _containers.RepeatedCompositeFieldContainer[Memo]
    next_page_token: str
    total_size: int
    def __init__(self, memos: _Optional[_Iterable[_Union[Memo, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class GetMemoRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateMemoRequest(_message.Message):
    __slots__ = ("memo", "update_mask", "allow_missing")
    MEMO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    memo: Memo
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    def __init__(self, memo: _Optional[_Union[Memo, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class DeleteMemoRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class RenameMemoTagRequest(_message.Message):
    __slots__ = ("parent", "old_tag", "new_tag")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OLD_TAG_FIELD_NUMBER: _ClassVar[int]
    NEW_TAG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    old_tag: str
    new_tag: str
    def __init__(self, parent: _Optional[str] = ..., old_tag: _Optional[str] = ..., new_tag: _Optional[str] = ...) -> None: ...

class DeleteMemoTagRequest(_message.Message):
    __slots__ = ("parent", "tag", "delete_related_memos")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    DELETE_RELATED_MEMOS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tag: str
    delete_related_memos: bool
    def __init__(self, parent: _Optional[str] = ..., tag: _Optional[str] = ..., delete_related_memos: bool = ...) -> None: ...

class SetMemoAttachmentsRequest(_message.Message):
    __slots__ = ("name", "attachments")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    attachments: _containers.RepeatedCompositeFieldContainer[_attachment_service_pb2.Attachment]
    def __init__(self, name: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[_attachment_service_pb2.Attachment, _Mapping]]] = ...) -> None: ...

class ListMemoAttachmentsRequest(_message.Message):
    __slots__ = ("name", "page_size", "page_token")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    def __init__(self, name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMemoAttachmentsResponse(_message.Message):
    __slots__ = ("attachments", "next_page_token", "total_size")
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    attachments: _containers.RepeatedCompositeFieldContainer[_attachment_service_pb2.Attachment]
    next_page_token: str
    total_size: int
    def __init__(self, attachments: _Optional[_Iterable[_Union[_attachment_service_pb2.Attachment, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class MemoRelation(_message.Message):
    __slots__ = ("memo", "related_memo", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[MemoRelation.Type]
        REFERENCE: _ClassVar[MemoRelation.Type]
        COMMENT: _ClassVar[MemoRelation.Type]
    TYPE_UNSPECIFIED: MemoRelation.Type
    REFERENCE: MemoRelation.Type
    COMMENT: MemoRelation.Type
    class Memo(_message.Message):
        __slots__ = ("name", "snippet")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SNIPPET_FIELD_NUMBER: _ClassVar[int]
        name: str
        snippet: str
        def __init__(self, name: _Optional[str] = ..., snippet: _Optional[str] = ...) -> None: ...
    MEMO_FIELD_NUMBER: _ClassVar[int]
    RELATED_MEMO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    memo: MemoRelation.Memo
    related_memo: MemoRelation.Memo
    type: MemoRelation.Type
    def __init__(self, memo: _Optional[_Union[MemoRelation.Memo, _Mapping]] = ..., related_memo: _Optional[_Union[MemoRelation.Memo, _Mapping]] = ..., type: _Optional[_Union[MemoRelation.Type, str]] = ...) -> None: ...

class SetMemoRelationsRequest(_message.Message):
    __slots__ = ("name", "relations")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    relations: _containers.RepeatedCompositeFieldContainer[MemoRelation]
    def __init__(self, name: _Optional[str] = ..., relations: _Optional[_Iterable[_Union[MemoRelation, _Mapping]]] = ...) -> None: ...

class ListMemoRelationsRequest(_message.Message):
    __slots__ = ("name", "page_size", "page_token")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    def __init__(self, name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMemoRelationsResponse(_message.Message):
    __slots__ = ("relations", "next_page_token", "total_size")
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    relations: _containers.RepeatedCompositeFieldContainer[MemoRelation]
    next_page_token: str
    total_size: int
    def __init__(self, relations: _Optional[_Iterable[_Union[MemoRelation, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class CreateMemoCommentRequest(_message.Message):
    __slots__ = ("name", "comment", "comment_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    comment: Memo
    comment_id: str
    def __init__(self, name: _Optional[str] = ..., comment: _Optional[_Union[Memo, _Mapping]] = ..., comment_id: _Optional[str] = ...) -> None: ...

class ListMemoCommentsRequest(_message.Message):
    __slots__ = ("name", "page_size", "page_token", "order_by")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    order_by: str
    def __init__(self, name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListMemoCommentsResponse(_message.Message):
    __slots__ = ("memos", "next_page_token", "total_size")
    MEMOS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    memos: _containers.RepeatedCompositeFieldContainer[Memo]
    next_page_token: str
    total_size: int
    def __init__(self, memos: _Optional[_Iterable[_Union[Memo, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class ListMemoReactionsRequest(_message.Message):
    __slots__ = ("name", "page_size", "page_token")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    def __init__(self, name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMemoReactionsResponse(_message.Message):
    __slots__ = ("reactions", "next_page_token", "total_size")
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    reactions: _containers.RepeatedCompositeFieldContainer[Reaction]
    next_page_token: str
    total_size: int
    def __init__(self, reactions: _Optional[_Iterable[_Union[Reaction, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpsertMemoReactionRequest(_message.Message):
    __slots__ = ("name", "reaction")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    reaction: Reaction
    def __init__(self, name: _Optional[str] = ..., reaction: _Optional[_Union[Reaction, _Mapping]] = ...) -> None: ...

class DeleteMemoReactionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
