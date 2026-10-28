import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tesla_protocol.command import vcsec_pb2 as _vcsec_pb2
from tesla_protocol.command import common_pb2 as _common_pb2
from tesla_protocol.command import managed_charging_pb2 as _managed_charging_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AutopilotBase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AutopilotBase_NONE: _ClassVar[AutopilotBase]
    AutopilotBase_HIGHWAY: _ClassVar[AutopilotBase]
    AutopilotBase_ENHANCED: _ClassVar[AutopilotBase]
    AutopilotBase_SELF_DRIVING: _ClassVar[AutopilotBase]
    AutopilotBase_BASIC: _ClassVar[AutopilotBase]

class AutopilotOverrideState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AutopilotOverrideState_BASE: _ClassVar[AutopilotOverrideState]
    AutopilotOverrideState_SUBSCRIPTION: _ClassVar[AutopilotOverrideState]
    AutopilotOverrideState_TRIAL: _ClassVar[AutopilotOverrideState]
    AutopilotOverrideState_TIMEBOUND_SUBSCRIPTION: _ClassVar[AutopilotOverrideState]
    AutopilotOverrideState_TIMEBOUND_TRIAL: _ClassVar[AutopilotOverrideState]
    AutopilotOverrideState_OPTION_CODE: _ClassVar[AutopilotOverrideState]
    AutopilotOverrideState_OPTION_OVERRIDE: _ClassVar[AutopilotOverrideState]
    AutopilotOverrideState_VEHICLE_MANAGED: _ClassVar[AutopilotOverrideState]
    AutopilotOverrideState_UNKNOWN: _ClassVar[AutopilotOverrideState]

class DashCamState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DashCamState_UNAVAILABLE: _ClassVar[DashCamState]
    DashCamState_AVAILABLE: _ClassVar[DashCamState]
    DashCamState_RECORDING: _ClassVar[DashCamState]
    DashCamState_SAVED: _ClassVar[DashCamState]
    DashCamState_STREAMING: _ClassVar[DashCamState]
    DashCamState_NO_SPACE: _ClassVar[DashCamState]
    DashCamState_SAVING: _ClassVar[DashCamState]
    DashCamState_PAUSED: _ClassVar[DashCamState]

class TheaterSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TheaterSource_None: _ClassVar[TheaterSource]
    TheaterSource_YouTube: _ClassVar[TheaterSource]
    TheaterSource_TeslaTutorials: _ClassVar[TheaterSource]
    TheaterSource_Netflix: _ClassVar[TheaterSource]
    TheaterSource_Twitch: _ClassVar[TheaterSource]
    TheaterSource_TikTok: _ClassVar[TheaterSource]
    TheaterSource_Hulu: _ClassVar[TheaterSource]
    TheaterSource_BiliBili: _ClassVar[TheaterSource]
    TheaterSource_Disney: _ClassVar[TheaterSource]
    TheaterSource_Douyin: _ClassVar[TheaterSource]
    TheaterSource_MontyPython: _ClassVar[TheaterSource]
    TheaterSource_Tencent: _ClassVar[TheaterSource]
    TheaterSource_Youku: _ClassVar[TheaterSource]
    TheaterSource_iQiyi: _ClassVar[TheaterSource]
    TheaterSource_ThunderStone: _ClassVar[TheaterSource]
    TheaterSource_MangoTV: _ClassVar[TheaterSource]
    TheaterSource_Kuaishou: _ClassVar[TheaterSource]

class MediaSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MediaSourceType_None: _ClassVar[MediaSourceType]
    MediaSourceType_AM: _ClassVar[MediaSourceType]
    MediaSourceType_FM: _ClassVar[MediaSourceType]
    MediaSourceType_XM: _ClassVar[MediaSourceType]
    MediaSourceType_Slacker: _ClassVar[MediaSourceType]
    MediaSourceType_LocalFiles: _ClassVar[MediaSourceType]
    MediaSourceType_iPod: _ClassVar[MediaSourceType]
    MediaSourceType_Bluetooth: _ClassVar[MediaSourceType]
    MediaSourceType_AuxIn: _ClassVar[MediaSourceType]
    MediaSourceType_DAB: _ClassVar[MediaSourceType]
    MediaSourceType_Rdio: _ClassVar[MediaSourceType]
    MediaSourceType_Spotify: _ClassVar[MediaSourceType]
    MediaSourceType_USRadio: _ClassVar[MediaSourceType]
    MediaSourceType_EURadio: _ClassVar[MediaSourceType]
    MediaSourceType_MediaFile: _ClassVar[MediaSourceType]
    MediaSourceType_TuneIn: _ClassVar[MediaSourceType]
    MediaSourceType_Stingray: _ClassVar[MediaSourceType]
    MediaSourceType_SiriusXM: _ClassVar[MediaSourceType]
    MediaSourceType_Tidal: _ClassVar[MediaSourceType]
    MediaSourceType_QQMusic: _ClassVar[MediaSourceType]
    MediaSourceType_QQMusic2: _ClassVar[MediaSourceType]
    MediaSourceType_Ximalaya: _ClassVar[MediaSourceType]
    MediaSourceType_OnlineRadio: _ClassVar[MediaSourceType]
    MediaSourceType_OnlineRadio2: _ClassVar[MediaSourceType]
    MediaSourceType_NetEaseMusic: _ClassVar[MediaSourceType]
    MediaSourceType_AppleMusic: _ClassVar[MediaSourceType]
    MediaSourceType_Browser: _ClassVar[MediaSourceType]
    MediaSourceType_Theater: _ClassVar[MediaSourceType]
    MediaSourceType_Game: _ClassVar[MediaSourceType]
    MediaSourceType_Tutorial: _ClassVar[MediaSourceType]
    MediaSourceType_Toybox: _ClassVar[MediaSourceType]
    MediaSourceType_RecentsFavorites: _ClassVar[MediaSourceType]
    MediaSourceType_HomeApps: _ClassVar[MediaSourceType]
    MediaSourceType_Search: _ClassVar[MediaSourceType]
    MediaSourceType_ApplePodcasts: _ClassVar[MediaSourceType]
    MediaSourceType_Audible: _ClassVar[MediaSourceType]
    MediaSourceType_AmazonMusic: _ClassVar[MediaSourceType]
    MediaSourceType_YouTubeMusic: _ClassVar[MediaSourceType]
    MediaSourceType_SiriusXmWeb: _ClassVar[MediaSourceType]
    MediaSourceType_Yunting: _ClassVar[MediaSourceType]
    MediaSourceType_TuneInWeb: _ClassVar[MediaSourceType]
    MediaSourceType_Kugou: _ClassVar[MediaSourceType]
    MediaSourceType_Vohico: _ClassVar[MediaSourceType]

class VehicleImageStateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APVIZ_INVALID: _ClassVar[VehicleImageStateType]
    APVIZ_WRAP: _ClassVar[VehicleImageStateType]
    APVIZ_LICENSE_PLATE: _ClassVar[VehicleImageStateType]

class KeepOnAccessoryPortRequest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KeepOnAccessoryPortRequest_Off: _ClassVar[KeepOnAccessoryPortRequest]
    KeepOnAccessoryPortRequest_On: _ClassVar[KeepOnAccessoryPortRequest]

class MobileAppFeature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOBILE_APP_FEATURE_ACTIVE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_CLIMATE_KEEPER: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_UNLOCK_STOP_CHARGE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SET_RATE_TARIFF: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_GET_RATE_TARIFF: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_DRIVENOTE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_CLIMATE_KEEPER_OVERRIDE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SIGNED_VIDEO_REQUEST: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SENTRY_CAM_FLASH_LIGHTS: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_BOOMBOX: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_DOOR_UNLATCH: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SEAT_HEATERS_INSTALLED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_LAST_SEEN_TPMS: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_UI_CHARGE_PORT: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_MONITOR_AND_CHARGE_ROLES: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_PROTO_FLOATS: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_BLUETOOTH_PAIRING: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_HMAC_AUTHENTICATION: _ClassVar[MobileAppFeature]
    MOBILE_APP_COP_USER_SET_TEMP: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_MEDIA_DETAILS: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_RESPONSE_CACHE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SCC: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SENTRY_CAM_WITH_DOG_MODE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_AUTO_STEERING_WHEEL_HEAT: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_MANAGED_CHARGING: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_TOGGLE_REMOTE_SERVICE_ACCESS_COMMAND_DECPRECATED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_TOGGLE_REMOTE_SERVICE_ACCESS_COMMAND: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SEND_NAVIGATION_ROUTE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_RED_BRAKE_CALIPER_FIX: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_PIN_TO_DRIVE: _ClassVar[MobileAppFeature]
    MOBILE_APP_COP_NOT_RUNNING_REASON: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SET_VEHICLE_NAME: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_VEHICLE_DATA_PII_V2: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_BOOMBOX_V2: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_UWB_STABLE_FOR_SUPPORTED_CARS: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SPEED_LIMIT_PIN_RESET_SIGNED_COMMAND: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_PRECISE_LOCATION_TAG: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_IMU_ALERT_IS_VISIBLE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_CT_SUPPORTS_COP: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_WAYPOINTS_SUPPORTED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_OCTA_VIEW: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_BT_GTW_UNLOCK: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_UI_PHONEKEY_WHITELIST_RELIABLE_DEPRECATED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_UI_PHONEKEY_WHITELIST_RELIABLE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SUMMON_PREWARMING: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_UWB_ENABLED_FOR_P2S_DEPRECATED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_UWB_ENABLED_FOR_P2S: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_UI_ONE_TIME_CHARGE_SUPPORTED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SCHEDULE_V3: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_ECIES_VEHICLE_DATA_ENCRYPTION: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_TENT_MODE_SUPPORTED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SCHEDULE_V3_NAMING: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_COLORIZER_COLOR_REMAP_ENABLED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SEND_NAVIGATION_REQUEST_GPS_DESTINATION: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SUMMON_WEBCAM: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_BLE_REMOTE_START: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SOH_TEST_OBSOLETE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SET_ARRIVAL_PERCENTAGE_OBSOLETE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_REMOTE_THEATER_CONTROL: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_CT_SUSPENSION: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SOH_TEST_V2: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_ANDROID_UWB_ENABLED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_LOW_POWER_MODE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_ROBOTAXI_UWB: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_KEEP_ACCESSORY_POWER_MODE: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SETUP_CLOUD_ACCOUNTS: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SETUP_CLOUD_ACCOUNTS_WITH_DELETION: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_FETCH_KEY_METADATA_DEPRECATED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_FETCH_KEY_METADATA: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_TRAILER_LIGHT_TEST: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_DELETE_DASHCAM_CLIPS_AND_FORMAT_USB: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SOFTWARE_UPDATE_AUTO_SCHEDULED: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_BLE_MESSAGE_FRAMING: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_WAYPOINTS_REQUEST_ACCEPTS_COORDINATES: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_PHONE_SETTING_PREFERENCES_SYNC: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_UPLOAD_CAR_WRAP: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_SHARE_URLS_X: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_DISPLAY_BRIGHTNESS: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_ANDROID_BLE_BONDING: _ClassVar[MobileAppFeature]
    MOBILE_APP_FEATURE_APVIZ_WHEEL_CAPS: _ClassVar[MobileAppFeature]
AutopilotBase_NONE: AutopilotBase
AutopilotBase_HIGHWAY: AutopilotBase
AutopilotBase_ENHANCED: AutopilotBase
AutopilotBase_SELF_DRIVING: AutopilotBase
AutopilotBase_BASIC: AutopilotBase
AutopilotOverrideState_BASE: AutopilotOverrideState
AutopilotOverrideState_SUBSCRIPTION: AutopilotOverrideState
AutopilotOverrideState_TRIAL: AutopilotOverrideState
AutopilotOverrideState_TIMEBOUND_SUBSCRIPTION: AutopilotOverrideState
AutopilotOverrideState_TIMEBOUND_TRIAL: AutopilotOverrideState
AutopilotOverrideState_OPTION_CODE: AutopilotOverrideState
AutopilotOverrideState_OPTION_OVERRIDE: AutopilotOverrideState
AutopilotOverrideState_VEHICLE_MANAGED: AutopilotOverrideState
AutopilotOverrideState_UNKNOWN: AutopilotOverrideState
DashCamState_UNAVAILABLE: DashCamState
DashCamState_AVAILABLE: DashCamState
DashCamState_RECORDING: DashCamState
DashCamState_SAVED: DashCamState
DashCamState_STREAMING: DashCamState
DashCamState_NO_SPACE: DashCamState
DashCamState_SAVING: DashCamState
DashCamState_PAUSED: DashCamState
TheaterSource_None: TheaterSource
TheaterSource_YouTube: TheaterSource
TheaterSource_TeslaTutorials: TheaterSource
TheaterSource_Netflix: TheaterSource
TheaterSource_Twitch: TheaterSource
TheaterSource_TikTok: TheaterSource
TheaterSource_Hulu: TheaterSource
TheaterSource_BiliBili: TheaterSource
TheaterSource_Disney: TheaterSource
TheaterSource_Douyin: TheaterSource
TheaterSource_MontyPython: TheaterSource
TheaterSource_Tencent: TheaterSource
TheaterSource_Youku: TheaterSource
TheaterSource_iQiyi: TheaterSource
TheaterSource_ThunderStone: TheaterSource
TheaterSource_MangoTV: TheaterSource
TheaterSource_Kuaishou: TheaterSource
MediaSourceType_None: MediaSourceType
MediaSourceType_AM: MediaSourceType
MediaSourceType_FM: MediaSourceType
MediaSourceType_XM: MediaSourceType
MediaSourceType_Slacker: MediaSourceType
MediaSourceType_LocalFiles: MediaSourceType
MediaSourceType_iPod: MediaSourceType
MediaSourceType_Bluetooth: MediaSourceType
MediaSourceType_AuxIn: MediaSourceType
MediaSourceType_DAB: MediaSourceType
MediaSourceType_Rdio: MediaSourceType
MediaSourceType_Spotify: MediaSourceType
MediaSourceType_USRadio: MediaSourceType
MediaSourceType_EURadio: MediaSourceType
MediaSourceType_MediaFile: MediaSourceType
MediaSourceType_TuneIn: MediaSourceType
MediaSourceType_Stingray: MediaSourceType
MediaSourceType_SiriusXM: MediaSourceType
MediaSourceType_Tidal: MediaSourceType
MediaSourceType_QQMusic: MediaSourceType
MediaSourceType_QQMusic2: MediaSourceType
MediaSourceType_Ximalaya: MediaSourceType
MediaSourceType_OnlineRadio: MediaSourceType
MediaSourceType_OnlineRadio2: MediaSourceType
MediaSourceType_NetEaseMusic: MediaSourceType
MediaSourceType_AppleMusic: MediaSourceType
MediaSourceType_Browser: MediaSourceType
MediaSourceType_Theater: MediaSourceType
MediaSourceType_Game: MediaSourceType
MediaSourceType_Tutorial: MediaSourceType
MediaSourceType_Toybox: MediaSourceType
MediaSourceType_RecentsFavorites: MediaSourceType
MediaSourceType_HomeApps: MediaSourceType
MediaSourceType_Search: MediaSourceType
MediaSourceType_ApplePodcasts: MediaSourceType
MediaSourceType_Audible: MediaSourceType
MediaSourceType_AmazonMusic: MediaSourceType
MediaSourceType_YouTubeMusic: MediaSourceType
MediaSourceType_SiriusXmWeb: MediaSourceType
MediaSourceType_Yunting: MediaSourceType
MediaSourceType_TuneInWeb: MediaSourceType
MediaSourceType_Kugou: MediaSourceType
MediaSourceType_Vohico: MediaSourceType
APVIZ_INVALID: VehicleImageStateType
APVIZ_WRAP: VehicleImageStateType
APVIZ_LICENSE_PLATE: VehicleImageStateType
KeepOnAccessoryPortRequest_Off: KeepOnAccessoryPortRequest
KeepOnAccessoryPortRequest_On: KeepOnAccessoryPortRequest
MOBILE_APP_FEATURE_ACTIVE: MobileAppFeature
MOBILE_APP_FEATURE_CLIMATE_KEEPER: MobileAppFeature
MOBILE_APP_FEATURE_UNLOCK_STOP_CHARGE: MobileAppFeature
MOBILE_APP_FEATURE_SET_RATE_TARIFF: MobileAppFeature
MOBILE_APP_FEATURE_GET_RATE_TARIFF: MobileAppFeature
MOBILE_APP_FEATURE_DRIVENOTE: MobileAppFeature
MOBILE_APP_FEATURE_CLIMATE_KEEPER_OVERRIDE: MobileAppFeature
MOBILE_APP_FEATURE_SIGNED_VIDEO_REQUEST: MobileAppFeature
MOBILE_APP_FEATURE_SENTRY_CAM_FLASH_LIGHTS: MobileAppFeature
MOBILE_APP_FEATURE_BOOMBOX: MobileAppFeature
MOBILE_APP_FEATURE_DOOR_UNLATCH: MobileAppFeature
MOBILE_APP_FEATURE_SEAT_HEATERS_INSTALLED: MobileAppFeature
MOBILE_APP_FEATURE_LAST_SEEN_TPMS: MobileAppFeature
MOBILE_APP_FEATURE_UI_CHARGE_PORT: MobileAppFeature
MOBILE_APP_FEATURE_MONITOR_AND_CHARGE_ROLES: MobileAppFeature
MOBILE_APP_FEATURE_PROTO_FLOATS: MobileAppFeature
MOBILE_APP_FEATURE_BLUETOOTH_PAIRING: MobileAppFeature
MOBILE_APP_FEATURE_HMAC_AUTHENTICATION: MobileAppFeature
MOBILE_APP_COP_USER_SET_TEMP: MobileAppFeature
MOBILE_APP_FEATURE_MEDIA_DETAILS: MobileAppFeature
MOBILE_APP_FEATURE_RESPONSE_CACHE: MobileAppFeature
MOBILE_APP_FEATURE_SCC: MobileAppFeature
MOBILE_APP_FEATURE_SENTRY_CAM_WITH_DOG_MODE: MobileAppFeature
MOBILE_APP_FEATURE_AUTO_STEERING_WHEEL_HEAT: MobileAppFeature
MOBILE_APP_FEATURE_MANAGED_CHARGING: MobileAppFeature
MOBILE_APP_FEATURE_TOGGLE_REMOTE_SERVICE_ACCESS_COMMAND_DECPRECATED: MobileAppFeature
MOBILE_APP_FEATURE_TOGGLE_REMOTE_SERVICE_ACCESS_COMMAND: MobileAppFeature
MOBILE_APP_FEATURE_SEND_NAVIGATION_ROUTE: MobileAppFeature
MOBILE_APP_FEATURE_RED_BRAKE_CALIPER_FIX: MobileAppFeature
MOBILE_APP_FEATURE_PIN_TO_DRIVE: MobileAppFeature
MOBILE_APP_COP_NOT_RUNNING_REASON: MobileAppFeature
MOBILE_APP_FEATURE_SET_VEHICLE_NAME: MobileAppFeature
MOBILE_APP_FEATURE_VEHICLE_DATA_PII_V2: MobileAppFeature
MOBILE_APP_FEATURE_BOOMBOX_V2: MobileAppFeature
MOBILE_APP_FEATURE_UWB_STABLE_FOR_SUPPORTED_CARS: MobileAppFeature
MOBILE_APP_FEATURE_SPEED_LIMIT_PIN_RESET_SIGNED_COMMAND: MobileAppFeature
MOBILE_APP_FEATURE_PRECISE_LOCATION_TAG: MobileAppFeature
MOBILE_APP_FEATURE_IMU_ALERT_IS_VISIBLE: MobileAppFeature
MOBILE_APP_FEATURE_CT_SUPPORTS_COP: MobileAppFeature
MOBILE_APP_FEATURE_WAYPOINTS_SUPPORTED: MobileAppFeature
MOBILE_APP_FEATURE_OCTA_VIEW: MobileAppFeature
MOBILE_APP_FEATURE_BT_GTW_UNLOCK: MobileAppFeature
MOBILE_APP_FEATURE_UI_PHONEKEY_WHITELIST_RELIABLE_DEPRECATED: MobileAppFeature
MOBILE_APP_FEATURE_UI_PHONEKEY_WHITELIST_RELIABLE: MobileAppFeature
MOBILE_APP_FEATURE_SUMMON_PREWARMING: MobileAppFeature
MOBILE_APP_FEATURE_UWB_ENABLED_FOR_P2S_DEPRECATED: MobileAppFeature
MOBILE_APP_FEATURE_UWB_ENABLED_FOR_P2S: MobileAppFeature
MOBILE_APP_FEATURE_UI_ONE_TIME_CHARGE_SUPPORTED: MobileAppFeature
MOBILE_APP_FEATURE_SCHEDULE_V3: MobileAppFeature
MOBILE_APP_FEATURE_ECIES_VEHICLE_DATA_ENCRYPTION: MobileAppFeature
MOBILE_APP_FEATURE_TENT_MODE_SUPPORTED: MobileAppFeature
MOBILE_APP_FEATURE_SCHEDULE_V3_NAMING: MobileAppFeature
MOBILE_APP_FEATURE_COLORIZER_COLOR_REMAP_ENABLED: MobileAppFeature
MOBILE_APP_FEATURE_SEND_NAVIGATION_REQUEST_GPS_DESTINATION: MobileAppFeature
MOBILE_APP_FEATURE_SUMMON_WEBCAM: MobileAppFeature
MOBILE_APP_FEATURE_BLE_REMOTE_START: MobileAppFeature
MOBILE_APP_FEATURE_SOH_TEST_OBSOLETE: MobileAppFeature
MOBILE_APP_FEATURE_SET_ARRIVAL_PERCENTAGE_OBSOLETE: MobileAppFeature
MOBILE_APP_FEATURE_REMOTE_THEATER_CONTROL: MobileAppFeature
MOBILE_APP_FEATURE_CT_SUSPENSION: MobileAppFeature
MOBILE_APP_FEATURE_SOH_TEST_V2: MobileAppFeature
MOBILE_APP_FEATURE_ANDROID_UWB_ENABLED: MobileAppFeature
MOBILE_APP_FEATURE_LOW_POWER_MODE: MobileAppFeature
MOBILE_APP_FEATURE_ROBOTAXI_UWB: MobileAppFeature
MOBILE_APP_FEATURE_KEEP_ACCESSORY_POWER_MODE: MobileAppFeature
MOBILE_APP_FEATURE_SETUP_CLOUD_ACCOUNTS: MobileAppFeature
MOBILE_APP_FEATURE_SETUP_CLOUD_ACCOUNTS_WITH_DELETION: MobileAppFeature
MOBILE_APP_FEATURE_FETCH_KEY_METADATA_DEPRECATED: MobileAppFeature
MOBILE_APP_FEATURE_FETCH_KEY_METADATA: MobileAppFeature
MOBILE_APP_FEATURE_TRAILER_LIGHT_TEST: MobileAppFeature
MOBILE_APP_FEATURE_DELETE_DASHCAM_CLIPS_AND_FORMAT_USB: MobileAppFeature
MOBILE_APP_FEATURE_SOFTWARE_UPDATE_AUTO_SCHEDULED: MobileAppFeature
MOBILE_APP_FEATURE_BLE_MESSAGE_FRAMING: MobileAppFeature
MOBILE_APP_FEATURE_WAYPOINTS_REQUEST_ACCEPTS_COORDINATES: MobileAppFeature
MOBILE_APP_FEATURE_PHONE_SETTING_PREFERENCES_SYNC: MobileAppFeature
MOBILE_APP_FEATURE_UPLOAD_CAR_WRAP: MobileAppFeature
MOBILE_APP_FEATURE_SHARE_URLS_X: MobileAppFeature
MOBILE_APP_FEATURE_DISPLAY_BRIGHTNESS: MobileAppFeature
MOBILE_APP_FEATURE_ANDROID_BLE_BONDING: MobileAppFeature
MOBILE_APP_FEATURE_APVIZ_WHEEL_CAPS: MobileAppFeature

class VehicleData(_message.Message):
    __slots__ = ("gui_settings", "charge_state", "climate_state", "drive_state", "legacy_vehicle_state", "vehicle_config", "location_state", "closures_state", "proto_json_version", "encrypted_data", "upload_reason", "parked_accessory_state", "charge_schedule_state", "preconditioning_schedule_state", "soh_state", "vehicle_state", "tire_pressure_state", "media_state", "media_detail_state", "vehicle_detail_state", "software_update_state", "parental_controls_state", "alert_state", "light_show_state", "vehicle_image_state", "suspension_state", "child_presence_detection_state", "display_state", "keep_on_accessory_ports_state", "pii_key_responses", "wrapped_key", "supports_optional_fields")
    GUI_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CHARGE_STATE_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_STATE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_STATE_FIELD_NUMBER: _ClassVar[int]
    LEGACY_VEHICLE_STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOCATION_STATE_FIELD_NUMBER: _ClassVar[int]
    CLOSURES_STATE_FIELD_NUMBER: _ClassVar[int]
    PROTO_JSON_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_DATA_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_REASON_FIELD_NUMBER: _ClassVar[int]
    PARKED_ACCESSORY_STATE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_SCHEDULE_STATE_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_SCHEDULE_STATE_FIELD_NUMBER: _ClassVar[int]
    SOH_STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_STATE_FIELD_NUMBER: _ClassVar[int]
    TIRE_PRESSURE_STATE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_STATE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DETAIL_STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_DETAIL_STATE_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_UPDATE_STATE_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_STATE_FIELD_NUMBER: _ClassVar[int]
    ALERT_STATE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_IMAGE_STATE_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_STATE_FIELD_NUMBER: _ClassVar[int]
    CHILD_PRESENCE_DETECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_STATE_FIELD_NUMBER: _ClassVar[int]
    KEEP_ON_ACCESSORY_PORTS_STATE_FIELD_NUMBER: _ClassVar[int]
    PII_KEY_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    WRAPPED_KEY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_OPTIONAL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    gui_settings: GuiSettings
    charge_state: ChargeState
    climate_state: ClimateState
    drive_state: DriveState
    legacy_vehicle_state: VehicleState
    vehicle_config: VehicleConfig
    location_state: LocationState
    closures_state: ClosuresState
    proto_json_version: int
    encrypted_data: _containers.RepeatedScalarFieldContainer[bytes]
    upload_reason: str
    parked_accessory_state: ParkedAccessoryState
    charge_schedule_state: ChargeScheduleState
    preconditioning_schedule_state: PreconditioningScheduleState
    soh_state: SohState
    vehicle_state: CurrentVehicleState
    tire_pressure_state: TirePressureState
    media_state: MediaState
    media_detail_state: MediaDetailState
    vehicle_detail_state: VehicleDetailState
    software_update_state: SoftwareUpdateState
    parental_controls_state: ParentalControlsState
    alert_state: AlertState
    light_show_state: LightShowState
    vehicle_image_state: VehicleImageState
    suspension_state: SuspensionState
    child_presence_detection_state: ChildPresenceDetectionState
    display_state: DisplayState
    keep_on_accessory_ports_state: KeepOnAccessoryPortsState
    pii_key_responses: _containers.RepeatedScalarFieldContainer[bytes]
    wrapped_key: bytes
    supports_optional_fields: bool
    def __init__(self, gui_settings: _Optional[_Union[GuiSettings, _Mapping]] = ..., charge_state: _Optional[_Union[ChargeState, _Mapping]] = ..., climate_state: _Optional[_Union[ClimateState, _Mapping]] = ..., drive_state: _Optional[_Union[DriveState, _Mapping]] = ..., legacy_vehicle_state: _Optional[_Union[VehicleState, _Mapping]] = ..., vehicle_config: _Optional[_Union[VehicleConfig, _Mapping]] = ..., location_state: _Optional[_Union[LocationState, _Mapping]] = ..., closures_state: _Optional[_Union[ClosuresState, _Mapping]] = ..., proto_json_version: _Optional[int] = ..., encrypted_data: _Optional[_Iterable[bytes]] = ..., upload_reason: _Optional[str] = ..., parked_accessory_state: _Optional[_Union[ParkedAccessoryState, _Mapping]] = ..., charge_schedule_state: _Optional[_Union[ChargeScheduleState, _Mapping]] = ..., preconditioning_schedule_state: _Optional[_Union[PreconditioningScheduleState, _Mapping]] = ..., soh_state: _Optional[_Union[SohState, _Mapping]] = ..., vehicle_state: _Optional[_Union[CurrentVehicleState, _Mapping]] = ..., tire_pressure_state: _Optional[_Union[TirePressureState, _Mapping]] = ..., media_state: _Optional[_Union[MediaState, _Mapping]] = ..., media_detail_state: _Optional[_Union[MediaDetailState, _Mapping]] = ..., vehicle_detail_state: _Optional[_Union[VehicleDetailState, _Mapping]] = ..., software_update_state: _Optional[_Union[SoftwareUpdateState, _Mapping]] = ..., parental_controls_state: _Optional[_Union[ParentalControlsState, _Mapping]] = ..., alert_state: _Optional[_Union[AlertState, _Mapping]] = ..., light_show_state: _Optional[_Union[LightShowState, _Mapping]] = ..., vehicle_image_state: _Optional[_Union[VehicleImageState, _Mapping]] = ..., suspension_state: _Optional[_Union[SuspensionState, _Mapping]] = ..., child_presence_detection_state: _Optional[_Union[ChildPresenceDetectionState, _Mapping]] = ..., display_state: _Optional[_Union[DisplayState, _Mapping]] = ..., keep_on_accessory_ports_state: _Optional[_Union[KeepOnAccessoryPortsState, _Mapping]] = ..., pii_key_responses: _Optional[_Iterable[bytes]] = ..., wrapped_key: _Optional[bytes] = ..., supports_optional_fields: _Optional[bool] = ...) -> None: ...

