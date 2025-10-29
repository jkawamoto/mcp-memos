from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Shortcut(_message.Message):
    __slots__ = ("name", "title", "filter")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    filter: str
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListShortcutsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListShortcutsResponse(_message.Message):
    __slots__ = ("shortcuts",)
    SHORTCUTS_FIELD_NUMBER: _ClassVar[int]
    shortcuts: _containers.RepeatedCompositeFieldContainer[Shortcut]
    def __init__(self, shortcuts: _Optional[_Iterable[_Union[Shortcut, _Mapping]]] = ...) -> None: ...

class GetShortcutRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateShortcutRequest(_message.Message):
    __slots__ = ("parent", "shortcut", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SHORTCUT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    shortcut: Shortcut
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., shortcut: _Optional[_Union[Shortcut, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class UpdateShortcutRequest(_message.Message):
    __slots__ = ("shortcut", "update_mask")
    SHORTCUT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    shortcut: Shortcut
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, shortcut: _Optional[_Union[Shortcut, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteShortcutRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
