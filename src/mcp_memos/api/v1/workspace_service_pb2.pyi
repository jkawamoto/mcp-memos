from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkspaceProfile(_message.Message):
    __slots__ = ("owner", "version", "mode", "instance_url")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_URL_FIELD_NUMBER: _ClassVar[int]
    owner: str
    version: str
    mode: str
    instance_url: str
    def __init__(self, owner: _Optional[str] = ..., version: _Optional[str] = ..., mode: _Optional[str] = ..., instance_url: _Optional[str] = ...) -> None: ...

class GetWorkspaceProfileRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WorkspaceSetting(_message.Message):
    __slots__ = ("name", "general_setting", "storage_setting", "memo_related_setting")
    class Key(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_UNSPECIFIED: _ClassVar[WorkspaceSetting.Key]
        GENERAL: _ClassVar[WorkspaceSetting.Key]
        STORAGE: _ClassVar[WorkspaceSetting.Key]
        MEMO_RELATED: _ClassVar[WorkspaceSetting.Key]
    KEY_UNSPECIFIED: WorkspaceSetting.Key
    GENERAL: WorkspaceSetting.Key
    STORAGE: WorkspaceSetting.Key
    MEMO_RELATED: WorkspaceSetting.Key
    class GeneralSetting(_message.Message):
        __slots__ = ("theme", "disallow_user_registration", "disallow_password_auth", "additional_script", "additional_style", "custom_profile", "week_start_day_offset", "disallow_change_username", "disallow_change_nickname")
        class CustomProfile(_message.Message):
            __slots__ = ("title", "description", "logo_url", "locale")
            TITLE_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            LOGO_URL_FIELD_NUMBER: _ClassVar[int]
            LOCALE_FIELD_NUMBER: _ClassVar[int]
            title: str
            description: str
            logo_url: str
            locale: str
            def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., logo_url: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...
        THEME_FIELD_NUMBER: _ClassVar[int]
        DISALLOW_USER_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
        DISALLOW_PASSWORD_AUTH_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_SCRIPT_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_STYLE_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_PROFILE_FIELD_NUMBER: _ClassVar[int]
        WEEK_START_DAY_OFFSET_FIELD_NUMBER: _ClassVar[int]
        DISALLOW_CHANGE_USERNAME_FIELD_NUMBER: _ClassVar[int]
        DISALLOW_CHANGE_NICKNAME_FIELD_NUMBER: _ClassVar[int]
        theme: str
        disallow_user_registration: bool
        disallow_password_auth: bool
        additional_script: str
        additional_style: str
        custom_profile: WorkspaceSetting.GeneralSetting.CustomProfile
        week_start_day_offset: int
        disallow_change_username: bool
        disallow_change_nickname: bool
        def __init__(self, theme: _Optional[str] = ..., disallow_user_registration: bool = ..., disallow_password_auth: bool = ..., additional_script: _Optional[str] = ..., additional_style: _Optional[str] = ..., custom_profile: _Optional[_Union[WorkspaceSetting.GeneralSetting.CustomProfile, _Mapping]] = ..., week_start_day_offset: _Optional[int] = ..., disallow_change_username: bool = ..., disallow_change_nickname: bool = ...) -> None: ...
    class StorageSetting(_message.Message):
        __slots__ = ("storage_type", "filepath_template", "upload_size_limit_mb", "s3_config")
        class StorageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STORAGE_TYPE_UNSPECIFIED: _ClassVar[WorkspaceSetting.StorageSetting.StorageType]
            DATABASE: _ClassVar[WorkspaceSetting.StorageSetting.StorageType]
            LOCAL: _ClassVar[WorkspaceSetting.StorageSetting.StorageType]
            S3: _ClassVar[WorkspaceSetting.StorageSetting.StorageType]
        STORAGE_TYPE_UNSPECIFIED: WorkspaceSetting.StorageSetting.StorageType
        DATABASE: WorkspaceSetting.StorageSetting.StorageType
        LOCAL: WorkspaceSetting.StorageSetting.StorageType
        S3: WorkspaceSetting.StorageSetting.StorageType
        class S3Config(_message.Message):
            __slots__ = ("access_key_id", "access_key_secret", "endpoint", "region", "bucket", "use_path_style")
            ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
            ACCESS_KEY_SECRET_FIELD_NUMBER: _ClassVar[int]
            ENDPOINT_FIELD_NUMBER: _ClassVar[int]
            REGION_FIELD_NUMBER: _ClassVar[int]
            BUCKET_FIELD_NUMBER: _ClassVar[int]
            USE_PATH_STYLE_FIELD_NUMBER: _ClassVar[int]
            access_key_id: str
            access_key_secret: str
            endpoint: str
            region: str
            bucket: str
            use_path_style: bool
            def __init__(self, access_key_id: _Optional[str] = ..., access_key_secret: _Optional[str] = ..., endpoint: _Optional[str] = ..., region: _Optional[str] = ..., bucket: _Optional[str] = ..., use_path_style: bool = ...) -> None: ...
        STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILEPATH_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_SIZE_LIMIT_MB_FIELD_NUMBER: _ClassVar[int]
        S3_CONFIG_FIELD_NUMBER: _ClassVar[int]
        storage_type: WorkspaceSetting.StorageSetting.StorageType
        filepath_template: str
        upload_size_limit_mb: int
        s3_config: WorkspaceSetting.StorageSetting.S3Config
        def __init__(self, storage_type: _Optional[_Union[WorkspaceSetting.StorageSetting.StorageType, str]] = ..., filepath_template: _Optional[str] = ..., upload_size_limit_mb: _Optional[int] = ..., s3_config: _Optional[_Union[WorkspaceSetting.StorageSetting.S3Config, _Mapping]] = ...) -> None: ...
    class MemoRelatedSetting(_message.Message):
        __slots__ = ("disallow_public_visibility", "display_with_update_time", "content_length_limit", "enable_double_click_edit", "enable_link_preview", "reactions", "disable_markdown_shortcuts", "enable_blur_nsfw_content", "nsfw_tags")
        DISALLOW_PUBLIC_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_WITH_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        CONTENT_LENGTH_LIMIT_FIELD_NUMBER: _ClassVar[int]
        ENABLE_DOUBLE_CLICK_EDIT_FIELD_NUMBER: _ClassVar[int]
        ENABLE_LINK_PREVIEW_FIELD_NUMBER: _ClassVar[int]
        REACTIONS_FIELD_NUMBER: _ClassVar[int]
        DISABLE_MARKDOWN_SHORTCUTS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_BLUR_NSFW_CONTENT_FIELD_NUMBER: _ClassVar[int]
        NSFW_TAGS_FIELD_NUMBER: _ClassVar[int]
        disallow_public_visibility: bool
        display_with_update_time: bool
        content_length_limit: int
        enable_double_click_edit: bool
        enable_link_preview: bool
        reactions: _containers.RepeatedScalarFieldContainer[str]
        disable_markdown_shortcuts: bool
        enable_blur_nsfw_content: bool
        nsfw_tags: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, disallow_public_visibility: bool = ..., display_with_update_time: bool = ..., content_length_limit: _Optional[int] = ..., enable_double_click_edit: bool = ..., enable_link_preview: bool = ..., reactions: _Optional[_Iterable[str]] = ..., disable_markdown_shortcuts: bool = ..., enable_blur_nsfw_content: bool = ..., nsfw_tags: _Optional[_Iterable[str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENERAL_SETTING_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SETTING_FIELD_NUMBER: _ClassVar[int]
    MEMO_RELATED_SETTING_FIELD_NUMBER: _ClassVar[int]
    name: str
    general_setting: WorkspaceSetting.GeneralSetting
    storage_setting: WorkspaceSetting.StorageSetting
    memo_related_setting: WorkspaceSetting.MemoRelatedSetting
    def __init__(self, name: _Optional[str] = ..., general_setting: _Optional[_Union[WorkspaceSetting.GeneralSetting, _Mapping]] = ..., storage_setting: _Optional[_Union[WorkspaceSetting.StorageSetting, _Mapping]] = ..., memo_related_setting: _Optional[_Union[WorkspaceSetting.MemoRelatedSetting, _Mapping]] = ...) -> None: ...

class GetWorkspaceSettingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateWorkspaceSettingRequest(_message.Message):
    __slots__ = ("setting", "update_mask")
    SETTING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    setting: WorkspaceSetting
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, setting: _Optional[_Union[WorkspaceSetting, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