class ClosuresState(_message.Message):
    __slots__ = ("door_open_driver_front", "door_open_driver_rear", "door_open_passenger_front", "door_open_passenger_rear", "door_open_trunk_front", "door_open_trunk_rear", "window_open_driver_front", "window_open_passenger_front", "window_open_driver_rear", "window_open_passenger_rear", "sun_roof_state", "sun_roof_percent_open", "locked", "is_user_present", "center_display_state", "remote_start", "valet_mode", "valet_pin_needed", "sentry_mode_state", "sentry_mode_available", "speed_limit_mode", "tonneau_state", "tonneau_percent_open", "tonneau_in_motion", "has_automatic_tonneau", "has_side_storage_doors", "door_open_side_storage_left", "door_open_side_storage_right", "cruise_speed_limit_mph", "timestamp")
    class SunRoofState(_message.Message):
        __slots__ = ("Unknown", "Calibrating", "Closed", "Open", "Moving", "Vent")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        CALIBRATING_FIELD_NUMBER: _ClassVar[int]
        CLOSED_FIELD_NUMBER: _ClassVar[int]
        OPEN_FIELD_NUMBER: _ClassVar[int]
        MOVING_FIELD_NUMBER: _ClassVar[int]
        VENT_FIELD_NUMBER: _ClassVar[int]
        Unknown: _common_pb2.Void
        Calibrating: _common_pb2.Void
        Closed: _common_pb2.Void
        Open: _common_pb2.Void
        Moving: _common_pb2.Void
        Vent: _common_pb2.Void
        def __init__(self, Unknown: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Calibrating: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Closed: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Open: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Moving: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Vent: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class DisplayState(_message.Message):
        __slots__ = ("Off", "Dim", "Accessory", "On", "Driving", "Charging", "Lock", "Sentry", "Dog", "Entertainment")
        OFF_FIELD_NUMBER: _ClassVar[int]
        DIM_FIELD_NUMBER: _ClassVar[int]
        ACCESSORY_FIELD_NUMBER: _ClassVar[int]
        ON_FIELD_NUMBER: _ClassVar[int]
        DRIVING_FIELD_NUMBER: _ClassVar[int]
        CHARGING_FIELD_NUMBER: _ClassVar[int]
        LOCK_FIELD_NUMBER: _ClassVar[int]
        SENTRY_FIELD_NUMBER: _ClassVar[int]
        DOG_FIELD_NUMBER: _ClassVar[int]
        ENTERTAINMENT_FIELD_NUMBER: _ClassVar[int]
        Off: _common_pb2.Void
        Dim: _common_pb2.Void
        Accessory: _common_pb2.Void
        On: _common_pb2.Void
        Driving: _common_pb2.Void
        Charging: _common_pb2.Void
        Lock: _common_pb2.Void
        Sentry: _common_pb2.Void
        Dog: _common_pb2.Void
        Entertainment: _common_pb2.Void
        def __init__(self, Off: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Dim: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Accessory: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., On: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Driving: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Charging: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Lock: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Sentry: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Dog: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Entertainment: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class SentryModeState(_message.Message):
        __slots__ = ("Off", "Idle", "Armed", "Aware", "Panic", "Quiet")
        OFF_FIELD_NUMBER: _ClassVar[int]
        IDLE_FIELD_NUMBER: _ClassVar[int]
        ARMED_FIELD_NUMBER: _ClassVar[int]
        AWARE_FIELD_NUMBER: _ClassVar[int]
        PANIC_FIELD_NUMBER: _ClassVar[int]
        QUIET_FIELD_NUMBER: _ClassVar[int]
        Off: _common_pb2.Void
        Idle: _common_pb2.Void
        Armed: _common_pb2.Void
        Aware: _common_pb2.Void
        Panic: _common_pb2.Void
        Quiet: _common_pb2.Void
        def __init__(self, Off: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Idle: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Armed: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Aware: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Panic: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Quiet: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    DOOR_OPEN_DRIVER_FRONT_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_DRIVER_REAR_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_PASSENGER_FRONT_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_PASSENGER_REAR_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_TRUNK_FRONT_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_TRUNK_REAR_FIELD_NUMBER: _ClassVar[int]
    WINDOW_OPEN_DRIVER_FRONT_FIELD_NUMBER: _ClassVar[int]
    WINDOW_OPEN_PASSENGER_FRONT_FIELD_NUMBER: _ClassVar[int]
    WINDOW_OPEN_DRIVER_REAR_FIELD_NUMBER: _ClassVar[int]
    WINDOW_OPEN_PASSENGER_REAR_FIELD_NUMBER: _ClassVar[int]
    SUN_ROOF_STATE_FIELD_NUMBER: _ClassVar[int]
    SUN_ROOF_PERCENT_OPEN_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    IS_USER_PRESENT_FIELD_NUMBER: _ClassVar[int]
    CENTER_DISPLAY_STATE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_START_FIELD_NUMBER: _ClassVar[int]
    VALET_MODE_FIELD_NUMBER: _ClassVar[int]
    VALET_PIN_NEEDED_FIELD_NUMBER: _ClassVar[int]
    SENTRY_MODE_STATE_FIELD_NUMBER: _ClassVar[int]
    SENTRY_MODE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SPEED_LIMIT_MODE_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_STATE_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_PERCENT_OPEN_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_IN_MOTION_FIELD_NUMBER: _ClassVar[int]
    HAS_AUTOMATIC_TONNEAU_FIELD_NUMBER: _ClassVar[int]
    HAS_SIDE_STORAGE_DOORS_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_SIDE_STORAGE_LEFT_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_SIDE_STORAGE_RIGHT_FIELD_NUMBER: _ClassVar[int]
    CRUISE_SPEED_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    door_open_driver_front: bool
    door_open_driver_rear: bool
    door_open_passenger_front: bool
    door_open_passenger_rear: bool
    door_open_trunk_front: bool
    door_open_trunk_rear: bool
    window_open_driver_front: bool
    window_open_passenger_front: bool
    window_open_driver_rear: bool
    window_open_passenger_rear: bool
    sun_roof_state: ClosuresState.SunRoofState
    sun_roof_percent_open: int
    locked: bool
    is_user_present: bool
    center_display_state: ClosuresState.DisplayState
    remote_start: bool
    valet_mode: bool
    valet_pin_needed: bool
    sentry_mode_state: ClosuresState.SentryModeState
    sentry_mode_available: bool
    speed_limit_mode: SpeedLimitMode
    tonneau_state: _vcsec_pb2.ClosureState_E
    tonneau_percent_open: int
    tonneau_in_motion: bool
    has_automatic_tonneau: bool
    has_side_storage_doors: bool
    door_open_side_storage_left: bool
    door_open_side_storage_right: bool
    cruise_speed_limit_mph: float
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, door_open_driver_front: _Optional[bool] = ..., door_open_driver_rear: _Optional[bool] = ..., door_open_passenger_front: _Optional[bool] = ..., door_open_passenger_rear: _Optional[bool] = ..., door_open_trunk_front: _Optional[bool] = ..., door_open_trunk_rear: _Optional[bool] = ..., window_open_driver_front: _Optional[bool] = ..., window_open_passenger_front: _Optional[bool] = ..., window_open_driver_rear: _Optional[bool] = ..., window_open_passenger_rear: _Optional[bool] = ..., sun_roof_state: _Optional[_Union[ClosuresState.SunRoofState, _Mapping]] = ..., sun_roof_percent_open: _Optional[int] = ..., locked: _Optional[bool] = ..., is_user_present: _Optional[bool] = ..., center_display_state: _Optional[_Union[ClosuresState.DisplayState, _Mapping]] = ..., remote_start: _Optional[bool] = ..., valet_mode: _Optional[bool] = ..., valet_pin_needed: _Optional[bool] = ..., sentry_mode_state: _Optional[_Union[ClosuresState.SentryModeState, _Mapping]] = ..., sentry_mode_available: _Optional[bool] = ..., speed_limit_mode: _Optional[_Union[SpeedLimitMode, _Mapping]] = ..., tonneau_state: _Optional[_Union[_vcsec_pb2.ClosureState_E, str]] = ..., tonneau_percent_open: _Optional[int] = ..., tonneau_in_motion: _Optional[bool] = ..., has_automatic_tonneau: _Optional[bool] = ..., has_side_storage_doors: _Optional[bool] = ..., door_open_side_storage_left: _Optional[bool] = ..., door_open_side_storage_right: _Optional[bool] = ..., cruise_speed_limit_mph: _Optional[float] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ChargeScheduleState(_message.Message):
    __slots__ = ("charge_schedules", "charge_schedule_window", "charge_buffer", "max_num_charge_schedules", "next_schedule", "show_schedule_complete_state", "timestamp")
    CHARGE_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    CHARGE_SCHEDULE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    CHARGE_BUFFER_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_CHARGE_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SHOW_SCHEDULE_COMPLETE_STATE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    charge_schedules: _containers.RepeatedCompositeFieldContainer[_common_pb2.ChargeSchedule]
    charge_schedule_window: _common_pb2.ChargeSchedule
    charge_buffer: int
    max_num_charge_schedules: int
    next_schedule: bool
    show_schedule_complete_state: bool
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, charge_schedules: _Optional[_Iterable[_Union[_common_pb2.ChargeSchedule, _Mapping]]] = ..., charge_schedule_window: _Optional[_Union[_common_pb2.ChargeSchedule, _Mapping]] = ..., charge_buffer: _Optional[int] = ..., max_num_charge_schedules: _Optional[int] = ..., next_schedule: _Optional[bool] = ..., show_schedule_complete_state: _Optional[bool] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PreconditioningScheduleState(_message.Message):
    __slots__ = ("precondition_schedules", "preconditioning_schedule_window", "max_num_precondition_schedules", "next_schedule", "timestamp")
    PRECONDITION_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_SCHEDULE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_PRECONDITION_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    precondition_schedules: _containers.RepeatedCompositeFieldContainer[_common_pb2.PreconditionSchedule]
    preconditioning_schedule_window: _common_pb2.PreconditionSchedule
    max_num_precondition_schedules: int
    next_schedule: bool
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, precondition_schedules: _Optional[_Iterable[_Union[_common_pb2.PreconditionSchedule, _Mapping]]] = ..., preconditioning_schedule_window: _Optional[_Union[_common_pb2.PreconditionSchedule, _Mapping]] = ..., max_num_precondition_schedules: _Optional[int] = ..., next_schedule: _Optional[bool] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SpeedLimitMode(_message.Message):
    __slots__ = ("active", "pin_code_set", "max_limit_mph", "min_limit_mph", "current_limit_mph")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PIN_CODE_SET_FIELD_NUMBER: _ClassVar[int]
    MAX_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    MIN_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    active: bool
    pin_code_set: bool
    max_limit_mph: float
    min_limit_mph: float
    current_limit_mph: float
    def __init__(self, active: _Optional[bool] = ..., pin_code_set: _Optional[bool] = ..., max_limit_mph: _Optional[float] = ..., min_limit_mph: _Optional[float] = ..., current_limit_mph: _Optional[float] = ...) -> None: ...

class ParentalControlsSettings(_message.Message):
    __slots__ = ("speed_limit_enabled", "max_limit_mph", "min_limit_mph", "current_limit_mph", "chill_acceleration_enabled", "require_safety_settings_enabled", "curfew_enabled", "curfew_start_time", "curfew_end_time", "browser_blocked", "theater_blocked", "arcade_blocked")
    SPEED_LIMIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    MIN_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    CHILL_ACCELERATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_SAFETY_SETTINGS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CURFEW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CURFEW_START_TIME_FIELD_NUMBER: _ClassVar[int]
    CURFEW_END_TIME_FIELD_NUMBER: _ClassVar[int]
    BROWSER_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    THEATER_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    ARCADE_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    speed_limit_enabled: bool
    max_limit_mph: float
    min_limit_mph: float
    current_limit_mph: float
    chill_acceleration_enabled: bool
    require_safety_settings_enabled: bool
    curfew_enabled: bool
    curfew_start_time: int
    curfew_end_time: int
    browser_blocked: bool
    theater_blocked: bool
    arcade_blocked: bool
    def __init__(self, speed_limit_enabled: _Optional[bool] = ..., max_limit_mph: _Optional[float] = ..., min_limit_mph: _Optional[float] = ..., current_limit_mph: _Optional[float] = ..., chill_acceleration_enabled: _Optional[bool] = ..., require_safety_settings_enabled: _Optional[bool] = ..., curfew_enabled: _Optional[bool] = ..., curfew_start_time: _Optional[int] = ..., curfew_end_time: _Optional[int] = ..., browser_blocked: _Optional[bool] = ..., theater_blocked: _Optional[bool] = ..., arcade_blocked: _Optional[bool] = ...) -> None: ...

class ParentalControlsState(_message.Message):
    __slots__ = ("timestamp", "parental_controls_active", "parental_controls_pin_set", "parental_controls_settings")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_PIN_SET_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    parental_controls_active: bool
    parental_controls_pin_set: bool
    parental_controls_settings: ParentalControlsSettings
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., parental_controls_active: _Optional[bool] = ..., parental_controls_pin_set: _Optional[bool] = ..., parental_controls_settings: _Optional[_Union[ParentalControlsSettings, _Mapping]] = ...) -> None: ...

class SoftwareUpdateState(_message.Message):
    __slots__ = ("status", "scheduled_time_ms", "warning_time_remaining_ms", "expected_duration_sec", "download_perc", "install_perc", "version", "timestamp", "auto_scheduled")
    class SoftwareUpdateStatus(_message.Message):
        __slots__ = ("Unknown", "Installing", "Scheduled", "Available", "DownloadingWifiWait", "Downloading")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        INSTALLING_FIELD_NUMBER: _ClassVar[int]
        SCHEDULED_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADINGWIFIWAIT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADING_FIELD_NUMBER: _ClassVar[int]
        Unknown: _common_pb2.Void
        Installing: _common_pb2.Void
        Scheduled: _common_pb2.Void
        Available: _common_pb2.Void
        DownloadingWifiWait: _common_pb2.Void
        Downloading: _common_pb2.Void
        def __init__(self, Unknown: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Installing: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Scheduled: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Available: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., DownloadingWifiWait: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Downloading: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    WARNING_TIME_REMAINING_MS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DURATION_SEC_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_PERC_FIELD_NUMBER: _ClassVar[int]
    INSTALL_PERC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AUTO_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    status: SoftwareUpdateState.SoftwareUpdateStatus
    scheduled_time_ms: int
    warning_time_remaining_ms: int
    expected_duration_sec: int
    download_perc: int
    install_perc: int
    version: str
    timestamp: _timestamp_pb2.Timestamp
    auto_scheduled: bool
    def __init__(self, status: _Optional[_Union[SoftwareUpdateState.SoftwareUpdateStatus, _Mapping]] = ..., scheduled_time_ms: _Optional[int] = ..., warning_time_remaining_ms: _Optional[int] = ..., expected_duration_sec: _Optional[int] = ..., download_perc: _Optional[int] = ..., install_perc: _Optional[int] = ..., version: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., auto_scheduled: _Optional[bool] = ...) -> None: ...

class DriveState(_message.Message):
    __slots__ = ("shift_state", "speed", "power", "timestamp", "odometer_in_hundredths_of_a_mile", "speed_float", "active_route_destination", "active_route_minutes_to_arrival", "active_route_miles_to_arrival", "active_route_traffic_minutes_delay", "active_route_energy_at_arrival", "last_route_update", "last_traffic_update", "active_route_coordinates", "fsd_user_total_miles_travelled", "fsd_user_total_miles", "fsd_user_miles_hands_free_current", "fsd_user_miles_hands_free_max", "fsd_total_miles_this_month", "fsd_monthly_history", "fsd_streak_days", "fsd_last_7_days_usage", "rainbow_road_enabled", "fsd_active")
    class FsdMonthlyMileage(_message.Message):
        __slots__ = ("year_month", "fsd_miles", "total_miles")
        YEAR_MONTH_FIELD_NUMBER: _ClassVar[int]
        FSD_MILES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_MILES_FIELD_NUMBER: _ClassVar[int]
        year_month: str
        fsd_miles: float
        total_miles: float
        def __init__(self, year_month: _Optional[str] = ..., fsd_miles: _Optional[float] = ..., total_miles: _Optional[float] = ...) -> None: ...
    class FsdLast7DaysUsage(_message.Message):
        __slots__ = ("week_starts_on_sunday", "day_usage")
        WEEK_STARTS_ON_SUNDAY_FIELD_NUMBER: _ClassVar[int]
        DAY_USAGE_FIELD_NUMBER: _ClassVar[int]
        week_starts_on_sunday: bool
        day_usage: _containers.RepeatedScalarFieldContainer[bool]
        def __init__(self, week_starts_on_sunday: _Optional[bool] = ..., day_usage: _Optional[_Iterable[bool]] = ...) -> None: ...
    SHIFT_STATE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ODOMETER_IN_HUNDREDTHS_OF_A_MILE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_MINUTES_TO_ARRIVAL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_MILES_TO_ARRIVAL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_TRAFFIC_MINUTES_DELAY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_ENERGY_AT_ARRIVAL_FIELD_NUMBER: _ClassVar[int]
    LAST_ROUTE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    LAST_TRAFFIC_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    FSD_USER_TOTAL_MILES_TRAVELLED_FIELD_NUMBER: _ClassVar[int]
    FSD_USER_TOTAL_MILES_FIELD_NUMBER: _ClassVar[int]
    FSD_USER_MILES_HANDS_FREE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    FSD_USER_MILES_HANDS_FREE_MAX_FIELD_NUMBER: _ClassVar[int]
    FSD_TOTAL_MILES_THIS_MONTH_FIELD_NUMBER: _ClassVar[int]
    FSD_MONTHLY_HISTORY_FIELD_NUMBER: _ClassVar[int]
    FSD_STREAK_DAYS_FIELD_NUMBER: _ClassVar[int]
    FSD_LAST_7_DAYS_USAGE_FIELD_NUMBER: _ClassVar[int]
    RAINBOW_ROAD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FSD_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    shift_state: ShiftState
    speed: int
    power: int
    timestamp: _timestamp_pb2.Timestamp
    odometer_in_hundredths_of_a_mile: int
    speed_float: float
    active_route_destination: str
    active_route_minutes_to_arrival: float
    active_route_miles_to_arrival: float
    active_route_traffic_minutes_delay: float
    active_route_energy_at_arrival: float
    last_route_update: int
    last_traffic_update: _timestamp_pb2.Timestamp
    active_route_coordinates: _common_pb2.LatLong
    fsd_user_total_miles_travelled: float
    fsd_user_total_miles: float
    fsd_user_miles_hands_free_current: float
    fsd_user_miles_hands_free_max: float
    fsd_total_miles_this_month: float
    fsd_monthly_history: _containers.RepeatedCompositeFieldContainer[DriveState.FsdMonthlyMileage]
    fsd_streak_days: int
    fsd_last_7_days_usage: DriveState.FsdLast7DaysUsage
    rainbow_road_enabled: bool
    fsd_active: bool
    def __init__(self, shift_state: _Optional[_Union[ShiftState, _Mapping]] = ..., speed: _Optional[int] = ..., power: _Optional[int] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., odometer_in_hundredths_of_a_mile: _Optional[int] = ..., speed_float: _Optional[float] = ..., active_route_destination: _Optional[str] = ..., active_route_minutes_to_arrival: _Optional[float] = ..., active_route_miles_to_arrival: _Optional[float] = ..., active_route_traffic_minutes_delay: _Optional[float] = ..., active_route_energy_at_arrival: _Optional[float] = ..., last_route_update: _Optional[int] = ..., last_traffic_update: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., active_route_coordinates: _Optional[_Union[_common_pb2.LatLong, _Mapping]] = ..., fsd_user_total_miles_travelled: _Optional[float] = ..., fsd_user_total_miles: _Optional[float] = ..., fsd_user_miles_hands_free_current: _Optional[float] = ..., fsd_user_miles_hands_free_max: _Optional[float] = ..., fsd_total_miles_this_month: _Optional[float] = ..., fsd_monthly_history: _Optional[_Iterable[_Union[DriveState.FsdMonthlyMileage, _Mapping]]] = ..., fsd_streak_days: _Optional[int] = ..., fsd_last_7_days_usage: _Optional[_Union[DriveState.FsdLast7DaysUsage, _Mapping]] = ..., rainbow_road_enabled: _Optional[bool] = ..., fsd_active: _Optional[bool] = ...) -> None: ...

class ChargeState(_message.Message):
    __slots__ = ("charging_state", "fast_charger_type", "fast_charger_brand", "charge_limit_soc", "charge_limit_soc_std", "charge_limit_soc_min", "charge_limit_soc_max", "max_range_charge_counter", "fast_charger_present", "battery_range", "est_battery_range", "ideal_battery_range", "battery_level", "usable_battery_level", "charge_energy_added", "charge_miles_added_rated", "charge_miles_added_ideal", "charger_voltage", "charger_pilot_current", "charger_actual_current", "charger_power", "minutes_to_full_charge", "minutes_to_charge_limit", "trip_charging", "charge_rate_mph", "charge_port_door_open", "conn_charge_cable", "scheduled_charging_start_time", "scheduled_charging_pending", "scheduled_departure_time", "user_charge_enable_request", "charge_enable_request", "charger_phases", "charge_port_latch", "charge_port_cold_weather_mode", "charge_current_request", "charge_current_request_max", "managed_charging_active", "managed_charging_user_canceled", "managed_charging_start_time", "timestamp", "preconditioning_times", "off_peak_charging_times", "off_peak_hours_end_time", "scheduled_charging_mode", "charging_amps", "scheduled_charging_start_time_minutes", "scheduled_departure_time_minutes", "preconditioning_enabled", "scheduled_charging_start_time_app", "supercharger_session_trip_planner", "charge_port_color", "charge_rate_mph_float", "charge_limit_reason", "managed_charging_state", "charge_cable_unlatched", "outlet_state", "power_feed_state", "outlet_soc_limit", "power_feed_soc_limit", "outlet_time_remaining", "power_feed_time_remaining", "powershare_feature_allowed", "powershare_feature_enabled", "powershare_request", "powershare_type", "powershare_status", "powershare_stop_reason", "powershare_instantaneous_load_kw", "powershare_vehicle_energy_left_hr", "powershare_soc_limit", "one_time_soc_limit", "home_location", "work_location", "outlet_max_timer_minutes", "batt_heat_min_to_start_charge", "batt_heat_min_to_start_charge_calculating", "has_ac_outlets", "paid_session_fee", "paid_session_fee_currency", "paid_session_kwh_rate", "discharge_limit_soe", "is_roaming", "paid_session_location_guid", "paid_session_pricebook_guid", "paid_session_start_time", "low_power_mode", "low_power_mode_forced_on", "convenience_features", "keep_accessory_power_mode", "should_hide_range_info")
    class ScheduledChargingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ScheduledChargingModeOff: _ClassVar[ChargeState.ScheduledChargingMode]
        ScheduledChargingModeStartAt: _ClassVar[ChargeState.ScheduledChargingMode]
        ScheduledChargingModeDepartBy: _ClassVar[ChargeState.ScheduledChargingMode]
    ScheduledChargingModeOff: ChargeState.ScheduledChargingMode
    ScheduledChargingModeStartAt: ChargeState.ScheduledChargingMode
    ScheduledChargingModeDepartBy: ChargeState.ScheduledChargingMode
    class ChargePortColor_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ChargePortColorOff: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorRed: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorGreen: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorBlue: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorWhite: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorFlashingGreen: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorFlashingAmber: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorAmber: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorRave: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorDebug: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorFlashingBlue: _ClassVar[ChargeState.ChargePortColor_E]
    ChargePortColorOff: ChargeState.ChargePortColor_E
    ChargePortColorRed: ChargeState.ChargePortColor_E
    ChargePortColorGreen: ChargeState.ChargePortColor_E
    ChargePortColorBlue: ChargeState.ChargePortColor_E
    ChargePortColorWhite: ChargeState.ChargePortColor_E
    ChargePortColorFlashingGreen: ChargeState.ChargePortColor_E
    ChargePortColorFlashingAmber: ChargeState.ChargePortColor_E
    ChargePortColorAmber: ChargeState.ChargePortColor_E
    ChargePortColorRave: ChargeState.ChargePortColor_E
    ChargePortColorDebug: ChargeState.ChargePortColor_E
    ChargePortColorFlashingBlue: ChargeState.ChargePortColor_E
    class ChargeLimitReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ChargeLimitReasonUnknown: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonNone: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonEvse: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonBattTempLow: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonHighSoc: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonCabin: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonEvseRelocationRecommended: _ClassVar[ChargeState.ChargeLimitReason]
    ChargeLimitReasonUnknown: ChargeState.ChargeLimitReason
    ChargeLimitReasonNone: ChargeState.ChargeLimitReason
    ChargeLimitReasonEvse: ChargeState.ChargeLimitReason
    ChargeLimitReasonBattTempLow: ChargeState.ChargeLimitReason
    ChargeLimitReasonHighSoc: ChargeState.ChargeLimitReason
    ChargeLimitReasonCabin: ChargeState.ChargeLimitReason
    ChargeLimitReasonEvseRelocationRecommended: ChargeState.ChargeLimitReason
    class OutletState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OutletStateOff: _ClassVar[ChargeState.OutletState]
        OutletStateCabinAndBed: _ClassVar[ChargeState.OutletState]
        OutletStateCabin: _ClassVar[ChargeState.OutletState]
    OutletStateOff: ChargeState.OutletState
    OutletStateCabinAndBed: ChargeState.OutletState
    OutletStateCabin: ChargeState.OutletState
    class PowerFeedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PowerFeedStateOff: _ClassVar[ChargeState.PowerFeedState]
        PowerFeedStateCabinAndBed: _ClassVar[ChargeState.PowerFeedState]
        PowerFeedStateCabin: _ClassVar[ChargeState.PowerFeedState]
    PowerFeedStateOff: ChargeState.PowerFeedState
    PowerFeedStateCabinAndBed: ChargeState.PowerFeedState
    PowerFeedStateCabin: ChargeState.PowerFeedState
    class PowershareStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PowershareStatusInactive: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusInit: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusActive: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusStopped: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusHandshaking: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusActiveReconnectingSoon: _ClassVar[ChargeState.PowershareStatus]
    PowershareStatusInactive: ChargeState.PowershareStatus
    PowershareStatusInit: ChargeState.PowershareStatus
    PowershareStatusActive: ChargeState.PowershareStatus
    PowershareStatusStopped: ChargeState.PowershareStatus
    PowershareStatusHandshaking: ChargeState.PowershareStatus
    PowershareStatusActiveReconnectingSoon: ChargeState.PowershareStatus
    class PowershareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PowershareTypeNone: _ClassVar[ChargeState.PowershareType]
        PowershareTypeLoad: _ClassVar[ChargeState.PowershareType]
        PowershareTypeHome: _ClassVar[ChargeState.PowershareType]
        PowershareTypeGrid: _ClassVar[ChargeState.PowershareType]
        PowershareTypePowerwall: _ClassVar[ChargeState.PowershareType]
    PowershareTypeNone: ChargeState.PowershareType
    PowershareTypeLoad: ChargeState.PowershareType
    PowershareTypeHome: ChargeState.PowershareType
    PowershareTypeGrid: ChargeState.PowershareType
    PowershareTypePowerwall: ChargeState.PowershareType
    class PowershareStopReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PowershareStopReasonNone: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonSOCTooLow: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonRetry: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonFault: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonUser: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonReconnecting: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonAuthentication: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonAdapterUpdating: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonAdapterInitializationFailed: _ClassVar[ChargeState.PowershareStopReason]
    PowershareStopReasonNone: ChargeState.PowershareStopReason
    PowershareStopReasonSOCTooLow: ChargeState.PowershareStopReason
    PowershareStopReasonRetry: ChargeState.PowershareStopReason
    PowershareStopReasonFault: ChargeState.PowershareStopReason
    PowershareStopReasonUser: ChargeState.PowershareStopReason
    PowershareStopReasonReconnecting: ChargeState.PowershareStopReason
    PowershareStopReasonAuthentication: ChargeState.PowershareStopReason
    PowershareStopReasonAdapterUpdating: ChargeState.PowershareStopReason
    PowershareStopReasonAdapterInitializationFailed: ChargeState.PowershareStopReason
    class CableType(_message.Message):
        __slots__ = ("SNA", "IEC", "SAE", "GB_AC", "GB_DC")
        SNA_FIELD_NUMBER: _ClassVar[int]
        IEC_FIELD_NUMBER: _ClassVar[int]
        SAE_FIELD_NUMBER: _ClassVar[int]
        GB_AC_FIELD_NUMBER: _ClassVar[int]
        GB_DC_FIELD_NUMBER: _ClassVar[int]
        SNA: _common_pb2.Void
        IEC: _common_pb2.Void
        SAE: _common_pb2.Void
        GB_AC: _common_pb2.Void
        GB_DC: _common_pb2.Void
        def __init__(self, SNA: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., IEC: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SAE: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., GB_AC: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., GB_DC: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class ChargerType(_message.Message):
        __slots__ = ("SNA", "Supercharger", "Chademo", "Gb", "ACSingleWireCAN", "Combo", "MCSingleWireCAN", "Other", "Tesla")
        SNA_FIELD_NUMBER: _ClassVar[int]
        SUPERCHARGER_FIELD_NUMBER: _ClassVar[int]
        CHADEMO_FIELD_NUMBER: _ClassVar[int]
        GB_FIELD_NUMBER: _ClassVar[int]
        ACSINGLEWIRECAN_FIELD_NUMBER: _ClassVar[int]
        COMBO_FIELD_NUMBER: _ClassVar[int]
        MCSINGLEWIRECAN_FIELD_NUMBER: _ClassVar[int]
        OTHER_FIELD_NUMBER: _ClassVar[int]
        TESLA_FIELD_NUMBER: _ClassVar[int]
        SNA: _common_pb2.Void
        Supercharger: _common_pb2.Void
        Chademo: _common_pb2.Void
        Gb: _common_pb2.Void
        ACSingleWireCAN: _common_pb2.Void
        Combo: _common_pb2.Void
        MCSingleWireCAN: _common_pb2.Void
        Other: _common_pb2.Void
        Tesla: _common_pb2.Void
        def __init__(self, SNA: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Supercharger: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Chademo: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Gb: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ACSingleWireCAN: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Combo: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MCSingleWireCAN: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Other: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Tesla: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class ChargingState(_message.Message):
        __slots__ = ("Unknown", "Disconnected", "NoPower", "Starting", "Charging", "Complete", "Stopped", "Calibrating")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
        NOPOWER_FIELD_NUMBER: _ClassVar[int]
        STARTING_FIELD_NUMBER: _ClassVar[int]
        CHARGING_FIELD_NUMBER: _ClassVar[int]
        COMPLETE_FIELD_NUMBER: _ClassVar[int]
        STOPPED_FIELD_NUMBER: _ClassVar[int]
        CALIBRATING_FIELD_NUMBER: _ClassVar[int]
        Unknown: _common_pb2.Void
        Disconnected: _common_pb2.Void
        NoPower: _common_pb2.Void
        Starting: _common_pb2.Void
        Charging: _common_pb2.Void
        Complete: _common_pb2.Void
        Stopped: _common_pb2.Void
        Calibrating: _common_pb2.Void
        def __init__(self, Unknown: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Disconnected: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., NoPower: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Starting: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Charging: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Complete: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Stopped: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Calibrating: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class ChargerBrand(_message.Message):
        __slots__ = ("Tesla", "SNA")
        TESLA_FIELD_NUMBER: _ClassVar[int]
        SNA_FIELD_NUMBER: _ClassVar[int]
        Tesla: _common_pb2.Void
        SNA: _common_pb2.Void
        def __init__(self, Tesla: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SNA: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    CHARGING_STATE_FIELD_NUMBER: _ClassVar[int]
    FAST_CHARGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FAST_CHARGER_BRAND_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_SOC_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_SOC_STD_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_SOC_MIN_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_SOC_MAX_FIELD_NUMBER: _ClassVar[int]
    MAX_RANGE_CHARGE_COUNTER_FIELD_NUMBER: _ClassVar[int]
    FAST_CHARGER_PRESENT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_RANGE_FIELD_NUMBER: _ClassVar[int]
    EST_BATTERY_RANGE_FIELD_NUMBER: _ClassVar[int]
    IDEAL_BATTERY_RANGE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    USABLE_BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHARGE_ENERGY_ADDED_FIELD_NUMBER: _ClassVar[int]
    CHARGE_MILES_ADDED_RATED_FIELD_NUMBER: _ClassVar[int]
    CHARGE_MILES_ADDED_IDEAL_FIELD_NUMBER: _ClassVar[int]
    CHARGER_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    CHARGER_PILOT_CURRENT_FIELD_NUMBER: _ClassVar[int]
    CHARGER_ACTUAL_CURRENT_FIELD_NUMBER: _ClassVar[int]
    CHARGER_POWER_FIELD_NUMBER: _ClassVar[int]
    MINUTES_TO_FULL_CHARGE_FIELD_NUMBER: _ClassVar[int]
    MINUTES_TO_CHARGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRIP_CHARGING_FIELD_NUMBER: _ClassVar[int]
    CHARGE_RATE_MPH_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_DOOR_OPEN_FIELD_NUMBER: _ClassVar[int]
    CONN_CHARGE_CABLE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_PENDING_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_CHARGE_ENABLE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHARGE_ENABLE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHARGER_PHASES_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_LATCH_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_COLD_WEATHER_MODE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_CURRENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHARGE_CURRENT_REQUEST_MAX_FIELD_NUMBER: _ClassVar[int]
    MANAGED_CHARGING_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MANAGED_CHARGING_USER_CANCELED_FIELD_NUMBER: _ClassVar[int]
    MANAGED_CHARGING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_TIMES_FIELD_NUMBER: _ClassVar[int]
    OFF_PEAK_CHARGING_TIMES_FIELD_NUMBER: _ClassVar[int]
    OFF_PEAK_HOURS_END_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_MODE_FIELD_NUMBER: _ClassVar[int]
    CHARGING_AMPS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_START_TIME_MINUTES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DEPARTURE_TIME_MINUTES_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_START_TIME_APP_FIELD_NUMBER: _ClassVar[int]
    SUPERCHARGER_SESSION_TRIP_PLANNER_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_COLOR_FIELD_NUMBER: _ClassVar[int]
    CHARGE_RATE_MPH_FLOAT_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_REASON_FIELD_NUMBER: _ClassVar[int]
    MANAGED_CHARGING_STATE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_CABLE_UNLATCHED_FIELD_NUMBER: _ClassVar[int]
    OUTLET_STATE_FIELD_NUMBER: _ClassVar[int]
    POWER_FEED_STATE_FIELD_NUMBER: _ClassVar[int]
    OUTLET_SOC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    POWER_FEED_SOC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OUTLET_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    POWER_FEED_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_FEATURE_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_STATUS_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_INSTANTANEOUS_LOAD_KW_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_VEHICLE_ENERGY_LEFT_HR_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_SOC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_SOC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    HOME_LOCATION_FIELD_NUMBER: _ClassVar[int]
    WORK_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OUTLET_MAX_TIMER_MINUTES_FIELD_NUMBER: _ClassVar[int]
    BATT_HEAT_MIN_TO_START_CHARGE_FIELD_NUMBER: _ClassVar[int]
    BATT_HEAT_MIN_TO_START_CHARGE_CALCULATING_FIELD_NUMBER: _ClassVar[int]
    HAS_AC_OUTLETS_FIELD_NUMBER: _ClassVar[int]
    PAID_SESSION_FEE_FIELD_NUMBER: _ClassVar[int]
    PAID_SESSION_FEE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PAID_SESSION_KWH_RATE_FIELD_NUMBER: _ClassVar[int]
    DISCHARGE_LIMIT_SOE_FIELD_NUMBER: _ClassVar[int]
    IS_ROAMING_FIELD_NUMBER: _ClassVar[int]
    PAID_SESSION_LOCATION_GUID_FIELD_NUMBER: _ClassVar[int]
    PAID_SESSION_PRICEBOOK_GUID_FIELD_NUMBER: _ClassVar[int]
    PAID_SESSION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LOW_POWER_MODE_FIELD_NUMBER: _ClassVar[int]
    LOW_POWER_MODE_FORCED_ON_FIELD_NUMBER: _ClassVar[int]
    CONVENIENCE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    KEEP_ACCESSORY_POWER_MODE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_HIDE_RANGE_INFO_FIELD_NUMBER: _ClassVar[int]
    charging_state: ChargeState.ChargingState
    fast_charger_type: ChargeState.ChargerType
    fast_charger_brand: ChargeState.ChargerBrand
    charge_limit_soc: int
    charge_limit_soc_std: int
    charge_limit_soc_min: int
    charge_limit_soc_max: int
    max_range_charge_counter: int
    fast_charger_present: bool
    battery_range: float
    est_battery_range: float
    ideal_battery_range: float
    battery_level: int
    usable_battery_level: int
    charge_energy_added: float
    charge_miles_added_rated: float
    charge_miles_added_ideal: float
    charger_voltage: int
    charger_pilot_current: int
    charger_actual_current: int
    charger_power: int
    minutes_to_full_charge: int
    minutes_to_charge_limit: int
    trip_charging: bool
    charge_rate_mph: int
    charge_port_door_open: bool
    conn_charge_cable: ChargeState.CableType
    scheduled_charging_start_time: int
    scheduled_charging_pending: bool
    scheduled_departure_time: _timestamp_pb2.Timestamp
    user_charge_enable_request: bool
    charge_enable_request: bool
    charger_phases: int
    charge_port_latch: _common_pb2.ChargePortLatchState
    charge_port_cold_weather_mode: bool
    charge_current_request: int
    charge_current_request_max: int
    managed_charging_active: bool
    managed_charging_user_canceled: bool
    managed_charging_start_time: int
    timestamp: _timestamp_pb2.Timestamp
    preconditioning_times: _common_pb2.PreconditioningTimes
    off_peak_charging_times: _common_pb2.OffPeakChargingTimes
    off_peak_hours_end_time: int
    scheduled_charging_mode: ChargeState.ScheduledChargingMode
    charging_amps: int
    scheduled_charging_start_time_minutes: int
    scheduled_departure_time_minutes: int
    preconditioning_enabled: bool
    scheduled_charging_start_time_app: int
    supercharger_session_trip_planner: bool
    charge_port_color: ChargeState.ChargePortColor_E
    charge_rate_mph_float: float
    charge_limit_reason: ChargeState.ChargeLimitReason
    managed_charging_state: ManagedChargingState
    charge_cable_unlatched: bool
    outlet_state: ChargeState.OutletState
    power_feed_state: ChargeState.PowerFeedState
    outlet_soc_limit: int
    power_feed_soc_limit: int
    outlet_time_remaining: int
    power_feed_time_remaining: int
    powershare_feature_allowed: bool
    powershare_feature_enabled: bool
    powershare_request: bool
    powershare_type: ChargeState.PowershareType
    powershare_status: ChargeState.PowershareStatus
    powershare_stop_reason: ChargeState.PowershareStopReason
    powershare_instantaneous_load_kw: float
    powershare_vehicle_energy_left_hr: int
    powershare_soc_limit: int
    one_time_soc_limit: int
    home_location: _common_pb2.LatLong
    work_location: _common_pb2.LatLong
    outlet_max_timer_minutes: int
    batt_heat_min_to_start_charge: int
    batt_heat_min_to_start_charge_calculating: bool
    has_ac_outlets: bool
    paid_session_fee: float
    paid_session_fee_currency: str
    paid_session_kwh_rate: float
    discharge_limit_soe: int
    is_roaming: bool
    paid_session_location_guid: str
    paid_session_pricebook_guid: str
    paid_session_start_time: _timestamp_pb2.Timestamp
    low_power_mode: bool
    low_power_mode_forced_on: bool
    convenience_features: int
    keep_accessory_power_mode: bool
    should_hide_range_info: bool
    def __init__(self, charging_state: _Optional[_Union[ChargeState.ChargingState, _Mapping]] = ..., fast_charger_type: _Optional[_Union[ChargeState.ChargerType, _Mapping]] = ..., fast_charger_brand: _Optional[_Union[ChargeState.ChargerBrand, _Mapping]] = ..., charge_limit_soc: _Optional[int] = ..., charge_limit_soc_std: _Optional[int] = ..., charge_limit_soc_min: _Optional[int] = ..., charge_limit_soc_max: _Optional[int] = ..., max_range_charge_counter: _Optional[int] = ..., fast_charger_present: _Optional[bool] = ..., battery_range: _Optional[float] = ..., est_battery_range: _Optional[float] = ..., ideal_battery_range: _Optional[float] = ..., battery_level: _Optional[int] = ..., usable_battery_level: _Optional[int] = ..., charge_energy_added: _Optional[float] = ..., charge_miles_added_rated: _Optional[float] = ..., charge_miles_added_ideal: _Optional[float] = ..., charger_voltage: _Optional[int] = ..., charger_pilot_current: _Optional[int] = ..., charger_actual_current: _Optional[int] = ..., charger_power: _Optional[int] = ..., minutes_to_full_charge: _Optional[int] = ..., minutes_to_charge_limit: _Optional[int] = ..., trip_charging: _Optional[bool] = ..., charge_rate_mph: _Optional[int] = ..., charge_port_door_open: _Optional[bool] = ..., conn_charge_cable: _Optional[_Union[ChargeState.CableType, _Mapping]] = ..., scheduled_charging_start_time: _Optional[int] = ..., scheduled_charging_pending: _Optional[bool] = ..., scheduled_departure_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_charge_enable_request: _Optional[bool] = ..., charge_enable_request: _Optional[bool] = ..., charger_phases: _Optional[int] = ..., charge_port_latch: _Optional[_Union[_common_pb2.ChargePortLatchState, _Mapping]] = ..., charge_port_cold_weather_mode: _Optional[bool] = ..., charge_current_request: _Optional[int] = ..., charge_current_request_max: _Optional[int] = ..., managed_charging_active: _Optional[bool] = ..., managed_charging_user_canceled: _Optional[bool] = ..., managed_charging_start_time: _Optional[int] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., preconditioning_times: _Optional[_Union[_common_pb2.PreconditioningTimes, _Mapping]] = ..., off_peak_charging_times: _Optional[_Union[_common_pb2.OffPeakChargingTimes, _Mapping]] = ..., off_peak_hours_end_time: _Optional[int] = ..., scheduled_charging_mode: _Optional[_Union[ChargeState.ScheduledChargingMode, str]] = ..., charging_amps: _Optional[int] = ..., scheduled_charging_start_time_minutes: _Optional[int] = ..., scheduled_departure_time_minutes: _Optional[int] = ..., preconditioning_enabled: _Optional[bool] = ..., scheduled_charging_start_time_app: _Optional[int] = ..., supercharger_session_trip_planner: _Optional[bool] = ..., charge_port_color: _Optional[_Union[ChargeState.ChargePortColor_E, str]] = ..., charge_rate_mph_float: _Optional[float] = ..., charge_limit_reason: _Optional[_Union[ChargeState.ChargeLimitReason, str]] = ..., managed_charging_state: _Optional[_Union[ManagedChargingState, _Mapping]] = ..., charge_cable_unlatched: _Optional[bool] = ..., outlet_state: _Optional[_Union[ChargeState.OutletState, str]] = ..., power_feed_state: _Optional[_Union[ChargeState.PowerFeedState, str]] = ..., outlet_soc_limit: _Optional[int] = ..., power_feed_soc_limit: _Optional[int] = ..., outlet_time_remaining: _Optional[int] = ..., power_feed_time_remaining: _Optional[int] = ..., powershare_feature_allowed: _Optional[bool] = ..., powershare_feature_enabled: _Optional[bool] = ..., powershare_request: _Optional[bool] = ..., powershare_type: _Optional[_Union[ChargeState.PowershareType, str]] = ..., powershare_status: _Optional[_Union[ChargeState.PowershareStatus, str]] = ..., powershare_stop_reason: _Optional[_Union[ChargeState.PowershareStopReason, str]] = ..., powershare_instantaneous_load_kw: _Optional[float] = ..., powershare_vehicle_energy_left_hr: _Optional[int] = ..., powershare_soc_limit: _Optional[int] = ..., one_time_soc_limit: _Optional[int] = ..., home_location: _Optional[_Union[_common_pb2.LatLong, _Mapping]] = ..., work_location: _Optional[_Union[_common_pb2.LatLong, _Mapping]] = ..., outlet_max_timer_minutes: _Optional[int] = ..., batt_heat_min_to_start_charge: _Optional[int] = ..., batt_heat_min_to_start_charge_calculating: _Optional[bool] = ..., has_ac_outlets: _Optional[bool] = ..., paid_session_fee: _Optional[float] = ..., paid_session_fee_currency: _Optional[str] = ..., paid_session_kwh_rate: _Optional[float] = ..., discharge_limit_soe: _Optional[int] = ..., is_roaming: _Optional[bool] = ..., paid_session_location_guid: _Optional[str] = ..., paid_session_pricebook_guid: _Optional[str] = ..., paid_session_start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., low_power_mode: _Optional[bool] = ..., low_power_mode_forced_on: _Optional[bool] = ..., convenience_features: _Optional[int] = ..., keep_accessory_power_mode: _Optional[bool] = ..., should_hide_range_info: _Optional[bool] = ...) -> None: ...

class ManagedChargingState(_message.Message):
    __slots__ = ("charge_on_solar_state", "charge_on_solar_gateway_din", "tesla_electric_asset_id", "minutes_to_lower_limit")
    CHARGE_ON_SOLAR_STATE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_ON_SOLAR_GATEWAY_DIN_FIELD_NUMBER: _ClassVar[int]
    TESLA_ELECTRIC_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    MINUTES_TO_LOWER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    charge_on_solar_state: ChargeOnSolarState
    charge_on_solar_gateway_din: str
    tesla_electric_asset_id: str
    minutes_to_lower_limit: int
    def __init__(self, charge_on_solar_state: _Optional[_Union[ChargeOnSolarState, _Mapping]] = ..., charge_on_solar_gateway_din: _Optional[str] = ..., tesla_electric_asset_id: _Optional[str] = ..., minutes_to_lower_limit: _Optional[int] = ...) -> None: ...

class ChargeOnSolarState(_message.Message):
    __slots__ = ("not_allowed", "no_charge_recommended", "charging_on_excess_solar", "charging_on_anything", "user_disabled", "waiting_for_server", "error", "user_stopped")
    NOT_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    NO_CHARGE_RECOMMENDED_FIELD_NUMBER: _ClassVar[int]
    CHARGING_ON_EXCESS_SOLAR_FIELD_NUMBER: _ClassVar[int]
    CHARGING_ON_ANYTHING_FIELD_NUMBER: _ClassVar[int]
    USER_DISABLED_FIELD_NUMBER: _ClassVar[int]
    WAITING_FOR_SERVER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_STOPPED_FIELD_NUMBER: _ClassVar[int]
    not_allowed: ChargeOnSolarStateNotAllowed
    no_charge_recommended: ChargeOnSolarStateNoChargeRecommended
    charging_on_excess_solar: ChargeOnSolarStateChargingOnExcessSolar
    charging_on_anything: ChargeOnSolarStateChargingOnAnything
    user_disabled: ChargeOnSolarStateUserDisabled
    waiting_for_server: ChargeOnSolarStateWaitingForServer
    error: ChargeOnSolarStateError
    user_stopped: ChargeOnSolarStateUserStopped
    def __init__(self, not_allowed: _Optional[_Union[ChargeOnSolarStateNotAllowed, _Mapping]] = ..., no_charge_recommended: _Optional[_Union[ChargeOnSolarStateNoChargeRecommended, _Mapping]] = ..., charging_on_excess_solar: _Optional[_Union[ChargeOnSolarStateChargingOnExcessSolar, _Mapping]] = ..., charging_on_anything: _Optional[_Union[ChargeOnSolarStateChargingOnAnything, _Mapping]] = ..., user_disabled: _Optional[_Union[ChargeOnSolarStateUserDisabled, _Mapping]] = ..., waiting_for_server: _Optional[_Union[ChargeOnSolarStateWaitingForServer, _Mapping]] = ..., error: _Optional[_Union[ChargeOnSolarStateError, _Mapping]] = ..., user_stopped: _Optional[_Union[ChargeOnSolarStateUserStopped, _Mapping]] = ...) -> None: ...

class ChargeOnSolarStateNotAllowed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChargeOnSolarStateNoChargeRecommended(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: _managed_charging_pb2.ChargeOnSolarNoChargeReason
    def __init__(self, reason: _Optional[_Union[_managed_charging_pb2.ChargeOnSolarNoChargeReason, str]] = ...) -> None: ...

class ChargeOnSolarStateChargingOnExcessSolar(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChargeOnSolarStateChargingOnAnything(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChargeOnSolarStateUserDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChargeOnSolarStateWaitingForServer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChargeOnSolarStateError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChargeOnSolarStateUserStopped(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocationState(_message.Message):
    __slots__ = ("latitude", "longitude", "heading", "gps_as_of", "native_location_supported", "native_latitude", "native_longitude", "native_type", "corrected_latitude", "corrected_longitude", "timestamp", "homelink_nearby", "location_name", "geo_latitude", "geo_longitude", "geo_heading", "geo_elevation", "geo_accuracy", "estimated_gps_valid", "estimated_to_raw_distance", "supercharger_trt_id", "native_latitude_d", "native_longitude_d", "geo_latitude_d", "geo_longitude_d", "geo_hw_raw_latitude_d", "geo_hw_raw_longitude_d", "geo_horizontal_accuracy")
    class GPSCoordinateType(_message.Message):
        __slots__ = ("GCJ", "WGS")
        GCJ_FIELD_NUMBER: _ClassVar[int]
        WGS_FIELD_NUMBER: _ClassVar[int]
        GCJ: _common_pb2.Void
        WGS: _common_pb2.Void
        def __init__(self, GCJ: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., WGS: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    GPS_AS_OF_FIELD_NUMBER: _ClassVar[int]
    NATIVE_LOCATION_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    NATIVE_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HOMELINK_NEARBY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    GEO_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    GEO_HEADING_FIELD_NUMBER: _ClassVar[int]
    GEO_ELEVATION_FIELD_NUMBER: _ClassVar[int]
    GEO_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_GPS_VALID_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TO_RAW_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    SUPERCHARGER_TRT_ID_FIELD_NUMBER: _ClassVar[int]
    NATIVE_LATITUDE_D_FIELD_NUMBER: _ClassVar[int]
    NATIVE_LONGITUDE_D_FIELD_NUMBER: _ClassVar[int]
    GEO_LATITUDE_D_FIELD_NUMBER: _ClassVar[int]
    GEO_LONGITUDE_D_FIELD_NUMBER: _ClassVar[int]
    GEO_HW_RAW_LATITUDE_D_FIELD_NUMBER: _ClassVar[int]
    GEO_HW_RAW_LONGITUDE_D_FIELD_NUMBER: _ClassVar[int]
    GEO_HORIZONTAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    heading: int
    gps_as_of: int
    native_location_supported: bool
    native_latitude: float
    native_longitude: float
    native_type: LocationState.GPSCoordinateType
    corrected_latitude: float
    corrected_longitude: float
    timestamp: _timestamp_pb2.Timestamp
    homelink_nearby: bool
    location_name: str
    geo_latitude: float
    geo_longitude: float
    geo_heading: float
    geo_elevation: float
    geo_accuracy: float
    estimated_gps_valid: bool
    estimated_to_raw_distance: float
    supercharger_trt_id: int
    native_latitude_d: float
    native_longitude_d: float
    geo_latitude_d: float
    geo_longitude_d: float
    geo_hw_raw_latitude_d: float
    geo_hw_raw_longitude_d: float
    geo_horizontal_accuracy: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., heading: _Optional[int] = ..., gps_as_of: _Optional[int] = ..., native_location_supported: _Optional[bool] = ..., native_latitude: _Optional[float] = ..., native_longitude: _Optional[float] = ..., native_type: _Optional[_Union[LocationState.GPSCoordinateType, _Mapping]] = ..., corrected_latitude: _Optional[float] = ..., corrected_longitude: _Optional[float] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., homelink_nearby: _Optional[bool] = ..., location_name: _Optional[str] = ..., geo_latitude: _Optional[float] = ..., geo_longitude: _Optional[float] = ..., geo_heading: _Optional[float] = ..., geo_elevation: _Optional[float] = ..., geo_accuracy: _Optional[float] = ..., estimated_gps_valid: _Optional[bool] = ..., estimated_to_raw_distance: _Optional[float] = ..., supercharger_trt_id: _Optional[int] = ..., native_latitude_d: _Optional[float] = ..., native_longitude_d: _Optional[float] = ..., geo_latitude_d: _Optional[float] = ..., geo_longitude_d: _Optional[float] = ..., geo_hw_raw_latitude_d: _Optional[float] = ..., geo_hw_raw_longitude_d: _Optional[float] = ..., geo_horizontal_accuracy: _Optional[float] = ...) -> None: ...

class VehicleState(_message.Message):
    __slots__ = ("autopark_style", "active_spoiler_state", "software_update_state", "legacy_media_state", "timestamp", "autopark_version", "autopark_state", "feature_bitmask", "tpms_last_seen_pressure_time_fl", "tpms_last_seen_pressure_time_fr", "tpms_last_seen_pressure_time_rl", "tpms_last_seen_pressure_time_rr", "legacy_media_info", "allow_authorized_mobile_devices_only", "guestMode", "drive_rail_on", "pin_to_drive_enabled", "pin_to_drive_pin_set", "frontfoglights_on", "rearfoglights_on", "headlights_on", "highbeamlights_on", "trailer_mode_on", "trailer_light_test_available", "trailer_light_test_requested", "truck_bed_lights_brightness", "signed_cmd_service_mode", "accessory_lightbar_middle_on", "transport_mode", "truck_bed_lights_auto_brightness", "truck_bed_lights_auto_state", "truck_bed_lights_controls_disabled", "service_mode_auth", "service_gtw_diag_session_active", "factory_mode", "training_wheels_mode", "gtw_diag_level", "parental_controls_active", "parental_controls_pin_set", "parental_controls_settings", "api_version", "car_version", "detailed_version", "autopilot_hash", "vehicle_name", "notifications_supported", "remote_start_supported", "remote_start_enabled", "last_autopark_error", "homelink_device_count", "smart_summon_available", "summon_standby_mode_enabled", "patsy_mode", "webcam_available", "vehicle_self_test_requested", "vehicle_self_test_progress", "calendar_supported", "dashcam_clip_save_available", "dashcam_state", "tpms_pressure_fl", "tpms_pressure_fr", "tpms_pressure_rl", "tpms_pressure_rr", "service_mode", "service_mode_plus", "tpms_hard_warning_fl", "tpms_hard_warning_fr", "tpms_hard_warning_rl", "tpms_hard_warning_rr", "tpms_soft_warning_fl", "tpms_soft_warning_fr", "tpms_soft_warning_rl", "tpms_soft_warning_rr", "tpms_rcp_front_value", "tpms_rcp_rear_value", "fsd_software_version")
    class GuestMode(_message.Message):
        __slots__ = ("GuestModeActive",)
        GUESTMODEACTIVE_FIELD_NUMBER: _ClassVar[int]
        GuestModeActive: bool
        def __init__(self, GuestModeActive: _Optional[bool] = ...) -> None: ...
    AUTOPARK_STYLE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SPOILER_STATE_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_UPDATE_STATE_FIELD_NUMBER: _ClassVar[int]
    LEGACY_MEDIA_STATE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AUTOPARK_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTOPARK_STATE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_BITMASK_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RR_FIELD_NUMBER: _ClassVar[int]
    LEGACY_MEDIA_INFO_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AUTHORIZED_MOBILE_DEVICES_ONLY_FIELD_NUMBER: _ClassVar[int]
    GUESTMODE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_RAIL_ON_FIELD_NUMBER: _ClassVar[int]
    PIN_TO_DRIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PIN_TO_DRIVE_PIN_SET_FIELD_NUMBER: _ClassVar[int]
    FRONTFOGLIGHTS_ON_FIELD_NUMBER: _ClassVar[int]
    REARFOGLIGHTS_ON_FIELD_NUMBER: _ClassVar[int]
    HEADLIGHTS_ON_FIELD_NUMBER: _ClassVar[int]
    HIGHBEAMLIGHTS_ON_FIELD_NUMBER: _ClassVar[int]
    TRAILER_MODE_ON_FIELD_NUMBER: _ClassVar[int]
    TRAILER_LIGHT_TEST_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    TRAILER_LIGHT_TEST_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    SIGNED_CMD_SERVICE_MODE_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_LIGHTBAR_MIDDLE_ON_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_AUTO_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_AUTO_STATE_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_CONTROLS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_MODE_AUTH_FIELD_NUMBER: _ClassVar[int]
    SERVICE_GTW_DIAG_SESSION_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FACTORY_MODE_FIELD_NUMBER: _ClassVar[int]
    TRAINING_WHEELS_MODE_FIELD_NUMBER: _ClassVar[int]
    GTW_DIAG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_PIN_SET_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    CAR_VERSION_FIELD_NUMBER: _ClassVar[int]
    DETAILED_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTOPILOT_HASH_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_NAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_START_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_START_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_AUTOPARK_ERROR_FIELD_NUMBER: _ClassVar[int]
    HOMELINK_DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SMART_SUMMON_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SUMMON_STANDBY_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PATSY_MODE_FIELD_NUMBER: _ClassVar[int]
    WEBCAM_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_SELF_TEST_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_SELF_TEST_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DASHCAM_CLIP_SAVE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DASHCAM_STATE_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RR_FIELD_NUMBER: _ClassVar[int]
    SERVICE_MODE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_MODE_PLUS_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_RCP_FRONT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TPMS_RCP_REAR_VALUE_FIELD_NUMBER: _ClassVar[int]
    FSD_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    autopark_style: AutoparkStyle
    active_spoiler_state: SpoilerState
    software_update_state: SoftwareUpdateState
    legacy_media_state: LegacyMediaState
    timestamp: _timestamp_pb2.Timestamp
    autopark_version: AutoparkVersion
    autopark_state: AutoparkState
    feature_bitmask: _containers.RepeatedScalarFieldContainer[int]
    tpms_last_seen_pressure_time_fl: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_fr: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_rl: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_rr: _timestamp_pb2.Timestamp
    legacy_media_info: LegacyMediaInfo
    allow_authorized_mobile_devices_only: bool
    guestMode: VehicleState.GuestMode
    drive_rail_on: bool
    pin_to_drive_enabled: bool
    pin_to_drive_pin_set: bool
    frontfoglights_on: bool
    rearfoglights_on: bool
    headlights_on: bool
    highbeamlights_on: bool
    trailer_mode_on: bool
    trailer_light_test_available: bool
    trailer_light_test_requested: bool
    truck_bed_lights_brightness: int
    signed_cmd_service_mode: bool
    accessory_lightbar_middle_on: bool
    transport_mode: bool
    truck_bed_lights_auto_brightness: int
    truck_bed_lights_auto_state: bool
    truck_bed_lights_controls_disabled: bool
    service_mode_auth: str
    service_gtw_diag_session_active: bool
    factory_mode: bool
    training_wheels_mode: bool
    gtw_diag_level: _common_pb2.GtwDiagLevel
    parental_controls_active: bool
    parental_controls_pin_set: bool
    parental_controls_settings: ParentalControlsSettings
    api_version: int
    car_version: str
    detailed_version: str
    autopilot_hash: str
    vehicle_name: str
    notifications_supported: bool
    remote_start_supported: bool
    remote_start_enabled: bool
    last_autopark_error: str
    homelink_device_count: int
    smart_summon_available: bool
    summon_standby_mode_enabled: bool
    patsy_mode: bool
    webcam_available: bool
    vehicle_self_test_requested: bool
    vehicle_self_test_progress: int
    calendar_supported: bool
    dashcam_clip_save_available: bool
    dashcam_state: DashCamState
    tpms_pressure_fl: float
    tpms_pressure_fr: float
    tpms_pressure_rl: float
    tpms_pressure_rr: float
    service_mode: bool
    service_mode_plus: bool
    tpms_hard_warning_fl: bool
    tpms_hard_warning_fr: bool
    tpms_hard_warning_rl: bool
    tpms_hard_warning_rr: bool
    tpms_soft_warning_fl: bool
    tpms_soft_warning_fr: bool
    tpms_soft_warning_rl: bool
    tpms_soft_warning_rr: bool
    tpms_rcp_front_value: float
    tpms_rcp_rear_value: float
    fsd_software_version: str
    def __init__(self, autopark_style: _Optional[_Union[AutoparkStyle, _Mapping]] = ..., active_spoiler_state: _Optional[_Union[SpoilerState, _Mapping]] = ..., software_update_state: _Optional[_Union[SoftwareUpdateState, _Mapping]] = ..., legacy_media_state: _Optional[_Union[LegacyMediaState, _Mapping]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., autopark_version: _Optional[_Union[AutoparkVersion, _Mapping]] = ..., autopark_state: _Optional[_Union[AutoparkState, _Mapping]] = ..., feature_bitmask: _Optional[_Iterable[int]] = ..., tpms_last_seen_pressure_time_fl: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_fr: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_rl: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_rr: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., legacy_media_info: _Optional[_Union[LegacyMediaInfo, _Mapping]] = ..., allow_authorized_mobile_devices_only: _Optional[bool] = ..., guestMode: _Optional[_Union[VehicleState.GuestMode, _Mapping]] = ..., drive_rail_on: _Optional[bool] = ..., pin_to_drive_enabled: _Optional[bool] = ..., pin_to_drive_pin_set: _Optional[bool] = ..., frontfoglights_on: _Optional[bool] = ..., rearfoglights_on: _Optional[bool] = ..., headlights_on: _Optional[bool] = ..., highbeamlights_on: _Optional[bool] = ..., trailer_mode_on: _Optional[bool] = ..., trailer_light_test_available: _Optional[bool] = ..., trailer_light_test_requested: _Optional[bool] = ..., truck_bed_lights_brightness: _Optional[int] = ..., signed_cmd_service_mode: _Optional[bool] = ..., accessory_lightbar_middle_on: _Optional[bool] = ..., transport_mode: _Optional[bool] = ..., truck_bed_lights_auto_brightness: _Optional[int] = ..., truck_bed_lights_auto_state: _Optional[bool] = ..., truck_bed_lights_controls_disabled: _Optional[bool] = ..., service_mode_auth: _Optional[str] = ..., service_gtw_diag_session_active: _Optional[bool] = ..., factory_mode: _Optional[bool] = ..., training_wheels_mode: _Optional[bool] = ..., gtw_diag_level: _Optional[_Union[_common_pb2.GtwDiagLevel, str]] = ..., parental_controls_active: _Optional[bool] = ..., parental_controls_pin_set: _Optional[bool] = ..., parental_controls_settings: _Optional[_Union[ParentalControlsSettings, _Mapping]] = ..., api_version: _Optional[int] = ..., car_version: _Optional[str] = ..., detailed_version: _Optional[str] = ..., autopilot_hash: _Optional[str] = ..., vehicle_name: _Optional[str] = ..., notifications_supported: _Optional[bool] = ..., remote_start_supported: _Optional[bool] = ..., remote_start_enabled: _Optional[bool] = ..., last_autopark_error: _Optional[str] = ..., homelink_device_count: _Optional[int] = ..., smart_summon_available: _Optional[bool] = ..., summon_standby_mode_enabled: _Optional[bool] = ..., patsy_mode: _Optional[bool] = ..., webcam_available: _Optional[bool] = ..., vehicle_self_test_requested: _Optional[bool] = ..., vehicle_self_test_progress: _Optional[int] = ..., calendar_supported: _Optional[bool] = ..., dashcam_clip_save_available: _Optional[bool] = ..., dashcam_state: _Optional[_Union[DashCamState, str]] = ..., tpms_pressure_fl: _Optional[float] = ..., tpms_pressure_fr: _Optional[float] = ..., tpms_pressure_rl: _Optional[float] = ..., tpms_pressure_rr: _Optional[float] = ..., service_mode: _Optional[bool] = ..., service_mode_plus: _Optional[bool] = ..., tpms_hard_warning_fl: _Optional[bool] = ..., tpms_hard_warning_fr: _Optional[bool] = ..., tpms_hard_warning_rl: _Optional[bool] = ..., tpms_hard_warning_rr: _Optional[bool] = ..., tpms_soft_warning_fl: _Optional[bool] = ..., tpms_soft_warning_fr: _Optional[bool] = ..., tpms_soft_warning_rl: _Optional[bool] = ..., tpms_soft_warning_rr: _Optional[bool] = ..., tpms_rcp_front_value: _Optional[float] = ..., tpms_rcp_rear_value: _Optional[float] = ..., fsd_software_version: _Optional[str] = ...) -> None: ...

class CurrentVehicleState(_message.Message):
    __slots__ = ("timestamp", "api_version", "notifications_supported", "remote_start_supported", "remote_start_enabled", "last_autopark_error", "homelink_device_count", "autopark_style", "smart_summon_available", "summon_standby_mode_enabled", "active_spoiler_state", "patsy_mode", "webcam_available", "vehicle_self_test_requested", "vehicle_self_test_progress", "autopark_version", "autopark_state", "calendar_supported", "dashcam_clip_save_available", "dashcam_state", "feature_bitmask", "service_mode", "service_mode_plus", "service_mode_auth", "service_gtw_diag_session_active", "allow_authorized_mobile_devices_only", "guest_mode", "drive_rail_on", "pin_to_drive_enabled", "pin_to_drive_pin_set", "frontfoglights_on", "rearfoglights_on", "headlights_on", "highbeamlights_on", "trailer_mode_on", "signed_cmd_service_mode", "transport_mode", "factory_mode", "training_wheels_mode", "gtw_diag_level", "trailer_light_test_available", "trailer_light_test_requested", "truck_bed_lights_brightness", "truck_bed_lights_auto_brightness", "truck_bed_lights_auto_state", "truck_bed_lights_controls_disabled", "accessory_lightbar_middle_on", "inlet_heater_on", "inlet_heater_supported", "field_53", "mobile_dashcam_viewer_enabled", "car_wrap_enabled", "dashcam_last_save_epoch", "wiper_service_request", "remote_photobooth_available", "dog_mode_live_activity_key", "photobooth_last_save_epoch", "photobooth_last_update_epoch", "fsd_stats_supported", "dashcam_utils", "remote_sketchpad_available", "deck_lights_on", "hazards_on", "deck_lights_allowed", "field_70", "halloween_mode", "trick_or_treat_mode")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_START_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_START_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_AUTOPARK_ERROR_FIELD_NUMBER: _ClassVar[int]
    HOMELINK_DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOPARK_STYLE_FIELD_NUMBER: _ClassVar[int]
    SMART_SUMMON_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SUMMON_STANDBY_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SPOILER_STATE_FIELD_NUMBER: _ClassVar[int]
    PATSY_MODE_FIELD_NUMBER: _ClassVar[int]
    WEBCAM_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_SELF_TEST_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_SELF_TEST_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    AUTOPARK_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTOPARK_STATE_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DASHCAM_CLIP_SAVE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DASHCAM_STATE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_BITMASK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_MODE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_MODE_PLUS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_MODE_AUTH_FIELD_NUMBER: _ClassVar[int]
    SERVICE_GTW_DIAG_SESSION_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AUTHORIZED_MOBILE_DEVICES_ONLY_FIELD_NUMBER: _ClassVar[int]
    GUEST_MODE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_RAIL_ON_FIELD_NUMBER: _ClassVar[int]
    PIN_TO_DRIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PIN_TO_DRIVE_PIN_SET_FIELD_NUMBER: _ClassVar[int]
    FRONTFOGLIGHTS_ON_FIELD_NUMBER: _ClassVar[int]
    REARFOGLIGHTS_ON_FIELD_NUMBER: _ClassVar[int]
    HEADLIGHTS_ON_FIELD_NUMBER: _ClassVar[int]
    HIGHBEAMLIGHTS_ON_FIELD_NUMBER: _ClassVar[int]
    TRAILER_MODE_ON_FIELD_NUMBER: _ClassVar[int]
    SIGNED_CMD_SERVICE_MODE_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    FACTORY_MODE_FIELD_NUMBER: _ClassVar[int]
    TRAINING_WHEELS_MODE_FIELD_NUMBER: _ClassVar[int]
    GTW_DIAG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TRAILER_LIGHT_TEST_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    TRAILER_LIGHT_TEST_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_AUTO_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_AUTO_STATE_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_CONTROLS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_LIGHTBAR_MIDDLE_ON_FIELD_NUMBER: _ClassVar[int]
    INLET_HEATER_ON_FIELD_NUMBER: _ClassVar[int]
    INLET_HEATER_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FIELD_53_FIELD_NUMBER: _ClassVar[int]
    MOBILE_DASHCAM_VIEWER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CAR_WRAP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DASHCAM_LAST_SAVE_EPOCH_FIELD_NUMBER: _ClassVar[int]
    WIPER_SERVICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PHOTOBOOTH_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DOG_MODE_LIVE_ACTIVITY_KEY_FIELD_NUMBER: _ClassVar[int]
    PHOTOBOOTH_LAST_SAVE_EPOCH_FIELD_NUMBER: _ClassVar[int]
    PHOTOBOOTH_LAST_UPDATE_EPOCH_FIELD_NUMBER: _ClassVar[int]
    FSD_STATS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DASHCAM_UTILS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SKETCHPAD_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DECK_LIGHTS_ON_FIELD_NUMBER: _ClassVar[int]
    HAZARDS_ON_FIELD_NUMBER: _ClassVar[int]
    DECK_LIGHTS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    FIELD_70_FIELD_NUMBER: _ClassVar[int]
    HALLOWEEN_MODE_FIELD_NUMBER: _ClassVar[int]
    TRICK_OR_TREAT_MODE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    api_version: int
    notifications_supported: bool
    remote_start_supported: bool
    remote_start_enabled: bool
    last_autopark_error: str
    homelink_device_count: int
    autopark_style: AutoparkStyle
    smart_summon_available: bool
    summon_standby_mode_enabled: bool
    active_spoiler_state: SpoilerState
    patsy_mode: bool
    webcam_available: bool
    vehicle_self_test_requested: bool
    vehicle_self_test_progress: int
    autopark_version: AutoparkVersion
    autopark_state: AutoparkState
    calendar_supported: bool
    dashcam_clip_save_available: bool
    dashcam_state: DashCamState
    feature_bitmask: _containers.RepeatedScalarFieldContainer[int]
    service_mode: bool
    service_mode_plus: bool
    service_mode_auth: str
    service_gtw_diag_session_active: bool
    allow_authorized_mobile_devices_only: bool
    guest_mode: VehicleState.GuestMode
    drive_rail_on: bool
    pin_to_drive_enabled: bool
    pin_to_drive_pin_set: bool
    frontfoglights_on: bool
    rearfoglights_on: bool
    headlights_on: bool
    highbeamlights_on: bool
    trailer_mode_on: bool
    signed_cmd_service_mode: bool
    transport_mode: bool
    factory_mode: bool
    training_wheels_mode: bool
    gtw_diag_level: _common_pb2.GtwDiagLevel
    trailer_light_test_available: bool
    trailer_light_test_requested: bool
    truck_bed_lights_brightness: int
    truck_bed_lights_auto_brightness: int
    truck_bed_lights_auto_state: bool
    truck_bed_lights_controls_disabled: bool
    accessory_lightbar_middle_on: bool
    inlet_heater_on: bool
    inlet_heater_supported: bool
    field_53: int
    mobile_dashcam_viewer_enabled: bool
    car_wrap_enabled: bool
    dashcam_last_save_epoch: int
    wiper_service_request: bool
    remote_photobooth_available: bool
    dog_mode_live_activity_key: str
    photobooth_last_save_epoch: int
    photobooth_last_update_epoch: int
    fsd_stats_supported: bool
    dashcam_utils: DashcamUtils
    remote_sketchpad_available: bool
    deck_lights_on: bool
    hazards_on: bool
    deck_lights_allowed: bool
    field_70: int
    halloween_mode: bool
    trick_or_treat_mode: bool
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., api_version: _Optional[int] = ..., notifications_supported: _Optional[bool] = ..., remote_start_supported: _Optional[bool] = ..., remote_start_enabled: _Optional[bool] = ..., last_autopark_error: _Optional[str] = ..., homelink_device_count: _Optional[int] = ..., autopark_style: _Optional[_Union[AutoparkStyle, _Mapping]] = ..., smart_summon_available: _Optional[bool] = ..., summon_standby_mode_enabled: _Optional[bool] = ..., active_spoiler_state: _Optional[_Union[SpoilerState, _Mapping]] = ..., patsy_mode: _Optional[bool] = ..., webcam_available: _Optional[bool] = ..., vehicle_self_test_requested: _Optional[bool] = ..., vehicle_self_test_progress: _Optional[int] = ..., autopark_version: _Optional[_Union[AutoparkVersion, _Mapping]] = ..., autopark_state: _Optional[_Union[AutoparkState, _Mapping]] = ..., calendar_supported: _Optional[bool] = ..., dashcam_clip_save_available: _Optional[bool] = ..., dashcam_state: _Optional[_Union[DashCamState, str]] = ..., feature_bitmask: _Optional[_Iterable[int]] = ..., service_mode: _Optional[bool] = ..., service_mode_plus: _Optional[bool] = ..., service_mode_auth: _Optional[str] = ..., service_gtw_diag_session_active: _Optional[bool] = ..., allow_authorized_mobile_devices_only: _Optional[bool] = ..., guest_mode: _Optional[_Union[VehicleState.GuestMode, _Mapping]] = ..., drive_rail_on: _Optional[bool] = ..., pin_to_drive_enabled: _Optional[bool] = ..., pin_to_drive_pin_set: _Optional[bool] = ..., frontfoglights_on: _Optional[bool] = ..., rearfoglights_on: _Optional[bool] = ..., headlights_on: _Optional[bool] = ..., highbeamlights_on: _Optional[bool] = ..., trailer_mode_on: _Optional[bool] = ..., signed_cmd_service_mode: _Optional[bool] = ..., transport_mode: _Optional[bool] = ..., factory_mode: _Optional[bool] = ..., training_wheels_mode: _Optional[bool] = ..., gtw_diag_level: _Optional[_Union[_common_pb2.GtwDiagLevel, str]] = ..., trailer_light_test_available: _Optional[bool] = ..., trailer_light_test_requested: _Optional[bool] = ..., truck_bed_lights_brightness: _Optional[int] = ..., truck_bed_lights_auto_brightness: _Optional[int] = ..., truck_bed_lights_auto_state: _Optional[bool] = ..., truck_bed_lights_controls_disabled: _Optional[bool] = ..., accessory_lightbar_middle_on: _Optional[bool] = ..., inlet_heater_on: _Optional[bool] = ..., inlet_heater_supported: _Optional[bool] = ..., field_53: _Optional[int] = ..., mobile_dashcam_viewer_enabled: _Optional[bool] = ..., car_wrap_enabled: _Optional[bool] = ..., dashcam_last_save_epoch: _Optional[int] = ..., wiper_service_request: _Optional[bool] = ..., remote_photobooth_available: _Optional[bool] = ..., dog_mode_live_activity_key: _Optional[str] = ..., photobooth_last_save_epoch: _Optional[int] = ..., photobooth_last_update_epoch: _Optional[int] = ..., fsd_stats_supported: _Optional[bool] = ..., dashcam_utils: _Optional[_Union[DashcamUtils, _Mapping]] = ..., remote_sketchpad_available: _Optional[bool] = ..., deck_lights_on: _Optional[bool] = ..., hazards_on: _Optional[bool] = ..., deck_lights_allowed: _Optional[bool] = ..., field_70: _Optional[int] = ..., halloween_mode: _Optional[bool] = ..., trick_or_treat_mode: _Optional[bool] = ...) -> None: ...

class DashcamUtils(_message.Message):
    __slots__ = ("delete_dashcam_clips_available", "format_usb_available")
    DELETE_DASHCAM_CLIPS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_USB_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    delete_dashcam_clips_available: bool
    format_usb_available: bool
    def __init__(self, delete_dashcam_clips_available: _Optional[bool] = ..., format_usb_available: _Optional[bool] = ...) -> None: ...

class AutoparkStyle(_message.Message):
    __slots__ = ("Deadman", "Standard")
    DEADMAN_FIELD_NUMBER: _ClassVar[int]
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    Deadman: _common_pb2.Void
    Standard: _common_pb2.Void
    def __init__(self, Deadman: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Standard: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class AutoparkVersion(_message.Message):
    __slots__ = ("Version2", "Version3", "Version4")
    VERSION2_FIELD_NUMBER: _ClassVar[int]
    VERSION3_FIELD_NUMBER: _ClassVar[int]
    VERSION4_FIELD_NUMBER: _ClassVar[int]
    Version2: _common_pb2.Void
    Version3: _common_pb2.Void
    Version4: _common_pb2.Void
    def __init__(self, Version2: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Version3: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Version4: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class AutoparkState(_message.Message):
    __slots__ = ("Standby", "Unavailable", "Ready", "ActiveForward", "ActiveReverse", "Disabled", "Panic", "Preparing", "Aborting", "Paused", "Resuming", "OpeningGate")
    STANDBY_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    ACTIVEFORWARD_FIELD_NUMBER: _ClassVar[int]
    ACTIVEREVERSE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    PANIC_FIELD_NUMBER: _ClassVar[int]
    PREPARING_FIELD_NUMBER: _ClassVar[int]
    ABORTING_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    RESUMING_FIELD_NUMBER: _ClassVar[int]
    OPENINGGATE_FIELD_NUMBER: _ClassVar[int]
    Standby: _common_pb2.Void
    Unavailable: _common_pb2.Void
    Ready: _common_pb2.Void
    ActiveForward: _common_pb2.Void
    ActiveReverse: _common_pb2.Void
    Disabled: _common_pb2.Void
    Panic: _common_pb2.Void
    Preparing: _common_pb2.Void
    Aborting: _common_pb2.Void
    Paused: _common_pb2.Void
    Resuming: _common_pb2.Void
    OpeningGate: _common_pb2.Void
    def __init__(self, Standby: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Unavailable: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Ready: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ActiveForward: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ActiveReverse: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Disabled: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Panic: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Preparing: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Aborting: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Paused: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Resuming: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., OpeningGate: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class SpoilerState(_message.Message):
    __slots__ = ("Unknown", "Retracted", "Extended", "Fault")
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    RETRACTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_FIELD_NUMBER: _ClassVar[int]
    FAULT_FIELD_NUMBER: _ClassVar[int]
    Unknown: _common_pb2.Void
    Retracted: _common_pb2.Void
    Extended: _common_pb2.Void
    Fault: _common_pb2.Void
    def __init__(self, Unknown: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Retracted: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Extended: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Fault: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class LegacyMediaState(_message.Message):
    __slots__ = ("remote_control_enabled",)
    REMOTE_CONTROL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    remote_control_enabled: bool
    def __init__(self, remote_control_enabled: _Optional[bool] = ...) -> None: ...

class LegacyMediaInfo(_message.Message):
    __slots__ = ("media_playback_status", "audio_volume", "now_playing_duration", "now_playing_elapsed", "now_playing_source", "now_playing_source_string", "now_playing_artist", "now_playing_title", "now_playing_album", "now_playing_station", "audio_volume_increment", "audio_volume_max", "a2dp_source_name")
    MEDIA_PLAYBACK_STATUS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_VOLUME_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_DURATION_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_ELAPSED_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_SOURCE_STRING_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_ARTIST_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_TITLE_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_ALBUM_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_STATION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_VOLUME_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_VOLUME_MAX_FIELD_NUMBER: _ClassVar[int]
    A2DP_SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    media_playback_status: _common_pb2.MediaPlaybackStatus
    audio_volume: float
    now_playing_duration: int
    now_playing_elapsed: int
    now_playing_source: MediaSourceType
    now_playing_source_string: str
    now_playing_artist: str
    now_playing_title: str
    now_playing_album: str
    now_playing_station: str
    audio_volume_increment: float
    audio_volume_max: float
    a2dp_source_name: str
    def __init__(self, media_playback_status: _Optional[_Union[_common_pb2.MediaPlaybackStatus, str]] = ..., audio_volume: _Optional[float] = ..., now_playing_duration: _Optional[int] = ..., now_playing_elapsed: _Optional[int] = ..., now_playing_source: _Optional[_Union[MediaSourceType, str]] = ..., now_playing_source_string: _Optional[str] = ..., now_playing_artist: _Optional[str] = ..., now_playing_title: _Optional[str] = ..., now_playing_album: _Optional[str] = ..., now_playing_station: _Optional[str] = ..., audio_volume_increment: _Optional[float] = ..., audio_volume_max: _Optional[float] = ..., a2dp_source_name: _Optional[str] = ...) -> None: ...

class ClimateState(_message.Message):
    __slots__ = ("inside_temp_celsius", "outside_temp_celsius", "driver_temp_setting", "passenger_temp_setting", "left_temp_direction", "right_temp_direction", "is_front_defroster_on", "is_rear_defroster_on", "fan_status", "is_climate_on", "min_avail_temp_celsius", "max_avail_temp_celsius", "seat_heater_left", "seat_heater_right", "seat_heater_rear_left", "seat_heater_rear_right", "seat_heater_rear_center", "seat_heater_rear_right_back", "seat_heater_rear_left_back", "seat_heater_third_row_right", "seat_heater_third_row_left", "battery_heater", "battery_heater_no_power", "steering_wheel_heater", "wiper_blade_heater", "side_mirror_heaters", "is_preconditioning", "remote_heater_control_enabled", "climate_keeper_mode", "timestamp", "bioweapon_mode_on", "defrost_mode", "is_auto_conditioning_on", "auto_seat_climate_left", "auto_seat_climate_right", "seat_fan_front_left", "seat_fan_front_right", "allow_cabin_overheat_protection", "supports_fan_only_cabin_overheat_protection", "cabin_overheat_protection", "cabin_overheat_protection_actively_cooling", "cop_activation_temperature", "auto_steering_wheel_heat", "steering_wheel_heat_level", "hvac_auto_request", "cop_not_running_reason", "seat_fan_second_row_left", "seat_fan_second_row_right", "dog_mode_state")
    class HvacAutoRequest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HvacAutoRequestOn: _ClassVar[ClimateState.HvacAutoRequest]
        HvacAutoRequestOverride: _ClassVar[ClimateState.HvacAutoRequest]
    HvacAutoRequestOn: ClimateState.HvacAutoRequest
    HvacAutoRequestOverride: ClimateState.HvacAutoRequest
    class CabinOverheatProtection_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CabinOverheatProtectionOff: _ClassVar[ClimateState.CabinOverheatProtection_E]
        CabinOverheatProtectionOn: _ClassVar[ClimateState.CabinOverheatProtection_E]
        CabinOverheatProtectionFanOnly: _ClassVar[ClimateState.CabinOverheatProtection_E]
    CabinOverheatProtectionOff: ClimateState.CabinOverheatProtection_E
    CabinOverheatProtectionOn: ClimateState.CabinOverheatProtection_E
    CabinOverheatProtectionFanOnly: ClimateState.CabinOverheatProtection_E
    class SeatHeaterLevel_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SeatHeaterLevelOff: _ClassVar[ClimateState.SeatHeaterLevel_E]
        SeatHeaterLevelLow: _ClassVar[ClimateState.SeatHeaterLevel_E]
        SeatHeaterLevelMed: _ClassVar[ClimateState.SeatHeaterLevel_E]
        SeatHeaterLevelHigh: _ClassVar[ClimateState.SeatHeaterLevel_E]
    SeatHeaterLevelOff: ClimateState.SeatHeaterLevel_E
    SeatHeaterLevelLow: ClimateState.SeatHeaterLevel_E
    SeatHeaterLevelMed: ClimateState.SeatHeaterLevel_E
    SeatHeaterLevelHigh: ClimateState.SeatHeaterLevel_E
    class SeatCoolingLevel_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SeatCoolingLevelOff: _ClassVar[ClimateState.SeatCoolingLevel_E]
        SeatCoolingLevelLow: _ClassVar[ClimateState.SeatCoolingLevel_E]
        SeatCoolingLevelMed: _ClassVar[ClimateState.SeatCoolingLevel_E]
        SeatCoolingLevelHigh: _ClassVar[ClimateState.SeatCoolingLevel_E]
    SeatCoolingLevelOff: ClimateState.SeatCoolingLevel_E
    SeatCoolingLevelLow: ClimateState.SeatCoolingLevel_E
    SeatCoolingLevelMed: ClimateState.SeatCoolingLevel_E
    SeatCoolingLevelHigh: ClimateState.SeatCoolingLevel_E
    class CopActivationTemp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CopActivationTempUnspecified: _ClassVar[ClimateState.CopActivationTemp]
        CopActivationTempLow: _ClassVar[ClimateState.CopActivationTemp]
        CopActivationTempMedium: _ClassVar[ClimateState.CopActivationTemp]
        CopActivationTempHigh: _ClassVar[ClimateState.CopActivationTemp]
    CopActivationTempUnspecified: ClimateState.CopActivationTemp
    CopActivationTempLow: ClimateState.CopActivationTemp
    CopActivationTempMedium: ClimateState.CopActivationTemp
    CopActivationTempHigh: ClimateState.CopActivationTemp
    class COPNotRunningReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COPNotRunningReasonNoReason: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonUserInteraction: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonEnergyConsumptionReached: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonTimeout: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonLowSolarLoad: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonFault: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonCabinBelowThreshold: _ClassVar[ClimateState.COPNotRunningReason]
    COPNotRunningReasonNoReason: ClimateState.COPNotRunningReason
    COPNotRunningReasonUserInteraction: ClimateState.COPNotRunningReason
    COPNotRunningReasonEnergyConsumptionReached: ClimateState.COPNotRunningReason
    COPNotRunningReasonTimeout: ClimateState.COPNotRunningReason
    COPNotRunningReasonLowSolarLoad: ClimateState.COPNotRunningReason
    COPNotRunningReasonFault: ClimateState.COPNotRunningReason
    COPNotRunningReasonCabinBelowThreshold: ClimateState.COPNotRunningReason
    class DogModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DogModeStateUnavailableFault: _ClassVar[ClimateState.DogModeState]
        DogModeStateUnavailableTooHot: _ClassVar[ClimateState.DogModeState]
        DogModeStateAvailable: _ClassVar[ClimateState.DogModeState]
        DogModeStateRunningNominal: _ClassVar[ClimateState.DogModeState]
        DogModeStateRunningFault: _ClassVar[ClimateState.DogModeState]
        DogModeStateRunningTemperatureMonitorTrip: _ClassVar[ClimateState.DogModeState]
    DogModeStateUnavailableFault: ClimateState.DogModeState
    DogModeStateUnavailableTooHot: ClimateState.DogModeState
    DogModeStateAvailable: ClimateState.DogModeState
    DogModeStateRunningNominal: ClimateState.DogModeState
    DogModeStateRunningFault: ClimateState.DogModeState
    DogModeStateRunningTemperatureMonitorTrip: ClimateState.DogModeState
    class ClimateKeeperMode(_message.Message):
        __slots__ = ("Unknown", "Off", "On", "Dog", "Party")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        OFF_FIELD_NUMBER: _ClassVar[int]
        ON_FIELD_NUMBER: _ClassVar[int]
        DOG_FIELD_NUMBER: _ClassVar[int]
        PARTY_FIELD_NUMBER: _ClassVar[int]
        Unknown: _common_pb2.Void
        Off: _common_pb2.Void
        On: _common_pb2.Void
        Dog: _common_pb2.Void
        Party: _common_pb2.Void
        def __init__(self, Unknown: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Off: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., On: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Dog: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Party: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class DefrostMode(_message.Message):
        __slots__ = ("Off", "Normal", "Max")
        OFF_FIELD_NUMBER: _ClassVar[int]
        NORMAL_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        Off: _common_pb2.Void
        Normal: _common_pb2.Void
        Max: _common_pb2.Void
        def __init__(self, Off: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Normal: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Max: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    INSIDE_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    OUTSIDE_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    DRIVER_TEMP_SETTING_FIELD_NUMBER: _ClassVar[int]
    PASSENGER_TEMP_SETTING_FIELD_NUMBER: _ClassVar[int]
    LEFT_TEMP_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    RIGHT_TEMP_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    IS_FRONT_DEFROSTER_ON_FIELD_NUMBER: _ClassVar[int]
    IS_REAR_DEFROSTER_ON_FIELD_NUMBER: _ClassVar[int]
    FAN_STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_CLIMATE_ON_FIELD_NUMBER: _ClassVar[int]
    MIN_AVAIL_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    MAX_AVAIL_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_LEFT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_LEFT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_CENTER_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_RIGHT_BACK_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_LEFT_BACK_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_THIRD_ROW_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_THIRD_ROW_LEFT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_HEATER_FIELD_NUMBER: _ClassVar[int]
    BATTERY_HEATER_NO_POWER_FIELD_NUMBER: _ClassVar[int]
    STEERING_WHEEL_HEATER_FIELD_NUMBER: _ClassVar[int]
    WIPER_BLADE_HEATER_FIELD_NUMBER: _ClassVar[int]
    SIDE_MIRROR_HEATERS_FIELD_NUMBER: _ClassVar[int]
    IS_PRECONDITIONING_FIELD_NUMBER: _ClassVar[int]
    REMOTE_HEATER_CONTROL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_KEEPER_MODE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BIOWEAPON_MODE_ON_FIELD_NUMBER: _ClassVar[int]
    DEFROST_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_CONDITIONING_ON_FIELD_NUMBER: _ClassVar[int]
    AUTO_SEAT_CLIMATE_LEFT_FIELD_NUMBER: _ClassVar[int]
    AUTO_SEAT_CLIMATE_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEAT_FAN_FRONT_LEFT_FIELD_NUMBER: _ClassVar[int]
    SEAT_FAN_FRONT_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CABIN_OVERHEAT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_FAN_ONLY_CABIN_OVERHEAT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    CABIN_OVERHEAT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    CABIN_OVERHEAT_PROTECTION_ACTIVELY_COOLING_FIELD_NUMBER: _ClassVar[int]
    COP_ACTIVATION_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    AUTO_STEERING_WHEEL_HEAT_FIELD_NUMBER: _ClassVar[int]
    STEERING_WHEEL_HEAT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    HVAC_AUTO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    COP_NOT_RUNNING_REASON_FIELD_NUMBER: _ClassVar[int]
    SEAT_FAN_SECOND_ROW_LEFT_FIELD_NUMBER: _ClassVar[int]
    SEAT_FAN_SECOND_ROW_RIGHT_FIELD_NUMBER: _ClassVar[int]
    DOG_MODE_STATE_FIELD_NUMBER: _ClassVar[int]
    inside_temp_celsius: float
    outside_temp_celsius: float
    driver_temp_setting: float
    passenger_temp_setting: float
    left_temp_direction: int
    right_temp_direction: int
    is_front_defroster_on: bool
    is_rear_defroster_on: bool
    fan_status: int
    is_climate_on: bool
    min_avail_temp_celsius: float
    max_avail_temp_celsius: float
    seat_heater_left: int
    seat_heater_right: int
    seat_heater_rear_left: int
    seat_heater_rear_right: int
    seat_heater_rear_center: int
    seat_heater_rear_right_back: int
    seat_heater_rear_left_back: int
    seat_heater_third_row_right: int
    seat_heater_third_row_left: int
    battery_heater: bool
    battery_heater_no_power: bool
    steering_wheel_heater: bool
    wiper_blade_heater: bool
    side_mirror_heaters: bool
    is_preconditioning: bool
    remote_heater_control_enabled: bool
    climate_keeper_mode: ClimateState.ClimateKeeperMode
    timestamp: _timestamp_pb2.Timestamp
    bioweapon_mode_on: bool
    defrost_mode: ClimateState.DefrostMode
    is_auto_conditioning_on: bool
    auto_seat_climate_left: bool
    auto_seat_climate_right: bool
    seat_fan_front_left: int
    seat_fan_front_right: int
    allow_cabin_overheat_protection: bool
    supports_fan_only_cabin_overheat_protection: bool
    cabin_overheat_protection: ClimateState.CabinOverheatProtection_E
    cabin_overheat_protection_actively_cooling: bool
    cop_activation_temperature: ClimateState.CopActivationTemp
    auto_steering_wheel_heat: bool
    steering_wheel_heat_level: _common_pb2.StwHeatLevel
    hvac_auto_request: ClimateState.HvacAutoRequest
    cop_not_running_reason: ClimateState.COPNotRunningReason
    seat_fan_second_row_left: int
    seat_fan_second_row_right: int
    dog_mode_state: ClimateState.DogModeState
    def __init__(self, inside_temp_celsius: _Optional[float] = ..., outside_temp_celsius: _Optional[float] = ..., driver_temp_setting: _Optional[float] = ..., passenger_temp_setting: _Optional[float] = ..., left_temp_direction: _Optional[int] = ..., right_temp_direction: _Optional[int] = ..., is_front_defroster_on: _Optional[bool] = ..., is_rear_defroster_on: _Optional[bool] = ..., fan_status: _Optional[int] = ..., is_climate_on: _Optional[bool] = ..., min_avail_temp_celsius: _Optional[float] = ..., max_avail_temp_celsius: _Optional[float] = ..., seat_heater_left: _Optional[int] = ..., seat_heater_right: _Optional[int] = ..., seat_heater_rear_left: _Optional[int] = ..., seat_heater_rear_right: _Optional[int] = ..., seat_heater_rear_center: _Optional[int] = ..., seat_heater_rear_right_back: _Optional[int] = ..., seat_heater_rear_left_back: _Optional[int] = ..., seat_heater_third_row_right: _Optional[int] = ..., seat_heater_third_row_left: _Optional[int] = ..., battery_heater: _Optional[bool] = ..., battery_heater_no_power: _Optional[bool] = ..., steering_wheel_heater: _Optional[bool] = ..., wiper_blade_heater: _Optional[bool] = ..., side_mirror_heaters: _Optional[bool] = ..., is_preconditioning: _Optional[bool] = ..., remote_heater_control_enabled: _Optional[bool] = ..., climate_keeper_mode: _Optional[_Union[ClimateState.ClimateKeeperMode, _Mapping]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., bioweapon_mode_on: _Optional[bool] = ..., defrost_mode: _Optional[_Union[ClimateState.DefrostMode, _Mapping]] = ..., is_auto_conditioning_on: _Optional[bool] = ..., auto_seat_climate_left: _Optional[bool] = ..., auto_seat_climate_right: _Optional[bool] = ..., seat_fan_front_left: _Optional[int] = ..., seat_fan_front_right: _Optional[int] = ..., allow_cabin_overheat_protection: _Optional[bool] = ..., supports_fan_only_cabin_overheat_protection: _Optional[bool] = ..., cabin_overheat_protection: _Optional[_Union[ClimateState.CabinOverheatProtection_E, str]] = ..., cabin_overheat_protection_actively_cooling: _Optional[bool] = ..., cop_activation_temperature: _Optional[_Union[ClimateState.CopActivationTemp, str]] = ..., auto_steering_wheel_heat: _Optional[bool] = ..., steering_wheel_heat_level: _Optional[_Union[_common_pb2.StwHeatLevel, str]] = ..., hvac_auto_request: _Optional[_Union[ClimateState.HvacAutoRequest, str]] = ..., cop_not_running_reason: _Optional[_Union[ClimateState.COPNotRunningReason, str]] = ..., seat_fan_second_row_left: _Optional[int] = ..., seat_fan_second_row_right: _Optional[int] = ..., dog_mode_state: _Optional[_Union[ClimateState.DogModeState, str]] = ...) -> None: ...

class TirePressureState(_message.Message):
    __slots__ = ("timestamp", "tpms_pressure_fl", "tpms_pressure_fr", "tpms_pressure_rl", "tpms_pressure_rr", "tpms_last_seen_pressure_time_fl", "tpms_last_seen_pressure_time_fr", "tpms_last_seen_pressure_time_rl", "tpms_last_seen_pressure_time_rr", "tpms_hard_warning_fl", "tpms_hard_warning_fr", "tpms_hard_warning_rl", "tpms_hard_warning_rr", "tpms_soft_warning_fl", "tpms_soft_warning_fr", "tpms_soft_warning_rl", "tpms_soft_warning_rr", "tpms_rcp_front_value", "tpms_rcp_rear_value", "tpms_pressure_re1_l0", "tpms_pressure_re1_l1", "tpms_pressure_re1_r0", "tpms_pressure_re1_r1", "tpms_pressure_re2_l0", "tpms_pressure_re2_l1", "tpms_pressure_re2_r0", "tpms_pressure_re2_r1", "tpms_last_seen_pressure_time_re1_l0", "tpms_last_seen_pressure_time_re1_l1", "tpms_last_seen_pressure_time_re1_r0", "tpms_last_seen_pressure_time_re1_r1", "tpms_last_seen_pressure_time_re2_l0", "tpms_last_seen_pressure_time_re2_l1", "tpms_last_seen_pressure_time_re2_r0", "tpms_last_seen_pressure_time_re2_r1", "tpms_hard_warning_re1_l0", "tpms_hard_warning_re1_l1", "tpms_hard_warning_re1_r0", "tpms_hard_warning_re1_r1", "tpms_hard_warning_re2_l0", "tpms_hard_warning_re2_l1", "tpms_hard_warning_re2_r0", "tpms_hard_warning_re2_r1", "tpms_soft_warning_re1_l0", "tpms_soft_warning_re1_l1", "tpms_soft_warning_re1_r0", "tpms_soft_warning_re1_r1", "tpms_soft_warning_re2_l0", "tpms_soft_warning_re2_l1", "tpms_soft_warning_re2_r0", "tpms_soft_warning_re2_r1", "tpms_temperature_fl", "tpms_temperature_fr", "tpms_temperature_rl", "tpms_temperature_rr", "tpms_temperature_re1_l0", "tpms_temperature_re1_l1", "tpms_temperature_re1_r0", "tpms_temperature_re1_r1", "tpms_temperature_re2_l0", "tpms_temperature_re2_l1", "tpms_temperature_re2_r0", "tpms_temperature_re2_r1", "tpms_temperature_hard_warning_fl", "tpms_temperature_hard_warning_fr", "tpms_temperature_hard_warning_rl", "tpms_temperature_hard_warning_rr", "tpms_temperature_hard_warning_re1_l0", "tpms_temperature_hard_warning_re1_l1", "tpms_temperature_hard_warning_re1_r0", "tpms_temperature_hard_warning_re1_r1", "tpms_temperature_hard_warning_re2_l0", "tpms_temperature_hard_warning_re2_l1", "tpms_temperature_hard_warning_re2_r0", "tpms_temperature_hard_warning_re2_r1", "tpms_temperature_soft_warning_fl", "tpms_temperature_soft_warning_fr", "tpms_temperature_soft_warning_rl", "tpms_temperature_soft_warning_rr", "tpms_temperature_soft_warning_re1_l0", "tpms_temperature_soft_warning_re1_l1", "tpms_temperature_soft_warning_re1_r0", "tpms_temperature_soft_warning_re1_r1", "tpms_temperature_soft_warning_re2_l0", "tpms_temperature_soft_warning_re2_l1", "tpms_temperature_soft_warning_re2_r0", "tpms_temperature_soft_warning_re2_r1")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_RCP_FRONT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TPMS_RCP_REAR_VALUE_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RE1_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RE1_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RE1_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RE1_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RE2_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RE2_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RE2_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RE2_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RE1_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RE1_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RE1_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RE1_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RE2_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RE2_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RE2_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RE2_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RE1_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RE1_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RE1_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RE1_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RE2_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RE2_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RE2_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RE2_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RE1_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RE1_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RE1_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RE1_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RE2_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RE2_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RE2_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RE2_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RE1_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RE1_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RE1_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RE1_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RE2_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RE2_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RE2_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_RE2_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RE1_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RE1_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RE1_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RE1_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RE2_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RE2_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RE2_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_HARD_WARNING_RE2_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RE1_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RE1_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RE1_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RE1_R1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RE2_L0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RE2_L1_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RE2_R0_FIELD_NUMBER: _ClassVar[int]
    TPMS_TEMPERATURE_SOFT_WARNING_RE2_R1_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    tpms_pressure_fl: float
    tpms_pressure_fr: float
    tpms_pressure_rl: float
    tpms_pressure_rr: float
    tpms_last_seen_pressure_time_fl: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_fr: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_rl: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_rr: _timestamp_pb2.Timestamp
    tpms_hard_warning_fl: bool
    tpms_hard_warning_fr: bool
    tpms_hard_warning_rl: bool
    tpms_hard_warning_rr: bool
    tpms_soft_warning_fl: bool
    tpms_soft_warning_fr: bool
    tpms_soft_warning_rl: bool
    tpms_soft_warning_rr: bool
    tpms_rcp_front_value: float
    tpms_rcp_rear_value: float
    tpms_pressure_re1_l0: float
    tpms_pressure_re1_l1: float
    tpms_pressure_re1_r0: float
    tpms_pressure_re1_r1: float
    tpms_pressure_re2_l0: float
    tpms_pressure_re2_l1: float
    tpms_pressure_re2_r0: float
    tpms_pressure_re2_r1: float
    tpms_last_seen_pressure_time_re1_l0: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_re1_l1: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_re1_r0: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_re1_r1: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_re2_l0: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_re2_l1: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_re2_r0: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_re2_r1: _timestamp_pb2.Timestamp
    tpms_hard_warning_re1_l0: bool
    tpms_hard_warning_re1_l1: bool
    tpms_hard_warning_re1_r0: bool
    tpms_hard_warning_re1_r1: bool
    tpms_hard_warning_re2_l0: bool
    tpms_hard_warning_re2_l1: bool
    tpms_hard_warning_re2_r0: bool
    tpms_hard_warning_re2_r1: bool
    tpms_soft_warning_re1_l0: bool
    tpms_soft_warning_re1_l1: bool
    tpms_soft_warning_re1_r0: bool
    tpms_soft_warning_re1_r1: bool
    tpms_soft_warning_re2_l0: bool
    tpms_soft_warning_re2_l1: bool
    tpms_soft_warning_re2_r0: bool
    tpms_soft_warning_re2_r1: bool
    tpms_temperature_fl: float
    tpms_temperature_fr: float
    tpms_temperature_rl: float
    tpms_temperature_rr: float
    tpms_temperature_re1_l0: float
    tpms_temperature_re1_l1: float
    tpms_temperature_re1_r0: float
    tpms_temperature_re1_r1: float
    tpms_temperature_re2_l0: float
    tpms_temperature_re2_l1: float
    tpms_temperature_re2_r0: float
    tpms_temperature_re2_r1: float
    tpms_temperature_hard_warning_fl: bool
    tpms_temperature_hard_warning_fr: bool
    tpms_temperature_hard_warning_rl: bool
    tpms_temperature_hard_warning_rr: bool
    tpms_temperature_hard_warning_re1_l0: bool
    tpms_temperature_hard_warning_re1_l1: bool
    tpms_temperature_hard_warning_re1_r0: bool
    tpms_temperature_hard_warning_re1_r1: bool
    tpms_temperature_hard_warning_re2_l0: bool
    tpms_temperature_hard_warning_re2_l1: bool
    tpms_temperature_hard_warning_re2_r0: bool
    tpms_temperature_hard_warning_re2_r1: bool
    tpms_temperature_soft_warning_fl: bool
    tpms_temperature_soft_warning_fr: bool
    tpms_temperature_soft_warning_rl: bool
    tpms_temperature_soft_warning_rr: bool
    tpms_temperature_soft_warning_re1_l0: bool
    tpms_temperature_soft_warning_re1_l1: bool
    tpms_temperature_soft_warning_re1_r0: bool
    tpms_temperature_soft_warning_re1_r1: bool
    tpms_temperature_soft_warning_re2_l0: bool
    tpms_temperature_soft_warning_re2_l1: bool
    tpms_temperature_soft_warning_re2_r0: bool
    tpms_temperature_soft_warning_re2_r1: bool
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_pressure_fl: _Optional[float] = ..., tpms_pressure_fr: _Optional[float] = ..., tpms_pressure_rl: _Optional[float] = ..., tpms_pressure_rr: _Optional[float] = ..., tpms_last_seen_pressure_time_fl: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_fr: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_rl: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_rr: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_hard_warning_fl: _Optional[bool] = ..., tpms_hard_warning_fr: _Optional[bool] = ..., tpms_hard_warning_rl: _Optional[bool] = ..., tpms_hard_warning_rr: _Optional[bool] = ..., tpms_soft_warning_fl: _Optional[bool] = ..., tpms_soft_warning_fr: _Optional[bool] = ..., tpms_soft_warning_rl: _Optional[bool] = ..., tpms_soft_warning_rr: _Optional[bool] = ..., tpms_rcp_front_value: _Optional[float] = ..., tpms_rcp_rear_value: _Optional[float] = ..., tpms_pressure_re1_l0: _Optional[float] = ..., tpms_pressure_re1_l1: _Optional[float] = ..., tpms_pressure_re1_r0: _Optional[float] = ..., tpms_pressure_re1_r1: _Optional[float] = ..., tpms_pressure_re2_l0: _Optional[float] = ..., tpms_pressure_re2_l1: _Optional[float] = ..., tpms_pressure_re2_r0: _Optional[float] = ..., tpms_pressure_re2_r1: _Optional[float] = ..., tpms_last_seen_pressure_time_re1_l0: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_re1_l1: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_re1_r0: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_re1_r1: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_re2_l0: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_re2_l1: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_re2_r0: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_last_seen_pressure_time_re2_r1: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tpms_hard_warning_re1_l0: _Optional[bool] = ..., tpms_hard_warning_re1_l1: _Optional[bool] = ..., tpms_hard_warning_re1_r0: _Optional[bool] = ..., tpms_hard_warning_re1_r1: _Optional[bool] = ..., tpms_hard_warning_re2_l0: _Optional[bool] = ..., tpms_hard_warning_re2_l1: _Optional[bool] = ..., tpms_hard_warning_re2_r0: _Optional[bool] = ..., tpms_hard_warning_re2_r1: _Optional[bool] = ..., tpms_soft_warning_re1_l0: _Optional[bool] = ..., tpms_soft_warning_re1_l1: _Optional[bool] = ..., tpms_soft_warning_re1_r0: _Optional[bool] = ..., tpms_soft_warning_re1_r1: _Optional[bool] = ..., tpms_soft_warning_re2_l0: _Optional[bool] = ..., tpms_soft_warning_re2_l1: _Optional[bool] = ..., tpms_soft_warning_re2_r0: _Optional[bool] = ..., tpms_soft_warning_re2_r1: _Optional[bool] = ..., tpms_temperature_fl: _Optional[float] = ..., tpms_temperature_fr: _Optional[float] = ..., tpms_temperature_rl: _Optional[float] = ..., tpms_temperature_rr: _Optional[float] = ..., tpms_temperature_re1_l0: _Optional[float] = ..., tpms_temperature_re1_l1: _Optional[float] = ..., tpms_temperature_re1_r0: _Optional[float] = ..., tpms_temperature_re1_r1: _Optional[float] = ..., tpms_temperature_re2_l0: _Optional[float] = ..., tpms_temperature_re2_l1: _Optional[float] = ..., tpms_temperature_re2_r0: _Optional[float] = ..., tpms_temperature_re2_r1: _Optional[float] = ..., tpms_temperature_hard_warning_fl: _Optional[bool] = ..., tpms_temperature_hard_warning_fr: _Optional[bool] = ..., tpms_temperature_hard_warning_rl: _Optional[bool] = ..., tpms_temperature_hard_warning_rr: _Optional[bool] = ..., tpms_temperature_hard_warning_re1_l0: _Optional[bool] = ..., tpms_temperature_hard_warning_re1_l1: _Optional[bool] = ..., tpms_temperature_hard_warning_re1_r0: _Optional[bool] = ..., tpms_temperature_hard_warning_re1_r1: _Optional[bool] = ..., tpms_temperature_hard_warning_re2_l0: _Optional[bool] = ..., tpms_temperature_hard_warning_re2_l1: _Optional[bool] = ..., tpms_temperature_hard_warning_re2_r0: _Optional[bool] = ..., tpms_temperature_hard_warning_re2_r1: _Optional[bool] = ..., tpms_temperature_soft_warning_fl: _Optional[bool] = ..., tpms_temperature_soft_warning_fr: _Optional[bool] = ..., tpms_temperature_soft_warning_rl: _Optional[bool] = ..., tpms_temperature_soft_warning_rr: _Optional[bool] = ..., tpms_temperature_soft_warning_re1_l0: _Optional[bool] = ..., tpms_temperature_soft_warning_re1_l1: _Optional[bool] = ..., tpms_temperature_soft_warning_re1_r0: _Optional[bool] = ..., tpms_temperature_soft_warning_re1_r1: _Optional[bool] = ..., tpms_temperature_soft_warning_re2_l0: _Optional[bool] = ..., tpms_temperature_soft_warning_re2_l1: _Optional[bool] = ..., tpms_temperature_soft_warning_re2_r0: _Optional[bool] = ..., tpms_temperature_soft_warning_re2_r1: _Optional[bool] = ...) -> None: ...

class MediaState(_message.Message):
    __slots__ = ("timestamp", "remote_control_enabled", "now_playing_artist", "now_playing_title", "audio_volume", "audio_volume_increment", "audio_volume_max", "now_playing_source", "media_playback_status")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CONTROL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_ARTIST_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_TITLE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_VOLUME_FIELD_NUMBER: _ClassVar[int]
    AUDIO_VOLUME_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_VOLUME_MAX_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_PLAYBACK_STATUS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    remote_control_enabled: bool
    now_playing_artist: str
    now_playing_title: str
    audio_volume: float
    audio_volume_increment: float
    audio_volume_max: float
    now_playing_source: MediaSourceType
    media_playback_status: _common_pb2.MediaPlaybackStatus
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., remote_control_enabled: _Optional[bool] = ..., now_playing_artist: _Optional[str] = ..., now_playing_title: _Optional[str] = ..., audio_volume: _Optional[float] = ..., audio_volume_increment: _Optional[float] = ..., audio_volume_max: _Optional[float] = ..., now_playing_source: _Optional[_Union[MediaSourceType, str]] = ..., media_playback_status: _Optional[_Union[_common_pb2.MediaPlaybackStatus, str]] = ...) -> None: ...

class MediaDetailState(_message.Message):
    __slots__ = ("timestamp", "now_playing_duration", "now_playing_elapsed", "now_playing_source_string", "now_playing_album", "now_playing_station", "a2dp_source_name", "recent_theater_source", "recent_theater_source_string", "theater_source_is_playing")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_DURATION_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_ELAPSED_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_SOURCE_STRING_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_ALBUM_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_STATION_FIELD_NUMBER: _ClassVar[int]
    A2DP_SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECENT_THEATER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RECENT_THEATER_SOURCE_STRING_FIELD_NUMBER: _ClassVar[int]
    THEATER_SOURCE_IS_PLAYING_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    now_playing_duration: int
    now_playing_elapsed: int
    now_playing_source_string: str
    now_playing_album: str
    now_playing_station: str
    a2dp_source_name: str
    recent_theater_source: TheaterSource
    recent_theater_source_string: str
    theater_source_is_playing: bool
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., now_playing_duration: _Optional[int] = ..., now_playing_elapsed: _Optional[int] = ..., now_playing_source_string: _Optional[str] = ..., now_playing_album: _Optional[str] = ..., now_playing_station: _Optional[str] = ..., a2dp_source_name: _Optional[str] = ..., recent_theater_source: _Optional[_Union[TheaterSource, str]] = ..., recent_theater_source_string: _Optional[str] = ..., theater_source_is_playing: _Optional[bool] = ...) -> None: ...

class ShiftState(_message.Message):
    __slots__ = ("Invalid", "P", "R", "N", "D", "SNA")
    INVALID_FIELD_NUMBER: _ClassVar[int]
    P_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    SNA_FIELD_NUMBER: _ClassVar[int]
    Invalid: _common_pb2.Void
    P: _common_pb2.Void
    R: _common_pb2.Void
    N: _common_pb2.Void
    D: _common_pb2.Void
    SNA: _common_pb2.Void
    def __init__(self, Invalid: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., P: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., R: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., N: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SNA: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class VehicleBadging(_message.Message):
    __slots__ = ("Base", "Founder", "Signature", "Performance", "LaunchSeries", "SignatureSeries")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FOUNDER_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    LAUNCHSERIES_FIELD_NUMBER: _ClassVar[int]
    SIGNATURESERIES_FIELD_NUMBER: _ClassVar[int]
    Base: _common_pb2.Void
    Founder: _common_pb2.Void
    Signature: _common_pb2.Void
    Performance: _common_pb2.Void
    LaunchSeries: _common_pb2.Void
    SignatureSeries: _common_pb2.Void
    def __init__(self, Base: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Founder: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Signature: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Performance: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., LaunchSeries: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SignatureSeries: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class CarTrim(_message.Message):
    __slots__ = ("Trim40", "OBSOLETETrim50", "OBSOLETETrim50D", "Trim60", "Trim60D", "Trim70", "Trim70D", "Trim75", "Trim75D", "TrimP75D", "Trim85", "TrimP85", "TrimP85Plus", "Trim85D", "TrimP85D", "Trim90", "TrimP90", "TrimP90Plus", "Trim90D", "TrimP90D", "Trim100", "TrimP100", "Trim100D", "TrimP100D", "Trim50", "Trim50D", "Trim62", "Trim62D", "Trim74", "Trim74D", "TrimP74D", "TrimDefault", "TrimCyberbeast", "TrimInvalid")
    TRIM40_FIELD_NUMBER: _ClassVar[int]
    OBSOLETETRIM50_FIELD_NUMBER: _ClassVar[int]
    OBSOLETETRIM50D_FIELD_NUMBER: _ClassVar[int]
    TRIM60_FIELD_NUMBER: _ClassVar[int]
    TRIM60D_FIELD_NUMBER: _ClassVar[int]
    TRIM70_FIELD_NUMBER: _ClassVar[int]
    TRIM70D_FIELD_NUMBER: _ClassVar[int]
    TRIM75_FIELD_NUMBER: _ClassVar[int]
    TRIM75D_FIELD_NUMBER: _ClassVar[int]
    TRIMP75D_FIELD_NUMBER: _ClassVar[int]
    TRIM85_FIELD_NUMBER: _ClassVar[int]
    TRIMP85_FIELD_NUMBER: _ClassVar[int]
    TRIMP85PLUS_FIELD_NUMBER: _ClassVar[int]
    TRIM85D_FIELD_NUMBER: _ClassVar[int]
    TRIMP85D_FIELD_NUMBER: _ClassVar[int]
    TRIM90_FIELD_NUMBER: _ClassVar[int]
    TRIMP90_FIELD_NUMBER: _ClassVar[int]
    TRIMP90PLUS_FIELD_NUMBER: _ClassVar[int]
    TRIM90D_FIELD_NUMBER: _ClassVar[int]
    TRIMP90D_FIELD_NUMBER: _ClassVar[int]
    TRIM100_FIELD_NUMBER: _ClassVar[int]
    TRIMP100_FIELD_NUMBER: _ClassVar[int]
    TRIM100D_FIELD_NUMBER: _ClassVar[int]
    TRIMP100D_FIELD_NUMBER: _ClassVar[int]
    TRIM50_FIELD_NUMBER: _ClassVar[int]
    TRIM50D_FIELD_NUMBER: _ClassVar[int]
    TRIM62_FIELD_NUMBER: _ClassVar[int]
    TRIM62D_FIELD_NUMBER: _ClassVar[int]
    TRIM74_FIELD_NUMBER: _ClassVar[int]
    TRIM74D_FIELD_NUMBER: _ClassVar[int]
    TRIMP74D_FIELD_NUMBER: _ClassVar[int]
    TRIMDEFAULT_FIELD_NUMBER: _ClassVar[int]
    TRIMCYBERBEAST_FIELD_NUMBER: _ClassVar[int]
    TRIMINVALID_FIELD_NUMBER: _ClassVar[int]
    Trim40: _common_pb2.Void
    OBSOLETETrim50: _common_pb2.Void
    OBSOLETETrim50D: _common_pb2.Void
    Trim60: _common_pb2.Void
    Trim60D: _common_pb2.Void
    Trim70: _common_pb2.Void
    Trim70D: _common_pb2.Void
    Trim75: _common_pb2.Void
    Trim75D: _common_pb2.Void
    TrimP75D: _common_pb2.Void
    Trim85: _common_pb2.Void
    TrimP85: _common_pb2.Void
    TrimP85Plus: _common_pb2.Void
    Trim85D: _common_pb2.Void
    TrimP85D: _common_pb2.Void
    Trim90: _common_pb2.Void
    TrimP90: _common_pb2.Void
    TrimP90Plus: _common_pb2.Void
    Trim90D: _common_pb2.Void
    TrimP90D: _common_pb2.Void
    Trim100: _common_pb2.Void
    TrimP100: _common_pb2.Void
    Trim100D: _common_pb2.Void
    TrimP100D: _common_pb2.Void
    Trim50: _common_pb2.Void
    Trim50D: _common_pb2.Void
    Trim62: _common_pb2.Void
    Trim62D: _common_pb2.Void
    Trim74: _common_pb2.Void
    Trim74D: _common_pb2.Void
    TrimP74D: _common_pb2.Void
    TrimDefault: _common_pb2.Void
    TrimCyberbeast: _common_pb2.Void
    TrimInvalid: _common_pb2.Void
    def __init__(self, Trim40: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., OBSOLETETrim50: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., OBSOLETETrim50D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim60: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim60D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim70: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim70D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim75: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim75D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP75D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim85: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP85: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP85Plus: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim85D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP85D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim90: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP90: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP90Plus: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim90D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP90D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim100: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP100: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim100D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP100D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim50: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim50D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim62: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim62D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim74: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Trim74D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimP74D: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimDefault: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimCyberbeast: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TrimInvalid: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class SunRoofType(_message.Message):
    __slots__ = ("None_", "Gen1", "Gen2")
    NONE__FIELD_NUMBER: _ClassVar[int]
    GEN1_FIELD_NUMBER: _ClassVar[int]
    GEN2_FIELD_NUMBER: _ClassVar[int]
    None_: _common_pb2.Void
    Gen1: _common_pb2.Void
    Gen2: _common_pb2.Void
    def __init__(self, None_: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Gen1: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Gen2: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class WheelType(_message.Message):
    __slots__ = ("Unknown", "ZeroG20Gunpowder", "Pinwheel18", "Pinwheel18CapKit", "Stiletto19", "Stiletto20", "Stiletto20DarkStaggered", "Stiletto20DarkSquare", "Gemini19Square", "Gemini19Staggered", "Induction20Black", "UberTurbine21Black", "Apollo19", "Apollo19CapKit", "ZeroG19Gunpowder", "Cardenio19", "Default", "NewTurbine22Black", "Cyberstream", "Arachnid21", "Base19", "Silver21", "Charcoal21", "Silver21Euro", "Aero19", "Charcoal21Euro", "Super21Gray", "Super21Silver", "Turbine19", "Turbine19Dark", "AeroTurbine19", "AeroTurbine19Black", "Helix20", "AeroTurbine20", "Turbine22", "Cyclone19Dark", "AeroTurbine20Dark", "Turbine22Dark", "Arachnid21Silver", "Arachnid21Black", "Arachnid21Grey", "Slipstream20Carbon", "Slipstream20Dark", "Slipstream19Carbon", "TwinTurbine21Silver", "TwinTurbine21Carbon", "Tempest19SonicSilver", "PinwheelRefresh18", "StilettoRefresh19", "UberTurbine20Gunpowder", "Glider18", "Helix19", "Wishbone20Staggered", "CtBase20", "CtPremium20", "CtBase18", "Apollo19MetallicShadow", "Wishbone19Staggered", "Crossflow19", "HelixV220", "Standard19", "Halo22", "Riptide20", "Cypress21", "MachinaV219", "ArachnidV221", "E4118", "D5018", "HelixV220Dark", "UberHelix20")
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    ZEROG20GUNPOWDER_FIELD_NUMBER: _ClassVar[int]
    PINWHEEL18_FIELD_NUMBER: _ClassVar[int]
    PINWHEEL18CAPKIT_FIELD_NUMBER: _ClassVar[int]
    STILETTO19_FIELD_NUMBER: _ClassVar[int]
    STILETTO20_FIELD_NUMBER: _ClassVar[int]
    STILETTO20DARKSTAGGERED_FIELD_NUMBER: _ClassVar[int]
    STILETTO20DARKSQUARE_FIELD_NUMBER: _ClassVar[int]
    GEMINI19SQUARE_FIELD_NUMBER: _ClassVar[int]
    GEMINI19STAGGERED_FIELD_NUMBER: _ClassVar[int]
    INDUCTION20BLACK_FIELD_NUMBER: _ClassVar[int]
    UBERTURBINE21BLACK_FIELD_NUMBER: _ClassVar[int]
    APOLLO19_FIELD_NUMBER: _ClassVar[int]
    APOLLO19CAPKIT_FIELD_NUMBER: _ClassVar[int]
    ZEROG19GUNPOWDER_FIELD_NUMBER: _ClassVar[int]
    CARDENIO19_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    NEWTURBINE22BLACK_FIELD_NUMBER: _ClassVar[int]
    CYBERSTREAM_FIELD_NUMBER: _ClassVar[int]
    ARACHNID21_FIELD_NUMBER: _ClassVar[int]
    BASE19_FIELD_NUMBER: _ClassVar[int]
    SILVER21_FIELD_NUMBER: _ClassVar[int]
    CHARCOAL21_FIELD_NUMBER: _ClassVar[int]
    SILVER21EURO_FIELD_NUMBER: _ClassVar[int]
    AERO19_FIELD_NUMBER: _ClassVar[int]
    CHARCOAL21EURO_FIELD_NUMBER: _ClassVar[int]
    SUPER21GRAY_FIELD_NUMBER: _ClassVar[int]
    SUPER21SILVER_FIELD_NUMBER: _ClassVar[int]
    TURBINE19_FIELD_NUMBER: _ClassVar[int]
    TURBINE19DARK_FIELD_NUMBER: _ClassVar[int]
    AEROTURBINE19_FIELD_NUMBER: _ClassVar[int]
    AEROTURBINE19BLACK_FIELD_NUMBER: _ClassVar[int]
    HELIX20_FIELD_NUMBER: _ClassVar[int]
    AEROTURBINE20_FIELD_NUMBER: _ClassVar[int]
    TURBINE22_FIELD_NUMBER: _ClassVar[int]
    CYCLONE19DARK_FIELD_NUMBER: _ClassVar[int]
    AEROTURBINE20DARK_FIELD_NUMBER: _ClassVar[int]
    TURBINE22DARK_FIELD_NUMBER: _ClassVar[int]
    ARACHNID21SILVER_FIELD_NUMBER: _ClassVar[int]
    ARACHNID21BLACK_FIELD_NUMBER: _ClassVar[int]
    ARACHNID21GREY_FIELD_NUMBER: _ClassVar[int]
    SLIPSTREAM20CARBON_FIELD_NUMBER: _ClassVar[int]
    SLIPSTREAM20DARK_FIELD_NUMBER: _ClassVar[int]
    SLIPSTREAM19CARBON_FIELD_NUMBER: _ClassVar[int]
    TWINTURBINE21SILVER_FIELD_NUMBER: _ClassVar[int]
    TWINTURBINE21CARBON_FIELD_NUMBER: _ClassVar[int]
    TEMPEST19SONICSILVER_FIELD_NUMBER: _ClassVar[int]
    PINWHEELREFRESH18_FIELD_NUMBER: _ClassVar[int]
    STILETTOREFRESH19_FIELD_NUMBER: _ClassVar[int]
    UBERTURBINE20GUNPOWDER_FIELD_NUMBER: _ClassVar[int]
    GLIDER18_FIELD_NUMBER: _ClassVar[int]
    HELIX19_FIELD_NUMBER: _ClassVar[int]
    WISHBONE20STAGGERED_FIELD_NUMBER: _ClassVar[int]
    CTBASE20_FIELD_NUMBER: _ClassVar[int]
    CTPREMIUM20_FIELD_NUMBER: _ClassVar[int]
    CTBASE18_FIELD_NUMBER: _ClassVar[int]
    APOLLO19METALLICSHADOW_FIELD_NUMBER: _ClassVar[int]
    WISHBONE19STAGGERED_FIELD_NUMBER: _ClassVar[int]
    CROSSFLOW19_FIELD_NUMBER: _ClassVar[int]
    HELIXV220_FIELD_NUMBER: _ClassVar[int]
    STANDARD19_FIELD_NUMBER: _ClassVar[int]
    HALO22_FIELD_NUMBER: _ClassVar[int]
    RIPTIDE20_FIELD_NUMBER: _ClassVar[int]
    CYPRESS21_FIELD_NUMBER: _ClassVar[int]
    MACHINAV219_FIELD_NUMBER: _ClassVar[int]
    ARACHNIDV221_FIELD_NUMBER: _ClassVar[int]
    E4118_FIELD_NUMBER: _ClassVar[int]
    D5018_FIELD_NUMBER: _ClassVar[int]
    HELIXV220DARK_FIELD_NUMBER: _ClassVar[int]
    UBERHELIX20_FIELD_NUMBER: _ClassVar[int]
    Unknown: _common_pb2.Void
    ZeroG20Gunpowder: _common_pb2.Void
    Pinwheel18: _common_pb2.Void
    Pinwheel18CapKit: _common_pb2.Void
    Stiletto19: _common_pb2.Void
    Stiletto20: _common_pb2.Void
    Stiletto20DarkStaggered: _common_pb2.Void
    Stiletto20DarkSquare: _common_pb2.Void
    Gemini19Square: _common_pb2.Void
    Gemini19Staggered: _common_pb2.Void
    Induction20Black: _common_pb2.Void
    UberTurbine21Black: _common_pb2.Void
    Apollo19: _common_pb2.Void
    Apollo19CapKit: _common_pb2.Void
    ZeroG19Gunpowder: _common_pb2.Void
    Cardenio19: _common_pb2.Void
    Default: _common_pb2.Void
    NewTurbine22Black: _common_pb2.Void
    Cyberstream: _common_pb2.Void
    Arachnid21: _common_pb2.Void
    Base19: _common_pb2.Void
    Silver21: _common_pb2.Void
    Charcoal21: _common_pb2.Void
    Silver21Euro: _common_pb2.Void
    Aero19: _common_pb2.Void
    Charcoal21Euro: _common_pb2.Void
    Super21Gray: _common_pb2.Void
    Super21Silver: _common_pb2.Void
    Turbine19: _common_pb2.Void
    Turbine19Dark: _common_pb2.Void
    AeroTurbine19: _common_pb2.Void
    AeroTurbine19Black: _common_pb2.Void
    Helix20: _common_pb2.Void
    AeroTurbine20: _common_pb2.Void
    Turbine22: _common_pb2.Void
    Cyclone19Dark: _common_pb2.Void
    AeroTurbine20Dark: _common_pb2.Void
    Turbine22Dark: _common_pb2.Void
    Arachnid21Silver: _common_pb2.Void
    Arachnid21Black: _common_pb2.Void
    Arachnid21Grey: _common_pb2.Void
    Slipstream20Carbon: _common_pb2.Void
    Slipstream20Dark: _common_pb2.Void
    Slipstream19Carbon: _common_pb2.Void
    TwinTurbine21Silver: _common_pb2.Void
    TwinTurbine21Carbon: _common_pb2.Void
    Tempest19SonicSilver: _common_pb2.Void
    PinwheelRefresh18: _common_pb2.Void
    StilettoRefresh19: _common_pb2.Void
    UberTurbine20Gunpowder: _common_pb2.Void
    Glider18: _common_pb2.Void
    Helix19: _common_pb2.Void
    Wishbone20Staggered: _common_pb2.Void
    CtBase20: _common_pb2.Void
    CtPremium20: _common_pb2.Void
    CtBase18: _common_pb2.Void
    Apollo19MetallicShadow: _common_pb2.Void
    Wishbone19Staggered: _common_pb2.Void
    Crossflow19: _common_pb2.Void
    HelixV220: _common_pb2.Void
    Standard19: _common_pb2.Void
    Halo22: _common_pb2.Void
    Riptide20: _common_pb2.Void
    Cypress21: _common_pb2.Void
    MachinaV219: _common_pb2.Void
    ArachnidV221: _common_pb2.Void
    E4118: _common_pb2.Void
    D5018: _common_pb2.Void
    HelixV220Dark: _common_pb2.Void
    UberHelix20: _common_pb2.Void
    def __init__(self, Unknown: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ZeroG20Gunpowder: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Pinwheel18: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Pinwheel18CapKit: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Stiletto19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Stiletto20: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Stiletto20DarkStaggered: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Stiletto20DarkSquare: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Gemini19Square: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Gemini19Staggered: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Induction20Black: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., UberTurbine21Black: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Apollo19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Apollo19CapKit: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ZeroG19Gunpowder: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Cardenio19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Default: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., NewTurbine22Black: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Cyberstream: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Arachnid21: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Base19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Silver21: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Charcoal21: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Silver21Euro: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Aero19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Charcoal21Euro: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Super21Gray: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Super21Silver: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Turbine19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Turbine19Dark: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., AeroTurbine19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., AeroTurbine19Black: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Helix20: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., AeroTurbine20: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Turbine22: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Cyclone19Dark: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., AeroTurbine20Dark: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Turbine22Dark: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Arachnid21Silver: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Arachnid21Black: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Arachnid21Grey: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Slipstream20Carbon: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Slipstream20Dark: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Slipstream19Carbon: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TwinTurbine21Silver: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TwinTurbine21Carbon: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Tempest19SonicSilver: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., PinwheelRefresh18: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., StilettoRefresh19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., UberTurbine20Gunpowder: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Glider18: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Helix19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Wishbone20Staggered: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CtBase20: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CtPremium20: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CtBase18: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Apollo19MetallicShadow: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Wishbone19Staggered: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Crossflow19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., HelixV220: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Standard19: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Halo22: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Riptide20: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Cypress21: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MachinaV219: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ArachnidV221: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., E4118: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., D5018: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., HelixV220Dark: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., UberHelix20: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class SpoilerType(_message.Message):
    __slots__ = ("None_", "Passive", "Active")
    NONE__FIELD_NUMBER: _ClassVar[int]
    PASSIVE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    None_: _common_pb2.Void
    Passive: _common_pb2.Void
    Active: _common_pb2.Void
    def __init__(self, None_: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Passive: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Active: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class RoofColor(_message.Message):
    __slots__ = ("None_", "Glass", "Black", "Colored")
    NONE__FIELD_NUMBER: _ClassVar[int]
    GLASS_FIELD_NUMBER: _ClassVar[int]
    BLACK_FIELD_NUMBER: _ClassVar[int]
    COLORED_FIELD_NUMBER: _ClassVar[int]
    None_: _common_pb2.Void
    Glass: _common_pb2.Void
    Black: _common_pb2.Void
    Colored: _common_pb2.Void
    def __init__(self, None_: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Glass: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Black: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Colored: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class ExteriorColor(_message.Message):
    __slots__ = ("Unknown", "RedMulticoat", "SolidBlack", "SilverMetallic", "MidnightSilver", "DeepBlue", "PearlWhite", "DefaultColor", "Black", "White", "Silver", "Grey", "Blue", "Green", "Brown", "Pearl", "SigRed", "Red", "SteelGrey", "MetallicBlack", "TitaniumCopper", "SignatureBlue", "MidnightCherryRed", "Quicksilver", "UltraRed", "StealthGrey", "LunarSilver", "GlacierBlue", "DiamondBlack", "FrostBlue", "SilkRoadSilver", "MarineBlue", "GarnetRed", "CoastalBlue")
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    REDMULTICOAT_FIELD_NUMBER: _ClassVar[int]
    SOLIDBLACK_FIELD_NUMBER: _ClassVar[int]
    SILVERMETALLIC_FIELD_NUMBER: _ClassVar[int]
    MIDNIGHTSILVER_FIELD_NUMBER: _ClassVar[int]
    DEEPBLUE_FIELD_NUMBER: _ClassVar[int]
    PEARLWHITE_FIELD_NUMBER: _ClassVar[int]
    DEFAULTCOLOR_FIELD_NUMBER: _ClassVar[int]
    BLACK_FIELD_NUMBER: _ClassVar[int]
    WHITE_FIELD_NUMBER: _ClassVar[int]
    SILVER_FIELD_NUMBER: _ClassVar[int]
    GREY_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BROWN_FIELD_NUMBER: _ClassVar[int]
    PEARL_FIELD_NUMBER: _ClassVar[int]
    SIGRED_FIELD_NUMBER: _ClassVar[int]
    RED_FIELD_NUMBER: _ClassVar[int]
    STEELGREY_FIELD_NUMBER: _ClassVar[int]
    METALLICBLACK_FIELD_NUMBER: _ClassVar[int]
    TITANIUMCOPPER_FIELD_NUMBER: _ClassVar[int]
    SIGNATUREBLUE_FIELD_NUMBER: _ClassVar[int]
    MIDNIGHTCHERRYRED_FIELD_NUMBER: _ClassVar[int]
    QUICKSILVER_FIELD_NUMBER: _ClassVar[int]
    ULTRARED_FIELD_NUMBER: _ClassVar[int]
    STEALTHGREY_FIELD_NUMBER: _ClassVar[int]
    LUNARSILVER_FIELD_NUMBER: _ClassVar[int]
    GLACIERBLUE_FIELD_NUMBER: _ClassVar[int]
    DIAMONDBLACK_FIELD_NUMBER: _ClassVar[int]
    FROSTBLUE_FIELD_NUMBER: _ClassVar[int]
    SILKROADSILVER_FIELD_NUMBER: _ClassVar[int]
    MARINEBLUE_FIELD_NUMBER: _ClassVar[int]
    GARNETRED_FIELD_NUMBER: _ClassVar[int]
    COASTALBLUE_FIELD_NUMBER: _ClassVar[int]
    Unknown: _common_pb2.Void
    RedMulticoat: _common_pb2.Void
    SolidBlack: _common_pb2.Void
    SilverMetallic: _common_pb2.Void
    MidnightSilver: _common_pb2.Void
    DeepBlue: _common_pb2.Void
    PearlWhite: _common_pb2.Void
    DefaultColor: _common_pb2.Void
    Black: _common_pb2.Void
    White: _common_pb2.Void
    Silver: _common_pb2.Void
    Grey: _common_pb2.Void
    Blue: _common_pb2.Void
    Green: _common_pb2.Void
    Brown: _common_pb2.Void
    Pearl: _common_pb2.Void
    SigRed: _common_pb2.Void
    Red: _common_pb2.Void
    SteelGrey: _common_pb2.Void
    MetallicBlack: _common_pb2.Void
    TitaniumCopper: _common_pb2.Void
    SignatureBlue: _common_pb2.Void
    MidnightCherryRed: _common_pb2.Void
    Quicksilver: _common_pb2.Void
    UltraRed: _common_pb2.Void
    StealthGrey: _common_pb2.Void
    LunarSilver: _common_pb2.Void
    GlacierBlue: _common_pb2.Void
    DiamondBlack: _common_pb2.Void
    FrostBlue: _common_pb2.Void
    SilkRoadSilver: _common_pb2.Void
    MarineBlue: _common_pb2.Void
    GarnetRed: _common_pb2.Void
    CoastalBlue: _common_pb2.Void
    def __init__(self, Unknown: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., RedMulticoat: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SolidBlack: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SilverMetallic: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MidnightSilver: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., DeepBlue: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., PearlWhite: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., DefaultColor: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Black: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., White: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Silver: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Grey: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Blue: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Green: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Brown: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Pearl: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SigRed: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Red: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SteelGrey: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MetallicBlack: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TitaniumCopper: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SignatureBlue: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MidnightCherryRed: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Quicksilver: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., UltraRed: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., StealthGrey: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., LunarSilver: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., GlacierBlue: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., DiamondBlack: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., FrostBlue: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SilkRoadSilver: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MarineBlue: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., GarnetRed: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CoastalBlue: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class RearSeatHeaters(_message.Message):
    __slots__ = ("None_", "Base", "Executive", "Gentherm", "BaseModelX")
    NONE__FIELD_NUMBER: _ClassVar[int]
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXECUTIVE_FIELD_NUMBER: _ClassVar[int]
    GENTHERM_FIELD_NUMBER: _ClassVar[int]
    BASEMODELX_FIELD_NUMBER: _ClassVar[int]
    None_: _common_pb2.Void
    Base: _common_pb2.Void
    Executive: _common_pb2.Void
    Gentherm: _common_pb2.Void
    BaseModelX: _common_pb2.Void
    def __init__(self, None_: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Base: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Executive: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Gentherm: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., BaseModelX: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class SeatType(_message.Message):
    __slots__ = ("Base", "Recaro", "TeslaMsGen1")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RECARO_FIELD_NUMBER: _ClassVar[int]
    TESLAMSGEN1_FIELD_NUMBER: _ClassVar[int]
    Base: _common_pb2.Void
    Recaro: _common_pb2.Void
    TeslaMsGen1: _common_pb2.Void
    def __init__(self, Base: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Recaro: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TeslaMsGen1: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class RearSeatType(_message.Message):
    __slots__ = ("Base", "Recaro", "Executive", "TwoSeat", "FoldFlat", "FoldFlatMotorized", "TwoSeatConsole", "FoldFlatTwoMotor", "FoldFlatTwoMotorHall", "FoldFlatHallBuckles")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RECARO_FIELD_NUMBER: _ClassVar[int]
    EXECUTIVE_FIELD_NUMBER: _ClassVar[int]
    TWOSEAT_FIELD_NUMBER: _ClassVar[int]
    FOLDFLAT_FIELD_NUMBER: _ClassVar[int]
    FOLDFLATMOTORIZED_FIELD_NUMBER: _ClassVar[int]
    TWOSEATCONSOLE_FIELD_NUMBER: _ClassVar[int]
    FOLDFLATTWOMOTOR_FIELD_NUMBER: _ClassVar[int]
    FOLDFLATTWOMOTORHALL_FIELD_NUMBER: _ClassVar[int]
    FOLDFLATHALLBUCKLES_FIELD_NUMBER: _ClassVar[int]
    Base: _common_pb2.Void
    Recaro: _common_pb2.Void
    Executive: _common_pb2.Void
    TwoSeat: _common_pb2.Void
    FoldFlat: _common_pb2.Void
    FoldFlatMotorized: _common_pb2.Void
    TwoSeatConsole: _common_pb2.Void
    FoldFlatTwoMotor: _common_pb2.Void
    FoldFlatTwoMotorHall: _common_pb2.Void
    FoldFlatHallBuckles: _common_pb2.Void
    def __init__(self, Base: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Recaro: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Executive: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TwoSeat: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., FoldFlat: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., FoldFlatMotorized: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TwoSeatConsole: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., FoldFlatTwoMotor: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., FoldFlatTwoMotorHall: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., FoldFlatHallBuckles: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class ThirdRowSeatType(_message.Message):
    __slots__ = ("None_", "FuturisFoldFlat", "FuturisNoFoldFlat", "FlatFold")
    NONE__FIELD_NUMBER: _ClassVar[int]
    FUTURISFOLDFLAT_FIELD_NUMBER: _ClassVar[int]
    FUTURISNOFOLDFLAT_FIELD_NUMBER: _ClassVar[int]
    FLATFOLD_FIELD_NUMBER: _ClassVar[int]
    None_: _common_pb2.Void
    FuturisFoldFlat: _common_pb2.Void
    FuturisNoFoldFlat: _common_pb2.Void
    FlatFold: _common_pb2.Void
    def __init__(self, None_: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., FuturisFoldFlat: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., FuturisNoFoldFlat: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., FlatFold: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class ChargePortType(_message.Message):
    __slots__ = ("US", "EU", "GB", "CCS")
    US_FIELD_NUMBER: _ClassVar[int]
    EU_FIELD_NUMBER: _ClassVar[int]
    GB_FIELD_NUMBER: _ClassVar[int]
    CCS_FIELD_NUMBER: _ClassVar[int]
    US: _common_pb2.Void
    EU: _common_pb2.Void
    GB: _common_pb2.Void
    CCS: _common_pb2.Void
    def __init__(self, US: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., EU: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., GB: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CCS: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class RearDriveUnit(_message.Message):
    __slots__ = ("None_", "LargeRear", "SmallRear", "PM216MOSFET", "PM216IGBT", "CorianderSingle", "CorianderDual", "PermanentMagnet", "InductionDual")
    NONE__FIELD_NUMBER: _ClassVar[int]
    LARGEREAR_FIELD_NUMBER: _ClassVar[int]
    SMALLREAR_FIELD_NUMBER: _ClassVar[int]
    PM216MOSFET_FIELD_NUMBER: _ClassVar[int]
    PM216IGBT_FIELD_NUMBER: _ClassVar[int]
    CORIANDERSINGLE_FIELD_NUMBER: _ClassVar[int]
    CORIANDERDUAL_FIELD_NUMBER: _ClassVar[int]
    PERMANENTMAGNET_FIELD_NUMBER: _ClassVar[int]
    INDUCTIONDUAL_FIELD_NUMBER: _ClassVar[int]
    None_: _common_pb2.Void
    LargeRear: _common_pb2.Void
    SmallRear: _common_pb2.Void
    PM216MOSFET: _common_pb2.Void
    PM216IGBT: _common_pb2.Void
    CorianderSingle: _common_pb2.Void
    CorianderDual: _common_pb2.Void
    PermanentMagnet: _common_pb2.Void
    InductionDual: _common_pb2.Void
    def __init__(self, None_: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., LargeRear: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SmallRear: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., PM216MOSFET: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., PM216IGBT: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CorianderSingle: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CorianderDual: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., PermanentMagnet: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., InductionDual: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class EfficiencyPackage(_message.Message):
    __slots__ = ("Default", "M3SRPlus2020", "M3LR2020", "M3LRPerformance2020", "M3SRPlus2020Q4GFSH", "MY2020", "M32021", "MY2021", "SX2020", "S2", "SX2020H2", "M3SRPlus2021Q3GFSH", "M3SRPlus2021Q3Fremont", "MYSRPlus2021Q3GFSH", "MYSRPlus2022Q1TX", "MYRWDEU2022", "M3Poppyseed2024", "M32023GFSHExport", "MY2023GFSHExport", "MY2024", "MS2024", "MX2024", "MY2023SRRWD", "MY2024C", "MY2024GFSHExportSRRWD", "M3Poppyseed2024C", "M32025", "MY2025", "M32025B", "MY2025B", "MS2025", "MX2025", "MYRefresh2025ROW", "MYStandard2025", "MYRefresh2025CN", "MS2026", "MX2026", "MY2025M53", "M32025M53", "MY2025CNPlus", "MS2026B", "M32026B", "MY2026US")
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    M3SRPLUS2020_FIELD_NUMBER: _ClassVar[int]
    M3LR2020_FIELD_NUMBER: _ClassVar[int]
    M3LRPERFORMANCE2020_FIELD_NUMBER: _ClassVar[int]
    M3SRPLUS2020Q4GFSH_FIELD_NUMBER: _ClassVar[int]
    MY2020_FIELD_NUMBER: _ClassVar[int]
    M32021_FIELD_NUMBER: _ClassVar[int]
    MY2021_FIELD_NUMBER: _ClassVar[int]
    SX2020_FIELD_NUMBER: _ClassVar[int]
    S2_FIELD_NUMBER: _ClassVar[int]
    SX2020H2_FIELD_NUMBER: _ClassVar[int]
    M3SRPLUS2021Q3GFSH_FIELD_NUMBER: _ClassVar[int]
    M3SRPLUS2021Q3FREMONT_FIELD_NUMBER: _ClassVar[int]
    MYSRPLUS2021Q3GFSH_FIELD_NUMBER: _ClassVar[int]
    MYSRPLUS2022Q1TX_FIELD_NUMBER: _ClassVar[int]
    MYRWDEU2022_FIELD_NUMBER: _ClassVar[int]
    M3POPPYSEED2024_FIELD_NUMBER: _ClassVar[int]
    M32023GFSHEXPORT_FIELD_NUMBER: _ClassVar[int]
    MY2023GFSHEXPORT_FIELD_NUMBER: _ClassVar[int]
    MY2024_FIELD_NUMBER: _ClassVar[int]
    MS2024_FIELD_NUMBER: _ClassVar[int]
    MX2024_FIELD_NUMBER: _ClassVar[int]
    MY2023SRRWD_FIELD_NUMBER: _ClassVar[int]
    MY2024C_FIELD_NUMBER: _ClassVar[int]
    MY2024GFSHEXPORTSRRWD_FIELD_NUMBER: _ClassVar[int]
    M3POPPYSEED2024C_FIELD_NUMBER: _ClassVar[int]
    M32025_FIELD_NUMBER: _ClassVar[int]
    MY2025_FIELD_NUMBER: _ClassVar[int]
    M32025B_FIELD_NUMBER: _ClassVar[int]
    MY2025B_FIELD_NUMBER: _ClassVar[int]
    MS2025_FIELD_NUMBER: _ClassVar[int]
    MX2025_FIELD_NUMBER: _ClassVar[int]
    MYREFRESH2025ROW_FIELD_NUMBER: _ClassVar[int]
    MYSTANDARD2025_FIELD_NUMBER: _ClassVar[int]
    MYREFRESH2025CN_FIELD_NUMBER: _ClassVar[int]
    MS2026_FIELD_NUMBER: _ClassVar[int]
    MX2026_FIELD_NUMBER: _ClassVar[int]
    MY2025M53_FIELD_NUMBER: _ClassVar[int]
    M32025M53_FIELD_NUMBER: _ClassVar[int]
    MY2025CNPLUS_FIELD_NUMBER: _ClassVar[int]
    MS2026B_FIELD_NUMBER: _ClassVar[int]
    M32026B_FIELD_NUMBER: _ClassVar[int]
    MY2026US_FIELD_NUMBER: _ClassVar[int]
    Default: _common_pb2.Void
    M3SRPlus2020: _common_pb2.Void
    M3LR2020: _common_pb2.Void
    M3LRPerformance2020: _common_pb2.Void
    M3SRPlus2020Q4GFSH: _common_pb2.Void
    MY2020: _common_pb2.Void
    M32021: _common_pb2.Void
    MY2021: _common_pb2.Void
    SX2020: _common_pb2.Void
    S2: _common_pb2.Void
    SX2020H2: _common_pb2.Void
    M3SRPlus2021Q3GFSH: _common_pb2.Void
    M3SRPlus2021Q3Fremont: _common_pb2.Void
    MYSRPlus2021Q3GFSH: _common_pb2.Void
    MYSRPlus2022Q1TX: _common_pb2.Void
    MYRWDEU2022: _common_pb2.Void
    M3Poppyseed2024: _common_pb2.Void
    M32023GFSHExport: _common_pb2.Void
    MY2023GFSHExport: _common_pb2.Void
    MY2024: _common_pb2.Void
    MS2024: _common_pb2.Void
    MX2024: _common_pb2.Void
    MY2023SRRWD: _common_pb2.Void
    MY2024C: _common_pb2.Void
    MY2024GFSHExportSRRWD: _common_pb2.Void
    M3Poppyseed2024C: _common_pb2.Void
    M32025: _common_pb2.Void
    MY2025: _common_pb2.Void
    M32025B: _common_pb2.Void
    MY2025B: _common_pb2.Void
    MS2025: _common_pb2.Void
    MX2025: _common_pb2.Void
    MYRefresh2025ROW: _common_pb2.Void
    MYStandard2025: _common_pb2.Void
    MYRefresh2025CN: _common_pb2.Void
    MS2026: _common_pb2.Void
    MX2026: _common_pb2.Void
    MY2025M53: _common_pb2.Void
    M32025M53: _common_pb2.Void
    MY2025CNPlus: _common_pb2.Void
    MS2026B: _common_pb2.Void
    M32026B: _common_pb2.Void
    MY2026US: _common_pb2.Void
    def __init__(self, Default: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M3SRPlus2020: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M3LR2020: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M3LRPerformance2020: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M3SRPlus2020Q4GFSH: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2020: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M32021: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2021: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SX2020: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., S2: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SX2020H2: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M3SRPlus2021Q3GFSH: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M3SRPlus2021Q3Fremont: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MYSRPlus2021Q3GFSH: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MYSRPlus2022Q1TX: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MYRWDEU2022: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M3Poppyseed2024: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M32023GFSHExport: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2023GFSHExport: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2024: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MS2024: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MX2024: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2023SRRWD: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2024C: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2024GFSHExportSRRWD: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M3Poppyseed2024C: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M32025: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2025: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M32025B: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2025B: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MS2025: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MX2025: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MYRefresh2025ROW: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MYStandard2025: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MYRefresh2025CN: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MS2026: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MX2026: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2025M53: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M32025M53: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2025CNPlus: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MS2026B: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., M32026B: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MY2026US: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...

class GuiSettings(_message.Message):
    __slots__ = ("gui_distance_units", "gui_temperature_units", "gui_charge_rate_units", "gui_range_display", "timestamp", "gui_24_hour_time", "show_range_units", "gui_tirepressure_units")
    class TirePressureUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TirePressureUnitPsi: _ClassVar[GuiSettings.TirePressureUnit]
        TirePressureUnitBar: _ClassVar[GuiSettings.TirePressureUnit]
    TirePressureUnitPsi: GuiSettings.TirePressureUnit
    TirePressureUnitBar: GuiSettings.TirePressureUnit
    class SpeedUnit(_message.Message):
        __slots__ = ("KilometersPerHour", "MilesPerHour")
        KILOMETERSPERHOUR_FIELD_NUMBER: _ClassVar[int]
        MILESPERHOUR_FIELD_NUMBER: _ClassVar[int]
        KilometersPerHour: _common_pb2.Void
        MilesPerHour: _common_pb2.Void
        def __init__(self, KilometersPerHour: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MilesPerHour: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class TemperatureUnit(_message.Message):
        __slots__ = ("TemperatureF", "TemperatureC")
        TEMPERATUREF_FIELD_NUMBER: _ClassVar[int]
        TEMPERATUREC_FIELD_NUMBER: _ClassVar[int]
        TemperatureF: _common_pb2.Void
        TemperatureC: _common_pb2.Void
        def __init__(self, TemperatureF: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TemperatureC: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class ChargeRateUnit(_message.Message):
        __slots__ = ("Invalid", "KilometersPerHour", "MilesPerHour", "KW")
        INVALID_FIELD_NUMBER: _ClassVar[int]
        KILOMETERSPERHOUR_FIELD_NUMBER: _ClassVar[int]
        MILESPERHOUR_FIELD_NUMBER: _ClassVar[int]
        KW_FIELD_NUMBER: _ClassVar[int]
        Invalid: _common_pb2.Void
        KilometersPerHour: _common_pb2.Void
        MilesPerHour: _common_pb2.Void
        KW: _common_pb2.Void
        def __init__(self, Invalid: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., KilometersPerHour: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MilesPerHour: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., KW: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class RangeDisplay(_message.Message):
        __slots__ = ("Ideal", "Rated")
        IDEAL_FIELD_NUMBER: _ClassVar[int]
        RATED_FIELD_NUMBER: _ClassVar[int]
        Ideal: _common_pb2.Void
        Rated: _common_pb2.Void
        def __init__(self, Ideal: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Rated: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    GUI_DISTANCE_UNITS_FIELD_NUMBER: _ClassVar[int]
    GUI_TEMPERATURE_UNITS_FIELD_NUMBER: _ClassVar[int]
    GUI_CHARGE_RATE_UNITS_FIELD_NUMBER: _ClassVar[int]
    GUI_RANGE_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GUI_24_HOUR_TIME_FIELD_NUMBER: _ClassVar[int]
    SHOW_RANGE_UNITS_FIELD_NUMBER: _ClassVar[int]
    GUI_TIREPRESSURE_UNITS_FIELD_NUMBER: _ClassVar[int]
    gui_distance_units: GuiSettings.SpeedUnit
    gui_temperature_units: GuiSettings.TemperatureUnit
    gui_charge_rate_units: GuiSettings.ChargeRateUnit
    gui_range_display: GuiSettings.RangeDisplay
    timestamp: _timestamp_pb2.Timestamp
    gui_24_hour_time: bool
    show_range_units: bool
    gui_tirepressure_units: GuiSettings.TirePressureUnit
    def __init__(self, gui_distance_units: _Optional[_Union[GuiSettings.SpeedUnit, _Mapping]] = ..., gui_temperature_units: _Optional[_Union[GuiSettings.TemperatureUnit, _Mapping]] = ..., gui_charge_rate_units: _Optional[_Union[GuiSettings.ChargeRateUnit, _Mapping]] = ..., gui_range_display: _Optional[_Union[GuiSettings.RangeDisplay, _Mapping]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gui_24_hour_time: _Optional[bool] = ..., show_range_units: _Optional[bool] = ..., gui_tirepressure_units: _Optional[_Union[GuiSettings.TirePressureUnit, str]] = ...) -> None: ...

class VehicleConfig(_message.Message):
    __slots__ = ("car_special_type", "car_trim", "car_type", "sun_roof_installed", "wheel_type", "spoiler_type", "roof_color", "exterior_color", "rear_seat_heaters", "seat_type", "rear_seat_type", "third_row_seat_type", "charge_port_type", "timestamp", "interior_trim_type", "driver_assist", "performance_package", "front_drive_unit", "rear_drive_unit", "efficiency_package", "exterior_trim_type", "steering_wheel_type", "red_brake_calipers", "use_range_badging", "range_plus_badging", "has_ludicrous_mode", "can_actuate_trunks", "has_air_suspension", "rhd", "plg", "ece_restrictions", "eu_vehicle", "motorized_charge_port", "can_accept_navigation_requests", "key_version", "mobile_enabled", "default_charge_to_max", "steering_wheel_heater_installed", "sentry_mode_supported", "homelink_supported", "webcam_supported", "bioweapon_mode_supported", "dashcam_clip_save_supported", "has_pws", "utc_offset", "has_seat_cooling", "paint_color_override", "tpms_pressures_supported", "vehicle_badging", "exterior_trim_override", "headlamp_type", "aux_park_lamps", "is_raven", "has_auto_seat_climate", "has_front_row_seat_heaters", "has_third_row_seat_heaters", "supports_qr_pairing", "vin", "disable_window_vent_close", "webcam_selfie_supported", "cop_user_set_temp_supported", "has_auto_stw_heat", "rearlight_type", "rear_seat_heater_type", "webcam_grid_supported", "has_tesla_badge", "has_tesla_wordmark", "fascia_type", "accessory_lightbar_type", "sentry_preview_supported", "seat_trim_type", "drivetrain_type", "lightshow_supported", "mobile_dashcam_viewer_version", "has_premium_connectivity", "car_wrap_enabled", "supports_ride_height", "supports_set_arrival_energy", "supports_pillar_camera_metadata", "chassis_type", "is_china_vehicle", "is_using_unreal_apviz", "supports_flexible_dashcam_bitrate", "front_fascia_camera_type", "turn_indicator_control_type", "has_rear_display", "window_tint_color", "interior_upper_trim_type", "badging_material_type", "webcam_interior_only", "country_code", "bed_lighting_type", "rear_light_hardware_variant", "autopilot_base", "autopilot_override_state", "autopilot_override_expire_time", "supports_dynamic_environments", "wheel_caps_on")
    class AuxParkLamps_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AuxParkLampsNaBase: _ClassVar[VehicleConfig.AuxParkLamps_E]
        AuxParkLampsNaPremium: _ClassVar[VehicleConfig.AuxParkLamps_E]
        AuxParkLampsEu: _ClassVar[VehicleConfig.AuxParkLamps_E]
        AuxParkLampsNone: _ClassVar[VehicleConfig.AuxParkLamps_E]
    AuxParkLampsNaBase: VehicleConfig.AuxParkLamps_E
    AuxParkLampsNaPremium: VehicleConfig.AuxParkLamps_E
    AuxParkLampsEu: VehicleConfig.AuxParkLamps_E
    AuxParkLampsNone: VehicleConfig.AuxParkLamps_E
    class BadgingMaterialType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BadgingMaterialTypeChromeSilver: _ClassVar[VehicleConfig.BadgingMaterialType]
        BadgingMaterialTypeBlackMatte: _ClassVar[VehicleConfig.BadgingMaterialType]
    BadgingMaterialTypeChromeSilver: VehicleConfig.BadgingMaterialType
    BadgingMaterialTypeBlackMatte: VehicleConfig.BadgingMaterialType
    class BedLightingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BedLightingTypeBase: _ClassVar[VehicleConfig.BedLightingType]
        BedLightingTypePremium: _ClassVar[VehicleConfig.BedLightingType]
    BedLightingTypeBase: VehicleConfig.BedLightingType
    BedLightingTypePremium: VehicleConfig.BedLightingType
    class DrivetrainType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DrivetrainTypeRWD: _ClassVar[VehicleConfig.DrivetrainType]
        DrivetrainTypeAWD: _ClassVar[VehicleConfig.DrivetrainType]
        DrivetrainTypeAWDTriMotor: _ClassVar[VehicleConfig.DrivetrainType]
    DrivetrainTypeRWD: VehicleConfig.DrivetrainType
    DrivetrainTypeAWD: VehicleConfig.DrivetrainType
    DrivetrainTypeAWDTriMotor: VehicleConfig.DrivetrainType
    class FrontFasciaCameraType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FrontFasciaCameraTypeNone: _ClassVar[VehicleConfig.FrontFasciaCameraType]
        FrontFasciaCameraTypeIMX963: _ClassVar[VehicleConfig.FrontFasciaCameraType]
        FrontFasciaCameraTypeIMX00N: _ClassVar[VehicleConfig.FrontFasciaCameraType]
    FrontFasciaCameraTypeNone: VehicleConfig.FrontFasciaCameraType
    FrontFasciaCameraTypeIMX963: VehicleConfig.FrontFasciaCameraType
    FrontFasciaCameraTypeIMX00N: VehicleConfig.FrontFasciaCameraType
    class HeadlampType_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HeadlampTypePremium: _ClassVar[VehicleConfig.HeadlampType_E]
        HeadlampTypeGlobal: _ClassVar[VehicleConfig.HeadlampType_E]
        HeadlampTypeHalogen: _ClassVar[VehicleConfig.HeadlampType_E]
        HeadlampTypeHid: _ClassVar[VehicleConfig.HeadlampType_E]
        HeadlampTypeLed: _ClassVar[VehicleConfig.HeadlampType_E]
        HeadlampTypeBase: _ClassVar[VehicleConfig.HeadlampType_E]
    HeadlampTypePremium: VehicleConfig.HeadlampType_E
    HeadlampTypeGlobal: VehicleConfig.HeadlampType_E
    HeadlampTypeHalogen: VehicleConfig.HeadlampType_E
    HeadlampTypeHid: VehicleConfig.HeadlampType_E
    HeadlampTypeLed: VehicleConfig.HeadlampType_E
    HeadlampTypeBase: VehicleConfig.HeadlampType_E
    class InteriorUpperTrimType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        InteriorUpperTrimTypePolarGrey: _ClassVar[VehicleConfig.InteriorUpperTrimType]
        InteriorUpperTrimTypeMammothBlack: _ClassVar[VehicleConfig.InteriorUpperTrimType]
    InteriorUpperTrimTypePolarGrey: VehicleConfig.InteriorUpperTrimType
    InteriorUpperTrimTypeMammothBlack: VehicleConfig.InteriorUpperTrimType
    class RearLightHardwareVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RearLightHardwareVariantUnknown: _ClassVar[VehicleConfig.RearLightHardwareVariant]
        RearLightHardwareVariantBase: _ClassVar[VehicleConfig.RearLightHardwareVariant]
        RearLightHardwareVariantPremiumV1: _ClassVar[VehicleConfig.RearLightHardwareVariant]
        RearLightHardwareVariantPremiumV2: _ClassVar[VehicleConfig.RearLightHardwareVariant]
    RearLightHardwareVariantUnknown: VehicleConfig.RearLightHardwareVariant
    RearLightHardwareVariantBase: VehicleConfig.RearLightHardwareVariant
    RearLightHardwareVariantPremiumV1: VehicleConfig.RearLightHardwareVariant
    RearLightHardwareVariantPremiumV2: VehicleConfig.RearLightHardwareVariant
    class RearLightType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RearLightTypeNA: _ClassVar[VehicleConfig.RearLightType]
        RearLightTypeEuCn: _ClassVar[VehicleConfig.RearLightType]
        RearLightTypeGlobal: _ClassVar[VehicleConfig.RearLightType]
    RearLightTypeNA: VehicleConfig.RearLightType
    RearLightTypeEuCn: VehicleConfig.RearLightType
    RearLightTypeGlobal: VehicleConfig.RearLightType
    class SeatTrimType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SeatTrimTypeBase: _ClassVar[VehicleConfig.SeatTrimType]
        SeatTrimTypeSport: _ClassVar[VehicleConfig.SeatTrimType]
        SeatTrimTypeBaseTextile: _ClassVar[VehicleConfig.SeatTrimType]
    SeatTrimTypeBase: VehicleConfig.SeatTrimType
    SeatTrimTypeSport: VehicleConfig.SeatTrimType
    SeatTrimTypeBaseTextile: VehicleConfig.SeatTrimType
    class TurnIndicatorControlType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TurnIndicatorControlTypeUnknown: _ClassVar[VehicleConfig.TurnIndicatorControlType]
        TurnIndicatorControlTypeSingleDetentStalk: _ClassVar[VehicleConfig.TurnIndicatorControlType]
        TurnIndicatorControlTypeSWSButton: _ClassVar[VehicleConfig.TurnIndicatorControlType]
    TurnIndicatorControlTypeUnknown: VehicleConfig.TurnIndicatorControlType
    TurnIndicatorControlTypeSingleDetentStalk: VehicleConfig.TurnIndicatorControlType
    TurnIndicatorControlTypeSWSButton: VehicleConfig.TurnIndicatorControlType
    class CarType(_message.Message):
        __slots__ = ("CarTypeModelS", "CarTypeModelX", "CarTypeModelS2", "CarTypeModel3", "CarTypeModelY", "CarTypeSemiTruck", "CarTypeLychee", "CarTypeTamarind", "CarTypeCybertruck", "CarTypeSemiTruckV2")
        CARTYPEMODELS_FIELD_NUMBER: _ClassVar[int]
        CARTYPEMODELX_FIELD_NUMBER: _ClassVar[int]
        CARTYPEMODELS2_FIELD_NUMBER: _ClassVar[int]
        CARTYPEMODEL3_FIELD_NUMBER: _ClassVar[int]
        CARTYPEMODELY_FIELD_NUMBER: _ClassVar[int]
        CARTYPESEMITRUCK_FIELD_NUMBER: _ClassVar[int]
        CARTYPELYCHEE_FIELD_NUMBER: _ClassVar[int]
        CARTYPETAMARIND_FIELD_NUMBER: _ClassVar[int]
        CARTYPECYBERTRUCK_FIELD_NUMBER: _ClassVar[int]
        CARTYPESEMITRUCKV2_FIELD_NUMBER: _ClassVar[int]
        CarTypeModelS: _common_pb2.Void
        CarTypeModelX: _common_pb2.Void
        CarTypeModelS2: _common_pb2.Void
        CarTypeModel3: _common_pb2.Void
        CarTypeModelY: _common_pb2.Void
        CarTypeSemiTruck: _common_pb2.Void
        CarTypeLychee: _common_pb2.Void
        CarTypeTamarind: _common_pb2.Void
        CarTypeCybertruck: _common_pb2.Void
        CarTypeSemiTruckV2: _common_pb2.Void
        def __init__(self, CarTypeModelS: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CarTypeModelX: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CarTypeModelS2: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CarTypeModel3: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CarTypeModelY: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CarTypeSemiTruck: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CarTypeLychee: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CarTypeTamarind: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CarTypeCybertruck: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CarTypeSemiTruckV2: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class DriverAssist(_message.Message):
        __slots__ = ("None_", "MonoCam", "ParkerPascal", "ParkerPascal25", "TeslaAP3")
        NONE__FIELD_NUMBER: _ClassVar[int]
        MONOCAM_FIELD_NUMBER: _ClassVar[int]
        PARKERPASCAL_FIELD_NUMBER: _ClassVar[int]
        PARKERPASCAL25_FIELD_NUMBER: _ClassVar[int]
        TESLAAP3_FIELD_NUMBER: _ClassVar[int]
        None_: _common_pb2.Void
        MonoCam: _common_pb2.Void
        ParkerPascal: _common_pb2.Void
        ParkerPascal25: _common_pb2.Void
        TeslaAP3: _common_pb2.Void
        def __init__(self, None_: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., MonoCam: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ParkerPascal: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ParkerPascal25: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TeslaAP3: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class PerformancePackage(_message.Message):
        __slots__ = ("None_", "Base", "Performance", "BasePlus")
        NONE__FIELD_NUMBER: _ClassVar[int]
        BASE_FIELD_NUMBER: _ClassVar[int]
        PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
        BASEPLUS_FIELD_NUMBER: _ClassVar[int]
        None_: _common_pb2.Void
        Base: _common_pb2.Void
        Performance: _common_pb2.Void
        BasePlus: _common_pb2.Void
        def __init__(self, None_: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Base: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Performance: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., BasePlus: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class FrontDriveUnit(_message.Message):
        __slots__ = ("NoneOrSmall", "PermanentMagnet")
        NONEORSMALL_FIELD_NUMBER: _ClassVar[int]
        PERMANENTMAGNET_FIELD_NUMBER: _ClassVar[int]
        NoneOrSmall: _common_pb2.Void
        PermanentMagnet: _common_pb2.Void
        def __init__(self, NoneOrSmall: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., PermanentMagnet: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class SteeringWheelType(_message.Message):
        __slots__ = ("Unknown", "Round", "Yoke", "Squircle")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        ROUND_FIELD_NUMBER: _ClassVar[int]
        YOKE_FIELD_NUMBER: _ClassVar[int]
        SQUIRCLE_FIELD_NUMBER: _ClassVar[int]
        Unknown: _common_pb2.Void
        Round: _common_pb2.Void
        Yoke: _common_pb2.Void
        Squircle: _common_pb2.Void
        def __init__(self, Unknown: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Round: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Yoke: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Squircle: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class InteriorTrimType(_message.Message):
        __slots__ = ("UNKNOWN", "BLACK", "WHITE", "BLACKCONSOLE2", "WHITECONSOLE2", "ALLBLACK", "BLACKANDWHITE", "CREAM", "WALNUTCREAM", "WALNUTWHITE", "EBONYBLACK", "CARBONCREAM", "CARBONWHITE", "CARBONBLACK", "TACTICALGREY")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        BLACK_FIELD_NUMBER: _ClassVar[int]
        WHITE_FIELD_NUMBER: _ClassVar[int]
        BLACKCONSOLE2_FIELD_NUMBER: _ClassVar[int]
        WHITECONSOLE2_FIELD_NUMBER: _ClassVar[int]
        ALLBLACK_FIELD_NUMBER: _ClassVar[int]
        BLACKANDWHITE_FIELD_NUMBER: _ClassVar[int]
        CREAM_FIELD_NUMBER: _ClassVar[int]
        WALNUTCREAM_FIELD_NUMBER: _ClassVar[int]
        WALNUTWHITE_FIELD_NUMBER: _ClassVar[int]
        EBONYBLACK_FIELD_NUMBER: _ClassVar[int]
        CARBONCREAM_FIELD_NUMBER: _ClassVar[int]
        CARBONWHITE_FIELD_NUMBER: _ClassVar[int]
        CARBONBLACK_FIELD_NUMBER: _ClassVar[int]
        TACTICALGREY_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN: _common_pb2.Void
        BLACK: _common_pb2.Void
        WHITE: _common_pb2.Void
        BLACKCONSOLE2: _common_pb2.Void
        WHITECONSOLE2: _common_pb2.Void
        ALLBLACK: _common_pb2.Void
        BLACKANDWHITE: _common_pb2.Void
        CREAM: _common_pb2.Void
        WALNUTCREAM: _common_pb2.Void
        WALNUTWHITE: _common_pb2.Void
        EBONYBLACK: _common_pb2.Void
        CARBONCREAM: _common_pb2.Void
        CARBONWHITE: _common_pb2.Void
        CARBONBLACK: _common_pb2.Void
        TACTICALGREY: _common_pb2.Void
        def __init__(self, UNKNOWN: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., BLACK: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., WHITE: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., BLACKCONSOLE2: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., WHITECONSOLE2: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ALLBLACK: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., BLACKANDWHITE: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CREAM: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., WALNUTCREAM: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., WALNUTWHITE: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., EBONYBLACK: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CARBONCREAM: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CARBONWHITE: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., CARBONBLACK: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., TACTICALGREY: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class ExteriorTrimType(_message.Message):
        __slots__ = ("UNKNOWN", "STANDARDCHROME", "SATINBLACK")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        STANDARDCHROME_FIELD_NUMBER: _ClassVar[int]
        SATINBLACK_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN: _common_pb2.Void
        STANDARDCHROME: _common_pb2.Void
        SATINBLACK: _common_pb2.Void
        def __init__(self, UNKNOWN: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., STANDARDCHROME: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., SATINBLACK: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    CAR_SPECIAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAR_TRIM_FIELD_NUMBER: _ClassVar[int]
    CAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUN_ROOF_INSTALLED_FIELD_NUMBER: _ClassVar[int]
    WHEEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPOILER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOF_COLOR_FIELD_NUMBER: _ClassVar[int]
    EXTERIOR_COLOR_FIELD_NUMBER: _ClassVar[int]
    REAR_SEAT_HEATERS_FIELD_NUMBER: _ClassVar[int]
    SEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REAR_SEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    THIRD_ROW_SEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    INTERIOR_TRIM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DRIVER_ASSIST_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    FRONT_DRIVE_UNIT_FIELD_NUMBER: _ClassVar[int]
    REAR_DRIVE_UNIT_FIELD_NUMBER: _ClassVar[int]
    EFFICIENCY_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    EXTERIOR_TRIM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STEERING_WHEEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    RED_BRAKE_CALIPERS_FIELD_NUMBER: _ClassVar[int]
    USE_RANGE_BADGING_FIELD_NUMBER: _ClassVar[int]
    RANGE_PLUS_BADGING_FIELD_NUMBER: _ClassVar[int]
    HAS_LUDICROUS_MODE_FIELD_NUMBER: _ClassVar[int]
    CAN_ACTUATE_TRUNKS_FIELD_NUMBER: _ClassVar[int]
    HAS_AIR_SUSPENSION_FIELD_NUMBER: _ClassVar[int]
    RHD_FIELD_NUMBER: _ClassVar[int]
    PLG_FIELD_NUMBER: _ClassVar[int]
    ECE_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    EU_VEHICLE_FIELD_NUMBER: _ClassVar[int]
    MOTORIZED_CHARGE_PORT_FIELD_NUMBER: _ClassVar[int]
    CAN_ACCEPT_NAVIGATION_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    MOBILE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHARGE_TO_MAX_FIELD_NUMBER: _ClassVar[int]
    STEERING_WHEEL_HEATER_INSTALLED_FIELD_NUMBER: _ClassVar[int]
    SENTRY_MODE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    HOMELINK_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    WEBCAM_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BIOWEAPON_MODE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DASHCAM_CLIP_SAVE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    HAS_PWS_FIELD_NUMBER: _ClassVar[int]
    UTC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    HAS_SEAT_COOLING_FIELD_NUMBER: _ClassVar[int]
    PAINT_COLOR_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_BADGING_FIELD_NUMBER: _ClassVar[int]
    EXTERIOR_TRIM_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    HEADLAMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUX_PARK_LAMPS_FIELD_NUMBER: _ClassVar[int]
    IS_RAVEN_FIELD_NUMBER: _ClassVar[int]
    HAS_AUTO_SEAT_CLIMATE_FIELD_NUMBER: _ClassVar[int]
    HAS_FRONT_ROW_SEAT_HEATERS_FIELD_NUMBER: _ClassVar[int]
    HAS_THIRD_ROW_SEAT_HEATERS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_QR_PAIRING_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    DISABLE_WINDOW_VENT_CLOSE_FIELD_NUMBER: _ClassVar[int]
    WEBCAM_SELFIE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    COP_USER_SET_TEMP_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    HAS_AUTO_STW_HEAT_FIELD_NUMBER: _ClassVar[int]
    REARLIGHT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REAR_SEAT_HEATER_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEBCAM_GRID_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    HAS_TESLA_BADGE_FIELD_NUMBER: _ClassVar[int]
    HAS_TESLA_WORDMARK_FIELD_NUMBER: _ClassVar[int]
    FASCIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_LIGHTBAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENTRY_PREVIEW_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SEAT_TRIM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DRIVETRAIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIGHTSHOW_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MOBILE_DASHCAM_VIEWER_VERSION_FIELD_NUMBER: _ClassVar[int]
    HAS_PREMIUM_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    CAR_WRAP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_RIDE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_SET_ARRIVAL_ENERGY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_PILLAR_CAMERA_METADATA_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_CHINA_VEHICLE_FIELD_NUMBER: _ClassVar[int]
    IS_USING_UNREAL_APVIZ_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_FLEXIBLE_DASHCAM_BITRATE_FIELD_NUMBER: _ClassVar[int]
    FRONT_FASCIA_CAMERA_TYPE_FIELD_NUMBER: _ClassVar[int]
    TURN_INDICATOR_CONTROL_TYPE_FIELD_NUMBER: _ClassVar[int]
    HAS_REAR_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TINT_COLOR_FIELD_NUMBER: _ClassVar[int]
    INTERIOR_UPPER_TRIM_TYPE_FIELD_NUMBER: _ClassVar[int]
    BADGING_MATERIAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEBCAM_INTERIOR_ONLY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    BED_LIGHTING_TYPE_FIELD_NUMBER: _ClassVar[int]
    REAR_LIGHT_HARDWARE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    AUTOPILOT_BASE_FIELD_NUMBER: _ClassVar[int]
    AUTOPILOT_OVERRIDE_STATE_FIELD_NUMBER: _ClassVar[int]
    AUTOPILOT_OVERRIDE_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_DYNAMIC_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    WHEEL_CAPS_ON_FIELD_NUMBER: _ClassVar[int]
    car_special_type: VehicleBadging
    car_trim: CarTrim
    car_type: VehicleConfig.CarType
    sun_roof_installed: SunRoofType
    wheel_type: WheelType
    spoiler_type: SpoilerType
    roof_color: RoofColor
    exterior_color: ExteriorColor
    rear_seat_heaters: RearSeatHeaters
    seat_type: SeatType
    rear_seat_type: RearSeatType
    third_row_seat_type: ThirdRowSeatType
    charge_port_type: ChargePortType
    timestamp: _timestamp_pb2.Timestamp
    interior_trim_type: VehicleConfig.InteriorTrimType
    driver_assist: VehicleConfig.DriverAssist
    performance_package: VehicleConfig.PerformancePackage
    front_drive_unit: VehicleConfig.FrontDriveUnit
    rear_drive_unit: RearDriveUnit
    efficiency_package: EfficiencyPackage
    exterior_trim_type: VehicleConfig.ExteriorTrimType
    steering_wheel_type: VehicleConfig.SteeringWheelType
    red_brake_calipers: bool
    use_range_badging: bool
    range_plus_badging: bool
    has_ludicrous_mode: bool
    can_actuate_trunks: bool
    has_air_suspension: bool
    rhd: bool
    plg: bool
    ece_restrictions: bool
    eu_vehicle: bool
    motorized_charge_port: bool
    can_accept_navigation_requests: bool
    key_version: int
    mobile_enabled: bool
    default_charge_to_max: bool
    steering_wheel_heater_installed: bool
    sentry_mode_supported: bool
    homelink_supported: bool
    webcam_supported: bool
    bioweapon_mode_supported: bool
    dashcam_clip_save_supported: bool
    has_pws: bool
    utc_offset: int
    has_seat_cooling: bool
    paint_color_override: str
    tpms_pressures_supported: bool
    vehicle_badging: int
    exterior_trim_override: str
    headlamp_type: VehicleConfig.HeadlampType_E
    aux_park_lamps: VehicleConfig.AuxParkLamps_E
    is_raven: bool
    has_auto_seat_climate: bool
    has_front_row_seat_heaters: bool
    has_third_row_seat_heaters: bool
    supports_qr_pairing: bool
    vin: str
    disable_window_vent_close: bool
    webcam_selfie_supported: bool
    cop_user_set_temp_supported: bool
    has_auto_stw_heat: bool
    rearlight_type: VehicleConfig.RearLightType
    rear_seat_heater_type: _common_pb2.RearSeatHeaterType
    webcam_grid_supported: bool
    has_tesla_badge: bool
    has_tesla_wordmark: bool
    fascia_type: _common_pb2.FasciaType
    accessory_lightbar_type: _common_pb2.AccessoryLightbarType
    sentry_preview_supported: bool
    seat_trim_type: VehicleConfig.SeatTrimType
    drivetrain_type: VehicleConfig.DrivetrainType
    lightshow_supported: bool
    mobile_dashcam_viewer_version: int
    has_premium_connectivity: bool
    car_wrap_enabled: bool
    supports_ride_height: bool
    supports_set_arrival_energy: bool
    supports_pillar_camera_metadata: bool
    chassis_type: _common_pb2.ChassisType
    is_china_vehicle: bool
    is_using_unreal_apviz: bool
    supports_flexible_dashcam_bitrate: bool
    front_fascia_camera_type: VehicleConfig.FrontFasciaCameraType
    turn_indicator_control_type: VehicleConfig.TurnIndicatorControlType
    has_rear_display: bool
    window_tint_color: str
    interior_upper_trim_type: VehicleConfig.InteriorUpperTrimType
    badging_material_type: VehicleConfig.BadgingMaterialType
    webcam_interior_only: bool
    country_code: str
    bed_lighting_type: VehicleConfig.BedLightingType
    rear_light_hardware_variant: VehicleConfig.RearLightHardwareVariant
    autopilot_base: AutopilotBase
    autopilot_override_state: AutopilotOverrideState
    autopilot_override_expire_time: int
    supports_dynamic_environments: bool
    wheel_caps_on: bool
    def __init__(self, car_special_type: _Optional[_Union[VehicleBadging, _Mapping]] = ..., car_trim: _Optional[_Union[CarTrim, _Mapping]] = ..., car_type: _Optional[_Union[VehicleConfig.CarType, _Mapping]] = ..., sun_roof_installed: _Optional[_Union[SunRoofType, _Mapping]] = ..., wheel_type: _Optional[_Union[WheelType, _Mapping]] = ..., spoiler_type: _Optional[_Union[SpoilerType, _Mapping]] = ..., roof_color: _Optional[_Union[RoofColor, _Mapping]] = ..., exterior_color: _Optional[_Union[ExteriorColor, _Mapping]] = ..., rear_seat_heaters: _Optional[_Union[RearSeatHeaters, _Mapping]] = ..., seat_type: _Optional[_Union[SeatType, _Mapping]] = ..., rear_seat_type: _Optional[_Union[RearSeatType, _Mapping]] = ..., third_row_seat_type: _Optional[_Union[ThirdRowSeatType, _Mapping]] = ..., charge_port_type: _Optional[_Union[ChargePortType, _Mapping]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., interior_trim_type: _Optional[_Union[VehicleConfig.InteriorTrimType, _Mapping]] = ..., driver_assist: _Optional[_Union[VehicleConfig.DriverAssist, _Mapping]] = ..., performance_package: _Optional[_Union[VehicleConfig.PerformancePackage, _Mapping]] = ..., front_drive_unit: _Optional[_Union[VehicleConfig.FrontDriveUnit, _Mapping]] = ..., rear_drive_unit: _Optional[_Union[RearDriveUnit, _Mapping]] = ..., efficiency_package: _Optional[_Union[EfficiencyPackage, _Mapping]] = ..., exterior_trim_type: _Optional[_Union[VehicleConfig.ExteriorTrimType, _Mapping]] = ..., steering_wheel_type: _Optional[_Union[VehicleConfig.SteeringWheelType, _Mapping]] = ..., red_brake_calipers: _Optional[bool] = ..., use_range_badging: _Optional[bool] = ..., range_plus_badging: _Optional[bool] = ..., has_ludicrous_mode: _Optional[bool] = ..., can_actuate_trunks: _Optional[bool] = ..., has_air_suspension: _Optional[bool] = ..., rhd: _Optional[bool] = ..., plg: _Optional[bool] = ..., ece_restrictions: _Optional[bool] = ..., eu_vehicle: _Optional[bool] = ..., motorized_charge_port: _Optional[bool] = ..., can_accept_navigation_requests: _Optional[bool] = ..., key_version: _Optional[int] = ..., mobile_enabled: _Optional[bool] = ..., default_charge_to_max: _Optional[bool] = ..., steering_wheel_heater_installed: _Optional[bool] = ..., sentry_mode_supported: _Optional[bool] = ..., homelink_supported: _Optional[bool] = ..., webcam_supported: _Optional[bool] = ..., bioweapon_mode_supported: _Optional[bool] = ..., dashcam_clip_save_supported: _Optional[bool] = ..., has_pws: _Optional[bool] = ..., utc_offset: _Optional[int] = ..., has_seat_cooling: _Optional[bool] = ..., paint_color_override: _Optional[str] = ..., tpms_pressures_supported: _Optional[bool] = ..., vehicle_badging: _Optional[int] = ..., exterior_trim_override: _Optional[str] = ..., headlamp_type: _Optional[_Union[VehicleConfig.HeadlampType_E, str]] = ..., aux_park_lamps: _Optional[_Union[VehicleConfig.AuxParkLamps_E, str]] = ..., is_raven: _Optional[bool] = ..., has_auto_seat_climate: _Optional[bool] = ..., has_front_row_seat_heaters: _Optional[bool] = ..., has_third_row_seat_heaters: _Optional[bool] = ..., supports_qr_pairing: _Optional[bool] = ..., vin: _Optional[str] = ..., disable_window_vent_close: _Optional[bool] = ..., webcam_selfie_supported: _Optional[bool] = ..., cop_user_set_temp_supported: _Optional[bool] = ..., has_auto_stw_heat: _Optional[bool] = ..., rearlight_type: _Optional[_Union[VehicleConfig.RearLightType, str]] = ..., rear_seat_heater_type: _Optional[_Union[_common_pb2.RearSeatHeaterType, str]] = ..., webcam_grid_supported: _Optional[bool] = ..., has_tesla_badge: _Optional[bool] = ..., has_tesla_wordmark: _Optional[bool] = ..., fascia_type: _Optional[_Union[_common_pb2.FasciaType, str]] = ..., accessory_lightbar_type: _Optional[_Union[_common_pb2.AccessoryLightbarType, str]] = ..., sentry_preview_supported: _Optional[bool] = ..., seat_trim_type: _Optional[_Union[VehicleConfig.SeatTrimType, str]] = ..., drivetrain_type: _Optional[_Union[VehicleConfig.DrivetrainType, str]] = ..., lightshow_supported: _Optional[bool] = ..., mobile_dashcam_viewer_version: _Optional[int] = ..., has_premium_connectivity: _Optional[bool] = ..., car_wrap_enabled: _Optional[bool] = ..., supports_ride_height: _Optional[bool] = ..., supports_set_arrival_energy: _Optional[bool] = ..., supports_pillar_camera_metadata: _Optional[bool] = ..., chassis_type: _Optional[_Union[_common_pb2.ChassisType, str]] = ..., is_china_vehicle: _Optional[bool] = ..., is_using_unreal_apviz: _Optional[bool] = ..., supports_flexible_dashcam_bitrate: _Optional[bool] = ..., front_fascia_camera_type: _Optional[_Union[VehicleConfig.FrontFasciaCameraType, str]] = ..., turn_indicator_control_type: _Optional[_Union[VehicleConfig.TurnIndicatorControlType, str]] = ..., has_rear_display: _Optional[bool] = ..., window_tint_color: _Optional[str] = ..., interior_upper_trim_type: _Optional[_Union[VehicleConfig.InteriorUpperTrimType, str]] = ..., badging_material_type: _Optional[_Union[VehicleConfig.BadgingMaterialType, str]] = ..., webcam_interior_only: _Optional[bool] = ..., country_code: _Optional[str] = ..., bed_lighting_type: _Optional[_Union[VehicleConfig.BedLightingType, str]] = ..., rear_light_hardware_variant: _Optional[_Union[VehicleConfig.RearLightHardwareVariant, str]] = ..., autopilot_base: _Optional[_Union[AutopilotBase, str]] = ..., autopilot_override_state: _Optional[_Union[AutopilotOverrideState, str]] = ..., autopilot_override_expire_time: _Optional[int] = ..., supports_dynamic_environments: _Optional[bool] = ..., wheel_caps_on: _Optional[bool] = ...) -> None: ...

class ParkedAccessoryState(_message.Message):
    __slots__ = ("tent_mode_request", "horizon_leveling_state", "front_zone_light_request", "rear_zone_light_request", "truck_bed_lights_brightness", "truck_bed_lights_auto_brightness", "truck_bed_lights_auto_state", "truck_bed_lights_controls_disabled", "accessory_lightbar_middle_on", "accessory_lightbar_ditch_on", "accessory_lightbar_brightness", "accessory_lightbar_low", "accessory_lightbar_med", "accessory_lightbar_high", "has_tent_mode", "timestamp")
    TENT_MODE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    HORIZON_LEVELING_STATE_FIELD_NUMBER: _ClassVar[int]
    FRONT_ZONE_LIGHT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REAR_ZONE_LIGHT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_AUTO_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_AUTO_STATE_FIELD_NUMBER: _ClassVar[int]
    TRUCK_BED_LIGHTS_CONTROLS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_LIGHTBAR_MIDDLE_ON_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_LIGHTBAR_DITCH_ON_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_LIGHTBAR_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_LIGHTBAR_LOW_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_LIGHTBAR_MED_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_LIGHTBAR_HIGH_FIELD_NUMBER: _ClassVar[int]
    HAS_TENT_MODE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    tent_mode_request: bool
    horizon_leveling_state: bool
    front_zone_light_request: _common_pb2.ZoneLightRequest
    rear_zone_light_request: _common_pb2.ZoneLightRequest
    truck_bed_lights_brightness: int
    truck_bed_lights_auto_brightness: int
    truck_bed_lights_auto_state: bool
    truck_bed_lights_controls_disabled: bool
    accessory_lightbar_middle_on: bool
    accessory_lightbar_ditch_on: bool
    accessory_lightbar_brightness: int
    accessory_lightbar_low: int
    accessory_lightbar_med: int
    accessory_lightbar_high: int
    has_tent_mode: bool
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, tent_mode_request: _Optional[bool] = ..., horizon_leveling_state: _Optional[bool] = ..., front_zone_light_request: _Optional[_Union[_common_pb2.ZoneLightRequest, str]] = ..., rear_zone_light_request: _Optional[_Union[_common_pb2.ZoneLightRequest, str]] = ..., truck_bed_lights_brightness: _Optional[int] = ..., truck_bed_lights_auto_brightness: _Optional[int] = ..., truck_bed_lights_auto_state: _Optional[bool] = ..., truck_bed_lights_controls_disabled: _Optional[bool] = ..., accessory_lightbar_middle_on: _Optional[bool] = ..., accessory_lightbar_ditch_on: _Optional[bool] = ..., accessory_lightbar_brightness: _Optional[int] = ..., accessory_lightbar_low: _Optional[int] = ..., accessory_lightbar_med: _Optional[int] = ..., accessory_lightbar_high: _Optional[int] = ..., has_tent_mode: _Optional[bool] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SohState(_message.Message):
    __slots__ = ("soh_test_state", "soh_test_end_mode", "soh_result", "timestamp")
    class WarrantyServiceResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOH_OK: _ClassVar[SohState.WarrantyServiceResult]
        SOH_REDUCED: _ClassVar[SohState.WarrantyServiceResult]
        SOH_NO_INTERNET: _ClassVar[SohState.WarrantyServiceResult]
        SOH_UNKNOWN: _ClassVar[SohState.WarrantyServiceResult]
    SOH_OK: SohState.WarrantyServiceResult
    SOH_REDUCED: SohState.WarrantyServiceResult
    SOH_NO_INTERNET: SohState.WarrantyServiceResult
    SOH_UNKNOWN: SohState.WarrantyServiceResult
    class SohTestPhase(_message.Message):
        __slots__ = ("Discharge", "DischargeRest", "Charge", "ChargeRest")
        DISCHARGE_FIELD_NUMBER: _ClassVar[int]
        DISCHARGEREST_FIELD_NUMBER: _ClassVar[int]
        CHARGE_FIELD_NUMBER: _ClassVar[int]
        CHARGEREST_FIELD_NUMBER: _ClassVar[int]
        Discharge: _common_pb2.Void
        DischargeRest: _common_pb2.Void
        Charge: _common_pb2.Void
        ChargeRest: _common_pb2.Void
        def __init__(self, Discharge: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., DischargeRest: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Charge: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., ChargeRest: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class SohTestEndMode(_message.Message):
        __slots__ = ("Complete", "Failed")
        COMPLETE_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        Complete: _common_pb2.Void
        Failed: _common_pb2.Void
        def __init__(self, Complete: _Optional[_Union[_common_pb2.Void, _Mapping]] = ..., Failed: _Optional[_Union[_common_pb2.Void, _Mapping]] = ...) -> None: ...
    class SohTestState(_message.Message):
        __slots__ = ("soh_test_phase", "soh_time_estimate", "soh_time_remaining")
        SOH_TEST_PHASE_FIELD_NUMBER: _ClassVar[int]
        SOH_TIME_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
        SOH_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
        soh_test_phase: SohState.SohTestPhase
        soh_time_estimate: float
        soh_time_remaining: float
        def __init__(self, soh_test_phase: _Optional[_Union[SohState.SohTestPhase, _Mapping]] = ..., soh_time_estimate: _Optional[float] = ..., soh_time_remaining: _Optional[float] = ...) -> None: ...
    class SohResult(_message.Message):
        __slots__ = ("soh", "soh_calibrated", "soh_last_test_time", "soh_health_result", "soh_distance_since_soh_test", "soh_regulated")
        SOH_FIELD_NUMBER: _ClassVar[int]
        SOH_CALIBRATED_FIELD_NUMBER: _ClassVar[int]
        SOH_LAST_TEST_TIME_FIELD_NUMBER: _ClassVar[int]
        SOH_HEALTH_RESULT_FIELD_NUMBER: _ClassVar[int]
        SOH_DISTANCE_SINCE_SOH_TEST_FIELD_NUMBER: _ClassVar[int]
        SOH_REGULATED_FIELD_NUMBER: _ClassVar[int]
        soh: float
        soh_calibrated: bool
        soh_last_test_time: int
        soh_health_result: SohState.WarrantyServiceResult
        soh_distance_since_soh_test: int
        soh_regulated: bool
        def __init__(self, soh: _Optional[float] = ..., soh_calibrated: _Optional[bool] = ..., soh_last_test_time: _Optional[int] = ..., soh_health_result: _Optional[_Union[SohState.WarrantyServiceResult, str]] = ..., soh_distance_since_soh_test: _Optional[int] = ..., soh_regulated: _Optional[bool] = ...) -> None: ...
    SOH_TEST_STATE_FIELD_NUMBER: _ClassVar[int]
    SOH_TEST_END_MODE_FIELD_NUMBER: _ClassVar[int]
    SOH_RESULT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    soh_test_state: SohState.SohTestState
    soh_test_end_mode: SohState.SohTestEndMode
    soh_result: SohState.SohResult
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, soh_test_state: _Optional[_Union[SohState.SohTestState, _Mapping]] = ..., soh_test_end_mode: _Optional[_Union[SohState.SohTestEndMode, _Mapping]] = ..., soh_result: _Optional[_Union[SohState.SohResult, _Mapping]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AlertState(_message.Message):
    __slots__ = ("charging_alerts", "timestamp")
    CHARGING_ALERTS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    charging_alerts: _containers.RepeatedCompositeFieldContainer[_common_pb2.ChargingAlert]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, charging_alerts: _Optional[_Iterable[_Union[_common_pb2.ChargingAlert, _Mapping]]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LightShowOption(_message.Message):
    __slots__ = ("light_show_name", "light_show_duration")
    LIGHT_SHOW_NAME_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_DURATION_FIELD_NUMBER: _ClassVar[int]
    light_show_name: str
    light_show_duration: str
    def __init__(self, light_show_name: _Optional[str] = ..., light_show_duration: _Optional[str] = ...) -> None: ...

class LightShowSettings(_message.Message):
    __slots__ = ("light_show_volume_min", "light_show_volume_max", "light_show_volume_step", "light_show_options", "light_show_schedule_times")
    LIGHT_SHOW_VOLUME_MIN_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_VOLUME_MAX_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_VOLUME_STEP_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_SCHEDULE_TIMES_FIELD_NUMBER: _ClassVar[int]
    light_show_volume_min: float
    light_show_volume_max: float
    light_show_volume_step: float
    light_show_options: _containers.RepeatedCompositeFieldContainer[LightShowOption]
    light_show_schedule_times: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, light_show_volume_min: _Optional[float] = ..., light_show_volume_max: _Optional[float] = ..., light_show_volume_step: _Optional[float] = ..., light_show_options: _Optional[_Iterable[_Union[LightShowOption, _Mapping]]] = ..., light_show_schedule_times: _Optional[_Iterable[int]] = ...) -> None: ...

class LightShowState(_message.Message):
    __slots__ = ("timestamp", "light_show_active", "light_show_selected_name", "light_show_start_time", "light_show_settings")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_SELECTED_NAME_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHOW_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    light_show_active: bool
    light_show_selected_name: str
    light_show_start_time: int
    light_show_settings: LightShowSettings
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., light_show_active: _Optional[bool] = ..., light_show_selected_name: _Optional[str] = ..., light_show_start_time: _Optional[int] = ..., light_show_settings: _Optional[_Union[LightShowSettings, _Mapping]] = ...) -> None: ...

class VehicleImageData(_message.Message):
    __slots__ = ("image_id", "data", "data_chunk_size", "start_offset")
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    image_id: bytes
    data: bytes
    data_chunk_size: int
    start_offset: int
    def __init__(self, image_id: _Optional[bytes] = ..., data: _Optional[bytes] = ..., data_chunk_size: _Optional[int] = ..., start_offset: _Optional[int] = ...) -> None: ...

class VehicleImage(_message.Message):
    __slots__ = ("image_id", "asset_data", "image_type", "is_local_image", "total_image_size")
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_DATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_IMAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_IMAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    image_id: bytes
    asset_data: VehicleImageData
    image_type: VehicleImageStateType
    is_local_image: bool
    total_image_size: int
    def __init__(self, image_id: _Optional[bytes] = ..., asset_data: _Optional[_Union[VehicleImageData, _Mapping]] = ..., image_type: _Optional[_Union[VehicleImageStateType, str]] = ..., is_local_image: _Optional[bool] = ..., total_image_size: _Optional[int] = ...) -> None: ...

class VehicleImageState(_message.Message):
    __slots__ = ("vehicle_images", "timestamp")
    VEHICLE_IMAGES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    vehicle_images: _containers.RepeatedCompositeFieldContainer[VehicleImage]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, vehicle_images: _Optional[_Iterable[_Union[VehicleImage, _Mapping]]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SuspensionState(_message.Message):
    __slots__ = ("allowed_levels", "current_level", "target_level", "movement_state", "offroad_on", "disabled_reason", "level_options", "timestamp")
    ALLOWED_LEVELS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TARGET_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MOVEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    OFFROAD_ON_FIELD_NUMBER: _ClassVar[int]
    DISABLED_REASON_FIELD_NUMBER: _ClassVar[int]
    LEVEL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    allowed_levels: _containers.RepeatedCompositeFieldContainer[_common_pb2.SuspensionLevelObj]
    current_level: _common_pb2.SuspensionLevel
    target_level: _common_pb2.SuspensionLevel
    movement_state: _common_pb2.SuspensionActuationState
    offroad_on: bool
    disabled_reason: str
    level_options: _containers.RepeatedCompositeFieldContainer[_common_pb2.SuspensionLevelObj]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, allowed_levels: _Optional[_Iterable[_Union[_common_pb2.SuspensionLevelObj, _Mapping]]] = ..., current_level: _Optional[_Union[_common_pb2.SuspensionLevel, str]] = ..., target_level: _Optional[_Union[_common_pb2.SuspensionLevel, str]] = ..., movement_state: _Optional[_Union[_common_pb2.SuspensionActuationState, str]] = ..., offroad_on: _Optional[bool] = ..., disabled_reason: _Optional[str] = ..., level_options: _Optional[_Iterable[_Union[_common_pb2.SuspensionLevelObj, _Mapping]]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ChildPresenceDetectionState(_message.Message):
    __slots__ = ("cpd_disable_notification_required", "cpd_hvac_active", "cpd_supports_critical_alerts", "timestamp")
    CPD_DISABLE_NOTIFICATION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CPD_HVAC_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CPD_SUPPORTS_CRITICAL_ALERTS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    cpd_disable_notification_required: bool
    cpd_hvac_active: bool
    cpd_supports_critical_alerts: bool
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, cpd_disable_notification_required: _Optional[bool] = ..., cpd_hvac_active: _Optional[bool] = ..., cpd_supports_critical_alerts: _Optional[bool] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DisplayState(_message.Message):
    __slots__ = ("displayBrightnessAuto", "displayBrightnessScalePreference", "timestamp")
    DISPLAYBRIGHTNESSAUTO_FIELD_NUMBER: _ClassVar[int]
    DISPLAYBRIGHTNESSSCALEPREFERENCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    displayBrightnessAuto: bool
    displayBrightnessScalePreference: int
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, displayBrightnessAuto: _Optional[bool] = ..., displayBrightnessScalePreference: _Optional[int] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class VehicleDetailState(_message.Message):
    __slots__ = ("timestamp", "vehicle_name", "car_version", "detailed_version", "autopilot_hash", "fsd_software_version", "current_profile_name", "china_autopilot_software_version", "is_fsd_v14_or_above")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAR_VERSION_FIELD_NUMBER: _ClassVar[int]
    DETAILED_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTOPILOT_HASH_FIELD_NUMBER: _ClassVar[int]
    FSD_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CHINA_AUTOPILOT_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_FSD_V14_OR_ABOVE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    vehicle_name: str
    car_version: str
    detailed_version: str
    autopilot_hash: str
    fsd_software_version: str
    current_profile_name: str
    china_autopilot_software_version: str
    is_fsd_v14_or_above: bool
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., vehicle_name: _Optional[str] = ..., car_version: _Optional[str] = ..., detailed_version: _Optional[str] = ..., autopilot_hash: _Optional[str] = ..., fsd_software_version: _Optional[str] = ..., current_profile_name: _Optional[str] = ..., china_autopilot_software_version: _Optional[str] = ..., is_fsd_v14_or_above: _Optional[bool] = ...) -> None: ...

class KeepOnAccessoryPortsState(_message.Message):
    __slots__ = ("keep_on_cabin_12v_port_request", "keep_on_cabin_48v_port_request", "timestamp")
    KEEP_ON_CABIN_12V_PORT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    KEEP_ON_CABIN_48V_PORT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    keep_on_cabin_12v_port_request: KeepOnAccessoryPortRequest
    keep_on_cabin_48v_port_request: KeepOnAccessoryPortRequest
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, keep_on_cabin_12v_port_request: _Optional[_Union[KeepOnAccessoryPortRequest, str]] = ..., keep_on_cabin_48v_port_request: _Optional[_Union[KeepOnAccessoryPortRequest, str]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
