from tesla_protocol.command import keys_pb2 as _keys_pb2
from tesla_protocol.command import errors_pb2 as _errors_pb2
from tesla_protocol.command import signatures_pb2 as _signatures_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_TYPE_NONE: _ClassVar[SignatureType]
    SIGNATURE_TYPE_ECDSA: _ClassVar[SignatureType]
    SIGNATURE_TYPE_PRESENT_KEY: _ClassVar[SignatureType]
    SIGNATURE_TYPE_AES_GCM_TOKEN: _ClassVar[SignatureType]
    SIGNATURE_TYPE_UNSIGNED: _ClassVar[SignatureType]

class KeyFormFactor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_FORM_FACTOR_UNKNOWN: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_NFC_CARD: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_3_BUTTON_BLE_CAR_KEYFOB: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_BLE_DEVICE: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_NFC_DEVICE: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_BLE_AND_NFC_DEVICE: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_IOS_DEVICE: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_ANDROID_DEVICE: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_3_BUTTON_BLE_CAR_KEYFOB_P60: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_CLOUD_KEY: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_3_BUTTON_GEN2_CAR_KEYFOB_P60: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_5_BUTTON_GEN2_CAR_KEYFOB_P60: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_3_BUTTON_GEN2_CAR_KEYFOB_P60_V2: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_3_BUTTON_GEN2_CAR_KEYFOB_P60_V3: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_NFC_CARD_P71: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_NFC_CARD_METAL_CARD: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_NFC_CARD_PLASTIC_CARD: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_APPLE_WATCH: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_NFC_CARD_WD_PLASTIC_CARD: _ClassVar[KeyFormFactor]
    KEY_FORM_FACTOR_HARMONY_OS_NEXT_DEVICE: _ClassVar[KeyFormFactor]

class InformationRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFORMATION_REQUEST_TYPE_GET_STATUS: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_TOKEN: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_COUNTER: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_EPHEMERAL_PUBLIC_KEY: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_SESSION_DATA: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_WHITELIST_INFO: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_WHITELIST_ENTRY_INFO: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_PERSONALIZATION_INFO: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_KEYSTATUS_INFO: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_ACTIVE_KEY: _ClassVar[InformationRequestType]
    INFORMATION_REQUEST_TYPE_GET_CAPABILITIES: _ClassVar[InformationRequestType]

class RKEAction_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RKE_ACTION_UNLOCK: _ClassVar[RKEAction_E]
    RKE_ACTION_LOCK: _ClassVar[RKEAction_E]
    RKE_ACTION_OPEN_TRUNK: _ClassVar[RKEAction_E]
    RKE_ACTION_OPEN_FRUNK: _ClassVar[RKEAction_E]
    RKE_ACTION_OPEN_CHARGE_PORT: _ClassVar[RKEAction_E]
    RKE_ACTION_CLOSE_CHARGE_PORT: _ClassVar[RKEAction_E]
    RKE_ACTION_CANCEL_EXTERNAL_AUTHENTICATE: _ClassVar[RKEAction_E]
    RKE_ACTION_UNKNOWN: _ClassVar[RKEAction_E]
    RKE_ACTION_REMOTE_DRIVE: _ClassVar[RKEAction_E]
    RKE_ACTION_AUTO_SECURE_VEHICLE: _ClassVar[RKEAction_E]
    RKE_ACTION_WAKE_VEHICLE: _ClassVar[RKEAction_E]
    RKE_ACTION_UNLOCK_AND_REMOTE_DRIVE: _ClassVar[RKEAction_E]
    RKE_ACTION_UNLOCK_UNRESTRICTED_CLOSURES: _ClassVar[RKEAction_E]
    RKE_ACTION_LEFT_STORAGE_OPEN: _ClassVar[RKEAction_E]
    RKE_ACTION_RIGHT_STORAGE_OPEN: _ClassVar[RKEAction_E]

class ClosureMoveType_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOSURE_MOVE_TYPE_NONE: _ClassVar[ClosureMoveType_E]
    CLOSURE_MOVE_TYPE_MOVE: _ClassVar[ClosureMoveType_E]
    CLOSURE_MOVE_TYPE_STOP: _ClassVar[ClosureMoveType_E]
    CLOSURE_MOVE_TYPE_OPEN: _ClassVar[ClosureMoveType_E]
    CLOSURE_MOVE_TYPE_CLOSE: _ClassVar[ClosureMoveType_E]
    CLOSURE_MOVE_TYPE_OVERRIDE_OPEN: _ClassVar[ClosureMoveType_E]
    CLOSURE_MOVE_TYPE_OVERRIDE_CLOSE: _ClassVar[ClosureMoveType_E]

class OperationStatus_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATIONSTATUS_OK: _ClassVar[OperationStatus_E]
    OPERATIONSTATUS_WAIT: _ClassVar[OperationStatus_E]
    OPERATIONSTATUS_ERROR: _ClassVar[OperationStatus_E]

class SignedMessage_information_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNEDMESSAGE_INFORMATION_NONE: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_UNKNOWN: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_NOT_ON_WHITELIST: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_IV_SMALLER_THAN_EXPECTED: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_INVALID_TOKEN: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_TOKEN_AND_COUNTER_INVALID: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_AES_DECRYPT_AUTH: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_ECDSA_INPUT: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_ECDSA_SIGNATURE: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_LOCAL_ENTITY_START: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_LOCAL_ENTITY_RESULT: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_COULD_NOT_RETRIEVE_KEY: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_COULD_NOT_RETRIEVE_TOKEN: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_SIGNATURE_TOO_SHORT: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_TOKEN_IS_INCORRECT_LENGTH: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_INCORRECT_EPOCH: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_IV_INCORRECT_LENGTH: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_TIME_EXPIRED: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_NOT_PROVISIONED_WITH_IDENTITY: _ClassVar[SignedMessage_information_E]
    SIGNEDMESSAGE_INFORMATION_FAULT_COULD_NOT_HASH_METADATA: _ClassVar[SignedMessage_information_E]

class WhitelistOperation_information_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WHITELISTOPERATION_INFORMATION_NONE: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_UNDOCUMENTED_ERROR: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_NO_PERMISSION_TO_REMOVE_ONESELF: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_KEYFOB_SLOTS_FULL: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_WHITELIST_FULL: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_NO_PERMISSION_TO_ADD: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_INVALID_PUBLIC_KEY: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_NO_PERMISSION_TO_REMOVE: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_NO_PERMISSION_TO_CHANGE_PERMISSIONS: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ELEVATE_OTHER_ABOVE_ONESELF: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_DEMOTE_SUPERIOR_TO_ONESELF: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_REMOVE_OWN_PERMISSIONS: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_PUBLIC_KEY_NOT_ON_WHITELIST: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ADD_KEY_THAT_IS_ALREADY_ON_THE_WHITELIST: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_NOT_ALLOWED_TO_ADD_UNLESS_ON_READER: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_FM_MODIFYING_OUTSIDE_OF_F_MODE: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_FM_ATTEMPTING_TO_ADD_PERMANENT_KEY: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_FM_ATTEMPTING_TO_REMOVE_PERMANENT_KEY: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_KEYCHAIN_WHILE_FS_FULL: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ADD_KEY_WITHOUT_ROLE: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ADD_KEY_WITH_SERVICE_ROLE: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_NON_SERVICE_KEY_ATTEMPTING_TO_ADD_SERVICE_TECH: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_SERVICE_KEY_ATTEMPTING_TO_ADD_SERVICE_TECH_OUTSIDE_SERVICE_MODE: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_COULD_NOT_START_LOCAL_ENTITY_AUTH: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_UI_DENIED: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_TIMED_OUT_WAITING_FOR_TAP: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_TIMED_OUT_WAITING_FOR_UI_ACK: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_VALET_MODE: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_CANCELLED: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_NON_SERVICE_KEY_ATTEMPTING_TO_ADD_RIDER_KEY: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ADD_RIDER_KEY_OUTSIDE_FLEET_MODE: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_NON_SERVICE_KEY_ATTEMPTING_TO_ADD_PREDELIVERY_KEY: _ClassVar[WhitelistOperation_information_E]
    WHITELISTOPERATION_INFORMATION_SERVICE_KEY_ATTEMPTING_TO_ADD_PREDELIVERY_KEY_WHEN_ALREADY_DELIVERED: _ClassVar[WhitelistOperation_information_E]

class AuthenticationLevel_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHENTICATION_LEVEL_NONE: _ClassVar[AuthenticationLevel_E]
    AUTHENTICATION_LEVEL_UNLOCK: _ClassVar[AuthenticationLevel_E]
    AUTHENTICATION_LEVEL_DRIVE: _ClassVar[AuthenticationLevel_E]

class AuthenticationReason_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHENTICATIONREASON_NOT_DOCUMENTED: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_IDENTIFICATION: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_POWER_ON_VEHICLE_REQUEST: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_GTW_REQUEST: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_UI_UNLOCK_PASSIVE_AUTH: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_PASSIVE_UNLOCK_EXTERIOR_HANDLE_PULL: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_PASSIVE_UNLOCK_INTERIOR_HANDLE_PULL: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_PASSIVE_UNLOCK_AUTOPRESENT_DOOR: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_ENTERED_HIGHER_AUTH_ZONE: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_WALK_UP_UNLOCK: _ClassVar[AuthenticationReason_E]
    AUTHENTICATIONREASON_IMMOBILIZER: _ClassVar[AuthenticationReason_E]

class AuthenticationRejection_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHENTICATIONREJECTION_NONE: _ClassVar[AuthenticationRejection_E]
    AUTHENTICATIONREJECTION_DEVICE_STATIONARY: _ClassVar[AuthenticationRejection_E]
    AUTHENTICATIONREJECTION_PASSIVE_DISABLED: _ClassVar[AuthenticationRejection_E]
    AUTHENTICATIONREJECTION_NO_TOKEN: _ClassVar[AuthenticationRejection_E]
    AUTHENTICATIONREJECTION_PASSIVE_DISABLED_AUTOMATION: _ClassVar[AuthenticationRejection_E]
    AUTHENTICATIONREJECTION_DEVICE_NOT_UNLOCKED_ON_WRIST: _ClassVar[AuthenticationRejection_E]

class ClosureState_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOSURESTATE_CLOSED: _ClassVar[ClosureState_E]
    CLOSURESTATE_OPEN: _ClassVar[ClosureState_E]
    CLOSURESTATE_AJAR: _ClassVar[ClosureState_E]
    CLOSURESTATE_UNKNOWN: _ClassVar[ClosureState_E]
    CLOSURESTATE_FAILED_UNLATCH: _ClassVar[ClosureState_E]
    CLOSURESTATE_OPENING: _ClassVar[ClosureState_E]
    CLOSURESTATE_CLOSING: _ClassVar[ClosureState_E]

class VehicleLockState_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VEHICLELOCKSTATE_UNLOCKED: _ClassVar[VehicleLockState_E]
    VEHICLELOCKSTATE_LOCKED: _ClassVar[VehicleLockState_E]
    VEHICLELOCKSTATE_INTERNAL_LOCKED: _ClassVar[VehicleLockState_E]
    VEHICLELOCKSTATE_SELECTIVE_UNLOCKED: _ClassVar[VehicleLockState_E]

class VehicleSleepStatus_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VEHICLE_SLEEP_STATUS_UNKNOWN: _ClassVar[VehicleSleepStatus_E]
    VEHICLE_SLEEP_STATUS_AWAKE: _ClassVar[VehicleSleepStatus_E]
    VEHICLE_SLEEP_STATUS_ASLEEP: _ClassVar[VehicleSleepStatus_E]

class UserPresence_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VEHICLE_USER_PRESENCE_UNKNOWN: _ClassVar[UserPresence_E]
    VEHICLE_USER_PRESENCE_NOT_PRESENT: _ClassVar[UserPresence_E]
    VEHICLE_USER_PRESENCE_PRESENT: _ClassVar[UserPresence_E]

class UIDesire_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UI_DESIRE_NONE: _ClassVar[UIDesire_E]
    UI_DESIRE_HAS_DATA: _ClassVar[UIDesire_E]

class Gear_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GEAR_UNKNOWN: _ClassVar[Gear_E]
    GEAR_PARK: _ClassVar[Gear_E]
    GEAR_DRIVE: _ClassVar[Gear_E]
    GEAR_REVERSE: _ClassVar[Gear_E]
    GEAR_NEUTRAL: _ClassVar[Gear_E]

class WhitelistKeyPermission_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WHITELISTKEYPERMISSION_ADD_TO_WHITELIST: _ClassVar[WhitelistKeyPermission_E]
    WHITELISTKEYPERMISSION_LOCAL_UNLOCK: _ClassVar[WhitelistKeyPermission_E]
    WHITELISTKEYPERMISSION_LOCAL_DRIVE: _ClassVar[WhitelistKeyPermission_E]
    WHITELISTKEYPERMISSION_REMOTE_UNLOCK: _ClassVar[WhitelistKeyPermission_E]
    WHITELISTKEYPERMISSION_REMOTE_DRIVE: _ClassVar[WhitelistKeyPermission_E]
    WHITELISTKEYPERMISSION_CHANGE_PERMISSIONS: _ClassVar[WhitelistKeyPermission_E]
    WHITELISTKEYPERMISSION_REMOVE_FROM_WHITELIST: _ClassVar[WhitelistKeyPermission_E]
    WHITELISTKEYPERMISSION_REMOVE_SELF_FROM_WHITELIST: _ClassVar[WhitelistKeyPermission_E]
    WHITELISTKEYPERMISSION_MODIFY_FLEET_RESERVED_SLOTS: _ClassVar[WhitelistKeyPermission_E]
    WHITELISTKEYPERMISSION_UNKNOWN: _ClassVar[WhitelistKeyPermission_E]

class KeyLocationStatus_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_LOCATION_UNKNOWN: _ClassVar[KeyLocationStatus_E]
    KEY_LOCATION_NOT_PRESENT: _ClassVar[KeyLocationStatus_E]
    KEY_LOCATION_PRESENT: _ClassVar[KeyLocationStatus_E]

class NFCPresence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NFC_PRESENCE_NOT_PRESENT: _ClassVar[NFCPresence]
    NFC_PRESENCE_PRESENT_AT_B_PILLAR: _ClassVar[NFCPresence]
    NFC_PRESENCE_PRESENT_AT_CENTER_CONSOLE: _ClassVar[NFCPresence]

class BLEPresence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BLE_PRESENCE_NOT_PRESENT: _ClassVar[BLEPresence]
    BLE_PRESENCE_PRESENT: _ClassVar[BLEPresence]
    BLE_PRESENCE_CONNECTED_NOT_PRESENT: _ClassVar[BLEPresence]

class RequestSource_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REQUEST_SOURCE_NOT_POPULATED: _ClassVar[RequestSource_E]
    REQUEST_SOURCE_BLE: _ClassVar[RequestSource_E]
    REQUEST_SOURCE_OTHER: _ClassVar[RequestSource_E]

class QRCodeStatus_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QR_CODE_STATUS_UNKNOWN: _ClassVar[QRCodeStatus_E]
    QR_CODE_STATUS_DISPLAYED: _ClassVar[QRCodeStatus_E]
    QR_CODE_STATUS_NOT_DISPLAYED: _ClassVar[QRCodeStatus_E]

class Activity_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTIVITY_NONE: _ClassVar[Activity_E]
    ACTIVITY_STATIONARY: _ClassVar[Activity_E]
    ACTIVITY_MOTION: _ClassVar[Activity_E]
    ACTIVITY_SIGNIFICANT_MOTION: _ClassVar[Activity_E]

class AlertConfirmation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_CONFIRMATION_NONE: _ClassVar[AlertConfirmation]
    ALERT_CONFIRMATION_PEER_REMOVED_INFORMATION: _ClassVar[AlertConfirmation]

class AppDeviceInfoRequest_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APP_DEVICE_INFO_REQUEST_NONE: _ClassVar[AppDeviceInfoRequest_E]
    APP_DEVICE_INFO_REQUEST_GET_MODEL_NUMBER: _ClassVar[AppDeviceInfoRequest_E]
    APP_DEVICE_INFO_REQUEST_ONCHANGE_BATTERY_STATE: _ClassVar[AppDeviceInfoRequest_E]

class AppOperatingSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[AppOperatingSystem]
    ANDROID: _ClassVar[AppOperatingSystem]
    IOS: _ClassVar[AppOperatingSystem]
    WATCHOS: _ClassVar[AppOperatingSystem]
    HARMONY_NEXT: _ClassVar[AppOperatingSystem]

class BLEAdditionalTRIMApplied_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BLE_ADDITIONAL_TRIM_APPLIED_NONE: _ClassVar[BLEAdditionalTRIMApplied_E]
    BLE_ADDITIONAL_TRIM_APPLIED_APPLIED: _ClassVar[BLEAdditionalTRIMApplied_E]
    BLE_ADDITIONAL_TRIM_APPLIED_NOT_APPLIED: _ClassVar[BLEAdditionalTRIMApplied_E]

class BLEEndpoint_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BLE_ENDPOINT_NONE: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_CENTER: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_FRONT: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_LEFT: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_RIGHT: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_REAR: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_REAR_LEFT: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_REAR_RIGHT: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_NFC_CRADLE: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_FRONT_LEFT: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_FRONT_RIGHT: _ClassVar[BLEEndpoint_E]
    BLE_ENDPOINT_SECONDARY_CENTER: _ClassVar[BLEEndpoint_E]

class BatteryState_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATTERY_STATE_UNKNOWN: _ClassVar[BatteryState_E]
    BATTERY_STATE_UNPLUGGED: _ClassVar[BatteryState_E]
    BATTERY_STATE_CHARGING: _ClassVar[BatteryState_E]
    BATTERY_STATE_FULL: _ClassVar[BatteryState_E]

