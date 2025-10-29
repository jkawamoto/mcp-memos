from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityProvider(_message.Message):
    __slots__ = ("name", "type", "title", "identifier_filter", "config")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[IdentityProvider.Type]
        OAUTH2: _ClassVar[IdentityProvider.Type]
    TYPE_UNSPECIFIED: IdentityProvider.Type
    OAUTH2: IdentityProvider.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FILTER_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: IdentityProvider.Type
    title: str
    identifier_filter: str
    config: IdentityProviderConfig
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[IdentityProvider.Type, str]] = ..., title: _Optional[str] = ..., identifier_filter: _Optional[str] = ..., config: _Optional[_Union[IdentityProviderConfig, _Mapping]] = ...) -> None: ...

class IdentityProviderConfig(_message.Message):
    __slots__ = ("oauth2_config",)
    OAUTH2_CONFIG_FIELD_NUMBER: _ClassVar[int]
    oauth2_config: OAuth2Config
    def __init__(self, oauth2_config: _Optional[_Union[OAuth2Config, _Mapping]] = ...) -> None: ...

class FieldMapping(_message.Message):
    __slots__ = ("identifier", "display_name", "email", "avatar_url")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    display_name: str
    email: str
    avatar_url: str
    def __init__(self, identifier: _Optional[str] = ..., display_name: _Optional[str] = ..., email: _Optional[str] = ..., avatar_url: _Optional[str] = ...) -> None: ...

class OAuth2Config(_message.Message):
    __slots__ = ("client_id", "client_secret", "auth_url", "token_url", "user_info_url", "scopes", "field_mapping")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    AUTH_URL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_URL_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAPPING_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    auth_url: str
    token_url: str
    user_info_url: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    field_mapping: FieldMapping
    def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., auth_url: _Optional[str] = ..., token_url: _Optional[str] = ..., user_info_url: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., field_mapping: _Optional[_Union[FieldMapping, _Mapping]] = ...) -> None: ...

class ListIdentityProvidersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListIdentityProvidersResponse(_message.Message):
    __slots__ = ("identity_providers",)
    IDENTITY_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    identity_providers: _containers.RepeatedCompositeFieldContainer[IdentityProvider]
    def __init__(self, identity_providers: _Optional[_Iterable[_Union[IdentityProvider, _Mapping]]] = ...) -> None: ...

class GetIdentityProviderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateIdentityProviderRequest(_message.Message):
    __slots__ = ("identity_provider", "identity_provider_id")
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    identity_provider: IdentityProvider
    identity_provider_id: str
    def __init__(self, identity_provider: _Optional[_Union[IdentityProvider, _Mapping]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class UpdateIdentityProviderRequest(_message.Message):
    __slots__ = ("identity_provider", "update_mask")
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    identity_provider: IdentityProvider
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, identity_provider: _Optional[_Union[IdentityProvider, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteIdentityProviderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
