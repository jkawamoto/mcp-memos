import datetime

from mcp_memos.api.v1 import common_pb2 as _common_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
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

class User(_message.Message):
    __slots__ = ("name", "role", "username", "email", "display_name", "avatar_url", "description", "password", "state", "create_time", "update_time")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[User.Role]
        HOST: _ClassVar[User.Role]
        ADMIN: _ClassVar[User.Role]
        USER: _ClassVar[User.Role]
    ROLE_UNSPECIFIED: User.Role
    HOST: User.Role
    ADMIN: User.Role
    USER: User.Role
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    role: User.Role
    username: str
    email: str
    display_name: str
    avatar_url: str
    description: str
    password: str
    state: _common_pb2.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., role: _Optional[_Union[User.Role, str]] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., display_name: _Optional[str] = ..., avatar_url: _Optional[str] = ..., description: _Optional[str] = ..., password: _Optional[str] = ..., state: _Optional[_Union[_common_pb2.State, str]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "filter", "show_deleted")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    show_deleted: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., show_deleted: bool = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "next_page_token", "total_size")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    next_page_token: str
    total_size: int
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("user", "user_id", "validate_only", "request_id")
    USER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    user: User
    user_id: str
    validate_only: bool
    request_id: str
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., user_id: _Optional[str] = ..., validate_only: bool = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user", "update_mask", "allow_missing")
    USER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    user: User
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class GetUserAvatarRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UserStats(_message.Message):
    __slots__ = ("name", "memo_display_timestamps", "memo_type_stats", "tag_count", "pinned_memos", "total_memo_count")
    class TagCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class MemoTypeStats(_message.Message):
        __slots__ = ("link_count", "code_count", "todo_count", "undo_count")
        LINK_COUNT_FIELD_NUMBER: _ClassVar[int]
        CODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        TODO_COUNT_FIELD_NUMBER: _ClassVar[int]
        UNDO_COUNT_FIELD_NUMBER: _ClassVar[int]
        link_count: int
        code_count: int
        todo_count: int
        undo_count: int
        def __init__(self, link_count: _Optional[int] = ..., code_count: _Optional[int] = ..., todo_count: _Optional[int] = ..., undo_count: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMO_DISPLAY_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    MEMO_TYPE_STATS_FIELD_NUMBER: _ClassVar[int]
    TAG_COUNT_FIELD_NUMBER: _ClassVar[int]
    PINNED_MEMOS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMO_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    memo_display_timestamps: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    memo_type_stats: UserStats.MemoTypeStats
    tag_count: _containers.ScalarMap[str, int]
    pinned_memos: _containers.RepeatedScalarFieldContainer[str]
    total_memo_count: int
    def __init__(self, name: _Optional[str] = ..., memo_display_timestamps: _Optional[_Iterable[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]] = ..., memo_type_stats: _Optional[_Union[UserStats.MemoTypeStats, _Mapping]] = ..., tag_count: _Optional[_Mapping[str, int]] = ..., pinned_memos: _Optional[_Iterable[str]] = ..., total_memo_count: _Optional[int] = ...) -> None: ...

class GetUserStatsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAllUserStatsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAllUserStatsResponse(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[UserStats]
    def __init__(self, stats: _Optional[_Iterable[_Union[UserStats, _Mapping]]] = ...) -> None: ...

class UserSetting(_message.Message):
    __slots__ = ("name", "general_setting", "sessions_setting", "access_tokens_setting", "webhooks_setting")
    class Key(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_UNSPECIFIED: _ClassVar[UserSetting.Key]
        GENERAL: _ClassVar[UserSetting.Key]
        SESSIONS: _ClassVar[UserSetting.Key]
        ACCESS_TOKENS: _ClassVar[UserSetting.Key]
        WEBHOOKS: _ClassVar[UserSetting.Key]
    KEY_UNSPECIFIED: UserSetting.Key
    GENERAL: UserSetting.Key
    SESSIONS: UserSetting.Key
    ACCESS_TOKENS: UserSetting.Key
    WEBHOOKS: UserSetting.Key
    class GeneralSetting(_message.Message):
        __slots__ = ("locale", "memo_visibility", "theme")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        MEMO_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        THEME_FIELD_NUMBER: _ClassVar[int]
        locale: str
        memo_visibility: str
        theme: str
        def __init__(self, locale: _Optional[str] = ..., memo_visibility: _Optional[str] = ..., theme: _Optional[str] = ...) -> None: ...
    class SessionsSetting(_message.Message):
        __slots__ = ("sessions",)
        SESSIONS_FIELD_NUMBER: _ClassVar[int]
        sessions: _containers.RepeatedCompositeFieldContainer[UserSession]
        def __init__(self, sessions: _Optional[_Iterable[_Union[UserSession, _Mapping]]] = ...) -> None: ...
    class AccessTokensSetting(_message.Message):
        __slots__ = ("access_tokens",)
        ACCESS_TOKENS_FIELD_NUMBER: _ClassVar[int]
        access_tokens: _containers.RepeatedCompositeFieldContainer[UserAccessToken]
        def __init__(self, access_tokens: _Optional[_Iterable[_Union[UserAccessToken, _Mapping]]] = ...) -> None: ...
    class WebhooksSetting(_message.Message):
        __slots__ = ("webhooks",)
        WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
        webhooks: _containers.RepeatedCompositeFieldContainer[UserWebhook]
        def __init__(self, webhooks: _Optional[_Iterable[_Union[UserWebhook, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENERAL_SETTING_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_SETTING_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKENS_SETTING_FIELD_NUMBER: _ClassVar[int]
    WEBHOOKS_SETTING_FIELD_NUMBER: _ClassVar[int]
    name: str
    general_setting: UserSetting.GeneralSetting
    sessions_setting: UserSetting.SessionsSetting
    access_tokens_setting: UserSetting.AccessTokensSetting
    webhooks_setting: UserSetting.WebhooksSetting
    def __init__(self, name: _Optional[str] = ..., general_setting: _Optional[_Union[UserSetting.GeneralSetting, _Mapping]] = ..., sessions_setting: _Optional[_Union[UserSetting.SessionsSetting, _Mapping]] = ..., access_tokens_setting: _Optional[_Union[UserSetting.AccessTokensSetting, _Mapping]] = ..., webhooks_setting: _Optional[_Union[UserSetting.WebhooksSetting, _Mapping]] = ...) -> None: ...

class GetUserSettingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateUserSettingRequest(_message.Message):
    __slots__ = ("setting", "update_mask")
    SETTING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    setting: UserSetting
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, setting: _Optional[_Union[UserSetting, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListUserSettingsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListUserSettingsResponse(_message.Message):
    __slots__ = ("settings", "next_page_token", "total_size")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[UserSetting]
    next_page_token: str
    total_size: int
    def __init__(self, settings: _Optional[_Iterable[_Union[UserSetting, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UserAccessToken(_message.Message):
    __slots__ = ("name", "access_token", "description", "issued_at", "expires_at")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    access_token: str
    description: str
    issued_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., access_token: _Optional[str] = ..., description: _Optional[str] = ..., issued_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListUserAccessTokensRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListUserAccessTokensResponse(_message.Message):
    __slots__ = ("access_tokens", "next_page_token", "total_size")
    ACCESS_TOKENS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    access_tokens: _containers.RepeatedCompositeFieldContainer[UserAccessToken]
    next_page_token: str
    total_size: int
    def __init__(self, access_tokens: _Optional[_Iterable[_Union[UserAccessToken, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class CreateUserAccessTokenRequest(_message.Message):
    __slots__ = ("parent", "access_token", "access_token_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_token: UserAccessToken
    access_token_id: str
    def __init__(self, parent: _Optional[str] = ..., access_token: _Optional[_Union[UserAccessToken, _Mapping]] = ..., access_token_id: _Optional[str] = ...) -> None: ...

class DeleteUserAccessTokenRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UserSession(_message.Message):
    __slots__ = ("name", "session_id", "create_time", "last_accessed_time", "client_info")
    class ClientInfo(_message.Message):
        __slots__ = ("user_agent", "ip_address", "device_type", "os", "browser")
        USER_AGENT_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        OS_FIELD_NUMBER: _ClassVar[int]
        BROWSER_FIELD_NUMBER: _ClassVar[int]
        user_agent: str
        ip_address: str
        device_type: str
        os: str
        browser: str
        def __init__(self, user_agent: _Optional[str] = ..., ip_address: _Optional[str] = ..., device_type: _Optional[str] = ..., os: _Optional[str] = ..., browser: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_TIME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    session_id: str
    create_time: _timestamp_pb2.Timestamp
    last_accessed_time: _timestamp_pb2.Timestamp
    client_info: UserSession.ClientInfo
    def __init__(self, name: _Optional[str] = ..., session_id: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_accessed_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., client_info: _Optional[_Union[UserSession.ClientInfo, _Mapping]] = ...) -> None: ...

class ListUserSessionsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListUserSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[UserSession]
    def __init__(self, sessions: _Optional[_Iterable[_Union[UserSession, _Mapping]]] = ...) -> None: ...

class RevokeUserSessionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UserWebhook(_message.Message):
    __slots__ = ("name", "url", "display_name", "create_time", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListUserWebhooksRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListUserWebhooksResponse(_message.Message):
    __slots__ = ("webhooks",)
    WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
    webhooks: _containers.RepeatedCompositeFieldContainer[UserWebhook]
    def __init__(self, webhooks: _Optional[_Iterable[_Union[UserWebhook, _Mapping]]] = ...) -> None: ...

class CreateUserWebhookRequest(_message.Message):
    __slots__ = ("parent", "webhook")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    webhook: UserWebhook
    def __init__(self, parent: _Optional[str] = ..., webhook: _Optional[_Union[UserWebhook, _Mapping]] = ...) -> None: ...

class UpdateUserWebhookRequest(_message.Message):
    __slots__ = ("webhook", "update_mask")
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    webhook: UserWebhook
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, webhook: _Optional[_Union[UserWebhook, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteUserWebhookRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