class CBManagerAuthorization(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CBMANAGERAUTHORIZATION_UNKNOWN: _ClassVar[CBManagerAuthorization]
    CBMANAGERAUTHORIZATION_ALWAYS: _ClassVar[CBManagerAuthorization]
    CBMANAGERAUTHORIZATION_DENIED: _ClassVar[CBManagerAuthorization]
    CBMANAGERAUTHORIZATION_NOTDETERMINED: _ClassVar[CBManagerAuthorization]
    CBMANAGERAUTHORIZATION_RESTRICTED: _ClassVar[CBManagerAuthorization]

class CBManagerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CBMANAGERSTATE_UNKNOWN: _ClassVar[CBManagerState]
    CBMANAGERSTATE_POWEREDOFF: _ClassVar[CBManagerState]
    CBMANAGERSTATE_POWEREDON: _ClassVar[CBManagerState]
    CBMANAGERSTATE_RESETTING: _ClassVar[CBManagerState]
    CBMANAGERSTATE_UNAUTHORIZED: _ClassVar[CBManagerState]
    CBMANAGERSTATE_UNSUPPORTED: _ClassVar[CBManagerState]

class CPDNotificationResponse_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CPD_NOTIFICATION_RESPONSE_SNA: _ClassVar[CPDNotificationResponse_E]
    CPD_NOTIFICATION_RESPONSE_INITIAL_WARNING_RECEIVED: _ClassVar[CPDNotificationResponse_E]
    CPD_NOTIFICATION_RESPONSE_ESCALATED_WARNING_RECEIVED: _ClassVar[CPDNotificationResponse_E]
    CPD_NOTIFICATION_RESPONSE_ERROR: _ClassVar[CPDNotificationResponse_E]

class CPDNotification_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CPD_NOTIFICATION_NONE: _ClassVar[CPDNotification_E]
    CPD_NOTIFICATION_INITIAL_WARNING: _ClassVar[CPDNotification_E]
    CPD_NOTIFICATION_ESCALATED_WARNING: _ClassVar[CPDNotification_E]

class DeviceTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_TARGET: _ClassVar[DeviceTarget]
    DEVELOPMENT_TARGET: _ClassVar[DeviceTarget]
    PRODUCTION_TARGET: _ClassVar[DeviceTarget]

class Device_Motion_Confidence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_MOTION_CONFIDENCE_UNKNOWN: _ClassVar[Device_Motion_Confidence]
    DEVICE_MOTION_CONFIDENCE_LOW: _ClassVar[Device_Motion_Confidence]
    DEVICE_MOTION_CONFIDENCE_MEDIUM: _ClassVar[Device_Motion_Confidence]
    DEVICE_MOTION_CONFIDENCE_HIGH: _ClassVar[Device_Motion_Confidence]

class Device_Motion_State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_MOTION_UNKNOWN: _ClassVar[Device_Motion_State]
    DEVICE_MOTION_STATIONARY: _ClassVar[Device_Motion_State]
    DEVICE_MOTION_WALKING: _ClassVar[Device_Motion_State]
    DEVICE_MOTION_RUNNING: _ClassVar[Device_Motion_State]
    DEVICE_MOTION_AUTOMOTIVE: _ClassVar[Device_Motion_State]
    DEVICE_MOTION_CYCLING: _ClassVar[Device_Motion_State]

class FiraError_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRAERROR_UNKNOWN: _ClassVar[FiraError_E]
    FIRAERROR_UWB_HARDWARE_NOT_AVAILABLE: _ClassVar[FiraError_E]
    FIRAERROR_ILLEGAL_ARGUMENT: _ClassVar[FiraError_E]
    FIRAERROR_ILLEGAL_STATE: _ClassVar[FiraError_E]
    FIRAERROR_SERVICE_VERSION_UPDATE_REQUIRED: _ClassVar[FiraError_E]
    FIRAERROR_SERVICE_DISABLED: _ClassVar[FiraError_E]
    FIRAERROR_SIGN_IN_REQUIRED: _ClassVar[FiraError_E]
    FIRAERROR_INVALID_ACCOUNT: _ClassVar[FiraError_E]
    FIRAERROR_RESOLUTION_REQUIRED: _ClassVar[FiraError_E]
    FIRAERROR_NETWORK_ERROR: _ClassVar[FiraError_E]
    FIRAERROR_INTERNAL_ERROR: _ClassVar[FiraError_E]
    FIRAERROR_DEVELOPER_ERROR: _ClassVar[FiraError_E]
    FIRAERROR_ERROR: _ClassVar[FiraError_E]
    FIRAERROR_INTERRUPTED: _ClassVar[FiraError_E]
    FIRAERROR_TIMEOUT: _ClassVar[FiraError_E]
    FIRAERROR_CANCELED: _ClassVar[FiraError_E]
    FIRAERROR_API_NOT_CONNECTED: _ClassVar[FiraError_E]
    FIRAERROR_STATUS_ERROR: _ClassVar[FiraError_E]
    FIRAERROR_SERVICE_NOT_AVAILABLE: _ClassVar[FiraError_E]
    FIRAERROR_NULL_RANGING_DEVICE: _ClassVar[FiraError_E]
    FIRAERROR_INVALID_API_CALL: _ClassVar[FiraError_E]
    FIRAERROR_RANGING_ALREADY_STARTED: _ClassVar[FiraError_E]
    FIRAERROR_UWB_SYSTEM_CALLBACK_FAILURE: _ClassVar[FiraError_E]
    FIRAERROR_RANGING_UNKNOWN: _ClassVar[FiraError_E]
    FIRAERROR_RANGING_INTERRUPTED: _ClassVar[FiraError_E]
    FIRAERROR_RANGING_INTERNAL_ERROR: _ClassVar[FiraError_E]
    FIRAERROR_RANGING_TIMEOUT: _ClassVar[FiraError_E]
    FIRAERROR_RANGING_CANCELED: _ClassVar[FiraError_E]
    FIRAERROR_RANGING_DEAD_CLIENT: _ClassVar[FiraError_E]
    FIRAERROR_COROUTINE_TASK_EXECUTION_EXCEPTION: _ClassVar[FiraError_E]
    FIRAERROR_COROUTINE_TASK_INTERRUPTED_EXCEPTION: _ClassVar[FiraError_E]
    FIRAERROR_NOT_SELECTED: _ClassVar[FiraError_E]

class FiraRangingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RANGING_TYPE_UNKNOWN: _ClassVar[FiraRangingType]
    MULTICAST_DS_TWR: _ClassVar[FiraRangingType]
    UNICAST_DS_TWR: _ClassVar[FiraRangingType]

class FiraSTSMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STS_UNKNOWN: _ClassVar[FiraSTSMode]
    STATIC: _ClassVar[FiraSTSMode]
    PROVISIONED: _ClassVar[FiraSTSMode]
    PROVISIONED_INDIVIDUAL: _ClassVar[FiraSTSMode]
    DYNAMIC: _ClassVar[FiraSTSMode]
    DYNAMIC_INDIVIDUAL: _ClassVar[FiraSTSMode]

class GATTServicesBitMask(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GATTSERVICESBITMASK_PHONE_KEY_SERVICE: _ClassVar[GATTServicesBitMask]
    GATTSERVICESBITMASK_FROM_VEHICLE_CHAR: _ClassVar[GATTServicesBitMask]
    GATTSERVICESBITMASK_TO_VEHICLE_CHAR: _ClassVar[GATTServicesBitMask]
    GATTSERVICESBITMASK_VERSION_CHAR: _ClassVar[GATTServicesBitMask]
    GATTSERVICESBITMASK_BONDING_SERVICE: _ClassVar[GATTServicesBitMask]
    GATTSERVICESBITMASK_BONDING_CHAR: _ClassVar[GATTServicesBitMask]

class GenealogyRequest_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENEALOGYREQUEST_NONE: _ClassVar[GenealogyRequest_E]
    GENEALOGYREQUEST_READ: _ClassVar[GenealogyRequest_E]
    GENEALOGYREQUEST_KEYFOBINFO_READ: _ClassVar[GenealogyRequest_E]
    GENEALOGYREQUEST_TPWHEELUNITINFO_READ: _ClassVar[GenealogyRequest_E]

class GenealogyStatus_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENEALOGY_STATUS_NONE: _ClassVar[GenealogyStatus_E]
    GENEALOGY_STATUS_NOT_WRITTEN: _ClassVar[GenealogyStatus_E]
    GENEALOGY_STATUS_WRITE_SUCCESS: _ClassVar[GenealogyStatus_E]
    GENEALOGY_STATUS_WRITE_FAILURE: _ClassVar[GenealogyStatus_E]
    GENEALOGY_STATUS_READ_SUCCESS: _ClassVar[GenealogyStatus_E]
    GENEALOGY_STATUS_READ_FAILURE: _ClassVar[GenealogyStatus_E]
    GENEALOGY_STATUS_CRC_FAILURE: _ClassVar[GenealogyStatus_E]

class GetReaderKeyCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GET_READER_KEY_COMMAND_UNKNOWN: _ClassVar[GetReaderKeyCommand]
    GET_READER_KEY_COMMAND_START_LOOKING: _ClassVar[GetReaderKeyCommand]
    GET_READER_KEY_COMMAND_STOP_LOOKING: _ClassVar[GetReaderKeyCommand]

class HandlePulled_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HANDLE_PULLED_FRONT_DRIVER_DOOR: _ClassVar[HandlePulled_E]
    HANDLE_PULLED_FRONT_PASSENGER_DOOR: _ClassVar[HandlePulled_E]
    HANDLE_PULLED_REAR_DRIVER_DOOR: _ClassVar[HandlePulled_E]
    HANDLE_PULLED_REAR_PASSENGER_DOOR: _ClassVar[HandlePulled_E]
    HANDLE_PULLED_TRUNK: _ClassVar[HandlePulled_E]
    HANDLE_PULLED_CHARGE_PORT: _ClassVar[HandlePulled_E]
    HANDLE_PULLED_FRONT_DRIVER_AUTO_PRESENT_DOOR: _ClassVar[HandlePulled_E]
    HANDLE_PULLED_FRONT_PASSENGER_AUTO_PRESENT_DOOR: _ClassVar[HandlePulled_E]
    HANDLE_PULLED_OTHER: _ClassVar[HandlePulled_E]
    HANDLE_PULLED_FRUNK: _ClassVar[HandlePulled_E]

class IMURequest_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMU_REQUEST_NONE: _ClassVar[IMURequest_E]
    IMU_REQUEST_GET_SLEEP_STATE: _ClassVar[IMURequest_E]
    IMU_REQUEST_ENABLE_CONTINUOUS_ACTIVITY_UPDATE: _ClassVar[IMURequest_E]
    IMU_REQUEST_DISABLE_CONTINUOUS_ACTIVITY_UPDATE: _ClassVar[IMURequest_E]

class LocationPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCATION_PERMISSION_UNKNOWN: _ClassVar[LocationPermission]
    LOCATION_PERMISSION_ASK_NEXT_TIME_OR_WHEN_I_SHARE: _ClassVar[LocationPermission]
    LOCATION_PERMISSION_WHILE_USING_THE_APP: _ClassVar[LocationPermission]
    LOCATION_PERMISSION_ALWAYS: _ClassVar[LocationPermission]
    LOCATION_PERMISSION_NEVER: _ClassVar[LocationPermission]

class NIError_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_UNKNOWN: _ClassVar[NIError_E]
    ERROR_SESSION_LIMIT_EXCEEDED: _ClassVar[NIError_E]
    ERROR_INVALID_CONFIGURATION: _ClassVar[NIError_E]
    ERROR_RESOURCE_USAGE_TIMEOUT: _ClassVar[NIError_E]
    ERROR_SESSION_FAILED: _ClassVar[NIError_E]
    ERROR_UNSUPPORTED_PLATFORM: _ClassVar[NIError_E]
    ERROR_USER_DID_NOT_ALLOW: _ClassVar[NIError_E]
    ERROR_BLE_PEER_UNAVAILABLE: _ClassVar[NIError_E]
    ERROR_VEHICLE_NOT_SELECTED_FOR_RANGING: _ClassVar[NIError_E]

class NISessionStatus_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NI_SESSION_STATUS_UNKNOWN: _ClassVar[NISessionStatus_E]
    NI_SESSION_STATUS_ACTIVE: _ClassVar[NISessionStatus_E]
    NI_SESSION_STATUS_INACTIVE: _ClassVar[NISessionStatus_E]
    NI_SESSION_STATUS_ERROR: _ClassVar[NISessionStatus_E]
    NI_SESSION_STATUS_UNAVAILABLE: _ClassVar[NISessionStatus_E]

class OperationMode_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_MODE_UNKNOWN: _ClassVar[OperationMode_E]
    OPERATION_MODE_OWNER: _ClassVar[OperationMode_E]
    OPERATION_MODE_FLEET: _ClassVar[OperationMode_E]

class PeripheralState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERIPHERALSTATE_SNA: _ClassVar[PeripheralState]
    PERIPHERALSTATE_DISCONNECTED: _ClassVar[PeripheralState]
    PERIPHERALSTATE_CONNECTED: _ClassVar[PeripheralState]
    PERIPHERALSTATE_CONNECTING: _ClassVar[PeripheralState]
    PERIPHERALSTATE_DISCONNECTING: _ClassVar[PeripheralState]

class PhoneThermalState_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PHONE_THERMAL_STATE_UNKNOWN: _ClassVar[PhoneThermalState_E]
    PHONE_THERMAL_STATE_NOMINAL: _ClassVar[PhoneThermalState_E]
    PHONE_THERMAL_STATE_FAIR: _ClassVar[PhoneThermalState_E]
    PHONE_THERMAL_STATE_LIGHT: _ClassVar[PhoneThermalState_E]
    PHONE_THERMAL_STATE_MODERATE: _ClassVar[PhoneThermalState_E]
    PHONE_THERMAL_STATE_SERIOUS: _ClassVar[PhoneThermalState_E]
    PHONE_THERMAL_STATE_SEVERE: _ClassVar[PhoneThermalState_E]
    PHONE_THERMAL_STATE_CRITICAL: _ClassVar[PhoneThermalState_E]
    PHONE_THERMAL_STATE_EMERGENCY: _ClassVar[PhoneThermalState_E]
    PHONE_THERMAL_STATE_SHUTDOWN: _ClassVar[PhoneThermalState_E]

class RangingConfigType_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RANGINGCONFIGTYPE_UNDEFINED: _ClassVar[RangingConfigType_E]
    RANGINGCONFIGTYPE_APPLE_UNICAST_BACKGROUND: _ClassVar[RangingConfigType_E]
    RANGINGCONFIGTYPE_APPLE_UNICAST_FOREGROUND: _ClassVar[RangingConfigType_E]
    RANGINGCONFIGTYPE_APPLE_MULTICAST_BACKGROUND: _ClassVar[RangingConfigType_E]
    RANGINGCONFIGTYPE_APPLE_MULTICAST_FOREGROUND: _ClassVar[RangingConfigType_E]

class RangingUpdateRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RANGING_UPDATE_RATE_UNKNOWN: _ClassVar[RangingUpdateRate]
    RANGING_UPDATE_RATE_AUTOMATIC: _ClassVar[RangingUpdateRate]
    RANGING_UPDATE_RATE_INFREQUENT: _ClassVar[RangingUpdateRate]
    RANGING_UPDATE_RATE_FREQUENT: _ClassVar[RangingUpdateRate]

class SleepManagerCommand_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SLEEPMANAGER_COMMAND_NONE: _ClassVar[SleepManagerCommand_E]
    SLEEPMANAGER_GET_STATS: _ClassVar[SleepManagerCommand_E]
    SLEEPMANAGER_RESET_STATS: _ClassVar[SleepManagerCommand_E]

class UIRequest_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UI_REQUEST_NONE: _ClassVar[UIRequest_E]
    UI_REQUEST_GET_VEHICLE_BLE_NICK_NAME: _ClassVar[UIRequest_E]

class UWBAvailability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UWB_AVAILABILITY_UNKNOWN: _ClassVar[UWBAvailability]
    UWB_AVAILABILITY_AVAILABLE: _ClassVar[UWBAvailability]
    UWB_AVAILABILITY_UNAVAILABLE_UNSUPPORTED_DEVICE: _ClassVar[UWBAvailability]
    UWB_AVAILABILITY_UNAVAILABLE_PERMISSION_DENIED: _ClassVar[UWBAvailability]
    UWB_AVAILABILITY_UNAVAILABLE: _ClassVar[UWBAvailability]
    UWB_AVAILABILITY_UNAVAILABLE_DISABLED_BY_USER: _ClassVar[UWBAvailability]

class UpdaterLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATER_LOCATION_NONE: _ClassVar[UpdaterLocation]
    UPDATER_LOCATION_APPLICATION: _ClassVar[UpdaterLocation]
    UPDATER_LOCATION_BOOTLOADER: _ClassVar[UpdaterLocation]
    UPDATER_LOCATION_SECONDARY_APPLICATION: _ClassVar[UpdaterLocation]
    UPDATER_LOCATION_APPLICATION_IN_EXTERNAL_FLASH: _ClassVar[UpdaterLocation]

class UpdaterStatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATER_STATUS_CODE_ERROR: _ClassVar[UpdaterStatusCode]
    UPDATER_STATUS_CODE_WAIT: _ClassVar[UpdaterStatusCode]
    UPDATER_STATUS_CODE_BLOCK_STAGED: _ClassVar[UpdaterStatusCode]
    UPDATER_STATUS_CODE_IMAGE_STAGED: _ClassVar[UpdaterStatusCode]
    UPDATER_STATUS_CODE_CRC_CHECK_SUCCESS: _ClassVar[UpdaterStatusCode]
    UPDATER_STATUS_CODE_CRC_CHECK_FAIL: _ClassVar[UpdaterStatusCode]
    UPDATER_STATUS_CODE_HASH_FAIL: _ClassVar[UpdaterStatusCode]
    UPDATER_STATUS_CODE_SIGNATURE_FAIL: _ClassVar[UpdaterStatusCode]
    UPDATER_STATUS_CODE_ERROR_HASH_RESTORE_FAIL: _ClassVar[UpdaterStatusCode]
    UPDATER_STATUS_CODE_LOCATION_SET: _ClassVar[UpdaterStatusCode]

class iBeaconState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IBEACON_STATE_SNA: _ClassVar[iBeaconState]
    IBEACON_STATE_INSIDE: _ClassVar[iBeaconState]
    IBEACON_STATE_OUTSIDE: _ClassVar[iBeaconState]

class iOS_AppState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IOS_APPSTATE_SNA: _ClassVar[iOS_AppState]
    IOS_APPSTATE_INACTIVE: _ClassVar[iOS_AppState]
    IOS_APPSTATE_ACTIVE: _ClassVar[iOS_AppState]
    IOS_APPSTATE_BACKGROUND: _ClassVar[iOS_AppState]

class iOS_CoreBTATTErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IOS_COREBTATTERRORCODE_SNA: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_SUCCESS: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_READ_NOT_PERMITTED: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_WRITE_NOT_PERMITTED: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_INVALID_PDU: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_INSUFFICIENT_AUTHENTICATION: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_REQUEST_NOT_SUPPORTED: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_INVALID_OFFSET: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_INSUFFICIENT_AUTHORIZATION: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_PREPARE_QUEUE_FULL: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_ATT_NOT_FOUND: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_ATT_NOT_LONG: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_INSUFFICIENT_ENCRYPTION_KEY_SIZE: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_INVALID_ATT_VALUE_LENGTH: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_UNLIKELY_ERROR: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_INSUFFICIENT_ENCRYPTION: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_UNSUPPORTED_GROUP_TYPE: _ClassVar[iOS_CoreBTATTErrorCode]
    IOS_COREBTATTERRORCODE_INSUFFICIENT_RESOURCES: _ClassVar[iOS_CoreBTATTErrorCode]

class iOS_CoreBTError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IOS_COREBTERROR_SNA: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_UNKNOWN: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_INVALID_PARAMETERS: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_INVALID_HANDLE: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_NOT_CONNECTED: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_OUT_OF_SPACE: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_OPERATION_CANCELLED: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_CONNECTION_TIMEOUT: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_PERIPHERAL_DISCONNECTED: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_UUID_NOT_ALLOWED: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_ALREADY_ADVERTISING: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_CONNECTION_FAILED: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_CONNECTION_LIMIT_REACHED: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_OPERATION_NOT_SUPPORTED: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_UNKNOWN_DEVICE: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_ENCRYPTIONTIMEDOUT: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_LEGATTEXCEEDEDBACKGROUNDNOTIFICATIONLIMIT: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_LEGATTNEARBACKGROUNDNOTIFICATIONLIMIT: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_PEERREMOVEDPAIRINGINFORMATION: _ClassVar[iOS_CoreBTError]
    IOS_COREBTERROR_TOOMANYLEPAIREDDEVICES: _ClassVar[iOS_CoreBTError]

class iOS_LaunchReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IOS_LAUNCHREASON_SNA: _ClassVar[iOS_LaunchReason]
    IOS_LAUNCHREASON_FOREGROUND: _ClassVar[iOS_LaunchReason]
    IOS_LAUNCHREASON_BLUETOOTH: _ClassVar[iOS_LaunchReason]
    IOS_LAUNCHREASON_BEACON: _ClassVar[iOS_LaunchReason]
    IOS_LAUNCHREASON_NOTIFICATION: _ClassVar[iOS_LaunchReason]
    IOS_LAUNCHREASON_URL: _ClassVar[iOS_LaunchReason]
    IOS_LAUNCHREASON_SHORTCUT: _ClassVar[iOS_LaunchReason]
SIGNATURE_TYPE_NONE: SignatureType
SIGNATURE_TYPE_ECDSA: SignatureType
SIGNATURE_TYPE_PRESENT_KEY: SignatureType
SIGNATURE_TYPE_AES_GCM_TOKEN: SignatureType
SIGNATURE_TYPE_UNSIGNED: SignatureType
KEY_FORM_FACTOR_UNKNOWN: KeyFormFactor
KEY_FORM_FACTOR_NFC_CARD: KeyFormFactor
KEY_FORM_FACTOR_3_BUTTON_BLE_CAR_KEYFOB: KeyFormFactor
KEY_FORM_FACTOR_BLE_DEVICE: KeyFormFactor
KEY_FORM_FACTOR_NFC_DEVICE: KeyFormFactor
KEY_FORM_FACTOR_BLE_AND_NFC_DEVICE: KeyFormFactor
KEY_FORM_FACTOR_IOS_DEVICE: KeyFormFactor
KEY_FORM_FACTOR_ANDROID_DEVICE: KeyFormFactor
KEY_FORM_FACTOR_3_BUTTON_BLE_CAR_KEYFOB_P60: KeyFormFactor
KEY_FORM_FACTOR_CLOUD_KEY: KeyFormFactor
KEY_FORM_FACTOR_3_BUTTON_GEN2_CAR_KEYFOB_P60: KeyFormFactor
KEY_FORM_FACTOR_5_BUTTON_GEN2_CAR_KEYFOB_P60: KeyFormFactor
KEY_FORM_FACTOR_3_BUTTON_GEN2_CAR_KEYFOB_P60_V2: KeyFormFactor
KEY_FORM_FACTOR_3_BUTTON_GEN2_CAR_KEYFOB_P60_V3: KeyFormFactor
KEY_FORM_FACTOR_NFC_CARD_P71: KeyFormFactor
KEY_FORM_FACTOR_NFC_CARD_METAL_CARD: KeyFormFactor
KEY_FORM_FACTOR_NFC_CARD_PLASTIC_CARD: KeyFormFactor
KEY_FORM_FACTOR_APPLE_WATCH: KeyFormFactor
KEY_FORM_FACTOR_NFC_CARD_WD_PLASTIC_CARD: KeyFormFactor
KEY_FORM_FACTOR_HARMONY_OS_NEXT_DEVICE: KeyFormFactor
INFORMATION_REQUEST_TYPE_GET_STATUS: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_TOKEN: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_COUNTER: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_EPHEMERAL_PUBLIC_KEY: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_SESSION_DATA: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_WHITELIST_INFO: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_WHITELIST_ENTRY_INFO: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_PERSONALIZATION_INFO: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_KEYSTATUS_INFO: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_ACTIVE_KEY: InformationRequestType
INFORMATION_REQUEST_TYPE_GET_CAPABILITIES: InformationRequestType
RKE_ACTION_UNLOCK: RKEAction_E
RKE_ACTION_LOCK: RKEAction_E
RKE_ACTION_OPEN_TRUNK: RKEAction_E
RKE_ACTION_OPEN_FRUNK: RKEAction_E
RKE_ACTION_OPEN_CHARGE_PORT: RKEAction_E
RKE_ACTION_CLOSE_CHARGE_PORT: RKEAction_E
RKE_ACTION_CANCEL_EXTERNAL_AUTHENTICATE: RKEAction_E
RKE_ACTION_UNKNOWN: RKEAction_E
RKE_ACTION_REMOTE_DRIVE: RKEAction_E
RKE_ACTION_AUTO_SECURE_VEHICLE: RKEAction_E
RKE_ACTION_WAKE_VEHICLE: RKEAction_E
RKE_ACTION_UNLOCK_AND_REMOTE_DRIVE: RKEAction_E
RKE_ACTION_UNLOCK_UNRESTRICTED_CLOSURES: RKEAction_E
RKE_ACTION_LEFT_STORAGE_OPEN: RKEAction_E
RKE_ACTION_RIGHT_STORAGE_OPEN: RKEAction_E
CLOSURE_MOVE_TYPE_NONE: ClosureMoveType_E
CLOSURE_MOVE_TYPE_MOVE: ClosureMoveType_E
CLOSURE_MOVE_TYPE_STOP: ClosureMoveType_E
CLOSURE_MOVE_TYPE_OPEN: ClosureMoveType_E
CLOSURE_MOVE_TYPE_CLOSE: ClosureMoveType_E
CLOSURE_MOVE_TYPE_OVERRIDE_OPEN: ClosureMoveType_E
CLOSURE_MOVE_TYPE_OVERRIDE_CLOSE: ClosureMoveType_E
OPERATIONSTATUS_OK: OperationStatus_E
OPERATIONSTATUS_WAIT: OperationStatus_E
OPERATIONSTATUS_ERROR: OperationStatus_E
SIGNEDMESSAGE_INFORMATION_NONE: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_UNKNOWN: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_NOT_ON_WHITELIST: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_IV_SMALLER_THAN_EXPECTED: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_INVALID_TOKEN: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_TOKEN_AND_COUNTER_INVALID: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_AES_DECRYPT_AUTH: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_ECDSA_INPUT: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_ECDSA_SIGNATURE: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_LOCAL_ENTITY_START: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_LOCAL_ENTITY_RESULT: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_COULD_NOT_RETRIEVE_KEY: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_COULD_NOT_RETRIEVE_TOKEN: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_SIGNATURE_TOO_SHORT: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_TOKEN_IS_INCORRECT_LENGTH: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_INCORRECT_EPOCH: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_IV_INCORRECT_LENGTH: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_TIME_EXPIRED: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_NOT_PROVISIONED_WITH_IDENTITY: SignedMessage_information_E
SIGNEDMESSAGE_INFORMATION_FAULT_COULD_NOT_HASH_METADATA: SignedMessage_information_E
WHITELISTOPERATION_INFORMATION_NONE: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_UNDOCUMENTED_ERROR: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_NO_PERMISSION_TO_REMOVE_ONESELF: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_KEYFOB_SLOTS_FULL: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_WHITELIST_FULL: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_NO_PERMISSION_TO_ADD: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_INVALID_PUBLIC_KEY: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_NO_PERMISSION_TO_REMOVE: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_NO_PERMISSION_TO_CHANGE_PERMISSIONS: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ELEVATE_OTHER_ABOVE_ONESELF: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_DEMOTE_SUPERIOR_TO_ONESELF: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_REMOVE_OWN_PERMISSIONS: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_PUBLIC_KEY_NOT_ON_WHITELIST: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ADD_KEY_THAT_IS_ALREADY_ON_THE_WHITELIST: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_NOT_ALLOWED_TO_ADD_UNLESS_ON_READER: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_FM_MODIFYING_OUTSIDE_OF_F_MODE: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_FM_ATTEMPTING_TO_ADD_PERMANENT_KEY: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_FM_ATTEMPTING_TO_REMOVE_PERMANENT_KEY: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_KEYCHAIN_WHILE_FS_FULL: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ADD_KEY_WITHOUT_ROLE: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ADD_KEY_WITH_SERVICE_ROLE: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_NON_SERVICE_KEY_ATTEMPTING_TO_ADD_SERVICE_TECH: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_SERVICE_KEY_ATTEMPTING_TO_ADD_SERVICE_TECH_OUTSIDE_SERVICE_MODE: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_COULD_NOT_START_LOCAL_ENTITY_AUTH: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_UI_DENIED: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_TIMED_OUT_WAITING_FOR_TAP: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_TIMED_OUT_WAITING_FOR_UI_ACK: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_VALET_MODE: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_LOCAL_ENTITY_AUTH_FAILED_CANCELLED: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_NON_SERVICE_KEY_ATTEMPTING_TO_ADD_RIDER_KEY: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_ATTEMPTING_TO_ADD_RIDER_KEY_OUTSIDE_FLEET_MODE: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_NON_SERVICE_KEY_ATTEMPTING_TO_ADD_PREDELIVERY_KEY: WhitelistOperation_information_E
WHITELISTOPERATION_INFORMATION_SERVICE_KEY_ATTEMPTING_TO_ADD_PREDELIVERY_KEY_WHEN_ALREADY_DELIVERED: WhitelistOperation_information_E
AUTHENTICATION_LEVEL_NONE: AuthenticationLevel_E
AUTHENTICATION_LEVEL_UNLOCK: AuthenticationLevel_E
AUTHENTICATION_LEVEL_DRIVE: AuthenticationLevel_E
AUTHENTICATIONREASON_NOT_DOCUMENTED: AuthenticationReason_E
AUTHENTICATIONREASON_IDENTIFICATION: AuthenticationReason_E
AUTHENTICATIONREASON_POWER_ON_VEHICLE_REQUEST: AuthenticationReason_E
AUTHENTICATIONREASON_GTW_REQUEST: AuthenticationReason_E
AUTHENTICATIONREASON_UI_UNLOCK_PASSIVE_AUTH: AuthenticationReason_E
AUTHENTICATIONREASON_PASSIVE_UNLOCK_EXTERIOR_HANDLE_PULL: AuthenticationReason_E
AUTHENTICATIONREASON_PASSIVE_UNLOCK_INTERIOR_HANDLE_PULL: AuthenticationReason_E
AUTHENTICATIONREASON_PASSIVE_UNLOCK_AUTOPRESENT_DOOR: AuthenticationReason_E
AUTHENTICATIONREASON_ENTERED_HIGHER_AUTH_ZONE: AuthenticationReason_E
AUTHENTICATIONREASON_WALK_UP_UNLOCK: AuthenticationReason_E
AUTHENTICATIONREASON_IMMOBILIZER: AuthenticationReason_E
AUTHENTICATIONREJECTION_NONE: AuthenticationRejection_E
AUTHENTICATIONREJECTION_DEVICE_STATIONARY: AuthenticationRejection_E
AUTHENTICATIONREJECTION_PASSIVE_DISABLED: AuthenticationRejection_E
AUTHENTICATIONREJECTION_NO_TOKEN: AuthenticationRejection_E
AUTHENTICATIONREJECTION_PASSIVE_DISABLED_AUTOMATION: AuthenticationRejection_E
AUTHENTICATIONREJECTION_DEVICE_NOT_UNLOCKED_ON_WRIST: AuthenticationRejection_E
CLOSURESTATE_CLOSED: ClosureState_E
CLOSURESTATE_OPEN: ClosureState_E
CLOSURESTATE_AJAR: ClosureState_E
CLOSURESTATE_UNKNOWN: ClosureState_E
CLOSURESTATE_FAILED_UNLATCH: ClosureState_E
CLOSURESTATE_OPENING: ClosureState_E
CLOSURESTATE_CLOSING: ClosureState_E
VEHICLELOCKSTATE_UNLOCKED: VehicleLockState_E
VEHICLELOCKSTATE_LOCKED: VehicleLockState_E
VEHICLELOCKSTATE_INTERNAL_LOCKED: VehicleLockState_E
VEHICLELOCKSTATE_SELECTIVE_UNLOCKED: VehicleLockState_E
VEHICLE_SLEEP_STATUS_UNKNOWN: VehicleSleepStatus_E
VEHICLE_SLEEP_STATUS_AWAKE: VehicleSleepStatus_E
VEHICLE_SLEEP_STATUS_ASLEEP: VehicleSleepStatus_E
VEHICLE_USER_PRESENCE_UNKNOWN: UserPresence_E
VEHICLE_USER_PRESENCE_NOT_PRESENT: UserPresence_E
VEHICLE_USER_PRESENCE_PRESENT: UserPresence_E
UI_DESIRE_NONE: UIDesire_E
UI_DESIRE_HAS_DATA: UIDesire_E
GEAR_UNKNOWN: Gear_E
GEAR_PARK: Gear_E
GEAR_DRIVE: Gear_E
GEAR_REVERSE: Gear_E
GEAR_NEUTRAL: Gear_E
WHITELISTKEYPERMISSION_ADD_TO_WHITELIST: WhitelistKeyPermission_E
WHITELISTKEYPERMISSION_LOCAL_UNLOCK: WhitelistKeyPermission_E
WHITELISTKEYPERMISSION_LOCAL_DRIVE: WhitelistKeyPermission_E
WHITELISTKEYPERMISSION_REMOTE_UNLOCK: WhitelistKeyPermission_E
WHITELISTKEYPERMISSION_REMOTE_DRIVE: WhitelistKeyPermission_E
WHITELISTKEYPERMISSION_CHANGE_PERMISSIONS: WhitelistKeyPermission_E
WHITELISTKEYPERMISSION_REMOVE_FROM_WHITELIST: WhitelistKeyPermission_E
WHITELISTKEYPERMISSION_REMOVE_SELF_FROM_WHITELIST: WhitelistKeyPermission_E
WHITELISTKEYPERMISSION_MODIFY_FLEET_RESERVED_SLOTS: WhitelistKeyPermission_E
WHITELISTKEYPERMISSION_UNKNOWN: WhitelistKeyPermission_E
KEY_LOCATION_UNKNOWN: KeyLocationStatus_E
KEY_LOCATION_NOT_PRESENT: KeyLocationStatus_E
KEY_LOCATION_PRESENT: KeyLocationStatus_E
NFC_PRESENCE_NOT_PRESENT: NFCPresence
NFC_PRESENCE_PRESENT_AT_B_PILLAR: NFCPresence
NFC_PRESENCE_PRESENT_AT_CENTER_CONSOLE: NFCPresence
BLE_PRESENCE_NOT_PRESENT: BLEPresence
BLE_PRESENCE_PRESENT: BLEPresence
BLE_PRESENCE_CONNECTED_NOT_PRESENT: BLEPresence
REQUEST_SOURCE_NOT_POPULATED: RequestSource_E
REQUEST_SOURCE_BLE: RequestSource_E
REQUEST_SOURCE_OTHER: RequestSource_E
QR_CODE_STATUS_UNKNOWN: QRCodeStatus_E
QR_CODE_STATUS_DISPLAYED: QRCodeStatus_E
QR_CODE_STATUS_NOT_DISPLAYED: QRCodeStatus_E
ACTIVITY_NONE: Activity_E
ACTIVITY_STATIONARY: Activity_E
ACTIVITY_MOTION: Activity_E
ACTIVITY_SIGNIFICANT_MOTION: Activity_E
ALERT_CONFIRMATION_NONE: AlertConfirmation
ALERT_CONFIRMATION_PEER_REMOVED_INFORMATION: AlertConfirmation
APP_DEVICE_INFO_REQUEST_NONE: AppDeviceInfoRequest_E
APP_DEVICE_INFO_REQUEST_GET_MODEL_NUMBER: AppDeviceInfoRequest_E
APP_DEVICE_INFO_REQUEST_ONCHANGE_BATTERY_STATE: AppDeviceInfoRequest_E
UNKNOWN: AppOperatingSystem
ANDROID: AppOperatingSystem
IOS: AppOperatingSystem
WATCHOS: AppOperatingSystem
HARMONY_NEXT: AppOperatingSystem
BLE_ADDITIONAL_TRIM_APPLIED_NONE: BLEAdditionalTRIMApplied_E
BLE_ADDITIONAL_TRIM_APPLIED_APPLIED: BLEAdditionalTRIMApplied_E
BLE_ADDITIONAL_TRIM_APPLIED_NOT_APPLIED: BLEAdditionalTRIMApplied_E
BLE_ENDPOINT_NONE: BLEEndpoint_E
BLE_ENDPOINT_CENTER: BLEEndpoint_E
BLE_ENDPOINT_FRONT: BLEEndpoint_E
BLE_ENDPOINT_LEFT: BLEEndpoint_E
BLE_ENDPOINT_RIGHT: BLEEndpoint_E
BLE_ENDPOINT_REAR: BLEEndpoint_E
BLE_ENDPOINT_REAR_LEFT: BLEEndpoint_E
BLE_ENDPOINT_REAR_RIGHT: BLEEndpoint_E
BLE_ENDPOINT_NFC_CRADLE: BLEEndpoint_E
BLE_ENDPOINT_FRONT_LEFT: BLEEndpoint_E
BLE_ENDPOINT_FRONT_RIGHT: BLEEndpoint_E
BLE_ENDPOINT_SECONDARY_CENTER: BLEEndpoint_E
BATTERY_STATE_UNKNOWN: BatteryState_E
BATTERY_STATE_UNPLUGGED: BatteryState_E
BATTERY_STATE_CHARGING: BatteryState_E
BATTERY_STATE_FULL: BatteryState_E
CBMANAGERAUTHORIZATION_UNKNOWN: CBManagerAuthorization
CBMANAGERAUTHORIZATION_ALWAYS: CBManagerAuthorization
CBMANAGERAUTHORIZATION_DENIED: CBManagerAuthorization
CBMANAGERAUTHORIZATION_NOTDETERMINED: CBManagerAuthorization
CBMANAGERAUTHORIZATION_RESTRICTED: CBManagerAuthorization
CBMANAGERSTATE_UNKNOWN: CBManagerState
CBMANAGERSTATE_POWEREDOFF: CBManagerState
CBMANAGERSTATE_POWEREDON: CBManagerState
CBMANAGERSTATE_RESETTING: CBManagerState
CBMANAGERSTATE_UNAUTHORIZED: CBManagerState
CBMANAGERSTATE_UNSUPPORTED: CBManagerState
CPD_NOTIFICATION_RESPONSE_SNA: CPDNotificationResponse_E
CPD_NOTIFICATION_RESPONSE_INITIAL_WARNING_RECEIVED: CPDNotificationResponse_E
CPD_NOTIFICATION_RESPONSE_ESCALATED_WARNING_RECEIVED: CPDNotificationResponse_E
CPD_NOTIFICATION_RESPONSE_ERROR: CPDNotificationResponse_E
CPD_NOTIFICATION_NONE: CPDNotification_E
CPD_NOTIFICATION_INITIAL_WARNING: CPDNotification_E
CPD_NOTIFICATION_ESCALATED_WARNING: CPDNotification_E
UNKNOWN_TARGET: DeviceTarget
DEVELOPMENT_TARGET: DeviceTarget
PRODUCTION_TARGET: DeviceTarget
DEVICE_MOTION_CONFIDENCE_UNKNOWN: Device_Motion_Confidence
DEVICE_MOTION_CONFIDENCE_LOW: Device_Motion_Confidence
DEVICE_MOTION_CONFIDENCE_MEDIUM: Device_Motion_Confidence
DEVICE_MOTION_CONFIDENCE_HIGH: Device_Motion_Confidence
DEVICE_MOTION_UNKNOWN: Device_Motion_State
DEVICE_MOTION_STATIONARY: Device_Motion_State
DEVICE_MOTION_WALKING: Device_Motion_State
DEVICE_MOTION_RUNNING: Device_Motion_State
DEVICE_MOTION_AUTOMOTIVE: Device_Motion_State
DEVICE_MOTION_CYCLING: Device_Motion_State
FIRAERROR_UNKNOWN: FiraError_E
FIRAERROR_UWB_HARDWARE_NOT_AVAILABLE: FiraError_E
FIRAERROR_ILLEGAL_ARGUMENT: FiraError_E
FIRAERROR_ILLEGAL_STATE: FiraError_E
FIRAERROR_SERVICE_VERSION_UPDATE_REQUIRED: FiraError_E
FIRAERROR_SERVICE_DISABLED: FiraError_E
FIRAERROR_SIGN_IN_REQUIRED: FiraError_E
FIRAERROR_INVALID_ACCOUNT: FiraError_E
FIRAERROR_RESOLUTION_REQUIRED: FiraError_E
FIRAERROR_NETWORK_ERROR: FiraError_E
FIRAERROR_INTERNAL_ERROR: FiraError_E
FIRAERROR_DEVELOPER_ERROR: FiraError_E
FIRAERROR_ERROR: FiraError_E
FIRAERROR_INTERRUPTED: FiraError_E
FIRAERROR_TIMEOUT: FiraError_E
FIRAERROR_CANCELED: FiraError_E
FIRAERROR_API_NOT_CONNECTED: FiraError_E
FIRAERROR_STATUS_ERROR: FiraError_E
FIRAERROR_SERVICE_NOT_AVAILABLE: FiraError_E
FIRAERROR_NULL_RANGING_DEVICE: FiraError_E
FIRAERROR_INVALID_API_CALL: FiraError_E
FIRAERROR_RANGING_ALREADY_STARTED: FiraError_E
FIRAERROR_UWB_SYSTEM_CALLBACK_FAILURE: FiraError_E
FIRAERROR_RANGING_UNKNOWN: FiraError_E
FIRAERROR_RANGING_INTERRUPTED: FiraError_E
FIRAERROR_RANGING_INTERNAL_ERROR: FiraError_E
FIRAERROR_RANGING_TIMEOUT: FiraError_E
FIRAERROR_RANGING_CANCELED: FiraError_E
FIRAERROR_RANGING_DEAD_CLIENT: FiraError_E
FIRAERROR_COROUTINE_TASK_EXECUTION_EXCEPTION: FiraError_E
FIRAERROR_COROUTINE_TASK_INTERRUPTED_EXCEPTION: FiraError_E
FIRAERROR_NOT_SELECTED: FiraError_E
RANGING_TYPE_UNKNOWN: FiraRangingType
MULTICAST_DS_TWR: FiraRangingType
UNICAST_DS_TWR: FiraRangingType
STS_UNKNOWN: FiraSTSMode
STATIC: FiraSTSMode
PROVISIONED: FiraSTSMode
PROVISIONED_INDIVIDUAL: FiraSTSMode
DYNAMIC: FiraSTSMode
DYNAMIC_INDIVIDUAL: FiraSTSMode
GATTSERVICESBITMASK_PHONE_KEY_SERVICE: GATTServicesBitMask
GATTSERVICESBITMASK_FROM_VEHICLE_CHAR: GATTServicesBitMask
GATTSERVICESBITMASK_TO_VEHICLE_CHAR: GATTServicesBitMask
GATTSERVICESBITMASK_VERSION_CHAR: GATTServicesBitMask
GATTSERVICESBITMASK_BONDING_SERVICE: GATTServicesBitMask
GATTSERVICESBITMASK_BONDING_CHAR: GATTServicesBitMask
GENEALOGYREQUEST_NONE: GenealogyRequest_E
GENEALOGYREQUEST_READ: GenealogyRequest_E
GENEALOGYREQUEST_KEYFOBINFO_READ: GenealogyRequest_E
GENEALOGYREQUEST_TPWHEELUNITINFO_READ: GenealogyRequest_E
GENEALOGY_STATUS_NONE: GenealogyStatus_E
GENEALOGY_STATUS_NOT_WRITTEN: GenealogyStatus_E
GENEALOGY_STATUS_WRITE_SUCCESS: GenealogyStatus_E
GENEALOGY_STATUS_WRITE_FAILURE: GenealogyStatus_E
GENEALOGY_STATUS_READ_SUCCESS: GenealogyStatus_E
GENEALOGY_STATUS_READ_FAILURE: GenealogyStatus_E
GENEALOGY_STATUS_CRC_FAILURE: GenealogyStatus_E
GET_READER_KEY_COMMAND_UNKNOWN: GetReaderKeyCommand
GET_READER_KEY_COMMAND_START_LOOKING: GetReaderKeyCommand
GET_READER_KEY_COMMAND_STOP_LOOKING: GetReaderKeyCommand
HANDLE_PULLED_FRONT_DRIVER_DOOR: HandlePulled_E
HANDLE_PULLED_FRONT_PASSENGER_DOOR: HandlePulled_E
HANDLE_PULLED_REAR_DRIVER_DOOR: HandlePulled_E
HANDLE_PULLED_REAR_PASSENGER_DOOR: HandlePulled_E
HANDLE_PULLED_TRUNK: HandlePulled_E
HANDLE_PULLED_CHARGE_PORT: HandlePulled_E
HANDLE_PULLED_FRONT_DRIVER_AUTO_PRESENT_DOOR: HandlePulled_E
HANDLE_PULLED_FRONT_PASSENGER_AUTO_PRESENT_DOOR: HandlePulled_E
HANDLE_PULLED_OTHER: HandlePulled_E
HANDLE_PULLED_FRUNK: HandlePulled_E
IMU_REQUEST_NONE: IMURequest_E
IMU_REQUEST_GET_SLEEP_STATE: IMURequest_E
IMU_REQUEST_ENABLE_CONTINUOUS_ACTIVITY_UPDATE: IMURequest_E
IMU_REQUEST_DISABLE_CONTINUOUS_ACTIVITY_UPDATE: IMURequest_E
LOCATION_PERMISSION_UNKNOWN: LocationPermission
LOCATION_PERMISSION_ASK_NEXT_TIME_OR_WHEN_I_SHARE: LocationPermission
LOCATION_PERMISSION_WHILE_USING_THE_APP: LocationPermission
LOCATION_PERMISSION_ALWAYS: LocationPermission
LOCATION_PERMISSION_NEVER: LocationPermission
ERROR_UNKNOWN: NIError_E
ERROR_SESSION_LIMIT_EXCEEDED: NIError_E
ERROR_INVALID_CONFIGURATION: NIError_E
ERROR_RESOURCE_USAGE_TIMEOUT: NIError_E
ERROR_SESSION_FAILED: NIError_E
ERROR_UNSUPPORTED_PLATFORM: NIError_E
ERROR_USER_DID_NOT_ALLOW: NIError_E
ERROR_BLE_PEER_UNAVAILABLE: NIError_E
ERROR_VEHICLE_NOT_SELECTED_FOR_RANGING: NIError_E
NI_SESSION_STATUS_UNKNOWN: NISessionStatus_E
NI_SESSION_STATUS_ACTIVE: NISessionStatus_E
NI_SESSION_STATUS_INACTIVE: NISessionStatus_E
NI_SESSION_STATUS_ERROR: NISessionStatus_E
NI_SESSION_STATUS_UNAVAILABLE: NISessionStatus_E
OPERATION_MODE_UNKNOWN: OperationMode_E
OPERATION_MODE_OWNER: OperationMode_E
OPERATION_MODE_FLEET: OperationMode_E
PERIPHERALSTATE_SNA: PeripheralState
PERIPHERALSTATE_DISCONNECTED: PeripheralState
PERIPHERALSTATE_CONNECTED: PeripheralState
PERIPHERALSTATE_CONNECTING: PeripheralState
PERIPHERALSTATE_DISCONNECTING: PeripheralState
PHONE_THERMAL_STATE_UNKNOWN: PhoneThermalState_E
PHONE_THERMAL_STATE_NOMINAL: PhoneThermalState_E
PHONE_THERMAL_STATE_FAIR: PhoneThermalState_E
PHONE_THERMAL_STATE_LIGHT: PhoneThermalState_E
PHONE_THERMAL_STATE_MODERATE: PhoneThermalState_E
PHONE_THERMAL_STATE_SERIOUS: PhoneThermalState_E
PHONE_THERMAL_STATE_SEVERE: PhoneThermalState_E
PHONE_THERMAL_STATE_CRITICAL: PhoneThermalState_E
PHONE_THERMAL_STATE_EMERGENCY: PhoneThermalState_E
PHONE_THERMAL_STATE_SHUTDOWN: PhoneThermalState_E
RANGINGCONFIGTYPE_UNDEFINED: RangingConfigType_E
RANGINGCONFIGTYPE_APPLE_UNICAST_BACKGROUND: RangingConfigType_E
RANGINGCONFIGTYPE_APPLE_UNICAST_FOREGROUND: RangingConfigType_E
RANGINGCONFIGTYPE_APPLE_MULTICAST_BACKGROUND: RangingConfigType_E
RANGINGCONFIGTYPE_APPLE_MULTICAST_FOREGROUND: RangingConfigType_E
RANGING_UPDATE_RATE_UNKNOWN: RangingUpdateRate
RANGING_UPDATE_RATE_AUTOMATIC: RangingUpdateRate
RANGING_UPDATE_RATE_INFREQUENT: RangingUpdateRate
RANGING_UPDATE_RATE_FREQUENT: RangingUpdateRate
SLEEPMANAGER_COMMAND_NONE: SleepManagerCommand_E
SLEEPMANAGER_GET_STATS: SleepManagerCommand_E
SLEEPMANAGER_RESET_STATS: SleepManagerCommand_E
UI_REQUEST_NONE: UIRequest_E
UI_REQUEST_GET_VEHICLE_BLE_NICK_NAME: UIRequest_E
UWB_AVAILABILITY_UNKNOWN: UWBAvailability
UWB_AVAILABILITY_AVAILABLE: UWBAvailability
UWB_AVAILABILITY_UNAVAILABLE_UNSUPPORTED_DEVICE: UWBAvailability
UWB_AVAILABILITY_UNAVAILABLE_PERMISSION_DENIED: UWBAvailability
UWB_AVAILABILITY_UNAVAILABLE: UWBAvailability
UWB_AVAILABILITY_UNAVAILABLE_DISABLED_BY_USER: UWBAvailability
UPDATER_LOCATION_NONE: UpdaterLocation
UPDATER_LOCATION_APPLICATION: UpdaterLocation
UPDATER_LOCATION_BOOTLOADER: UpdaterLocation
UPDATER_LOCATION_SECONDARY_APPLICATION: UpdaterLocation
UPDATER_LOCATION_APPLICATION_IN_EXTERNAL_FLASH: UpdaterLocation
UPDATER_STATUS_CODE_ERROR: UpdaterStatusCode
UPDATER_STATUS_CODE_WAIT: UpdaterStatusCode
UPDATER_STATUS_CODE_BLOCK_STAGED: UpdaterStatusCode
UPDATER_STATUS_CODE_IMAGE_STAGED: UpdaterStatusCode
UPDATER_STATUS_CODE_CRC_CHECK_SUCCESS: UpdaterStatusCode
UPDATER_STATUS_CODE_CRC_CHECK_FAIL: UpdaterStatusCode
UPDATER_STATUS_CODE_HASH_FAIL: UpdaterStatusCode
UPDATER_STATUS_CODE_SIGNATURE_FAIL: UpdaterStatusCode
UPDATER_STATUS_CODE_ERROR_HASH_RESTORE_FAIL: UpdaterStatusCode
UPDATER_STATUS_CODE_LOCATION_SET: UpdaterStatusCode
IBEACON_STATE_SNA: iBeaconState
IBEACON_STATE_INSIDE: iBeaconState
IBEACON_STATE_OUTSIDE: iBeaconState
IOS_APPSTATE_SNA: iOS_AppState
IOS_APPSTATE_INACTIVE: iOS_AppState
IOS_APPSTATE_ACTIVE: iOS_AppState
IOS_APPSTATE_BACKGROUND: iOS_AppState
IOS_COREBTATTERRORCODE_SNA: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_SUCCESS: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_READ_NOT_PERMITTED: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_WRITE_NOT_PERMITTED: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_INVALID_PDU: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_INSUFFICIENT_AUTHENTICATION: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_REQUEST_NOT_SUPPORTED: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_INVALID_OFFSET: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_INSUFFICIENT_AUTHORIZATION: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_PREPARE_QUEUE_FULL: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_ATT_NOT_FOUND: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_ATT_NOT_LONG: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_INSUFFICIENT_ENCRYPTION_KEY_SIZE: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_INVALID_ATT_VALUE_LENGTH: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_UNLIKELY_ERROR: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_INSUFFICIENT_ENCRYPTION: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_UNSUPPORTED_GROUP_TYPE: iOS_CoreBTATTErrorCode
IOS_COREBTATTERRORCODE_INSUFFICIENT_RESOURCES: iOS_CoreBTATTErrorCode
IOS_COREBTERROR_SNA: iOS_CoreBTError
IOS_COREBTERROR_UNKNOWN: iOS_CoreBTError
IOS_COREBTERROR_INVALID_PARAMETERS: iOS_CoreBTError
IOS_COREBTERROR_INVALID_HANDLE: iOS_CoreBTError
IOS_COREBTERROR_NOT_CONNECTED: iOS_CoreBTError
IOS_COREBTERROR_OUT_OF_SPACE: iOS_CoreBTError
IOS_COREBTERROR_OPERATION_CANCELLED: iOS_CoreBTError
IOS_COREBTERROR_CONNECTION_TIMEOUT: iOS_CoreBTError
IOS_COREBTERROR_PERIPHERAL_DISCONNECTED: iOS_CoreBTError
IOS_COREBTERROR_UUID_NOT_ALLOWED: iOS_CoreBTError
IOS_COREBTERROR_ALREADY_ADVERTISING: iOS_CoreBTError
IOS_COREBTERROR_CONNECTION_FAILED: iOS_CoreBTError
IOS_COREBTERROR_CONNECTION_LIMIT_REACHED: iOS_CoreBTError
IOS_COREBTERROR_OPERATION_NOT_SUPPORTED: iOS_CoreBTError
IOS_COREBTERROR_UNKNOWN_DEVICE: iOS_CoreBTError
IOS_COREBTERROR_ENCRYPTIONTIMEDOUT: iOS_CoreBTError
IOS_COREBTERROR_LEGATTEXCEEDEDBACKGROUNDNOTIFICATIONLIMIT: iOS_CoreBTError
IOS_COREBTERROR_LEGATTNEARBACKGROUNDNOTIFICATIONLIMIT: iOS_CoreBTError
IOS_COREBTERROR_PEERREMOVEDPAIRINGINFORMATION: iOS_CoreBTError
IOS_COREBTERROR_TOOMANYLEPAIREDDEVICES: iOS_CoreBTError
IOS_LAUNCHREASON_SNA: iOS_LaunchReason
IOS_LAUNCHREASON_FOREGROUND: iOS_LaunchReason
IOS_LAUNCHREASON_BLUETOOTH: iOS_LaunchReason
IOS_LAUNCHREASON_BEACON: iOS_LaunchReason
IOS_LAUNCHREASON_NOTIFICATION: iOS_LaunchReason
IOS_LAUNCHREASON_URL: iOS_LaunchReason
IOS_LAUNCHREASON_SHORTCUT: iOS_LaunchReason

class SignedMessage(_message.Message):
    __slots__ = ("protobufMessageAsBytes", "signatureType", "token", "signature", "keyId", "counter")
    PROTOBUFMESSAGEASBYTES_FIELD_NUMBER: _ClassVar[int]
    SIGNATURETYPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    KEYID_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    protobufMessageAsBytes: bytes
    signatureType: SignatureType
    token: bytes
    signature: bytes
    keyId: bytes
    counter: int
    def __init__(self, protobufMessageAsBytes: _Optional[bytes] = ..., signatureType: _Optional[_Union[SignatureType, str]] = ..., token: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., keyId: _Optional[bytes] = ..., counter: _Optional[int] = ...) -> None: ...

class ToVCSECMessage(_message.Message):
    __slots__ = ("signedMessage", "unsignedMessage")
    SIGNEDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNSIGNEDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    signedMessage: SignedMessage
    unsignedMessage: UnsignedMessage
    def __init__(self, signedMessage: _Optional[_Union[SignedMessage, _Mapping]] = ..., unsignedMessage: _Optional[_Union[UnsignedMessage, _Mapping]] = ...) -> None: ...

class KeyIdentifier(_message.Message):
    __slots__ = ("publicKeySHA1",)
    PUBLICKEYSHA1_FIELD_NUMBER: _ClassVar[int]
    publicKeySHA1: bytes
    def __init__(self, publicKeySHA1: _Optional[bytes] = ...) -> None: ...

class KeyMetadata(_message.Message):
    __slots__ = ("keyFormFactor",)
    KEYFORMFACTOR_FIELD_NUMBER: _ClassVar[int]
    keyFormFactor: KeyFormFactor
    def __init__(self, keyFormFactor: _Optional[_Union[KeyFormFactor, str]] = ...) -> None: ...

class PublicKey(_message.Message):
    __slots__ = ("PublicKeyRaw",)
    PUBLICKEYRAW_FIELD_NUMBER: _ClassVar[int]
    PublicKeyRaw: bytes
    def __init__(self, PublicKeyRaw: _Optional[bytes] = ...) -> None: ...

class WhitelistInfo(_message.Message):
    __slots__ = ("numberOfEntries", "whitelistEntries", "slotMask")
    NUMBEROFENTRIES_FIELD_NUMBER: _ClassVar[int]
    WHITELISTENTRIES_FIELD_NUMBER: _ClassVar[int]
    SLOTMASK_FIELD_NUMBER: _ClassVar[int]
    numberOfEntries: int
    whitelistEntries: _containers.RepeatedCompositeFieldContainer[KeyIdentifier]
    slotMask: int
    def __init__(self, numberOfEntries: _Optional[int] = ..., whitelistEntries: _Optional[_Iterable[_Union[KeyIdentifier, _Mapping]]] = ..., slotMask: _Optional[int] = ...) -> None: ...

class WhitelistEntryInfo(_message.Message):
    __slots__ = ("keyId", "publicKey", "metadataForKey", "slot", "permissions", "secondsEntryRemainsActive", "keyRole")
    KEYID_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    METADATAFORKEY_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SECONDSENTRYREMAINSACTIVE_FIELD_NUMBER: _ClassVar[int]
    KEYROLE_FIELD_NUMBER: _ClassVar[int]
    keyId: KeyIdentifier
    publicKey: PublicKey
    metadataForKey: KeyMetadata
    slot: int
    permissions: _containers.RepeatedScalarFieldContainer[WhitelistKeyPermission_E]
    secondsEntryRemainsActive: int
    keyRole: _keys_pb2.Role
    def __init__(self, keyId: _Optional[_Union[KeyIdentifier, _Mapping]] = ..., publicKey: _Optional[_Union[PublicKey, _Mapping]] = ..., metadataForKey: _Optional[_Union[KeyMetadata, _Mapping]] = ..., slot: _Optional[int] = ..., permissions: _Optional[_Iterable[_Union[WhitelistKeyPermission_E, str]]] = ..., secondsEntryRemainsActive: _Optional[int] = ..., keyRole: _Optional[_Union[_keys_pb2.Role, str]] = ...) -> None: ...

class InformationRequest(_message.Message):
    __slots__ = ("informationRequestType", "keyId", "publicKey", "slot")
    INFORMATIONREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    KEYID_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    informationRequestType: InformationRequestType
    keyId: KeyIdentifier
    publicKey: bytes
    slot: int
    def __init__(self, informationRequestType: _Optional[_Union[InformationRequestType, str]] = ..., keyId: _Optional[_Union[KeyIdentifier, _Mapping]] = ..., publicKey: _Optional[bytes] = ..., slot: _Optional[int] = ...) -> None: ...

class ClosureMoveRequest(_message.Message):
    __slots__ = ("frontDriverDoor", "frontPassengerDoor", "rearDriverDoor", "rearPassengerDoor", "rearTrunk", "frontTrunk", "chargePort", "tonneau")
    FRONTDRIVERDOOR_FIELD_NUMBER: _ClassVar[int]
    FRONTPASSENGERDOOR_FIELD_NUMBER: _ClassVar[int]
    REARDRIVERDOOR_FIELD_NUMBER: _ClassVar[int]
    REARPASSENGERDOOR_FIELD_NUMBER: _ClassVar[int]
    REARTRUNK_FIELD_NUMBER: _ClassVar[int]
    FRONTTRUNK_FIELD_NUMBER: _ClassVar[int]
    CHARGEPORT_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_FIELD_NUMBER: _ClassVar[int]
    frontDriverDoor: ClosureMoveType_E
    frontPassengerDoor: ClosureMoveType_E
    rearDriverDoor: ClosureMoveType_E
    rearPassengerDoor: ClosureMoveType_E
    rearTrunk: ClosureMoveType_E
    frontTrunk: ClosureMoveType_E
    chargePort: ClosureMoveType_E
    tonneau: ClosureMoveType_E
    def __init__(self, frontDriverDoor: _Optional[_Union[ClosureMoveType_E, str]] = ..., frontPassengerDoor: _Optional[_Union[ClosureMoveType_E, str]] = ..., rearDriverDoor: _Optional[_Union[ClosureMoveType_E, str]] = ..., rearPassengerDoor: _Optional[_Union[ClosureMoveType_E, str]] = ..., rearTrunk: _Optional[_Union[ClosureMoveType_E, str]] = ..., frontTrunk: _Optional[_Union[ClosureMoveType_E, str]] = ..., chargePort: _Optional[_Union[ClosureMoveType_E, str]] = ..., tonneau: _Optional[_Union[ClosureMoveType_E, str]] = ...) -> None: ...

class PermissionChange(_message.Message):
    __slots__ = ("key", "permission", "secondsToBeActive", "keyRole")
    KEY_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SECONDSTOBEACTIVE_FIELD_NUMBER: _ClassVar[int]
    KEYROLE_FIELD_NUMBER: _ClassVar[int]
    key: PublicKey
    permission: _containers.RepeatedScalarFieldContainer[WhitelistKeyPermission_E]
    secondsToBeActive: int
    keyRole: _keys_pb2.Role
    def __init__(self, key: _Optional[_Union[PublicKey, _Mapping]] = ..., permission: _Optional[_Iterable[_Union[WhitelistKeyPermission_E, str]]] = ..., secondsToBeActive: _Optional[int] = ..., keyRole: _Optional[_Union[_keys_pb2.Role, str]] = ...) -> None: ...

class ReplaceKey(_message.Message):
    __slots__ = ("publicKeyToReplace", "slotToReplace", "keyToAdd", "keyRole", "impermanent")
    PUBLICKEYTOREPLACE_FIELD_NUMBER: _ClassVar[int]
    SLOTTOREPLACE_FIELD_NUMBER: _ClassVar[int]
    KEYTOADD_FIELD_NUMBER: _ClassVar[int]
    KEYROLE_FIELD_NUMBER: _ClassVar[int]
    IMPERMANENT_FIELD_NUMBER: _ClassVar[int]
    publicKeyToReplace: PublicKey
    slotToReplace: int
    keyToAdd: PublicKey
    keyRole: _keys_pb2.Role
    impermanent: bool
    def __init__(self, publicKeyToReplace: _Optional[_Union[PublicKey, _Mapping]] = ..., slotToReplace: _Optional[int] = ..., keyToAdd: _Optional[_Union[PublicKey, _Mapping]] = ..., keyRole: _Optional[_Union[_keys_pb2.Role, str]] = ..., impermanent: _Optional[bool] = ...) -> None: ...

class WhitelistOperation(_message.Message):
    __slots__ = ("addPublicKeyToWhitelist", "removePublicKeyFromWhitelist", "addPermissionsToPublicKey", "removePermissionsFromPublicKey", "addKeyToWhitelistAndAddPermissions", "updateKeyAndPermissions", "addImpermanentKey", "addImpermanentKeyAndRemoveExisting", "removeAllImpermanentKeys", "replaceKey", "setInfotainmentKey", "metadataForKey", "sessionID")
    ADDPUBLICKEYTOWHITELIST_FIELD_NUMBER: _ClassVar[int]
    REMOVEPUBLICKEYFROMWHITELIST_FIELD_NUMBER: _ClassVar[int]
    ADDPERMISSIONSTOPUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    REMOVEPERMISSIONSFROMPUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    ADDKEYTOWHITELISTANDADDPERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATEKEYANDPERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ADDIMPERMANENTKEY_FIELD_NUMBER: _ClassVar[int]
    ADDIMPERMANENTKEYANDREMOVEEXISTING_FIELD_NUMBER: _ClassVar[int]
    REMOVEALLIMPERMANENTKEYS_FIELD_NUMBER: _ClassVar[int]
    REPLACEKEY_FIELD_NUMBER: _ClassVar[int]
    SETINFOTAINMENTKEY_FIELD_NUMBER: _ClassVar[int]
    METADATAFORKEY_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    addPublicKeyToWhitelist: PublicKey
    removePublicKeyFromWhitelist: PublicKey
    addPermissionsToPublicKey: PermissionChange
    removePermissionsFromPublicKey: PermissionChange
    addKeyToWhitelistAndAddPermissions: PermissionChange
    updateKeyAndPermissions: PermissionChange
    addImpermanentKey: PermissionChange
    addImpermanentKeyAndRemoveExisting: PermissionChange
    removeAllImpermanentKeys: bool
    replaceKey: ReplaceKey
    setInfotainmentKey: PublicKey
    metadataForKey: KeyMetadata
    sessionID: bytes
    def __init__(self, addPublicKeyToWhitelist: _Optional[_Union[PublicKey, _Mapping]] = ..., removePublicKeyFromWhitelist: _Optional[_Union[PublicKey, _Mapping]] = ..., addPermissionsToPublicKey: _Optional[_Union[PermissionChange, _Mapping]] = ..., removePermissionsFromPublicKey: _Optional[_Union[PermissionChange, _Mapping]] = ..., addKeyToWhitelistAndAddPermissions: _Optional[_Union[PermissionChange, _Mapping]] = ..., updateKeyAndPermissions: _Optional[_Union[PermissionChange, _Mapping]] = ..., addImpermanentKey: _Optional[_Union[PermissionChange, _Mapping]] = ..., addImpermanentKeyAndRemoveExisting: _Optional[_Union[PermissionChange, _Mapping]] = ..., removeAllImpermanentKeys: _Optional[bool] = ..., replaceKey: _Optional[_Union[ReplaceKey, _Mapping]] = ..., setInfotainmentKey: _Optional[_Union[PublicKey, _Mapping]] = ..., metadataForKey: _Optional[_Union[KeyMetadata, _Mapping]] = ..., sessionID: _Optional[bytes] = ...) -> None: ...

class WhitelistOperation_status(_message.Message):
    __slots__ = ("whitelistOperationInformation", "signerOfOperation", "operationStatus")
    WHITELISTOPERATIONINFORMATION_FIELD_NUMBER: _ClassVar[int]
    SIGNEROFOPERATION_FIELD_NUMBER: _ClassVar[int]
    OPERATIONSTATUS_FIELD_NUMBER: _ClassVar[int]
    whitelistOperationInformation: WhitelistOperation_information_E
    signerOfOperation: KeyIdentifier
    operationStatus: OperationStatus_E
    def __init__(self, whitelistOperationInformation: _Optional[_Union[WhitelistOperation_information_E, str]] = ..., signerOfOperation: _Optional[_Union[KeyIdentifier, _Mapping]] = ..., operationStatus: _Optional[_Union[OperationStatus_E, str]] = ...) -> None: ...

class SignedMessage_status(_message.Message):
    __slots__ = ("counter", "signedMessageInformation")
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    SIGNEDMESSAGEINFORMATION_FIELD_NUMBER: _ClassVar[int]
    counter: int
    signedMessageInformation: SignedMessage_information_E
    def __init__(self, counter: _Optional[int] = ..., signedMessageInformation: _Optional[_Union[SignedMessage_information_E, str]] = ...) -> None: ...

class CommandStatus(_message.Message):
    __slots__ = ("operationStatus", "signedMessageStatus", "whitelistOperationStatus")
    OPERATIONSTATUS_FIELD_NUMBER: _ClassVar[int]
    SIGNEDMESSAGESTATUS_FIELD_NUMBER: _ClassVar[int]
    WHITELISTOPERATIONSTATUS_FIELD_NUMBER: _ClassVar[int]
    operationStatus: OperationStatus_E
    signedMessageStatus: SignedMessage_status
    whitelistOperationStatus: WhitelistOperation_status
    def __init__(self, operationStatus: _Optional[_Union[OperationStatus_E, str]] = ..., signedMessageStatus: _Optional[_Union[SignedMessage_status, _Mapping]] = ..., whitelistOperationStatus: _Optional[_Union[WhitelistOperation_status, _Mapping]] = ...) -> None: ...

class AutonomyCommand(_message.Message):
    __slots__ = ("pullOverCommand",)
    class PullOverCommand(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    PULLOVERCOMMAND_FIELD_NUMBER: _ClassVar[int]
    pullOverCommand: AutonomyCommand.PullOverCommand
    def __init__(self, pullOverCommand: _Optional[_Union[AutonomyCommand.PullOverCommand, _Mapping]] = ...) -> None: ...

class AuthenticationRequestToken(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: bytes
    def __init__(self, token: _Optional[bytes] = ...) -> None: ...

class AuthenticationRequest(_message.Message):
    __slots__ = ("sessionInfo", "requestedLevel", "reasonsForAuth")
    SESSIONINFO_FIELD_NUMBER: _ClassVar[int]
    REQUESTEDLEVEL_FIELD_NUMBER: _ClassVar[int]
    REASONSFORAUTH_FIELD_NUMBER: _ClassVar[int]
    sessionInfo: AuthenticationRequestToken
    requestedLevel: AuthenticationLevel_E
    reasonsForAuth: _containers.RepeatedScalarFieldContainer[AuthenticationReason_E]
    def __init__(self, sessionInfo: _Optional[_Union[AuthenticationRequestToken, _Mapping]] = ..., requestedLevel: _Optional[_Union[AuthenticationLevel_E, str]] = ..., reasonsForAuth: _Optional[_Iterable[_Union[AuthenticationReason_E, str]]] = ...) -> None: ...

class AuthenticationResponse(_message.Message):
    __slots__ = ("authenticationLevel", "estimatedDistance", "authenticationRejection")
    AUTHENTICATIONLEVEL_FIELD_NUMBER: _ClassVar[int]
    ESTIMATEDDISTANCE_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATIONREJECTION_FIELD_NUMBER: _ClassVar[int]
    authenticationLevel: AuthenticationLevel_E
    estimatedDistance: int
    authenticationRejection: AuthenticationRejection_E
    def __init__(self, authenticationLevel: _Optional[_Union[AuthenticationLevel_E, str]] = ..., estimatedDistance: _Optional[int] = ..., authenticationRejection: _Optional[_Union[AuthenticationRejection_E, str]] = ...) -> None: ...

class UnsignedMessage(_message.Message):
    __slots__ = ("InformationRequest", "RKEAction", "authenticationResponse", "closureMoveRequest", "WhitelistOperation", "autonomyCommand", "setMetaDataForKey", "deviceActivity", "getEpochSessionInfo", "deviceMotion", "appDeviceInfo", "getReaderKey", "NISessionResponse", "NISessionStopped", "appEventLog", "serviceDiagnosticRequest", "NIBatchResponse", "provisionIdentity", "changeOperationMode", "cpdResponse", "securityControl", "personalizationInformation", "field_58", "field_59", "field_60")
    INFORMATIONREQUEST_FIELD_NUMBER: _ClassVar[int]
    RKEACTION_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CLOSUREMOVEREQUEST_FIELD_NUMBER: _ClassVar[int]
    WHITELISTOPERATION_FIELD_NUMBER: _ClassVar[int]
    AUTONOMYCOMMAND_FIELD_NUMBER: _ClassVar[int]
    SETMETADATAFORKEY_FIELD_NUMBER: _ClassVar[int]
    DEVICEACTIVITY_FIELD_NUMBER: _ClassVar[int]
    GETEPOCHSESSIONINFO_FIELD_NUMBER: _ClassVar[int]
    DEVICEMOTION_FIELD_NUMBER: _ClassVar[int]
    APPDEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    GETREADERKEY_FIELD_NUMBER: _ClassVar[int]
    NISESSIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    NISESSIONSTOPPED_FIELD_NUMBER: _ClassVar[int]
    APPEVENTLOG_FIELD_NUMBER: _ClassVar[int]
    SERVICEDIAGNOSTICREQUEST_FIELD_NUMBER: _ClassVar[int]
    NIBATCHRESPONSE_FIELD_NUMBER: _ClassVar[int]
    PROVISIONIDENTITY_FIELD_NUMBER: _ClassVar[int]
    CHANGEOPERATIONMODE_FIELD_NUMBER: _ClassVar[int]
    CPDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SECURITYCONTROL_FIELD_NUMBER: _ClassVar[int]
    PERSONALIZATIONINFORMATION_FIELD_NUMBER: _ClassVar[int]
    FIELD_58_FIELD_NUMBER: _ClassVar[int]
    FIELD_59_FIELD_NUMBER: _ClassVar[int]
    FIELD_60_FIELD_NUMBER: _ClassVar[int]
    InformationRequest: InformationRequest
    RKEAction: RKEAction_E
    authenticationResponse: AuthenticationResponse
    closureMoveRequest: ClosureMoveRequest
    WhitelistOperation: WhitelistOperation
    autonomyCommand: AutonomyCommand
    setMetaDataForKey: KeyMetadata
    deviceActivity: Activity_E
    getEpochSessionInfo: _signatures_pb2.GetSessionInfoRequest
    deviceMotion: DeviceMotion
    appDeviceInfo: AppDeviceInfo
    getReaderKey: GetReaderKey
    NISessionResponse: NISessionResponse
    NISessionStopped: NISessionStopped
    appEventLog: AppEventLog
    serviceDiagnosticRequest: ServiceDiagnosticRequest
    NIBatchResponse: NIBatchResponse
    provisionIdentity: ProvisionIdentity
    changeOperationMode: ChangeOperationMode
    cpdResponse: CPDResponse
    securityControl: SecurityControl
    personalizationInformation: PersonalizationInformation
    field_58: FiraCapabilities
    field_59: FiraResponse
    field_60: AppStateEvent
    def __init__(self, InformationRequest: _Optional[_Union[InformationRequest, _Mapping]] = ..., RKEAction: _Optional[_Union[RKEAction_E, str]] = ..., authenticationResponse: _Optional[_Union[AuthenticationResponse, _Mapping]] = ..., closureMoveRequest: _Optional[_Union[ClosureMoveRequest, _Mapping]] = ..., WhitelistOperation: _Optional[_Union[WhitelistOperation, _Mapping]] = ..., autonomyCommand: _Optional[_Union[AutonomyCommand, _Mapping]] = ..., setMetaDataForKey: _Optional[_Union[KeyMetadata, _Mapping]] = ..., deviceActivity: _Optional[_Union[Activity_E, str]] = ..., getEpochSessionInfo: _Optional[_Union[_signatures_pb2.GetSessionInfoRequest, _Mapping]] = ..., deviceMotion: _Optional[_Union[DeviceMotion, _Mapping]] = ..., appDeviceInfo: _Optional[_Union[AppDeviceInfo, _Mapping]] = ..., getReaderKey: _Optional[_Union[GetReaderKey, _Mapping]] = ..., NISessionResponse: _Optional[_Union[NISessionResponse, _Mapping]] = ..., NISessionStopped: _Optional[_Union[NISessionStopped, _Mapping]] = ..., appEventLog: _Optional[_Union[AppEventLog, _Mapping]] = ..., serviceDiagnosticRequest: _Optional[_Union[ServiceDiagnosticRequest, _Mapping]] = ..., NIBatchResponse: _Optional[_Union[NIBatchResponse, _Mapping]] = ..., provisionIdentity: _Optional[_Union[ProvisionIdentity, _Mapping]] = ..., changeOperationMode: _Optional[_Union[ChangeOperationMode, _Mapping]] = ..., cpdResponse: _Optional[_Union[CPDResponse, _Mapping]] = ..., securityControl: _Optional[_Union[SecurityControl, _Mapping]] = ..., personalizationInformation: _Optional[_Union[PersonalizationInformation, _Mapping]] = ..., field_58: _Optional[_Union[FiraCapabilities, _Mapping]] = ..., field_59: _Optional[_Union[FiraResponse, _Mapping]] = ..., field_60: _Optional[_Union[AppStateEvent, _Mapping]] = ...) -> None: ...

class ClosureStatuses(_message.Message):
    __slots__ = ("frontDriverDoor", "frontPassengerDoor", "rearDriverDoor", "rearPassengerDoor", "rearTrunk", "frontTrunk", "chargePort", "tonneau")
    FRONTDRIVERDOOR_FIELD_NUMBER: _ClassVar[int]
    FRONTPASSENGERDOOR_FIELD_NUMBER: _ClassVar[int]
    REARDRIVERDOOR_FIELD_NUMBER: _ClassVar[int]
    REARPASSENGERDOOR_FIELD_NUMBER: _ClassVar[int]
    REARTRUNK_FIELD_NUMBER: _ClassVar[int]
    FRONTTRUNK_FIELD_NUMBER: _ClassVar[int]
    CHARGEPORT_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_FIELD_NUMBER: _ClassVar[int]
    frontDriverDoor: ClosureState_E
    frontPassengerDoor: ClosureState_E
    rearDriverDoor: ClosureState_E
    rearPassengerDoor: ClosureState_E
    rearTrunk: ClosureState_E
    frontTrunk: ClosureState_E
    chargePort: ClosureState_E
    tonneau: ClosureState_E
    def __init__(self, frontDriverDoor: _Optional[_Union[ClosureState_E, str]] = ..., frontPassengerDoor: _Optional[_Union[ClosureState_E, str]] = ..., rearDriverDoor: _Optional[_Union[ClosureState_E, str]] = ..., rearPassengerDoor: _Optional[_Union[ClosureState_E, str]] = ..., rearTrunk: _Optional[_Union[ClosureState_E, str]] = ..., frontTrunk: _Optional[_Union[ClosureState_E, str]] = ..., chargePort: _Optional[_Union[ClosureState_E, str]] = ..., tonneau: _Optional[_Union[ClosureState_E, str]] = ...) -> None: ...

class DetailedClosureStatus(_message.Message):
    __slots__ = ("tonneauPercentOpen",)
    TONNEAUPERCENTOPEN_FIELD_NUMBER: _ClassVar[int]
    tonneauPercentOpen: int
    def __init__(self, tonneauPercentOpen: _Optional[int] = ...) -> None: ...

class KeyLocationStatus(_message.Message):
    __slots__ = ("keyCloseToCenterConsoleWithHighProbability",)
    KEYCLOSETOCENTERCONSOLEWITHHIGHPROBABILITY_FIELD_NUMBER: _ClassVar[int]
    keyCloseToCenterConsoleWithHighProbability: KeyLocationStatus_E
    def __init__(self, keyCloseToCenterConsoleWithHighProbability: _Optional[_Union[KeyLocationStatus_E, str]] = ...) -> None: ...

class PersonalizationInformation(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: bytes
    def __init__(self, vin: _Optional[bytes] = ...) -> None: ...

class Capabilities(_message.Message):
    __slots__ = ("chargePortOpen", "chargePortClose")
    CHARGEPORTOPEN_FIELD_NUMBER: _ClassVar[int]
    CHARGEPORTCLOSE_FIELD_NUMBER: _ClassVar[int]
    chargePortOpen: bool
    chargePortClose: bool
    def __init__(self, chargePortOpen: _Optional[bool] = ..., chargePortClose: _Optional[bool] = ...) -> None: ...

class KeyStatus(_message.Message):
    __slots__ = ("keyId", "nfcPresence", "blePresence", "publicKey", "keyFormFactor", "slot", "role")
    KEYID_FIELD_NUMBER: _ClassVar[int]
    NFCPRESENCE_FIELD_NUMBER: _ClassVar[int]
    BLEPRESENCE_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    KEYFORMFACTOR_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    keyId: KeyIdentifier
    nfcPresence: NFCPresence
    blePresence: BLEPresence
    publicKey: PublicKey
    keyFormFactor: KeyFormFactor
    slot: int
    role: _keys_pb2.Role
    def __init__(self, keyId: _Optional[_Union[KeyIdentifier, _Mapping]] = ..., nfcPresence: _Optional[_Union[NFCPresence, str]] = ..., blePresence: _Optional[_Union[BLEPresence, str]] = ..., publicKey: _Optional[_Union[PublicKey, _Mapping]] = ..., keyFormFactor: _Optional[_Union[KeyFormFactor, str]] = ..., slot: _Optional[int] = ..., role: _Optional[_Union[_keys_pb2.Role, str]] = ...) -> None: ...

class KeyStatusInfo(_message.Message):
    __slots__ = ("keyStatuses", "requestSource", "QRCodeStatus")
    KEYSTATUSES_FIELD_NUMBER: _ClassVar[int]
    REQUESTSOURCE_FIELD_NUMBER: _ClassVar[int]
    QRCODESTATUS_FIELD_NUMBER: _ClassVar[int]
    keyStatuses: _containers.RepeatedCompositeFieldContainer[KeyStatus]
    requestSource: RequestSource_E
    QRCodeStatus: QRCodeStatus_E
    def __init__(self, keyStatuses: _Optional[_Iterable[_Union[KeyStatus, _Mapping]]] = ..., requestSource: _Optional[_Union[RequestSource_E, str]] = ..., QRCodeStatus: _Optional[_Union[QRCodeStatus_E, str]] = ...) -> None: ...

class ActiveKey(_message.Message):
    __slots__ = ("activeKey",)
    ACTIVEKEY_FIELD_NUMBER: _ClassVar[int]
    activeKey: KeyIdentifier
    def __init__(self, activeKey: _Optional[_Union[KeyIdentifier, _Mapping]] = ...) -> None: ...

class VehicleStatus(_message.Message):
    __slots__ = ("closureStatuses", "vehicleLockState", "vehicleSleepStatus", "userPresence", "detailedClosureStatus", "UIDesire", "gear", "keyLocationStatus")
    CLOSURESTATUSES_FIELD_NUMBER: _ClassVar[int]
    VEHICLELOCKSTATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLESLEEPSTATUS_FIELD_NUMBER: _ClassVar[int]
    USERPRESENCE_FIELD_NUMBER: _ClassVar[int]
    DETAILEDCLOSURESTATUS_FIELD_NUMBER: _ClassVar[int]
    UIDESIRE_FIELD_NUMBER: _ClassVar[int]
    GEAR_FIELD_NUMBER: _ClassVar[int]
    KEYLOCATIONSTATUS_FIELD_NUMBER: _ClassVar[int]
    closureStatuses: ClosureStatuses
    vehicleLockState: VehicleLockState_E
    vehicleSleepStatus: VehicleSleepStatus_E
    userPresence: UserPresence_E
    detailedClosureStatus: DetailedClosureStatus
    UIDesire: UIDesire_E
    gear: Gear_E
    keyLocationStatus: KeyLocationStatus
    def __init__(self, closureStatuses: _Optional[_Union[ClosureStatuses, _Mapping]] = ..., vehicleLockState: _Optional[_Union[VehicleLockState_E, str]] = ..., vehicleSleepStatus: _Optional[_Union[VehicleSleepStatus_E, str]] = ..., userPresence: _Optional[_Union[UserPresence_E, str]] = ..., detailedClosureStatus: _Optional[_Union[DetailedClosureStatus, _Mapping]] = ..., UIDesire: _Optional[_Union[UIDesire_E, str]] = ..., gear: _Optional[_Union[Gear_E, str]] = ..., keyLocationStatus: _Optional[_Union[KeyLocationStatus, _Mapping]] = ...) -> None: ...

class FromVCSECMessage(_message.Message):
    __slots__ = ("vehicleStatus", "authenticationRequest", "commandStatus", "personalizationInformation", "whitelistInfo", "whitelistEntryInfo", "capabilities", "keyStatusInfo", "activeKey", "nominalError", "sessionInfo", "unknownKeyInfo", "genealogyRequest", "imuRequest", "unsecureNotification", "epochSessionInfo", "appDeviceInfoRequest", "alert", "NISessionRequest", "NISessionStop", "NIBatchRequest", "CPDMessage", "NIStatusUpdate")
    VEHICLESTATUS_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATIONREQUEST_FIELD_NUMBER: _ClassVar[int]
    COMMANDSTATUS_FIELD_NUMBER: _ClassVar[int]
    PERSONALIZATIONINFORMATION_FIELD_NUMBER: _ClassVar[int]
    WHITELISTINFO_FIELD_NUMBER: _ClassVar[int]
    WHITELISTENTRYINFO_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    KEYSTATUSINFO_FIELD_NUMBER: _ClassVar[int]
    ACTIVEKEY_FIELD_NUMBER: _ClassVar[int]
    NOMINALERROR_FIELD_NUMBER: _ClassVar[int]
    SESSIONINFO_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNKEYINFO_FIELD_NUMBER: _ClassVar[int]
    GENEALOGYREQUEST_FIELD_NUMBER: _ClassVar[int]
    IMUREQUEST_FIELD_NUMBER: _ClassVar[int]
    UNSECURENOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    EPOCHSESSIONINFO_FIELD_NUMBER: _ClassVar[int]
    APPDEVICEINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    NISESSIONREQUEST_FIELD_NUMBER: _ClassVar[int]
    NISESSIONSTOP_FIELD_NUMBER: _ClassVar[int]
    NIBATCHREQUEST_FIELD_NUMBER: _ClassVar[int]
    CPDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    NISTATUSUPDATE_FIELD_NUMBER: _ClassVar[int]
    vehicleStatus: VehicleStatus
    authenticationRequest: AuthenticationRequest
    commandStatus: CommandStatus
    personalizationInformation: PersonalizationInformation
    whitelistInfo: WhitelistInfo
    whitelistEntryInfo: WhitelistEntryInfo
    capabilities: Capabilities
    keyStatusInfo: KeyStatusInfo
    activeKey: ActiveKey
    nominalError: _errors_pb2.NominalError
    sessionInfo: SessionInfo
    unknownKeyInfo: UnknownKeyInfo
    genealogyRequest: GenealogyRequest_E
    imuRequest: IMURequest_E
    unsecureNotification: UnsecureNotification
    epochSessionInfo: _signatures_pb2.SessionInfo
    appDeviceInfoRequest: AppDeviceInfoRequest_E
    alert: Alert
    NISessionRequest: NISessionRequest
    NISessionStop: NISessionStop
    NIBatchRequest: NIBatchRequest
    CPDMessage: CPDMessage
    NIStatusUpdate: NIStatusUpdate
    def __init__(self, vehicleStatus: _Optional[_Union[VehicleStatus, _Mapping]] = ..., authenticationRequest: _Optional[_Union[AuthenticationRequest, _Mapping]] = ..., commandStatus: _Optional[_Union[CommandStatus, _Mapping]] = ..., personalizationInformation: _Optional[_Union[PersonalizationInformation, _Mapping]] = ..., whitelistInfo: _Optional[_Union[WhitelistInfo, _Mapping]] = ..., whitelistEntryInfo: _Optional[_Union[WhitelistEntryInfo, _Mapping]] = ..., capabilities: _Optional[_Union[Capabilities, _Mapping]] = ..., keyStatusInfo: _Optional[_Union[KeyStatusInfo, _Mapping]] = ..., activeKey: _Optional[_Union[ActiveKey, _Mapping]] = ..., nominalError: _Optional[_Union[_errors_pb2.NominalError, _Mapping]] = ..., sessionInfo: _Optional[_Union[SessionInfo, _Mapping]] = ..., unknownKeyInfo: _Optional[_Union[UnknownKeyInfo, _Mapping]] = ..., genealogyRequest: _Optional[_Union[GenealogyRequest_E, str]] = ..., imuRequest: _Optional[_Union[IMURequest_E, str]] = ..., unsecureNotification: _Optional[_Union[UnsecureNotification, _Mapping]] = ..., epochSessionInfo: _Optional[_Union[_signatures_pb2.SessionInfo, _Mapping]] = ..., appDeviceInfoRequest: _Optional[_Union[AppDeviceInfoRequest_E, str]] = ..., alert: _Optional[_Union[Alert, _Mapping]] = ..., NISessionRequest: _Optional[_Union[NISessionRequest, _Mapping]] = ..., NISessionStop: _Optional[_Union[NISessionStop, _Mapping]] = ..., NIBatchRequest: _Optional[_Union[NIBatchRequest, _Mapping]] = ..., CPDMessage: _Optional[_Union[CPDMessage, _Mapping]] = ..., NIStatusUpdate: _Optional[_Union[NIStatusUpdate, _Mapping]] = ...) -> None: ...

class Alert(_message.Message):
    __slots__ = ("alertHandlePulledWithoutAuth", "alertConfirmation")
    ALERTHANDLEPULLEDWITHOUTAUTH_FIELD_NUMBER: _ClassVar[int]
    ALERTCONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    alertHandlePulledWithoutAuth: AlertHandlePulledWithoutAuth
    alertConfirmation: AlertConfirmation
    def __init__(self, alertHandlePulledWithoutAuth: _Optional[_Union[AlertHandlePulledWithoutAuth, _Mapping]] = ..., alertConfirmation: _Optional[_Union[AlertConfirmation, str]] = ...) -> None: ...

class AlertHandlePulledWithoutAuth(_message.Message):
    __slots__ = ("timeSinceAlertSet_ms", "handlePulled", "connectionCount", "unknownDevicePresent", "authRequested", "deviceSpecificPayload")
    TIMESINCEALERTSET_MS_FIELD_NUMBER: _ClassVar[int]
    HANDLEPULLED_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNDEVICEPRESENT_FIELD_NUMBER: _ClassVar[int]
    AUTHREQUESTED_FIELD_NUMBER: _ClassVar[int]
    DEVICESPECIFICPAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timeSinceAlertSet_ms: int
    handlePulled: HandlePulled_E
    connectionCount: int
    unknownDevicePresent: bool
    authRequested: bool
    deviceSpecificPayload: _containers.RepeatedCompositeFieldContainer[HandlePulledWithoutAuthDeviceSpecificPayload]
    def __init__(self, timeSinceAlertSet_ms: _Optional[int] = ..., handlePulled: _Optional[_Union[HandlePulled_E, str]] = ..., connectionCount: _Optional[int] = ..., unknownDevicePresent: _Optional[bool] = ..., authRequested: _Optional[bool] = ..., deviceSpecificPayload: _Optional[_Iterable[_Union[HandlePulledWithoutAuthDeviceSpecificPayload, _Mapping]]] = ...) -> None: ...

class AppDeviceInfo(_message.Message):
    __slots__ = ("hardware_model_sha256", "os", "UWBAvailable", "phoneVersion", "batchedNISessionsSupported", "batteryLevelPercent", "batteryState", "thermalState", "lowPowerMode")
    HARDWARE_MODEL_SHA256_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    UWBAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PHONEVERSION_FIELD_NUMBER: _ClassVar[int]
    BATCHEDNISESSIONSSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BATTERYLEVELPERCENT_FIELD_NUMBER: _ClassVar[int]
    BATTERYSTATE_FIELD_NUMBER: _ClassVar[int]
    THERMALSTATE_FIELD_NUMBER: _ClassVar[int]
    LOWPOWERMODE_FIELD_NUMBER: _ClassVar[int]
    hardware_model_sha256: bytes
    os: AppOperatingSystem
    UWBAvailable: UWBAvailability
    phoneVersion: PhoneVersionInfo
    batchedNISessionsSupported: bool
    batteryLevelPercent: int
    batteryState: BatteryState_E
    thermalState: PhoneThermalState_E
    lowPowerMode: bool
    def __init__(self, hardware_model_sha256: _Optional[bytes] = ..., os: _Optional[_Union[AppOperatingSystem, str]] = ..., UWBAvailable: _Optional[_Union[UWBAvailability, str]] = ..., phoneVersion: _Optional[_Union[PhoneVersionInfo, _Mapping]] = ..., batchedNISessionsSupported: _Optional[bool] = ..., batteryLevelPercent: _Optional[int] = ..., batteryState: _Optional[_Union[BatteryState_E, str]] = ..., thermalState: _Optional[_Union[PhoneThermalState_E, str]] = ..., lowPowerMode: _Optional[bool] = ...) -> None: ...

class AppEventBondingStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AppEventLog(_message.Message):
    __slots__ = ("timestamp", "peerRemovedPairingInformation", "phoneLogForHandlePulledWithoutAuthentication", "bondingStarted")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PEERREMOVEDPAIRINGINFORMATION_FIELD_NUMBER: _ClassVar[int]
    PHONELOGFORHANDLEPULLEDWITHOUTAUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    BONDINGSTARTED_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    peerRemovedPairingInformation: AppEventPeerRemovedPairingInformation
    phoneLogForHandlePulledWithoutAuthentication: PhoneLogForHandlePulledWithoutAuthentication
    bondingStarted: AppEventBondingStarted
    def __init__(self, timestamp: _Optional[int] = ..., peerRemovedPairingInformation: _Optional[_Union[AppEventPeerRemovedPairingInformation, _Mapping]] = ..., phoneLogForHandlePulledWithoutAuthentication: _Optional[_Union[PhoneLogForHandlePulledWithoutAuthentication, _Mapping]] = ..., bondingStarted: _Optional[_Union[AppEventBondingStarted, _Mapping]] = ...) -> None: ...

class AppEventPeerRemovedPairingInformation(_message.Message):
    __slots__ = ("keyId",)
    KEYID_FIELD_NUMBER: _ClassVar[int]
    keyId: KeyIdentifier
    def __init__(self, keyId: _Optional[_Union[KeyIdentifier, _Mapping]] = ...) -> None: ...

class AppStateEvent(_message.Message):
    __slots__ = ("field_1",)
    FIELD_1_FIELD_NUMBER: _ClassVar[int]
    field_1: WatchAppStateEvent
    def __init__(self, field_1: _Optional[_Union[WatchAppStateEvent, _Mapping]] = ...) -> None: ...

class CPDMessage(_message.Message):
    __slots__ = ("CPDNotification",)
    CPDNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    CPDNotification: CPDNotification_E
    def __init__(self, CPDNotification: _Optional[_Union[CPDNotification_E, str]] = ...) -> None: ...

class CPDResponse(_message.Message):
    __slots__ = ("CPDNotificationResponse",)
    CPDNOTIFICATIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CPDNotificationResponse: CPDNotificationResponse_E
    def __init__(self, CPDNotificationResponse: _Optional[_Union[CPDNotificationResponse_E, str]] = ...) -> None: ...

class ChangeOperationMode(_message.Message):
    __slots__ = ("operationMode",)
    OPERATIONMODE_FIELD_NUMBER: _ClassVar[int]
    operationMode: OperationMode_E
    def __init__(self, operationMode: _Optional[_Union[OperationMode_E, str]] = ...) -> None: ...

class CodeDescriptor(_message.Message):
    __slots__ = ("codeDescriptorLocation", "version", "codeDescriptorBytes")
    CODEDESCRIPTORLOCATION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CODEDESCRIPTORBYTES_FIELD_NUMBER: _ClassVar[int]
    codeDescriptorLocation: UpdaterLocation
    version: int
    codeDescriptorBytes: bytes
    def __init__(self, codeDescriptorLocation: _Optional[_Union[UpdaterLocation, str]] = ..., version: _Optional[int] = ..., codeDescriptorBytes: _Optional[bytes] = ...) -> None: ...

class DelaySleepRequest(_message.Message):
    __slots__ = ("delayTime_ms",)
    DELAYTIME_MS_FIELD_NUMBER: _ClassVar[int]
    delayTime_ms: int
    def __init__(self, delayTime_ms: _Optional[int] = ...) -> None: ...

class DeviceMotion(_message.Message):
    __slots__ = ("states", "confidence")
    STATES_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedScalarFieldContainer[Device_Motion_State]
    confidence: Device_Motion_Confidence
    def __init__(self, states: _Optional[_Iterable[_Union[Device_Motion_State, str]]] = ..., confidence: _Optional[_Union[Device_Motion_Confidence, str]] = ...) -> None: ...

class FiraCapabilities(_message.Message):
    __slots__ = ("field_1", "field_2", "field_3", "field_4", "field_5", "field_6", "field_7")
    FIELD_1_FIELD_NUMBER: _ClassVar[int]
    FIELD_2_FIELD_NUMBER: _ClassVar[int]
    FIELD_3_FIELD_NUMBER: _ClassVar[int]
    FIELD_4_FIELD_NUMBER: _ClassVar[int]
    FIELD_5_FIELD_NUMBER: _ClassVar[int]
    FIELD_6_FIELD_NUMBER: _ClassVar[int]
    FIELD_7_FIELD_NUMBER: _ClassVar[int]
    field_1: int
    field_2: int
    field_3: int
    field_4: int
    field_5: _containers.RepeatedScalarFieldContainer[int]
    field_6: int
    field_7: bool
    def __init__(self, field_1: _Optional[int] = ..., field_2: _Optional[int] = ..., field_3: _Optional[int] = ..., field_4: _Optional[int] = ..., field_5: _Optional[_Iterable[int]] = ..., field_6: _Optional[int] = ..., field_7: _Optional[bool] = ...) -> None: ...

class FiraRequest(_message.Message):
    __slots__ = ("field_1",)
    FIELD_1_FIELD_NUMBER: _ClassVar[int]
    field_1: _containers.RepeatedCompositeFieldContainer[FiraSessionRequest]
    def __init__(self, field_1: _Optional[_Iterable[_Union[FiraSessionRequest, _Mapping]]] = ...) -> None: ...

class FiraResponse(_message.Message):
    __slots__ = ("field_1", "field_2", "field_3")
    FIELD_1_FIELD_NUMBER: _ClassVar[int]
    FIELD_2_FIELD_NUMBER: _ClassVar[int]
    FIELD_3_FIELD_NUMBER: _ClassVar[int]
    field_1: _containers.RepeatedCompositeFieldContainer[FiraSessionResponse]
    field_2: int
    field_3: KeyIdentifier
    def __init__(self, field_1: _Optional[_Iterable[_Union[FiraSessionResponse, _Mapping]]] = ..., field_2: _Optional[int] = ..., field_3: _Optional[_Union[KeyIdentifier, _Mapping]] = ...) -> None: ...

class FiraSessionData(_message.Message):
    __slots__ = ("field_1", "field_2", "field_3", "field_4", "field_5", "field_6")
    FIELD_1_FIELD_NUMBER: _ClassVar[int]
    FIELD_2_FIELD_NUMBER: _ClassVar[int]
    FIELD_3_FIELD_NUMBER: _ClassVar[int]
    FIELD_4_FIELD_NUMBER: _ClassVar[int]
    FIELD_5_FIELD_NUMBER: _ClassVar[int]
    FIELD_6_FIELD_NUMBER: _ClassVar[int]
    field_1: bytes
    field_2: int
    field_3: int
    field_4: int
    field_5: bytes
    field_6: bytes
    def __init__(self, field_1: _Optional[bytes] = ..., field_2: _Optional[int] = ..., field_3: _Optional[int] = ..., field_4: _Optional[int] = ..., field_5: _Optional[bytes] = ..., field_6: _Optional[bytes] = ...) -> None: ...

class FiraSessionRequest(_message.Message):
    __slots__ = ("field_1", "field_2", "field_3", "field_5", "field_6", "field_7", "field_8", "field_9", "field_10")
    FIELD_1_FIELD_NUMBER: _ClassVar[int]
    FIELD_2_FIELD_NUMBER: _ClassVar[int]
    FIELD_3_FIELD_NUMBER: _ClassVar[int]
    FIELD_5_FIELD_NUMBER: _ClassVar[int]
    FIELD_6_FIELD_NUMBER: _ClassVar[int]
    FIELD_7_FIELD_NUMBER: _ClassVar[int]
    FIELD_8_FIELD_NUMBER: _ClassVar[int]
    FIELD_9_FIELD_NUMBER: _ClassVar[int]
    FIELD_10_FIELD_NUMBER: _ClassVar[int]
    field_1: int
    field_2: FiraRangingType
    field_3: bytes
    field_5: int
    field_6: int
    field_7: FiraSTSMode
    field_8: bytes
    field_9: RangingUpdateRate
    field_10: int
    def __init__(self, field_1: _Optional[int] = ..., field_2: _Optional[_Union[FiraRangingType, str]] = ..., field_3: _Optional[bytes] = ..., field_5: _Optional[int] = ..., field_6: _Optional[int] = ..., field_7: _Optional[_Union[FiraSTSMode, str]] = ..., field_8: _Optional[bytes] = ..., field_9: _Optional[_Union[RangingUpdateRate, str]] = ..., field_10: _Optional[int] = ...) -> None: ...

class FiraSessionResponse(_message.Message):
    __slots__ = ("field_1", "field_2", "field_3")
    FIELD_1_FIELD_NUMBER: _ClassVar[int]
    FIELD_2_FIELD_NUMBER: _ClassVar[int]
    FIELD_3_FIELD_NUMBER: _ClassVar[int]
    field_1: int
    field_2: FiraSessionData
    field_3: FiraError_E
    def __init__(self, field_1: _Optional[int] = ..., field_2: _Optional[_Union[FiraSessionData, _Mapping]] = ..., field_3: _Optional[_Union[FiraError_E, str]] = ...) -> None: ...

class FirmwareInfo(_message.Message):
    __slots__ = ("deviceTarget", "versionCounter")
    DEVICETARGET_FIELD_NUMBER: _ClassVar[int]
    VERSIONCOUNTER_FIELD_NUMBER: _ClassVar[int]
    deviceTarget: DeviceTarget
    versionCounter: int
    def __init__(self, deviceTarget: _Optional[_Union[DeviceTarget, str]] = ..., versionCounter: _Optional[int] = ...) -> None: ...

class FromUIMessage(_message.Message):
    __slots__ = ("unsignedMessage",)
    UNSIGNEDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    unsignedMessage: UnsignedMessageUI
    def __init__(self, unsignedMessage: _Optional[_Union[UnsignedMessageUI, _Mapping]] = ...) -> None: ...

class FromVCSECMessage_ResponseMessage(_message.Message):
    __slots__ = ("nominalError",)
    NOMINALERROR_FIELD_NUMBER: _ClassVar[int]
    nominalError: _errors_pb2.NominalError
    def __init__(self, nominalError: _Optional[_Union[_errors_pb2.NominalError, _Mapping]] = ...) -> None: ...

class Genealogy(_message.Message):
    __slots__ = ("serialNumber", "partNumber")
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    PARTNUMBER_FIELD_NUMBER: _ClassVar[int]
    serialNumber: bytes
    partNumber: bytes
    def __init__(self, serialNumber: _Optional[bytes] = ..., partNumber: _Optional[bytes] = ...) -> None: ...

class GenealogyResponse(_message.Message):
    __slots__ = ("currentGenealogy", "status")
    CURRENTGENEALOGY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    currentGenealogy: Genealogy
    status: GenealogyStatus_E
    def __init__(self, currentGenealogy: _Optional[_Union[Genealogy, _Mapping]] = ..., status: _Optional[_Union[GenealogyStatus_E, str]] = ...) -> None: ...

class GetCodeDescriptor(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: UpdaterLocation
    def __init__(self, location: _Optional[_Union[UpdaterLocation, str]] = ...) -> None: ...

class GetReaderKey(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: GetReaderKeyCommand
    def __init__(self, command: _Optional[_Union[GetReaderKeyCommand, str]] = ...) -> None: ...

class HandlePulledWithoutAuthDeviceSpecificPayload(_message.Message):
    __slots__ = ("keyChannel", "authenticationLevel", "present", "RSSILeft", "RSSIRight", "RSSIRear", "RSSICenter", "RSSIFront", "RSSISecondary", "RSSINFCCradle", "RSSIRearLeft", "RSSIRearRight", "highThreshLeftPresent", "highThreshRightPresent", "highThreshCenterPresent", "highThreshFrontPresent", "highThreshRearPresent", "highThreshRearLeftPresent", "highThreshRearRightPresent", "highThreshSecondaryPresent", "highThreshNFCPresent", "sortedDeltaBayesLeftPresent", "sortedDeltaBayesRightPresent", "rawDeltaBayesLeftPresent", "rawDeltaBayesRightPresent")
    KEYCHANNEL_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATIONLEVEL_FIELD_NUMBER: _ClassVar[int]
    PRESENT_FIELD_NUMBER: _ClassVar[int]
    RSSILEFT_FIELD_NUMBER: _ClassVar[int]
    RSSIRIGHT_FIELD_NUMBER: _ClassVar[int]
    RSSIREAR_FIELD_NUMBER: _ClassVar[int]
    RSSICENTER_FIELD_NUMBER: _ClassVar[int]
    RSSIFRONT_FIELD_NUMBER: _ClassVar[int]
    RSSISECONDARY_FIELD_NUMBER: _ClassVar[int]
    RSSINFCCRADLE_FIELD_NUMBER: _ClassVar[int]
    RSSIREARLEFT_FIELD_NUMBER: _ClassVar[int]
    RSSIREARRIGHT_FIELD_NUMBER: _ClassVar[int]
    HIGHTHRESHLEFTPRESENT_FIELD_NUMBER: _ClassVar[int]
    HIGHTHRESHRIGHTPRESENT_FIELD_NUMBER: _ClassVar[int]
    HIGHTHRESHCENTERPRESENT_FIELD_NUMBER: _ClassVar[int]
    HIGHTHRESHFRONTPRESENT_FIELD_NUMBER: _ClassVar[int]
    HIGHTHRESHREARPRESENT_FIELD_NUMBER: _ClassVar[int]
    HIGHTHRESHREARLEFTPRESENT_FIELD_NUMBER: _ClassVar[int]
    HIGHTHRESHREARRIGHTPRESENT_FIELD_NUMBER: _ClassVar[int]
    HIGHTHRESHSECONDARYPRESENT_FIELD_NUMBER: _ClassVar[int]
    HIGHTHRESHNFCPRESENT_FIELD_NUMBER: _ClassVar[int]
    SORTEDDELTABAYESLEFTPRESENT_FIELD_NUMBER: _ClassVar[int]
    SORTEDDELTABAYESRIGHTPRESENT_FIELD_NUMBER: _ClassVar[int]
    RAWDELTABAYESLEFTPRESENT_FIELD_NUMBER: _ClassVar[int]
    RAWDELTABAYESRIGHTPRESENT_FIELD_NUMBER: _ClassVar[int]
    keyChannel: int
    authenticationLevel: AuthenticationLevel_E
    present: bool
    RSSILeft: int
    RSSIRight: int
    RSSIRear: int
    RSSICenter: int
    RSSIFront: int
    RSSISecondary: int
    RSSINFCCradle: int
    RSSIRearLeft: int
    RSSIRearRight: int
    highThreshLeftPresent: bool
    highThreshRightPresent: bool
    highThreshCenterPresent: bool
    highThreshFrontPresent: bool
    highThreshRearPresent: bool
    highThreshRearLeftPresent: bool
    highThreshRearRightPresent: bool
    highThreshSecondaryPresent: bool
    highThreshNFCPresent: bool
    sortedDeltaBayesLeftPresent: bool
    sortedDeltaBayesRightPresent: bool
    rawDeltaBayesLeftPresent: bool
    rawDeltaBayesRightPresent: bool
    def __init__(self, keyChannel: _Optional[int] = ..., authenticationLevel: _Optional[_Union[AuthenticationLevel_E, str]] = ..., present: _Optional[bool] = ..., RSSILeft: _Optional[int] = ..., RSSIRight: _Optional[int] = ..., RSSIRear: _Optional[int] = ..., RSSICenter: _Optional[int] = ..., RSSIFront: _Optional[int] = ..., RSSISecondary: _Optional[int] = ..., RSSINFCCradle: _Optional[int] = ..., RSSIRearLeft: _Optional[int] = ..., RSSIRearRight: _Optional[int] = ..., highThreshLeftPresent: _Optional[bool] = ..., highThreshRightPresent: _Optional[bool] = ..., highThreshCenterPresent: _Optional[bool] = ..., highThreshFrontPresent: _Optional[bool] = ..., highThreshRearPresent: _Optional[bool] = ..., highThreshRearLeftPresent: _Optional[bool] = ..., highThreshRearRightPresent: _Optional[bool] = ..., highThreshSecondaryPresent: _Optional[bool] = ..., highThreshNFCPresent: _Optional[bool] = ..., sortedDeltaBayesLeftPresent: _Optional[bool] = ..., sortedDeltaBayesRightPresent: _Optional[bool] = ..., rawDeltaBayesLeftPresent: _Optional[bool] = ..., rawDeltaBayesRightPresent: _Optional[bool] = ...) -> None: ...

class NIBatchRequest(_message.Message):
    __slots__ = ("requests",)
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[NISessionRequest]
    def __init__(self, requests: _Optional[_Iterable[_Union[NISessionRequest, _Mapping]]] = ...) -> None: ...

class NIBatchResponse(_message.Message):
    __slots__ = ("responses", "keyId", "field_3", "field_4")
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    KEYID_FIELD_NUMBER: _ClassVar[int]
    FIELD_3_FIELD_NUMBER: _ClassVar[int]
    FIELD_4_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[NISessionResponse]
    keyId: KeyIdentifier
    field_3: int
    field_4: RangingConfigType_E
    def __init__(self, responses: _Optional[_Iterable[_Union[NISessionResponse, _Mapping]]] = ..., keyId: _Optional[_Union[KeyIdentifier, _Mapping]] = ..., field_3: _Optional[int] = ..., field_4: _Optional[_Union[RangingConfigType_E, str]] = ...) -> None: ...

class NIConfigurationData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class NISessionRequest(_message.Message):
    __slots__ = ("sessionId", "accessoryConfigurationData")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    ACCESSORYCONFIGURATIONDATA_FIELD_NUMBER: _ClassVar[int]
    sessionId: BLEEndpoint_E
    accessoryConfigurationData: bytes
    def __init__(self, sessionId: _Optional[_Union[BLEEndpoint_E, str]] = ..., accessoryConfigurationData: _Optional[bytes] = ...) -> None: ...

class NISessionResponse(_message.Message):
    __slots__ = ("sessionId", "NIConfigurationData", "errorCode")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    NICONFIGURATIONDATA_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    sessionId: BLEEndpoint_E
    NIConfigurationData: NIConfigurationData
    errorCode: NIError_E
    def __init__(self, sessionId: _Optional[_Union[BLEEndpoint_E, str]] = ..., NIConfigurationData: _Optional[_Union[NIConfigurationData, _Mapping]] = ..., errorCode: _Optional[_Union[NIError_E, str]] = ...) -> None: ...

class NISessionStatus(_message.Message):
    __slots__ = ("sessionId", "status")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    sessionId: BLEEndpoint_E
    status: NISessionStatus_E
    def __init__(self, sessionId: _Optional[_Union[BLEEndpoint_E, str]] = ..., status: _Optional[_Union[NISessionStatus_E, str]] = ...) -> None: ...

class NISessionStop(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: _containers.RepeatedScalarFieldContainer[BLEEndpoint_E]
    def __init__(self, sessionId: _Optional[_Iterable[_Union[BLEEndpoint_E, str]]] = ...) -> None: ...

class NISessionStopped(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: _containers.RepeatedScalarFieldContainer[BLEEndpoint_E]
    def __init__(self, sessionId: _Optional[_Iterable[_Union[BLEEndpoint_E, str]]] = ...) -> None: ...

class NIStatusUpdate(_message.Message):
    __slots__ = ("sessionStatus",)
    SESSIONSTATUS_FIELD_NUMBER: _ClassVar[int]
    sessionStatus: _containers.RepeatedCompositeFieldContainer[NISessionStatus]
    def __init__(self, sessionStatus: _Optional[_Iterable[_Union[NISessionStatus, _Mapping]]] = ...) -> None: ...

class PhoneKeyTelemetry_Android(_message.Message):
    __slots__ = ("permissionsBitmask", "serviceRunningState", "runningState_timeSince_S", "processStartTime_timeSince_S", "osStartTime_timeSince_S", "screenOnReceiver_timeSince_S", "bootReceiver_timeSince_S", "serviceStartReason")
    class PhoneKeyPermissionsBitfield(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLUETOOTH_SCAN: _ClassVar[PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield]
        BLUETOOTH_CONNECT: _ClassVar[PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield]
        ACCESS_FINE_LOCATION: _ClassVar[PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield]
        LEGACY_BLUETOOTH: _ClassVar[PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield]
        LEGACY_BLUETOOTH_ADMIN: _ClassVar[PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield]
        UWB_RANGING: _ClassVar[PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield]
        BATTERY_OPTIMIZATION: _ClassVar[PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield]
        IMU_ENABLED: _ClassVar[PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield]
    BLUETOOTH_SCAN: PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield
    BLUETOOTH_CONNECT: PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield
    ACCESS_FINE_LOCATION: PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield
    LEGACY_BLUETOOTH: PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield
    LEGACY_BLUETOOTH_ADMIN: PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield
    UWB_RANGING: PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield
    BATTERY_OPTIMIZATION: PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield
    IMU_ENABLED: PhoneKeyTelemetry_Android.PhoneKeyPermissionsBitfield
    class ServiceRunningState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVICERUNNINGSTATE_SNA: _ClassVar[PhoneKeyTelemetry_Android.ServiceRunningState]
        SERVICERUNNINGSTATE_BACKGROUND: _ClassVar[PhoneKeyTelemetry_Android.ServiceRunningState]
        SERVICERUNNINGSTATE_FOREGROUND: _ClassVar[PhoneKeyTelemetry_Android.ServiceRunningState]
        SERVICERUNNINGSTATE_OFF: _ClassVar[PhoneKeyTelemetry_Android.ServiceRunningState]
    SERVICERUNNINGSTATE_SNA: PhoneKeyTelemetry_Android.ServiceRunningState
    SERVICERUNNINGSTATE_BACKGROUND: PhoneKeyTelemetry_Android.ServiceRunningState
    SERVICERUNNINGSTATE_FOREGROUND: PhoneKeyTelemetry_Android.ServiceRunningState
    SERVICERUNNINGSTATE_OFF: PhoneKeyTelemetry_Android.ServiceRunningState
    class ServiceStartReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVICE_START_REASON_SNA: _ClassVar[PhoneKeyTelemetry_Android.ServiceStartReason]
        SERVICE_START_REASON_JS: _ClassVar[PhoneKeyTelemetry_Android.ServiceStartReason]
        SERVICE_START_REASON_BOOT_COMPLETE: _ClassVar[PhoneKeyTelemetry_Android.ServiceStartReason]
        SERVICE_START_REASON_MI_BEACON: _ClassVar[PhoneKeyTelemetry_Android.ServiceStartReason]
        SERVICE_START_REASON_HONOR_WALLET: _ClassVar[PhoneKeyTelemetry_Android.ServiceStartReason]
        SERVICE_START_REASON_OPPO_WALLET: _ClassVar[PhoneKeyTelemetry_Android.ServiceStartReason]
        SERVICE_START_REASON_VIVO_WALLET: _ClassVar[PhoneKeyTelemetry_Android.ServiceStartReason]
        SERVICE_START_REASON_PACKAGE_REPLACED: _ClassVar[PhoneKeyTelemetry_Android.ServiceStartReason]
    SERVICE_START_REASON_SNA: PhoneKeyTelemetry_Android.ServiceStartReason
    SERVICE_START_REASON_JS: PhoneKeyTelemetry_Android.ServiceStartReason
    SERVICE_START_REASON_BOOT_COMPLETE: PhoneKeyTelemetry_Android.ServiceStartReason
    SERVICE_START_REASON_MI_BEACON: PhoneKeyTelemetry_Android.ServiceStartReason
    SERVICE_START_REASON_HONOR_WALLET: PhoneKeyTelemetry_Android.ServiceStartReason
    SERVICE_START_REASON_OPPO_WALLET: PhoneKeyTelemetry_Android.ServiceStartReason
    SERVICE_START_REASON_VIVO_WALLET: PhoneKeyTelemetry_Android.ServiceStartReason
    SERVICE_START_REASON_PACKAGE_REPLACED: PhoneKeyTelemetry_Android.ServiceStartReason
    PERMISSIONSBITMASK_FIELD_NUMBER: _ClassVar[int]
    SERVICERUNNINGSTATE_FIELD_NUMBER: _ClassVar[int]
    RUNNINGSTATE_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    PROCESSSTARTTIME_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    OSSTARTTIME_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    SCREENONRECEIVER_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    BOOTRECEIVER_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    SERVICESTARTREASON_FIELD_NUMBER: _ClassVar[int]
    permissionsBitmask: int
    serviceRunningState: PhoneKeyTelemetry_Android.ServiceRunningState
    runningState_timeSince_S: int
    processStartTime_timeSince_S: int
    osStartTime_timeSince_S: int
    screenOnReceiver_timeSince_S: int
    bootReceiver_timeSince_S: int
    serviceStartReason: PhoneKeyTelemetry_Android.ServiceStartReason
    def __init__(self, permissionsBitmask: _Optional[int] = ..., serviceRunningState: _Optional[_Union[PhoneKeyTelemetry_Android.ServiceRunningState, str]] = ..., runningState_timeSince_S: _Optional[int] = ..., processStartTime_timeSince_S: _Optional[int] = ..., osStartTime_timeSince_S: _Optional[int] = ..., screenOnReceiver_timeSince_S: _Optional[int] = ..., bootReceiver_timeSince_S: _Optional[int] = ..., serviceStartReason: _Optional[_Union[PhoneKeyTelemetry_Android.ServiceStartReason, str]] = ...) -> None: ...

class PhoneKeyTelemetry_iOS(_message.Message):
    __slots__ = ("iBeaconState", "iBeaconState_timeSince_S", "CBManagerState", "CBManagerState_timeSince_S", "CBManagerAuthorization", "CBManagerAuthorization_timeSince_S", "CoreBTError", "CoreBTError_timeSince_S", "CoreBTATTErrorCode", "CoreBTATTError_timeSince_S", "launchReason", "launchReason_timeSince_S", "appState")
    IBEACONSTATE_FIELD_NUMBER: _ClassVar[int]
    IBEACONSTATE_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    CBMANAGERSTATE_FIELD_NUMBER: _ClassVar[int]
    CBMANAGERSTATE_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    CBMANAGERAUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    CBMANAGERAUTHORIZATION_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    COREBTERROR_FIELD_NUMBER: _ClassVar[int]
    COREBTERROR_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    COREBTATTERRORCODE_FIELD_NUMBER: _ClassVar[int]
    COREBTATTERROR_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    LAUNCHREASON_FIELD_NUMBER: _ClassVar[int]
    LAUNCHREASON_TIMESINCE_S_FIELD_NUMBER: _ClassVar[int]
    APPSTATE_FIELD_NUMBER: _ClassVar[int]
    iBeaconState: iBeaconState
    iBeaconState_timeSince_S: int
    CBManagerState: CBManagerState
    CBManagerState_timeSince_S: int
    CBManagerAuthorization: CBManagerAuthorization
    CBManagerAuthorization_timeSince_S: int
    CoreBTError: iOS_CoreBTError
    CoreBTError_timeSince_S: int
    CoreBTATTErrorCode: iOS_CoreBTATTErrorCode
    CoreBTATTError_timeSince_S: int
    launchReason: iOS_LaunchReason
    launchReason_timeSince_S: int
    appState: iOS_AppState
    def __init__(self, iBeaconState: _Optional[_Union[iBeaconState, str]] = ..., iBeaconState_timeSince_S: _Optional[int] = ..., CBManagerState: _Optional[_Union[CBManagerState, str]] = ..., CBManagerState_timeSince_S: _Optional[int] = ..., CBManagerAuthorization: _Optional[_Union[CBManagerAuthorization, str]] = ..., CBManagerAuthorization_timeSince_S: _Optional[int] = ..., CoreBTError: _Optional[_Union[iOS_CoreBTError, str]] = ..., CoreBTError_timeSince_S: _Optional[int] = ..., CoreBTATTErrorCode: _Optional[_Union[iOS_CoreBTATTErrorCode, str]] = ..., CoreBTATTError_timeSince_S: _Optional[int] = ..., launchReason: _Optional[_Union[iOS_LaunchReason, str]] = ..., launchReason_timeSince_S: _Optional[int] = ..., appState: _Optional[_Union[iOS_AppState, str]] = ...) -> None: ...

class PhoneLogForHandlePulledWithoutAuthentication(_message.Message):
    __slots__ = ("timeSinceBLESwitchEnableInSeconds", "timeSinceAppLaunchInSeconds", "timeSinceBeaconInSeconds", "timeSinceConnectInSeconds", "timeSinceForegroundInSeconds", "timeSinceBackgroundInSeconds", "locationPermission", "remoteStartIssued", "peripheralState", "GATTDiscoveryBitmask", "timeSinceLastMessageCurrentSession", "timeSinceLastMessageAckCurrentSession", "iOS", "android")
    TIMESINCEBLESWITCHENABLEINSECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMESINCEAPPLAUNCHINSECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMESINCEBEACONINSECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMESINCECONNECTINSECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMESINCEFOREGROUNDINSECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMESINCEBACKGROUNDINSECONDS_FIELD_NUMBER: _ClassVar[int]
    LOCATIONPERMISSION_FIELD_NUMBER: _ClassVar[int]
    REMOTESTARTISSUED_FIELD_NUMBER: _ClassVar[int]
    PERIPHERALSTATE_FIELD_NUMBER: _ClassVar[int]
    GATTDISCOVERYBITMASK_FIELD_NUMBER: _ClassVar[int]
    TIMESINCELASTMESSAGECURRENTSESSION_FIELD_NUMBER: _ClassVar[int]
    TIMESINCELASTMESSAGEACKCURRENTSESSION_FIELD_NUMBER: _ClassVar[int]
    IOS_FIELD_NUMBER: _ClassVar[int]
    ANDROID_FIELD_NUMBER: _ClassVar[int]
    timeSinceBLESwitchEnableInSeconds: int
    timeSinceAppLaunchInSeconds: int
    timeSinceBeaconInSeconds: int
    timeSinceConnectInSeconds: int
    timeSinceForegroundInSeconds: int
    timeSinceBackgroundInSeconds: int
    locationPermission: LocationPermission
    remoteStartIssued: bool
    peripheralState: PeripheralState
    GATTDiscoveryBitmask: int
    timeSinceLastMessageCurrentSession: int
    timeSinceLastMessageAckCurrentSession: int
    iOS: PhoneKeyTelemetry_iOS
    android: PhoneKeyTelemetry_Android
    def __init__(self, timeSinceBLESwitchEnableInSeconds: _Optional[int] = ..., timeSinceAppLaunchInSeconds: _Optional[int] = ..., timeSinceBeaconInSeconds: _Optional[int] = ..., timeSinceConnectInSeconds: _Optional[int] = ..., timeSinceForegroundInSeconds: _Optional[int] = ..., timeSinceBackgroundInSeconds: _Optional[int] = ..., locationPermission: _Optional[_Union[LocationPermission, str]] = ..., remoteStartIssued: _Optional[bool] = ..., peripheralState: _Optional[_Union[PeripheralState, str]] = ..., GATTDiscoveryBitmask: _Optional[int] = ..., timeSinceLastMessageCurrentSession: _Optional[int] = ..., timeSinceLastMessageAckCurrentSession: _Optional[int] = ..., iOS: _Optional[_Union[PhoneKeyTelemetry_iOS, _Mapping]] = ..., android: _Optional[_Union[PhoneKeyTelemetry_Android, _Mapping]] = ...) -> None: ...

class PhoneVersionInfo(_message.Message):
    __slots__ = ("os_version_major", "os_version_minor", "os_version_patch", "app_version_major", "app_version_minor", "app_version_patch")
    OS_VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_MINOR_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_PATCH_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_MINOR_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_PATCH_FIELD_NUMBER: _ClassVar[int]
    os_version_major: int
    os_version_minor: int
    os_version_patch: int
    app_version_major: int
    app_version_minor: int
    app_version_patch: int
    def __init__(self, os_version_major: _Optional[int] = ..., os_version_minor: _Optional[int] = ..., os_version_patch: _Optional[int] = ..., app_version_major: _Optional[int] = ..., app_version_minor: _Optional[int] = ..., app_version_patch: _Optional[int] = ...) -> None: ...

class ProvisionIdentity(_message.Message):
    __slots__ = ("identity",)
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    identity: bytes
    def __init__(self, identity: _Optional[bytes] = ...) -> None: ...

class SecurityControl(_message.Message):
    __slots__ = ("immobilizationControl",)
    class ImmobilizationControl_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMMOBILIZATION_CONTROL_NONE: _ClassVar[SecurityControl.ImmobilizationControl_E]
        IMMOBILIZATION_CONTROL_IMMOBILIZE_VEHICLE: _ClassVar[SecurityControl.ImmobilizationControl_E]
        IMMOBILIZATION_CONTROL_MOBILIZE_VEHICLE: _ClassVar[SecurityControl.ImmobilizationControl_E]
    IMMOBILIZATION_CONTROL_NONE: SecurityControl.ImmobilizationControl_E
    IMMOBILIZATION_CONTROL_IMMOBILIZE_VEHICLE: SecurityControl.ImmobilizationControl_E
    IMMOBILIZATION_CONTROL_MOBILIZE_VEHICLE: SecurityControl.ImmobilizationControl_E
    IMMOBILIZATIONCONTROL_FIELD_NUMBER: _ClassVar[int]
    immobilizationControl: SecurityControl.ImmobilizationControl_E
    def __init__(self, immobilizationControl: _Optional[_Union[SecurityControl.ImmobilizationControl_E, str]] = ...) -> None: ...

class ServiceDiagnosticRequest(_message.Message):
    __slots__ = ("enterServiceModePlus",)
    ENTERSERVICEMODEPLUS_FIELD_NUMBER: _ClassVar[int]
    enterServiceModePlus: bool
    def __init__(self, enterServiceModePlus: _Optional[bool] = ...) -> None: ...

class SessionInfo(_message.Message):
    __slots__ = ("token", "counter", "publicKey")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    token: bytes
    counter: int
    publicKey: bytes
    def __init__(self, token: _Optional[bytes] = ..., counter: _Optional[int] = ..., publicKey: _Optional[bytes] = ...) -> None: ...

class SetUpdaterLocation(_message.Message):
    __slots__ = ("updaterLocation",)
    UPDATERLOCATION_FIELD_NUMBER: _ClassVar[int]
    updaterLocation: UpdaterLocation
    def __init__(self, updaterLocation: _Optional[_Union[UpdaterLocation, str]] = ...) -> None: ...

class SleepManagerRequest(_message.Message):
    __slots__ = ("delaySleepRequest", "sleepManagerCommand")
    DELAYSLEEPREQUEST_FIELD_NUMBER: _ClassVar[int]
    SLEEPMANAGERCOMMAND_FIELD_NUMBER: _ClassVar[int]
    delaySleepRequest: DelaySleepRequest
    sleepManagerCommand: SleepManagerCommand_E
    def __init__(self, delaySleepRequest: _Optional[_Union[DelaySleepRequest, _Mapping]] = ..., sleepManagerCommand: _Optional[_Union[SleepManagerCommand_E, str]] = ...) -> None: ...

class SleepManagerStats(_message.Message):
    __slots__ = ("totalCPUTime", "totalAwakeTime", "isBLETrimApplied")
    TOTALCPUTIME_FIELD_NUMBER: _ClassVar[int]
    TOTALAWAKETIME_FIELD_NUMBER: _ClassVar[int]
    ISBLETRIMAPPLIED_FIELD_NUMBER: _ClassVar[int]
    totalCPUTime: int
    totalAwakeTime: int
    isBLETrimApplied: BLEAdditionalTRIMApplied_E
    def __init__(self, totalCPUTime: _Optional[int] = ..., totalAwakeTime: _Optional[int] = ..., isBLETrimApplied: _Optional[_Union[BLEAdditionalTRIMApplied_E, str]] = ...) -> None: ...

class StageBlock(_message.Message):
    __slots__ = ("blockAddress", "blockToStage")
    BLOCKADDRESS_FIELD_NUMBER: _ClassVar[int]
    BLOCKTOSTAGE_FIELD_NUMBER: _ClassVar[int]
    blockAddress: int
    blockToStage: bytes
    def __init__(self, blockAddress: _Optional[int] = ..., blockToStage: _Optional[bytes] = ...) -> None: ...

class ToUIMessage(_message.Message):
    __slots__ = ("commandStatus", "whitelistInfo", "whitelistEntryInfo", "keyStatusInfo", "unknownKeyInfo", "UIRequest")
    COMMANDSTATUS_FIELD_NUMBER: _ClassVar[int]
    WHITELISTINFO_FIELD_NUMBER: _ClassVar[int]
    WHITELISTENTRYINFO_FIELD_NUMBER: _ClassVar[int]
    KEYSTATUSINFO_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNKEYINFO_FIELD_NUMBER: _ClassVar[int]
    UIREQUEST_FIELD_NUMBER: _ClassVar[int]
    commandStatus: CommandStatus
    whitelistInfo: WhitelistInfo
    whitelistEntryInfo: WhitelistEntryInfo
    keyStatusInfo: KeyStatusInfo
    unknownKeyInfo: UnknownKeyInfo
    UIRequest: UIRequest_E
    def __init__(self, commandStatus: _Optional[_Union[CommandStatus, _Mapping]] = ..., whitelistInfo: _Optional[_Union[WhitelistInfo, _Mapping]] = ..., whitelistEntryInfo: _Optional[_Union[WhitelistEntryInfo, _Mapping]] = ..., keyStatusInfo: _Optional[_Union[KeyStatusInfo, _Mapping]] = ..., unknownKeyInfo: _Optional[_Union[UnknownKeyInfo, _Mapping]] = ..., UIRequest: _Optional[_Union[UIRequest_E, str]] = ...) -> None: ...

class ToVCSECMessageV0Protocol(_message.Message):
    __slots__ = ("signedMessage", "unsignedMessageAsBytes")
    SIGNEDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNSIGNEDMESSAGEASBYTES_FIELD_NUMBER: _ClassVar[int]
    signedMessage: SignedMessage
    unsignedMessageAsBytes: bytes
    def __init__(self, signedMessage: _Optional[_Union[SignedMessage, _Mapping]] = ..., unsignedMessageAsBytes: _Optional[bytes] = ...) -> None: ...

class UnknownKeyInfo(_message.Message):
    __slots__ = ("keyStatus", "publicKey", "keyFormFactor")
    KEYSTATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    KEYFORMFACTOR_FIELD_NUMBER: _ClassVar[int]
    keyStatus: KeyStatus
    publicKey: PublicKey
    keyFormFactor: KeyFormFactor
    def __init__(self, keyStatus: _Optional[_Union[KeyStatus, _Mapping]] = ..., publicKey: _Optional[_Union[PublicKey, _Mapping]] = ..., keyFormFactor: _Optional[_Union[KeyFormFactor, str]] = ...) -> None: ...

class UnsecureNotification(_message.Message):
    __slots__ = ("notifyUser", "closureStatuses")
    NOTIFYUSER_FIELD_NUMBER: _ClassVar[int]
    CLOSURESTATUSES_FIELD_NUMBER: _ClassVar[int]
    notifyUser: bool
    closureStatuses: ClosureStatuses
    def __init__(self, notifyUser: _Optional[bool] = ..., closureStatuses: _Optional[_Union[ClosureStatuses, _Mapping]] = ...) -> None: ...

class UnsignedMessageUI(_message.Message):
    __slots__ = ("InformationRequest", "RKEAction", "WhitelistOperation", "BLENickName")
    INFORMATIONREQUEST_FIELD_NUMBER: _ClassVar[int]
    RKEACTION_FIELD_NUMBER: _ClassVar[int]
    WHITELISTOPERATION_FIELD_NUMBER: _ClassVar[int]
    BLENICKNAME_FIELD_NUMBER: _ClassVar[int]
    InformationRequest: InformationRequest
    RKEAction: RKEAction_E
    WhitelistOperation: WhitelistOperation
    BLENickName: VehicleBLENickName
    def __init__(self, InformationRequest: _Optional[_Union[InformationRequest, _Mapping]] = ..., RKEAction: _Optional[_Union[RKEAction_E, str]] = ..., WhitelistOperation: _Optional[_Union[WhitelistOperation, _Mapping]] = ..., BLENickName: _Optional[_Union[VehicleBLENickName, _Mapping]] = ...) -> None: ...

class UpdaterCommand(_message.Message):
    __slots__ = ("getCodeDescriptor", "setUpdaterLocation", "stageBlock", "verifyAndInstallApp", "firmwareInfo")
    GETCODEDESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    SETUPDATERLOCATION_FIELD_NUMBER: _ClassVar[int]
    STAGEBLOCK_FIELD_NUMBER: _ClassVar[int]
    VERIFYANDINSTALLAPP_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREINFO_FIELD_NUMBER: _ClassVar[int]
    getCodeDescriptor: GetCodeDescriptor
    setUpdaterLocation: SetUpdaterLocation
    stageBlock: StageBlock
    verifyAndInstallApp: VerifyAndInstallApp
    firmwareInfo: bytes
    def __init__(self, getCodeDescriptor: _Optional[_Union[GetCodeDescriptor, _Mapping]] = ..., setUpdaterLocation: _Optional[_Union[SetUpdaterLocation, _Mapping]] = ..., stageBlock: _Optional[_Union[StageBlock, _Mapping]] = ..., verifyAndInstallApp: _Optional[_Union[VerifyAndInstallApp, _Mapping]] = ..., firmwareInfo: _Optional[bytes] = ...) -> None: ...

class UpdaterResponse(_message.Message):
    __slots__ = ("codeDescriptorMessage", "updaterStatus")
    CODEDESCRIPTORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATERSTATUS_FIELD_NUMBER: _ClassVar[int]
    codeDescriptorMessage: CodeDescriptor
    updaterStatus: UpdaterStatus
    def __init__(self, codeDescriptorMessage: _Optional[_Union[CodeDescriptor, _Mapping]] = ..., updaterStatus: _Optional[_Union[UpdaterStatus, _Mapping]] = ...) -> None: ...

class UpdaterStatus(_message.Message):
    __slots__ = ("statusCode", "location", "nextAddressNumber")
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NEXTADDRESSNUMBER_FIELD_NUMBER: _ClassVar[int]
    statusCode: UpdaterStatusCode
    location: UpdaterLocation
    nextAddressNumber: int
    def __init__(self, statusCode: _Optional[_Union[UpdaterStatusCode, str]] = ..., location: _Optional[_Union[UpdaterLocation, str]] = ..., nextAddressNumber: _Optional[int] = ...) -> None: ...

class VehicleBLENickName(_message.Message):
    __slots__ = ("nickName",)
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    nickName: bytes
    def __init__(self, nickName: _Optional[bytes] = ...) -> None: ...

class VerifyAndInstallApp(_message.Message):
    __slots__ = ("sha256", "rValue", "sValue")
    SHA256_FIELD_NUMBER: _ClassVar[int]
    RVALUE_FIELD_NUMBER: _ClassVar[int]
    SVALUE_FIELD_NUMBER: _ClassVar[int]
    sha256: bytes
    rValue: bytes
    sValue: bytes
    def __init__(self, sha256: _Optional[bytes] = ..., rValue: _Optional[bytes] = ..., sValue: _Optional[bytes] = ...) -> None: ...

class WatchAppStateEvent(_message.Message):
    __slots__ = ("field_1", "field_2", "field_3", "batteryLevelPercent")
    FIELD_1_FIELD_NUMBER: _ClassVar[int]
    FIELD_2_FIELD_NUMBER: _ClassVar[int]
    FIELD_3_FIELD_NUMBER: _ClassVar[int]
    BATTERYLEVELPERCENT_FIELD_NUMBER: _ClassVar[int]
    field_1: iOS_AppState
    field_2: bool
    field_3: bool
    batteryLevelPercent: int
    def __init__(self, field_1: _Optional[_Union[iOS_AppState, str]] = ..., field_2: _Optional[bool] = ..., field_3: _Optional[bool] = ..., batteryLevelPercent: _Optional[int] = ...) -> None: ...
