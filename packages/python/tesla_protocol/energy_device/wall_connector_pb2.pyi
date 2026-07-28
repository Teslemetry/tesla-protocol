import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from . import device_pb2 as _device_pb2
from . import networking_pb2 as _networking_pb2
from . import energy_pb2 as _energy_pb2
from . import neurio_meter_api_pb2 as _neurio_meter_api_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WCChargeScheduleChargingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_CHARGE_SCHEDULE_CHARGING_STATUS_INVALID: _ClassVar[WCChargeScheduleChargingStatus]
    WC_CHARGE_SCHEDULE_CHARGING_STATUS_UNCONFIGURED_DISABLED: _ClassVar[WCChargeScheduleChargingStatus]
    WC_CHARGE_SCHEDULE_CHARGING_STATUS_CHARGE_BLOCKED: _ClassVar[WCChargeScheduleChargingStatus]
    WC_CHARGE_SCHEDULE_CHARGING_STATUS_DELAYED_CHARGE_BLOCKED: _ClassVar[WCChargeScheduleChargingStatus]
    WC_CHARGE_SCHEDULE_CHARGING_STATUS_CHARGE_ALLOWED: _ClassVar[WCChargeScheduleChargingStatus]
    WC_CHARGE_SCHEDULE_CHARGING_STATUS_DELAYED_CHARGE_ALLOWED: _ClassVar[WCChargeScheduleChargingStatus]
    WC_CHARGE_SCHEDULE_CHARGING_STATUS_VEHICLE_OVERRIDDEN: _ClassVar[WCChargeScheduleChargingStatus]

class WCChargeScheduleConfigError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_CHARGE_SCHEDULE_CONFIG_ERROR_INVALID: _ClassVar[WCChargeScheduleConfigError]
    WC_CHARGE_SCHEDULE_CONFIG_ERROR_NONE: _ClassVar[WCChargeScheduleConfigError]
    WC_CHARGE_SCHEDULE_CONFIG_ERROR_NO_SITE_WIFI: _ClassVar[WCChargeScheduleConfigError]
    WC_CHARGE_SCHEDULE_CONFIG_ERROR_NO_INTERNET: _ClassVar[WCChargeScheduleConfigError]
    WC_CHARGE_SCHEDULE_CONFIG_ERROR_INVALID_PARAMETERS: _ClassVar[WCChargeScheduleConfigError]
    WC_CHARGE_SCHEDULE_CONFIG_ERROR_INTERNAL_ERROR: _ClassVar[WCChargeScheduleConfigError]

class WCChargeScheduleDay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_CHARGE_SCHEDULE_DAY_INVALID: _ClassVar[WCChargeScheduleDay]
    WC_CHARGE_SCHEDULE_DAY_SUNDAY: _ClassVar[WCChargeScheduleDay]
    WC_CHARGE_SCHEDULE_DAY_MONDAY: _ClassVar[WCChargeScheduleDay]
    WC_CHARGE_SCHEDULE_DAY_TUESDAY: _ClassVar[WCChargeScheduleDay]
    WC_CHARGE_SCHEDULE_DAY_WEDNESDAY: _ClassVar[WCChargeScheduleDay]
    WC_CHARGE_SCHEDULE_DAY_THURSDAY: _ClassVar[WCChargeScheduleDay]
    WC_CHARGE_SCHEDULE_DAY_FRIDAY: _ClassVar[WCChargeScheduleDay]
    WC_CHARGE_SCHEDULE_DAY_SATURDAY: _ClassVar[WCChargeScheduleDay]

class WCChargeScheduleError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_CHARGE_SCHEDULE_ERROR_INVALID: _ClassVar[WCChargeScheduleError]
    WC_CHARGE_SCHEDULE_ERROR_NONE: _ClassVar[WCChargeScheduleError]
    WC_CHARGE_SCHEDULE_ERROR_NO_INTERNET: _ClassVar[WCChargeScheduleError]
    WC_CHARGE_SCHEDULE_ERROR_NON_VOLATILE_DATA_READ_WRITE_FAIL: _ClassVar[WCChargeScheduleError]
    WC_CHARGE_SCHEDULE_ERROR_INTERNAL: _ClassVar[WCChargeScheduleError]

class WCConfigureAccessControlOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_CONFIGURE_ACCESS_CONTROL_OPERATION_INVALID: _ClassVar[WCConfigureAccessControlOperation]
    WC_CONFIGURE_ACCESS_CONTROL_OPERATION_ADD: _ClassVar[WCConfigureAccessControlOperation]
    WC_CONFIGURE_ACCESS_CONTROL_OPERATION_REMOVE: _ClassVar[WCConfigureAccessControlOperation]
    WC_CONFIGURE_ACCESS_CONTROL_OPERATION_CLEAR_ALL: _ClassVar[WCConfigureAccessControlOperation]
    WC_CONFIGURE_ACCESS_CONTROL_OPERATION_RENAME: _ClassVar[WCConfigureAccessControlOperation]

class WCFaultStatusState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_FAULT_STATUS_STATE_INVALID: _ClassVar[WCFaultStatusState]
    WC_FAULT_STATUS_STATE_STARTUP: _ClassVar[WCFaultStatusState]
    WC_FAULT_STATUS_STATE_READY: _ClassVar[WCFaultStatusState]
    WC_FAULT_STATUS_STATE_CRITICAL_FAULT: _ClassVar[WCFaultStatusState]
    WC_FAULT_STATUS_STATE_NON_CRITICAL_FAULT: _ClassVar[WCFaultStatusState]
    WC_FAULT_STATUS_STATE_RETRY_PENDING: _ClassVar[WCFaultStatusState]
    WC_FAULT_STATUS_STATE_LOCKOUT: _ClassVar[WCFaultStatusState]
    WC_FAULT_STATUS_STATE_FOLDBACK: _ClassVar[WCFaultStatusState]
    WC_FAULT_STATUS_STATE_CHARGING: _ClassVar[WCFaultStatusState]
    WC_FAULT_STATUS_STATE_CONFIGURATION_REQUIRED: _ClassVar[WCFaultStatusState]

class WCGroundMonitorMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_GROUND_MONITOR_MODE_INVALID: _ClassVar[WCGroundMonitorMode]
    WC_GROUND_MONITOR_MODE_DISABLED: _ClassVar[WCGroundMonitorMode]
    WC_GROUND_MONITOR_MODE_INFORMATIONAL: _ClassVar[WCGroundMonitorMode]
    WC_GROUND_MONITOR_MODE_ENABLED: _ClassVar[WCGroundMonitorMode]

class WCLoadSharingNetworkChargingInhibitor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_LOAD_SHARING_NETWORK_CHARGING_INHIBITOR_INVALID: _ClassVar[WCLoadSharingNetworkChargingInhibitor]
    WC_LOAD_SHARING_NETWORK_CHARGING_INHIBITOR_INSUFFICIENT_CURRENT: _ClassVar[WCLoadSharingNetworkChargingInhibitor]
    WC_LOAD_SHARING_NETWORK_CHARGING_INHIBITOR_INSUFFICIENT_DEVICES: _ClassVar[WCLoadSharingNetworkChargingInhibitor]
    WC_LOAD_SHARING_NETWORK_CHARGING_INHIBITOR_DEVICES_MIA: _ClassVar[WCLoadSharingNetworkChargingInhibitor]

class WCPpuSessionReportingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_PPU_SESSION_REPORTING_MODE_INVALID: _ClassVar[WCPpuSessionReportingMode]
    WC_PPU_SESSION_REPORTING_MODE_NONE: _ClassVar[WCPpuSessionReportingMode]
    WC_PPU_SESSION_REPORTING_MODE_ALL_INFO: _ClassVar[WCPpuSessionReportingMode]

class WCTeslaVehicleDriveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_TESLA_VEHICLE_DRIVE_TYPE_INVALID: _ClassVar[WCTeslaVehicleDriveType]
    WC_TESLA_VEHICLE_DRIVE_TYPE_SINGLE_MOTOR_STANDARD: _ClassVar[WCTeslaVehicleDriveType]
    WC_TESLA_VEHICLE_DRIVE_TYPE_SINGLE_MOTOR_PERFORMANCE: _ClassVar[WCTeslaVehicleDriveType]
    WC_TESLA_VEHICLE_DRIVE_TYPE_DUAL_MOTOR_STANDARD: _ClassVar[WCTeslaVehicleDriveType]
    WC_TESLA_VEHICLE_DRIVE_TYPE_DUAL_MOTOR_PERFORMANCE: _ClassVar[WCTeslaVehicleDriveType]

class WCTeslaVehicleModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_TESLA_VEHICLE_MODEL_INVALID: _ClassVar[WCTeslaVehicleModel]
    WC_TESLA_VEHICLE_MODEL_S: _ClassVar[WCTeslaVehicleModel]
    WC_TESLA_VEHICLE_MODEL_X: _ClassVar[WCTeslaVehicleModel]
    WC_TESLA_VEHICLE_MODEL_3: _ClassVar[WCTeslaVehicleModel]
    WC_TESLA_VEHICLE_MODEL_Y: _ClassVar[WCTeslaVehicleModel]

class WCThirdPartyVehicleMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_THIRD_PARTY_VEHICLE_MODE_INVALID: _ClassVar[WCThirdPartyVehicleMode]
    WC_THIRD_PARTY_VEHICLE_MODE_ENABLED: _ClassVar[WCThirdPartyVehicleMode]
    WC_THIRD_PARTY_VEHICLE_MODE_DISABLED: _ClassVar[WCThirdPartyVehicleMode]
    WC_THIRD_PARTY_VEHICLE_MODE_DISABLED_NO_ROADSTER: _ClassVar[WCThirdPartyVehicleMode]
    WC_THIRD_PARTY_VEHICLE_MODE_VIN_ALLOW_LIST: _ClassVar[WCThirdPartyVehicleMode]

class WCEvseNotReadyReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_EVSE_NOT_READY_REASON_INVALID: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_COLD_LOAD_PICKUP: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_HANDLE_BUTTON: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_SESSION_AUTH: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_FAULT_NO_CHARGE: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_FAULT_STARTUP: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_GMI_NO_CHARGE: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_PILOT_NOT_CONN: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_CONFIG_NOT_RECV: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_LOAD_SHARE_NO_CHARGE: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_OCPP_NO_CHARGE: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_ACCESS_CONTROL_LIST: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_PAY_PER_USE: _ClassVar[WCEvseNotReadyReason]
    WC_EVSE_NOT_READY_REASON_THIRD_PARTY_VEHICLE: _ClassVar[WCEvseNotReadyReason]

class WCOcppStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_OCPP_STATUS_INVALID: _ClassVar[WCOcppStatus]
    WC_OCPP_STATUS_UNCONFIGURED: _ClassVar[WCOcppStatus]
    WC_OCPP_STATUS_INCOMPLETE_CONFIGURATION: _ClassVar[WCOcppStatus]
    WC_OCPP_STATUS_CONFIGURED_DISABLED: _ClassVar[WCOcppStatus]
    WC_OCPP_STATUS_CONFIGURED_ENABLED: _ClassVar[WCOcppStatus]
    WC_OCPP_STATUS_CONFIGURED_ENABLED_CONNECTED: _ClassVar[WCOcppStatus]
    WC_OCPP_STATUS_CONFIGURED_ENABLED_INVALID_CONFIGURATION: _ClassVar[WCOcppStatus]

class WCDryContactControlState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_DRY_CONTACT_CONTROL_STATE_INVALID: _ClassVar[WCDryContactControlState]
    WC_DRY_CONTACT_CONTROL_STATE_INACTIVE: _ClassVar[WCDryContactControlState]
    WC_DRY_CONTACT_CONTROL_STATE_ACTIVE: _ClassVar[WCDryContactControlState]

class WCDryContactDefaultState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_DRY_CONTACT_DEFAULT_STATE_INVALID: _ClassVar[WCDryContactDefaultState]
    WC_DRY_CONTACT_DEFAULT_STATE_NORMALLY_OPEN: _ClassVar[WCDryContactDefaultState]
    WC_DRY_CONTACT_DEFAULT_STATE_NORMALLY_CLOSED: _ClassVar[WCDryContactDefaultState]

class WCTimeSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_TIME_SOURCE_INVALID: _ClassVar[WCTimeSource]
    WC_TIME_SOURCE_BUILD: _ClassVar[WCTimeSource]
    WC_TIME_SOURCE_SAVED: _ClassVar[WCTimeSource]
    WC_TIME_SOURCE_STALE: _ClassVar[WCTimeSource]
    WC_TIME_SOURCE_SYNCED: _ClassVar[WCTimeSource]

class WCOperationalMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_OPERATIONAL_MODE_INVALID: _ClassVar[WCOperationalMode]
    WC_OPERATIONAL_MODE_COMMERCIAL_PAY_PER_USE: _ClassVar[WCOperationalMode]
    WC_OPERATIONAL_MODE_COMMERCIAL_NOT_PAY_PER_USE: _ClassVar[WCOperationalMode]
    WC_OPERATIONAL_MODE_NOT_COMMERCIAL: _ClassVar[WCOperationalMode]
    WC_OPERATIONAL_MODE_COMMERCIAL_PAY_PER_USE_WITH_ACCESS_CONTROL: _ClassVar[WCOperationalMode]
    WC_OPERATIONAL_MODE_COMMERCIAL_WITH_ACCESS_CONTROL: _ClassVar[WCOperationalMode]

class WCOcppSecurityParameterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_OCPP_SECURITY_PARAMETER_TYPE_INVALID: _ClassVar[WCOcppSecurityParameterType]
    WC_OCPP_SECURITY_PARAMETER_TYPE_CP_AUTH_KEY: _ClassVar[WCOcppSecurityParameterType]
    WC_OCPP_SECURITY_PARAMETER_TYPE_CS_CA_CERT: _ClassVar[WCOcppSecurityParameterType]
    WC_OCPP_SECURITY_PARAMETER_TYPE_CP_CERT: _ClassVar[WCOcppSecurityParameterType]
    WC_OCPP_SECURITY_PARAMETER_TYPE_ALTERNATE_CS_CA_CERT: _ClassVar[WCOcppSecurityParameterType]

class WCOcppVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_OCPP_VERSION_INVALID: _ClassVar[WCOcppVersion]
    WC_OCPP_VERSION_1_6: _ClassVar[WCOcppVersion]
    WC_OCPP_VERSION_2_0_1: _ClassVar[WCOcppVersion]

class WCOcppSecurityProfile(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_OCPP_SECURITY_PROFILE_INVALID: _ClassVar[WCOcppSecurityProfile]
    WC_OCPP_SECURITY_PROFILE_UNSECURED_BASIC_AUTH: _ClassVar[WCOcppSecurityProfile]
    WC_OCPP_SECURITY_PROFILE_TLS_BASIC_AUTH: _ClassVar[WCOcppSecurityProfile]
    WC_OCPP_SECURITY_PROFILE_TLS_CLIENT_CERTS: _ClassVar[WCOcppSecurityProfile]

class WCOcppScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_OCPP_SCOPE_INVALID: _ClassVar[WCOcppScope]
    WC_OCPP_SCOPE_REIMBURSEMENT: _ClassVar[WCOcppScope]
    WC_OCPP_SCOPE_FULL: _ClassVar[WCOcppScope]

class WCSmartChargingReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_SMART_CHARGING_REASON_INVALID: _ClassVar[WCSmartChargingReason]
    WC_SMART_CHARGING_REASON_DISABLED_BY_SCHEDULE: _ClassVar[WCSmartChargingReason]
    WC_SMART_CHARGING_REASON_ENABLED_BY_SCHEDULE: _ClassVar[WCSmartChargingReason]
    WC_SMART_CHARGING_REASON_EXPLICITLY_STOPPED: _ClassVar[WCSmartChargingReason]
    WC_SMART_CHARGING_REASON_EXPLICITLY_STARTED: _ClassVar[WCSmartChargingReason]
    WC_SMART_CHARGING_REASON_SMART_CHARGING_ALLOWED: _ClassVar[WCSmartChargingReason]
    WC_SMART_CHARGING_REASON_SMART_CHARGING_DISALLOWED: _ClassVar[WCSmartChargingReason]
    WC_SMART_CHARGING_REASON_SMART_CHARGING_TARGET_POWER: _ClassVar[WCSmartChargingReason]
    WC_SMART_CHARGING_REASON_SMART_CHARGING_LOW_VOLTAGE: _ClassVar[WCSmartChargingReason]
    WC_SMART_CHARGING_REASON_SMART_CHARGING_TARGET_POWER_BELOW_MINIMUM: _ClassVar[WCSmartChargingReason]

class WCPowershareSessionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_POWERSHARE_SESSION_STATE_INVALID: _ClassVar[WCPowershareSessionState]
    WC_POWERSHARE_SESSION_STATE_NONE: _ClassVar[WCPowershareSessionState]
    WC_POWERSHARE_SESSION_STATE_IN_PROGRESS: _ClassVar[WCPowershareSessionState]

class WCChargingCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_CHARGING_COMMAND_INVALID: _ClassVar[WCChargingCommand]
    WC_CHARGING_COMMAND_START: _ClassVar[WCChargingCommand]
    WC_CHARGING_COMMAND_STOP: _ClassVar[WCChargingCommand]
WC_CHARGE_SCHEDULE_CHARGING_STATUS_INVALID: WCChargeScheduleChargingStatus
WC_CHARGE_SCHEDULE_CHARGING_STATUS_UNCONFIGURED_DISABLED: WCChargeScheduleChargingStatus
WC_CHARGE_SCHEDULE_CHARGING_STATUS_CHARGE_BLOCKED: WCChargeScheduleChargingStatus
WC_CHARGE_SCHEDULE_CHARGING_STATUS_DELAYED_CHARGE_BLOCKED: WCChargeScheduleChargingStatus
WC_CHARGE_SCHEDULE_CHARGING_STATUS_CHARGE_ALLOWED: WCChargeScheduleChargingStatus
WC_CHARGE_SCHEDULE_CHARGING_STATUS_DELAYED_CHARGE_ALLOWED: WCChargeScheduleChargingStatus
WC_CHARGE_SCHEDULE_CHARGING_STATUS_VEHICLE_OVERRIDDEN: WCChargeScheduleChargingStatus
WC_CHARGE_SCHEDULE_CONFIG_ERROR_INVALID: WCChargeScheduleConfigError
WC_CHARGE_SCHEDULE_CONFIG_ERROR_NONE: WCChargeScheduleConfigError
WC_CHARGE_SCHEDULE_CONFIG_ERROR_NO_SITE_WIFI: WCChargeScheduleConfigError
WC_CHARGE_SCHEDULE_CONFIG_ERROR_NO_INTERNET: WCChargeScheduleConfigError
WC_CHARGE_SCHEDULE_CONFIG_ERROR_INVALID_PARAMETERS: WCChargeScheduleConfigError
WC_CHARGE_SCHEDULE_CONFIG_ERROR_INTERNAL_ERROR: WCChargeScheduleConfigError
WC_CHARGE_SCHEDULE_DAY_INVALID: WCChargeScheduleDay
WC_CHARGE_SCHEDULE_DAY_SUNDAY: WCChargeScheduleDay
WC_CHARGE_SCHEDULE_DAY_MONDAY: WCChargeScheduleDay
WC_CHARGE_SCHEDULE_DAY_TUESDAY: WCChargeScheduleDay
WC_CHARGE_SCHEDULE_DAY_WEDNESDAY: WCChargeScheduleDay
WC_CHARGE_SCHEDULE_DAY_THURSDAY: WCChargeScheduleDay
WC_CHARGE_SCHEDULE_DAY_FRIDAY: WCChargeScheduleDay
WC_CHARGE_SCHEDULE_DAY_SATURDAY: WCChargeScheduleDay
WC_CHARGE_SCHEDULE_ERROR_INVALID: WCChargeScheduleError
WC_CHARGE_SCHEDULE_ERROR_NONE: WCChargeScheduleError
WC_CHARGE_SCHEDULE_ERROR_NO_INTERNET: WCChargeScheduleError
WC_CHARGE_SCHEDULE_ERROR_NON_VOLATILE_DATA_READ_WRITE_FAIL: WCChargeScheduleError
WC_CHARGE_SCHEDULE_ERROR_INTERNAL: WCChargeScheduleError
WC_CONFIGURE_ACCESS_CONTROL_OPERATION_INVALID: WCConfigureAccessControlOperation
WC_CONFIGURE_ACCESS_CONTROL_OPERATION_ADD: WCConfigureAccessControlOperation
WC_CONFIGURE_ACCESS_CONTROL_OPERATION_REMOVE: WCConfigureAccessControlOperation
WC_CONFIGURE_ACCESS_CONTROL_OPERATION_CLEAR_ALL: WCConfigureAccessControlOperation
WC_CONFIGURE_ACCESS_CONTROL_OPERATION_RENAME: WCConfigureAccessControlOperation
WC_FAULT_STATUS_STATE_INVALID: WCFaultStatusState
WC_FAULT_STATUS_STATE_STARTUP: WCFaultStatusState
WC_FAULT_STATUS_STATE_READY: WCFaultStatusState
WC_FAULT_STATUS_STATE_CRITICAL_FAULT: WCFaultStatusState
WC_FAULT_STATUS_STATE_NON_CRITICAL_FAULT: WCFaultStatusState
WC_FAULT_STATUS_STATE_RETRY_PENDING: WCFaultStatusState
WC_FAULT_STATUS_STATE_LOCKOUT: WCFaultStatusState
WC_FAULT_STATUS_STATE_FOLDBACK: WCFaultStatusState
WC_FAULT_STATUS_STATE_CHARGING: WCFaultStatusState
WC_FAULT_STATUS_STATE_CONFIGURATION_REQUIRED: WCFaultStatusState
WC_GROUND_MONITOR_MODE_INVALID: WCGroundMonitorMode
WC_GROUND_MONITOR_MODE_DISABLED: WCGroundMonitorMode
WC_GROUND_MONITOR_MODE_INFORMATIONAL: WCGroundMonitorMode
WC_GROUND_MONITOR_MODE_ENABLED: WCGroundMonitorMode
WC_LOAD_SHARING_NETWORK_CHARGING_INHIBITOR_INVALID: WCLoadSharingNetworkChargingInhibitor
WC_LOAD_SHARING_NETWORK_CHARGING_INHIBITOR_INSUFFICIENT_CURRENT: WCLoadSharingNetworkChargingInhibitor
WC_LOAD_SHARING_NETWORK_CHARGING_INHIBITOR_INSUFFICIENT_DEVICES: WCLoadSharingNetworkChargingInhibitor
WC_LOAD_SHARING_NETWORK_CHARGING_INHIBITOR_DEVICES_MIA: WCLoadSharingNetworkChargingInhibitor
WC_PPU_SESSION_REPORTING_MODE_INVALID: WCPpuSessionReportingMode
WC_PPU_SESSION_REPORTING_MODE_NONE: WCPpuSessionReportingMode
WC_PPU_SESSION_REPORTING_MODE_ALL_INFO: WCPpuSessionReportingMode
WC_TESLA_VEHICLE_DRIVE_TYPE_INVALID: WCTeslaVehicleDriveType
WC_TESLA_VEHICLE_DRIVE_TYPE_SINGLE_MOTOR_STANDARD: WCTeslaVehicleDriveType
WC_TESLA_VEHICLE_DRIVE_TYPE_SINGLE_MOTOR_PERFORMANCE: WCTeslaVehicleDriveType
WC_TESLA_VEHICLE_DRIVE_TYPE_DUAL_MOTOR_STANDARD: WCTeslaVehicleDriveType
WC_TESLA_VEHICLE_DRIVE_TYPE_DUAL_MOTOR_PERFORMANCE: WCTeslaVehicleDriveType
WC_TESLA_VEHICLE_MODEL_INVALID: WCTeslaVehicleModel
WC_TESLA_VEHICLE_MODEL_S: WCTeslaVehicleModel
WC_TESLA_VEHICLE_MODEL_X: WCTeslaVehicleModel
WC_TESLA_VEHICLE_MODEL_3: WCTeslaVehicleModel
WC_TESLA_VEHICLE_MODEL_Y: WCTeslaVehicleModel
WC_THIRD_PARTY_VEHICLE_MODE_INVALID: WCThirdPartyVehicleMode
WC_THIRD_PARTY_VEHICLE_MODE_ENABLED: WCThirdPartyVehicleMode
WC_THIRD_PARTY_VEHICLE_MODE_DISABLED: WCThirdPartyVehicleMode
WC_THIRD_PARTY_VEHICLE_MODE_DISABLED_NO_ROADSTER: WCThirdPartyVehicleMode
WC_THIRD_PARTY_VEHICLE_MODE_VIN_ALLOW_LIST: WCThirdPartyVehicleMode
WC_EVSE_NOT_READY_REASON_INVALID: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_COLD_LOAD_PICKUP: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_HANDLE_BUTTON: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_SESSION_AUTH: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_FAULT_NO_CHARGE: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_FAULT_STARTUP: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_GMI_NO_CHARGE: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_PILOT_NOT_CONN: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_CONFIG_NOT_RECV: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_LOAD_SHARE_NO_CHARGE: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_OCPP_NO_CHARGE: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_ACCESS_CONTROL_LIST: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_PAY_PER_USE: WCEvseNotReadyReason
WC_EVSE_NOT_READY_REASON_THIRD_PARTY_VEHICLE: WCEvseNotReadyReason
WC_OCPP_STATUS_INVALID: WCOcppStatus
WC_OCPP_STATUS_UNCONFIGURED: WCOcppStatus
WC_OCPP_STATUS_INCOMPLETE_CONFIGURATION: WCOcppStatus
WC_OCPP_STATUS_CONFIGURED_DISABLED: WCOcppStatus
WC_OCPP_STATUS_CONFIGURED_ENABLED: WCOcppStatus
WC_OCPP_STATUS_CONFIGURED_ENABLED_CONNECTED: WCOcppStatus
WC_OCPP_STATUS_CONFIGURED_ENABLED_INVALID_CONFIGURATION: WCOcppStatus
WC_DRY_CONTACT_CONTROL_STATE_INVALID: WCDryContactControlState
WC_DRY_CONTACT_CONTROL_STATE_INACTIVE: WCDryContactControlState
WC_DRY_CONTACT_CONTROL_STATE_ACTIVE: WCDryContactControlState
WC_DRY_CONTACT_DEFAULT_STATE_INVALID: WCDryContactDefaultState
WC_DRY_CONTACT_DEFAULT_STATE_NORMALLY_OPEN: WCDryContactDefaultState
WC_DRY_CONTACT_DEFAULT_STATE_NORMALLY_CLOSED: WCDryContactDefaultState
WC_TIME_SOURCE_INVALID: WCTimeSource
WC_TIME_SOURCE_BUILD: WCTimeSource
WC_TIME_SOURCE_SAVED: WCTimeSource
WC_TIME_SOURCE_STALE: WCTimeSource
WC_TIME_SOURCE_SYNCED: WCTimeSource
WC_OPERATIONAL_MODE_INVALID: WCOperationalMode
WC_OPERATIONAL_MODE_COMMERCIAL_PAY_PER_USE: WCOperationalMode
WC_OPERATIONAL_MODE_COMMERCIAL_NOT_PAY_PER_USE: WCOperationalMode
WC_OPERATIONAL_MODE_NOT_COMMERCIAL: WCOperationalMode
WC_OPERATIONAL_MODE_COMMERCIAL_PAY_PER_USE_WITH_ACCESS_CONTROL: WCOperationalMode
WC_OPERATIONAL_MODE_COMMERCIAL_WITH_ACCESS_CONTROL: WCOperationalMode
WC_OCPP_SECURITY_PARAMETER_TYPE_INVALID: WCOcppSecurityParameterType
WC_OCPP_SECURITY_PARAMETER_TYPE_CP_AUTH_KEY: WCOcppSecurityParameterType
WC_OCPP_SECURITY_PARAMETER_TYPE_CS_CA_CERT: WCOcppSecurityParameterType
WC_OCPP_SECURITY_PARAMETER_TYPE_CP_CERT: WCOcppSecurityParameterType
WC_OCPP_SECURITY_PARAMETER_TYPE_ALTERNATE_CS_CA_CERT: WCOcppSecurityParameterType
WC_OCPP_VERSION_INVALID: WCOcppVersion
WC_OCPP_VERSION_1_6: WCOcppVersion
WC_OCPP_VERSION_2_0_1: WCOcppVersion
WC_OCPP_SECURITY_PROFILE_INVALID: WCOcppSecurityProfile
WC_OCPP_SECURITY_PROFILE_UNSECURED_BASIC_AUTH: WCOcppSecurityProfile
WC_OCPP_SECURITY_PROFILE_TLS_BASIC_AUTH: WCOcppSecurityProfile
WC_OCPP_SECURITY_PROFILE_TLS_CLIENT_CERTS: WCOcppSecurityProfile
WC_OCPP_SCOPE_INVALID: WCOcppScope
WC_OCPP_SCOPE_REIMBURSEMENT: WCOcppScope
WC_OCPP_SCOPE_FULL: WCOcppScope
WC_SMART_CHARGING_REASON_INVALID: WCSmartChargingReason
WC_SMART_CHARGING_REASON_DISABLED_BY_SCHEDULE: WCSmartChargingReason
WC_SMART_CHARGING_REASON_ENABLED_BY_SCHEDULE: WCSmartChargingReason
WC_SMART_CHARGING_REASON_EXPLICITLY_STOPPED: WCSmartChargingReason
WC_SMART_CHARGING_REASON_EXPLICITLY_STARTED: WCSmartChargingReason
WC_SMART_CHARGING_REASON_SMART_CHARGING_ALLOWED: WCSmartChargingReason
WC_SMART_CHARGING_REASON_SMART_CHARGING_DISALLOWED: WCSmartChargingReason
WC_SMART_CHARGING_REASON_SMART_CHARGING_TARGET_POWER: WCSmartChargingReason
WC_SMART_CHARGING_REASON_SMART_CHARGING_LOW_VOLTAGE: WCSmartChargingReason
WC_SMART_CHARGING_REASON_SMART_CHARGING_TARGET_POWER_BELOW_MINIMUM: WCSmartChargingReason
WC_POWERSHARE_SESSION_STATE_INVALID: WCPowershareSessionState
WC_POWERSHARE_SESSION_STATE_NONE: WCPowershareSessionState
WC_POWERSHARE_SESSION_STATE_IN_PROGRESS: WCPowershareSessionState
WC_CHARGING_COMMAND_INVALID: WCChargingCommand
WC_CHARGING_COMMAND_START: WCChargingCommand
WC_CHARGING_COMMAND_STOP: WCChargingCommand

class WCFaultStatusLatchedAlert(_message.Message):
    __slots__ = ('alert_id', 'alert_timestamp')
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    alert_id: int
    alert_timestamp: _timestamp_pb2.Timestamp

    def __init__(self, alert_id: _Optional[int]=..., alert_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class WCVitals(_message.Message):
    __slots__ = ('uptime_s', 'alerts', 'contactor_closed', 'vehicle_connected', 'pcba_temp_c', 'handle_temp_c', 'mcu_temp_c', 'input_thermopile_v', 'prox_v', 'pilot_high_v', 'pilot_low_v', 'session_duration_s', 'session_energy', 'ac_measurement_grid', 'ac_measurement_vehicle', 'ground_resistance_ohms', 'line1_earth_vrms', 'neutral_earth_vrms', 'fault_status', 'recent_fault_status_latched_alerts', 'vin', 'instantaneous_power_watts', 'scheduled_charging_status', 'instantaneous_line_current', 'ocpp_status', 'evse_not_ready_reasons', 'powershare_session_state', 'dry_contact_control_state', 'smart_charging_reason')
    UPTIME_S_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    CONTACTOR_CLOSED_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    PCBA_TEMP_C_FIELD_NUMBER: _ClassVar[int]
    HANDLE_TEMP_C_FIELD_NUMBER: _ClassVar[int]
    MCU_TEMP_C_FIELD_NUMBER: _ClassVar[int]
    INPUT_THERMOPILE_V_FIELD_NUMBER: _ClassVar[int]
    PROX_V_FIELD_NUMBER: _ClassVar[int]
    PILOT_HIGH_V_FIELD_NUMBER: _ClassVar[int]
    PILOT_LOW_V_FIELD_NUMBER: _ClassVar[int]
    SESSION_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENERGY_FIELD_NUMBER: _ClassVar[int]
    AC_MEASUREMENT_GRID_FIELD_NUMBER: _ClassVar[int]
    AC_MEASUREMENT_VEHICLE_FIELD_NUMBER: _ClassVar[int]
    GROUND_RESISTANCE_OHMS_FIELD_NUMBER: _ClassVar[int]
    LINE1_EARTH_VRMS_FIELD_NUMBER: _ClassVar[int]
    NEUTRAL_EARTH_VRMS_FIELD_NUMBER: _ClassVar[int]
    FAULT_STATUS_FIELD_NUMBER: _ClassVar[int]
    RECENT_FAULT_STATUS_LATCHED_ALERTS_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    INSTANTANEOUS_POWER_WATTS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTANTANEOUS_LINE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    OCPP_STATUS_FIELD_NUMBER: _ClassVar[int]
    EVSE_NOT_READY_REASONS_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    DRY_CONTACT_CONTROL_STATE_FIELD_NUMBER: _ClassVar[int]
    SMART_CHARGING_REASON_FIELD_NUMBER: _ClassVar[int]
    uptime_s: int
    alerts: _containers.RepeatedScalarFieldContainer[int]
    contactor_closed: bool
    vehicle_connected: bool
    pcba_temp_c: float
    handle_temp_c: float
    mcu_temp_c: float
    input_thermopile_v: float
    prox_v: float
    pilot_high_v: float
    pilot_low_v: float
    session_duration_s: int
    session_energy: _energy_pb2.AccumulatedEnergy
    ac_measurement_grid: _energy_pb2.InstACMeasurement
    ac_measurement_vehicle: _energy_pb2.InstACMeasurement
    ground_resistance_ohms: float
    line1_earth_vrms: float
    neutral_earth_vrms: float
    fault_status: WCFaultStatusState
    recent_fault_status_latched_alerts: _containers.RepeatedCompositeFieldContainer[WCFaultStatusLatchedAlert]
    vin: _device_pb2.VIN
    instantaneous_power_watts: _wrappers_pb2.FloatValue
    scheduled_charging_status: WCChargeScheduleChargingStatus
    instantaneous_line_current: _wrappers_pb2.FloatValue
    ocpp_status: WCOcppStatus
    evse_not_ready_reasons: _containers.RepeatedScalarFieldContainer[WCEvseNotReadyReason]
    powershare_session_state: WCPowershareSessionState
    dry_contact_control_state: WCDryContactControlState
    smart_charging_reason: WCSmartChargingReason

    def __init__(self, uptime_s: _Optional[int]=..., alerts: _Optional[_Iterable[int]]=..., contactor_closed: bool=..., vehicle_connected: bool=..., pcba_temp_c: _Optional[float]=..., handle_temp_c: _Optional[float]=..., mcu_temp_c: _Optional[float]=..., input_thermopile_v: _Optional[float]=..., prox_v: _Optional[float]=..., pilot_high_v: _Optional[float]=..., pilot_low_v: _Optional[float]=..., session_duration_s: _Optional[int]=..., session_energy: _Optional[_Union[_energy_pb2.AccumulatedEnergy, _Mapping]]=..., ac_measurement_grid: _Optional[_Union[_energy_pb2.InstACMeasurement, _Mapping]]=..., ac_measurement_vehicle: _Optional[_Union[_energy_pb2.InstACMeasurement, _Mapping]]=..., ground_resistance_ohms: _Optional[float]=..., line1_earth_vrms: _Optional[float]=..., neutral_earth_vrms: _Optional[float]=..., fault_status: _Optional[_Union[WCFaultStatusState, str]]=..., recent_fault_status_latched_alerts: _Optional[_Iterable[_Union[WCFaultStatusLatchedAlert, _Mapping]]]=..., vin: _Optional[_Union[_device_pb2.VIN, _Mapping]]=..., instantaneous_power_watts: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., scheduled_charging_status: _Optional[_Union[WCChargeScheduleChargingStatus, str]]=..., instantaneous_line_current: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., ocpp_status: _Optional[_Union[WCOcppStatus, str]]=..., evse_not_ready_reasons: _Optional[_Iterable[_Union[WCEvseNotReadyReason, str]]]=..., powershare_session_state: _Optional[_Union[WCPowershareSessionState, str]]=..., dry_contact_control_state: _Optional[_Union[WCDryContactControlState, str]]=..., smart_charging_reason: _Optional[_Union[WCSmartChargingReason, str]]=...) -> None:
        ...

class WCLifetimeStats(_message.Message):
    __slots__ = ('uptime_s', 'alert_count', 'contactor_cycles', 'contactor_cycles_loaded', 'connector_cycles', 'thermal_foldbacks', 'avg_startup_temp_c', 'charge_starts', 'charging_time_s', 'charging_energy')
    UPTIME_S_FIELD_NUMBER: _ClassVar[int]
    ALERT_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTACTOR_CYCLES_FIELD_NUMBER: _ClassVar[int]
    CONTACTOR_CYCLES_LOADED_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CYCLES_FIELD_NUMBER: _ClassVar[int]
    THERMAL_FOLDBACKS_FIELD_NUMBER: _ClassVar[int]
    AVG_STARTUP_TEMP_C_FIELD_NUMBER: _ClassVar[int]
    CHARGE_STARTS_FIELD_NUMBER: _ClassVar[int]
    CHARGING_TIME_S_FIELD_NUMBER: _ClassVar[int]
    CHARGING_ENERGY_FIELD_NUMBER: _ClassVar[int]
    uptime_s: int
    alert_count: int
    contactor_cycles: int
    contactor_cycles_loaded: int
    connector_cycles: int
    thermal_foldbacks: int
    avg_startup_temp_c: float
    charge_starts: int
    charging_time_s: int
    charging_energy: _energy_pb2.AccumulatedEnergy

    def __init__(self, uptime_s: _Optional[int]=..., alert_count: _Optional[int]=..., contactor_cycles: _Optional[int]=..., contactor_cycles_loaded: _Optional[int]=..., connector_cycles: _Optional[int]=..., thermal_foldbacks: _Optional[int]=..., avg_startup_temp_c: _Optional[float]=..., charge_starts: _Optional[int]=..., charging_time_s: _Optional[int]=..., charging_energy: _Optional[_Union[_energy_pb2.AccumulatedEnergy, _Mapping]]=...) -> None:
        ...

class WCLoadSharingFixedLimitConfig(_message.Message):
    __slots__ = ('network_limit_amps',)
    NETWORK_LIMIT_AMPS_FIELD_NUMBER: _ClassVar[int]
    network_limit_amps: int

    def __init__(self, network_limit_amps: _Optional[int]=...) -> None:
        ...

class WCLoadSharingConductorLimitConfig(_message.Message):
    __slots__ = ('conductor_limit_amps',)
    CONDUCTOR_LIMIT_AMPS_FIELD_NUMBER: _ClassVar[int]
    conductor_limit_amps: int

    def __init__(self, conductor_limit_amps: _Optional[int]=...) -> None:
        ...

class WCLoadSharingSettings(_message.Message):
    __slots__ = ('fixed_limit', 'conductor_limit')
    FIXED_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CONDUCTOR_LIMIT_FIELD_NUMBER: _ClassVar[int]
    fixed_limit: WCLoadSharingFixedLimitConfig
    conductor_limit: WCLoadSharingConductorLimitConfig

    def __init__(self, fixed_limit: _Optional[_Union[WCLoadSharingFixedLimitConfig, _Mapping]]=..., conductor_limit: _Optional[_Union[WCLoadSharingConductorLimitConfig, _Mapping]]=...) -> None:
        ...

class WCLoadSharingLimits(_message.Message):
    __slots__ = ('max_participants',)
    MAX_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    max_participants: int

    def __init__(self, max_participants: _Optional[int]=...) -> None:
        ...

class WCLoadSharingNetworkStatus(_message.Message):
    __slots__ = ('network_charging_inhibitors',)
    NETWORK_CHARGING_INHIBITORS_FIELD_NUMBER: _ClassVar[int]
    network_charging_inhibitors: _containers.RepeatedScalarFieldContainer[WCLoadSharingNetworkChargingInhibitor]

    def __init__(self, network_charging_inhibitors: _Optional[_Iterable[_Union[WCLoadSharingNetworkChargingInhibitor, str]]]=...) -> None:
        ...

class WCLoadSharingConfig(_message.Message):
    __slots__ = ('version', 'participant_dins', 'fixed_limit', 'settings', 'charging_enabled')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_DINS_FIELD_NUMBER: _ClassVar[int]
    FIXED_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CHARGING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    version: int
    participant_dins: _containers.RepeatedCompositeFieldContainer[_device_pb2.Din]
    fixed_limit: WCLoadSharingFixedLimitConfig
    settings: WCLoadSharingSettings
    charging_enabled: bool

    def __init__(self, version: _Optional[int]=..., participant_dins: _Optional[_Iterable[_Union[_device_pb2.Din, _Mapping]]]=..., fixed_limit: _Optional[_Union[WCLoadSharingFixedLimitConfig, _Mapping]]=..., settings: _Optional[_Union[WCLoadSharingSettings, _Mapping]]=..., charging_enabled: bool=...) -> None:
        ...

class WCPpuConfig(_message.Message):
    __slots__ = ('session_reporting_mode',)
    SESSION_REPORTING_MODE_FIELD_NUMBER: _ClassVar[int]
    session_reporting_mode: WCPpuSessionReportingMode

    def __init__(self, session_reporting_mode: _Optional[_Union[WCPpuSessionReportingMode, str]]=...) -> None:
        ...

class WCOperationalSettingsConfig(_message.Message):
    __slots__ = ('operational_mode', 'emit_increased_telemetry')
    OPERATIONAL_MODE_FIELD_NUMBER: _ClassVar[int]
    EMIT_INCREASED_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    operational_mode: WCOperationalMode
    emit_increased_telemetry: bool

    def __init__(self, operational_mode: _Optional[_Union[WCOperationalMode, str]]=..., emit_increased_telemetry: bool=...) -> None:
        ...

class WCMeterInterface(_message.Message):
    __slots__ = ('neurio',)
    NEURIO_FIELD_NUMBER: _ClassVar[int]
    neurio: _neurio_meter_api_pb2.NeurioMeterInterface

    def __init__(self, neurio: _Optional[_Union[_neurio_meter_api_pb2.NeurioMeterInterface, _Mapping]]=...) -> None:
        ...

class WCDryContactConfig(_message.Message):
    __slots__ = ('enabled', 'default_state', 'disable_charging', 'max_current_amps', 'germany_14a')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STATE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CHARGING_FIELD_NUMBER: _ClassVar[int]
    MAX_CURRENT_AMPS_FIELD_NUMBER: _ClassVar[int]
    GERMANY_14A_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    default_state: WCDryContactDefaultState
    disable_charging: bool
    max_current_amps: int
    germany_14a: bool

    def __init__(self, enabled: bool=..., default_state: _Optional[_Union[WCDryContactDefaultState, str]]=..., disable_charging: bool=..., max_current_amps: _Optional[int]=..., germany_14a: bool=...) -> None:
        ...

class WCTimeZoneTransition(_message.Message):
    __slots__ = ('timestamp', 'local_time_utc_offset')
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIME_UTC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    local_time_utc_offset: int

    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., local_time_utc_offset: _Optional[int]=...) -> None:
        ...

class WCTimeZoneInfo(_message.Message):
    __slots__ = ('transitions',)
    TRANSITIONS_FIELD_NUMBER: _ClassVar[int]
    transitions: _containers.RepeatedCompositeFieldContainer[WCTimeZoneTransition]

    def __init__(self, transitions: _Optional[_Iterable[_Union[WCTimeZoneTransition, _Mapping]]]=...) -> None:
        ...

class WCTimeZone(_message.Message):
    __slots__ = ('time_zone_id', 'time_zone_info')
    TIME_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_INFO_FIELD_NUMBER: _ClassVar[int]
    time_zone_id: str
    time_zone_info: WCTimeZoneInfo

    def __init__(self, time_zone_id: _Optional[str]=..., time_zone_info: _Optional[_Union[WCTimeZoneInfo, _Mapping]]=...) -> None:
        ...

class WCMIDConfig(_message.Message):
    __slots__ = ('enabled', 'time_zone')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    time_zone: WCTimeZone

    def __init__(self, enabled: bool=..., time_zone: _Optional[_Union[WCTimeZone, _Mapping]]=...) -> None:
        ...

class WCSettings(_message.Message):
    __slots__ = ('max_output_current_amps', 'gmi_mode', 'country', 'third_party_vehicle_mode', 'load_sharing_config', 'dry_contact', 'mid_config')
    MAX_OUTPUT_CURRENT_AMPS_FIELD_NUMBER: _ClassVar[int]
    GMI_MODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_VEHICLE_MODE_FIELD_NUMBER: _ClassVar[int]
    LOAD_SHARING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DRY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    MID_CONFIG_FIELD_NUMBER: _ClassVar[int]
    max_output_current_amps: int
    gmi_mode: WCGroundMonitorMode
    country: str
    third_party_vehicle_mode: WCThirdPartyVehicleMode
    load_sharing_config: WCLoadSharingConfig
    dry_contact: WCDryContactConfig
    mid_config: WCMIDConfig

    def __init__(self, max_output_current_amps: _Optional[int]=..., gmi_mode: _Optional[_Union[WCGroundMonitorMode, str]]=..., country: _Optional[str]=..., third_party_vehicle_mode: _Optional[_Union[WCThirdPartyVehicleMode, str]]=..., load_sharing_config: _Optional[_Union[WCLoadSharingConfig, _Mapping]]=..., dry_contact: _Optional[_Union[WCDryContactConfig, _Mapping]]=..., mid_config: _Optional[_Union[WCMIDConfig, _Mapping]]=...) -> None:
        ...

class WCGenealogy(_message.Message):
    __slots__ = ('region', 'handle_type', 'hardware_features', 'sub_usage_id')
    REGION_FIELD_NUMBER: _ClassVar[int]
    HANDLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    SUB_USAGE_ID_FIELD_NUMBER: _ClassVar[int]
    region: int
    handle_type: int
    hardware_features: int
    sub_usage_id: int

    def __init__(self, region: _Optional[int]=..., handle_type: _Optional[int]=..., hardware_features: _Optional[int]=..., sub_usage_id: _Optional[int]=...) -> None:
        ...

class ComplianceCRC32(_message.Message):
    __slots__ = ('name', 'crc32')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRC32_FIELD_NUMBER: _ClassVar[int]
    name: str
    crc32: int

    def __init__(self, name: _Optional[str]=..., crc32: _Optional[int]=...) -> None:
        ...

class WCLoadSharingFollowerState(_message.Message):
    __slots__ = ('version', 'charge_request', 'load_current_amps', 'vehicle_connected', 'alert_count', 'contactor_closed', 'pilot_current_amps', 'individual_pilot_current_amps')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHARGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LOAD_CURRENT_AMPS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    ALERT_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTACTOR_CLOSED_FIELD_NUMBER: _ClassVar[int]
    PILOT_CURRENT_AMPS_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_PILOT_CURRENT_AMPS_FIELD_NUMBER: _ClassVar[int]
    version: int
    charge_request: bool
    load_current_amps: float
    vehicle_connected: bool
    alert_count: int
    contactor_closed: bool
    pilot_current_amps: int
    individual_pilot_current_amps: int

    def __init__(self, version: _Optional[int]=..., charge_request: bool=..., load_current_amps: _Optional[float]=..., vehicle_connected: bool=..., alert_count: _Optional[int]=..., contactor_closed: bool=..., pilot_current_amps: _Optional[int]=..., individual_pilot_current_amps: _Optional[int]=...) -> None:
        ...

class WCLoadSharingLeaderCommand(_message.Message):
    __slots__ = ('charge_allowed', 'pilot_current_amps')
    CHARGE_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    PILOT_CURRENT_AMPS_FIELD_NUMBER: _ClassVar[int]
    charge_allowed: bool
    pilot_current_amps: int

    def __init__(self, charge_allowed: bool=..., pilot_current_amps: _Optional[int]=...) -> None:
        ...

class WCLoadSharingLeaderState(_message.Message):
    __slots__ = ('version', 'network_current_limit_amps', 'fallback_current_amps', 'round_robin_index', 'charging_enabled', 'active_unit_count')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CURRENT_LIMIT_AMPS_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_CURRENT_AMPS_FIELD_NUMBER: _ClassVar[int]
    ROUND_ROBIN_INDEX_FIELD_NUMBER: _ClassVar[int]
    CHARGING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_UNIT_COUNT_FIELD_NUMBER: _ClassVar[int]
    version: int
    network_current_limit_amps: int
    fallback_current_amps: int
    round_robin_index: int
    charging_enabled: bool
    active_unit_count: int

    def __init__(self, version: _Optional[int]=..., network_current_limit_amps: _Optional[int]=..., fallback_current_amps: _Optional[int]=..., round_robin_index: _Optional[int]=..., charging_enabled: bool=..., active_unit_count: _Optional[int]=...) -> None:
        ...

class WCLoadSharingDeviceEntry(_message.Message):
    __slots__ = ('din', 'leader_command', 'follower_state', 'mia')
    DIN_FIELD_NUMBER: _ClassVar[int]
    LEADER_COMMAND_FIELD_NUMBER: _ClassVar[int]
    FOLLOWER_STATE_FIELD_NUMBER: _ClassVar[int]
    MIA_FIELD_NUMBER: _ClassVar[int]
    din: _device_pb2.Din
    leader_command: WCLoadSharingLeaderCommand
    follower_state: WCLoadSharingFollowerState
    mia: bool

    def __init__(self, din: _Optional[_Union[_device_pb2.Din, _Mapping]]=..., leader_command: _Optional[_Union[WCLoadSharingLeaderCommand, _Mapping]]=..., follower_state: _Optional[_Union[WCLoadSharingFollowerState, _Mapping]]=..., mia: bool=...) -> None:
        ...

class WCLoadSharingNetworkState(_message.Message):
    __slots__ = ('devices', 'leader_state', 'settings', 'status', 'limits')
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    LEADER_STATE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[WCLoadSharingDeviceEntry]
    leader_state: WCLoadSharingLeaderState
    settings: WCLoadSharingSettings
    status: WCLoadSharingNetworkStatus
    limits: WCLoadSharingLimits

    def __init__(self, devices: _Optional[_Iterable[_Union[WCLoadSharingDeviceEntry, _Mapping]]]=..., leader_state: _Optional[_Union[WCLoadSharingLeaderState, _Mapping]]=..., settings: _Optional[_Union[WCLoadSharingSettings, _Mapping]]=..., status: _Optional[_Union[WCLoadSharingNetworkStatus, _Mapping]]=..., limits: _Optional[_Union[WCLoadSharingLimits, _Mapping]]=...) -> None:
        ...

class WCProvisionalOperationalParams(_message.Message):
    __slots__ = ('limit_current_max_amps', 'limit_timeout_s', 'inhibit_charging')
    LIMIT_CURRENT_MAX_AMPS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TIMEOUT_S_FIELD_NUMBER: _ClassVar[int]
    INHIBIT_CHARGING_FIELD_NUMBER: _ClassVar[int]
    limit_current_max_amps: int
    limit_timeout_s: int
    inhibit_charging: bool

    def __init__(self, limit_current_max_amps: _Optional[int]=..., limit_timeout_s: _Optional[int]=..., inhibit_charging: bool=...) -> None:
        ...

class WCAccessControlEntry(_message.Message):
    __slots__ = ('vin', 'name', 'model', 'model_year', 'drive_type')
    VIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_YEAR_FIELD_NUMBER: _ClassVar[int]
    DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    vin: _device_pb2.VIN
    name: str
    model: WCTeslaVehicleModel
    model_year: int
    drive_type: WCTeslaVehicleDriveType

    def __init__(self, vin: _Optional[_Union[_device_pb2.VIN, _Mapping]]=..., name: _Optional[str]=..., model: _Optional[_Union[WCTeslaVehicleModel, str]]=..., model_year: _Optional[int]=..., drive_type: _Optional[_Union[WCTeslaVehicleDriveType, str]]=...) -> None:
        ...

class WCChargeScheduleTimePeriod(_message.Message):
    __slots__ = ('start_seconds', 'end_seconds')
    START_SECONDS_FIELD_NUMBER: _ClassVar[int]
    END_SECONDS_FIELD_NUMBER: _ClassVar[int]
    start_seconds: int
    end_seconds: int

    def __init__(self, start_seconds: _Optional[int]=..., end_seconds: _Optional[int]=...) -> None:
        ...

class WCChargeScheduleDayTimePeriods(_message.Message):
    __slots__ = ('time_periods', 'day_bitmask')
    TIME_PERIODS_FIELD_NUMBER: _ClassVar[int]
    DAY_BITMASK_FIELD_NUMBER: _ClassVar[int]
    time_periods: _containers.RepeatedCompositeFieldContainer[WCChargeScheduleTimePeriod]
    day_bitmask: int

    def __init__(self, time_periods: _Optional[_Iterable[_Union[WCChargeScheduleTimePeriod, _Mapping]]]=..., day_bitmask: _Optional[int]=...) -> None:
        ...

class WCChargeSchedule(_message.Message):
    __slots__ = ('day_time_periods',)
    DAY_TIME_PERIODS_FIELD_NUMBER: _ClassVar[int]
    day_time_periods: _containers.RepeatedCompositeFieldContainer[WCChargeScheduleDayTimePeriods]

    def __init__(self, day_time_periods: _Optional[_Iterable[_Union[WCChargeScheduleDayTimePeriods, _Mapping]]]=...) -> None:
        ...

class WCChargeScheduleDelay(_message.Message):
    __slots__ = ('max_delay_seconds',)
    MAX_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    max_delay_seconds: int

    def __init__(self, max_delay_seconds: _Optional[int]=...) -> None:
        ...

class WCChargeScheduleConfig(_message.Message):
    __slots__ = ('enable_schedule', 'schedule', 'delay')
    ENABLE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    enable_schedule: bool
    schedule: WCChargeSchedule
    delay: WCChargeScheduleDelay

    def __init__(self, enable_schedule: bool=..., schedule: _Optional[_Union[WCChargeSchedule, _Mapping]]=..., delay: _Optional[_Union[WCChargeScheduleDelay, _Mapping]]=...) -> None:
        ...

class WCChargeScheduleConfigStatus(_message.Message):
    __slots__ = ('config', 'error')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    config: WCChargeScheduleConfig
    error: WCChargeScheduleConfigError

    def __init__(self, config: _Optional[_Union[WCChargeScheduleConfig, _Mapping]]=..., error: _Optional[_Union[WCChargeScheduleConfigError, str]]=...) -> None:
        ...

class WCChargeCommand(_message.Message):
    __slots__ = ('charging_command',)
    CHARGING_COMMAND_FIELD_NUMBER: _ClassVar[int]
    charging_command: WCChargingCommand

    def __init__(self, charging_command: _Optional[_Union[WCChargingCommand, str]]=...) -> None:
        ...

class WCOcppSettings(_message.Message):
    __slots__ = ('connection_url', 'chargepoint_id', 'version', 'security_profile', 'enable', 'provider_name', 'scope')
    CONNECTION_URL_FIELD_NUMBER: _ClassVar[int]
    CHARGEPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SECURITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    connection_url: str
    chargepoint_id: str
    version: WCOcppVersion
    security_profile: WCOcppSecurityProfile
    enable: bool
    provider_name: str
    scope: WCOcppScope

    def __init__(self, connection_url: _Optional[str]=..., chargepoint_id: _Optional[str]=..., version: _Optional[_Union[WCOcppVersion, str]]=..., security_profile: _Optional[_Union[WCOcppSecurityProfile, str]]=..., enable: bool=..., provider_name: _Optional[str]=..., scope: _Optional[_Union[WCOcppScope, str]]=...) -> None:
        ...

class WCOcppAuthorizationData(_message.Message):
    __slots__ = ('id_tag',)
    ID_TAG_FIELD_NUMBER: _ClassVar[int]
    id_tag: str

    def __init__(self, id_tag: _Optional[str]=...) -> None:
        ...

class WCOcppAuthorizationList(_message.Message):
    __slots__ = ('auth_data',)
    AUTH_DATA_FIELD_NUMBER: _ClassVar[int]
    auth_data: _containers.RepeatedCompositeFieldContainer[WCOcppAuthorizationData]

    def __init__(self, auth_data: _Optional[_Iterable[_Union[WCOcppAuthorizationData, _Mapping]]]=...) -> None:
        ...

class WCVehicleToHomeConfig(_message.Message):
    __slots__ = ('site_controller_din', 'modbus_node_id')
    SITE_CONTROLLER_DIN_FIELD_NUMBER: _ClassVar[int]
    MODBUS_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    site_controller_din: _device_pb2.Din
    modbus_node_id: int

    def __init__(self, site_controller_din: _Optional[_Union[_device_pb2.Din, _Mapping]]=..., modbus_node_id: _Optional[int]=...) -> None:
        ...

class WCAPIGetVitalsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetVitalsResponse(_message.Message):
    __slots__ = ('vitals',)
    VITALS_FIELD_NUMBER: _ClassVar[int]
    vitals: WCVitals

    def __init__(self, vitals: _Optional[_Union[WCVitals, _Mapping]]=...) -> None:
        ...

class WCAPIGetLifetimeStatsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetLifetimeStatsResponse(_message.Message):
    __slots__ = ('lifetime_stats',)
    LIFETIME_STATS_FIELD_NUMBER: _ClassVar[int]
    lifetime_stats: WCLifetimeStats

    def __init__(self, lifetime_stats: _Optional[_Union[WCLifetimeStats, _Mapping]]=...) -> None:
        ...

class WCAPIGetConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetConfigResponse(_message.Message):
    __slots__ = ('settings', 'wifi_config', 'wifi', 'meters', 'charge_schedule', 'ocpp_settings', 'vehicle_to_home', 'time_source')
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    WIFI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    METERS_FIELD_NUMBER: _ClassVar[int]
    CHARGE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    OCPP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_TO_HOME_FIELD_NUMBER: _ClassVar[int]
    TIME_SOURCE_FIELD_NUMBER: _ClassVar[int]
    settings: WCSettings
    wifi_config: _networking_pb2.WifiConfig
    wifi: _networking_pb2.NetworkInterface
    meters: _containers.RepeatedCompositeFieldContainer[WCMeterInterface]
    charge_schedule: WCChargeScheduleConfig
    ocpp_settings: WCOcppSettings
    vehicle_to_home: WCVehicleToHomeConfig
    time_source: WCTimeSource

    def __init__(self, settings: _Optional[_Union[WCSettings, _Mapping]]=..., wifi_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., meters: _Optional[_Iterable[_Union[WCMeterInterface, _Mapping]]]=..., charge_schedule: _Optional[_Union[WCChargeScheduleConfig, _Mapping]]=..., ocpp_settings: _Optional[_Union[WCOcppSettings, _Mapping]]=..., vehicle_to_home: _Optional[_Union[WCVehicleToHomeConfig, _Mapping]]=..., time_source: _Optional[_Union[WCTimeSource, str]]=...) -> None:
        ...

class WCAPIConfigureSettingsRequest(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: WCSettings

    def __init__(self, settings: _Optional[_Union[WCSettings, _Mapping]]=...) -> None:
        ...

class WCAPIConfigureSettingsResponse(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: WCSettings

    def __init__(self, settings: _Optional[_Union[WCSettings, _Mapping]]=...) -> None:
        ...

class WCAPIGetSystemInfoRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetSystemInfoResponse(_message.Message):
    __slots__ = ('genealogy', 'compliance_crcs')
    GENEALOGY_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_CRCS_FIELD_NUMBER: _ClassVar[int]
    genealogy: WCGenealogy
    compliance_crcs: _containers.RepeatedCompositeFieldContainer[ComplianceCRC32]

    def __init__(self, genealogy: _Optional[_Union[WCGenealogy, _Mapping]]=..., compliance_crcs: _Optional[_Iterable[_Union[ComplianceCRC32, _Mapping]]]=...) -> None:
        ...

class WCAPIGetLoadSharingNetworkStateRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetLoadSharingNetworkStateResponse(_message.Message):
    __slots__ = ('network_state',)
    NETWORK_STATE_FIELD_NUMBER: _ClassVar[int]
    network_state: WCLoadSharingNetworkState

    def __init__(self, network_state: _Optional[_Union[WCLoadSharingNetworkState, _Mapping]]=...) -> None:
        ...

class WCAPIPushLoadSharingFollowerStateRequest(_message.Message):
    __slots__ = ('follower_state',)
    FOLLOWER_STATE_FIELD_NUMBER: _ClassVar[int]
    follower_state: WCLoadSharingFollowerState

    def __init__(self, follower_state: _Optional[_Union[WCLoadSharingFollowerState, _Mapping]]=...) -> None:
        ...

class WCAPIPushLoadSharingFollowerStateResponse(_message.Message):
    __slots__ = ('leader_state', 'leader_command')
    LEADER_STATE_FIELD_NUMBER: _ClassVar[int]
    LEADER_COMMAND_FIELD_NUMBER: _ClassVar[int]
    leader_state: WCLoadSharingLeaderState
    leader_command: WCLoadSharingLeaderCommand

    def __init__(self, leader_state: _Optional[_Union[WCLoadSharingLeaderState, _Mapping]]=..., leader_command: _Optional[_Union[WCLoadSharingLeaderCommand, _Mapping]]=...) -> None:
        ...

class WCAPIPushLoadSharingLeaderCommandRequest(_message.Message):
    __slots__ = ('leader_state', 'leader_command')
    LEADER_STATE_FIELD_NUMBER: _ClassVar[int]
    LEADER_COMMAND_FIELD_NUMBER: _ClassVar[int]
    leader_state: WCLoadSharingLeaderState
    leader_command: WCLoadSharingLeaderCommand

    def __init__(self, leader_state: _Optional[_Union[WCLoadSharingLeaderState, _Mapping]]=..., leader_command: _Optional[_Union[WCLoadSharingLeaderCommand, _Mapping]]=...) -> None:
        ...

class WCAPIPushLoadSharingLeaderCommandResponse(_message.Message):
    __slots__ = ('follower_state',)
    FOLLOWER_STATE_FIELD_NUMBER: _ClassVar[int]
    follower_state: WCLoadSharingFollowerState

    def __init__(self, follower_state: _Optional[_Union[WCLoadSharingFollowerState, _Mapping]]=...) -> None:
        ...

class WCAPISetLoadSharingNetworkOperationRequest(_message.Message):
    __slots__ = ('charging_enabled',)
    CHARGING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    charging_enabled: bool

    def __init__(self, charging_enabled: bool=...) -> None:
        ...

class WCAPISetLoadSharingNetworkOperationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIConfigureLoadSharingSettingsRequest(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: WCLoadSharingSettings

    def __init__(self, settings: _Optional[_Union[WCLoadSharingSettings, _Mapping]]=...) -> None:
        ...

class WCAPIConfigureLoadSharingSettingsResponse(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: WCLoadSharingSettings

    def __init__(self, settings: _Optional[_Union[WCLoadSharingSettings, _Mapping]]=...) -> None:
        ...

class WCAPIPushLoadSharingConfigRequest(_message.Message):
    __slots__ = ('load_sharing_config',)
    LOAD_SHARING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    load_sharing_config: WCLoadSharingConfig

    def __init__(self, load_sharing_config: _Optional[_Union[WCLoadSharingConfig, _Mapping]]=...) -> None:
        ...

class WCAPIPushLoadSharingConfigResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIConfigurePpuSettingsRequest(_message.Message):
    __slots__ = ('ppu_config',)
    PPU_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ppu_config: WCPpuConfig

    def __init__(self, ppu_config: _Optional[_Union[WCPpuConfig, _Mapping]]=...) -> None:
        ...

class WCAPIConfigurePpuSettingsResponse(_message.Message):
    __slots__ = ('ppu_config',)
    PPU_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ppu_config: WCPpuConfig

    def __init__(self, ppu_config: _Optional[_Union[WCPpuConfig, _Mapping]]=...) -> None:
        ...

class WCAPIGetPpuSettingsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetPpuSettingsResponse(_message.Message):
    __slots__ = ('ppu_config',)
    PPU_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ppu_config: WCPpuConfig

    def __init__(self, ppu_config: _Optional[_Union[WCPpuConfig, _Mapping]]=...) -> None:
        ...

class WCAPIConfigureOperationalSettingsRequest(_message.Message):
    __slots__ = ('operational_settings_config',)
    OPERATIONAL_SETTINGS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    operational_settings_config: WCOperationalSettingsConfig

    def __init__(self, operational_settings_config: _Optional[_Union[WCOperationalSettingsConfig, _Mapping]]=...) -> None:
        ...

class WCAPIConfigureOperationalSettingsResponse(_message.Message):
    __slots__ = ('operational_settings_config',)
    OPERATIONAL_SETTINGS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    operational_settings_config: WCOperationalSettingsConfig

    def __init__(self, operational_settings_config: _Optional[_Union[WCOperationalSettingsConfig, _Mapping]]=...) -> None:
        ...

class WCAPIGetOperationalSettingsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetOperationalSettingsResponse(_message.Message):
    __slots__ = ('operational_settings_config',)
    OPERATIONAL_SETTINGS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    operational_settings_config: WCOperationalSettingsConfig

    def __init__(self, operational_settings_config: _Optional[_Union[WCOperationalSettingsConfig, _Mapping]]=...) -> None:
        ...

class WCAPISetProvisionalOperationalParamsRequest(_message.Message):
    __slots__ = ('prov_op_params',)
    PROV_OP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    prov_op_params: WCProvisionalOperationalParams

    def __init__(self, prov_op_params: _Optional[_Union[WCProvisionalOperationalParams, _Mapping]]=...) -> None:
        ...

class WCAPISetProvisionalOperationalParamsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetProvisionalOperationalParamsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetProvisionalOperationalParamsResponse(_message.Message):
    __slots__ = ('prov_op_params', 'configured_current_limit_amps')
    PROV_OP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_CURRENT_LIMIT_AMPS_FIELD_NUMBER: _ClassVar[int]
    prov_op_params: WCProvisionalOperationalParams
    configured_current_limit_amps: int

    def __init__(self, prov_op_params: _Optional[_Union[WCProvisionalOperationalParams, _Mapping]]=..., configured_current_limit_amps: _Optional[int]=...) -> None:
        ...

class WCAPIGetAccessControlSettingsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetAccessControlSettingsResponse(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[WCAccessControlEntry]

    def __init__(self, entries: _Optional[_Iterable[_Union[WCAccessControlEntry, _Mapping]]]=...) -> None:
        ...

class WCAPIConfigureAccessControlSettingsRequest(_message.Message):
    __slots__ = ('operation', 'vin', 'name')
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    operation: WCConfigureAccessControlOperation
    vin: _device_pb2.VIN
    name: str

    def __init__(self, operation: _Optional[_Union[WCConfigureAccessControlOperation, str]]=..., vin: _Optional[_Union[_device_pb2.VIN, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class WCAPIConfigureAccessControlSettingsResponse(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[WCAccessControlEntry]

    def __init__(self, entries: _Optional[_Iterable[_Union[WCAccessControlEntry, _Mapping]]]=...) -> None:
        ...

class WCAPIGetRecentVehiclesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetRecentVehiclesResponse(_message.Message):
    __slots__ = ('recent_vehicles',)
    RECENT_VEHICLES_FIELD_NUMBER: _ClassVar[int]
    recent_vehicles: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, recent_vehicles: _Optional[_Iterable[str]]=...) -> None:
        ...

class WCAPIPushPpuAuthorizationStateRequest(_message.Message):
    __slots__ = ('authorized', 'auth_uuid')
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    AUTH_UUID_FIELD_NUMBER: _ClassVar[int]
    authorized: bool
    auth_uuid: _device_pb2.UUIDv4Bytes

    def __init__(self, authorized: bool=..., auth_uuid: _Optional[_Union[_device_pb2.UUIDv4Bytes, _Mapping]]=...) -> None:
        ...

class WCAPIPushPpuAuthorizationStateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIConfigureChargeScheduleRequest(_message.Message):
    __slots__ = ('config', 'time_zone')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    config: WCChargeScheduleConfig
    time_zone: WCTimeZone

    def __init__(self, config: _Optional[_Union[WCChargeScheduleConfig, _Mapping]]=..., time_zone: _Optional[_Union[WCTimeZone, _Mapping]]=...) -> None:
        ...

class WCAPIConfigureChargeScheduleResponse(_message.Message):
    __slots__ = ('error',)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: WCChargeScheduleError

    def __init__(self, error: _Optional[_Union[WCChargeScheduleError, str]]=...) -> None:
        ...

class WCAPIConfigureThirdPartyVehicleModeRequest(_message.Message):
    __slots__ = ('third_party_vehicle_mode',)
    THIRD_PARTY_VEHICLE_MODE_FIELD_NUMBER: _ClassVar[int]
    third_party_vehicle_mode: WCThirdPartyVehicleMode

    def __init__(self, third_party_vehicle_mode: _Optional[_Union[WCThirdPartyVehicleMode, str]]=...) -> None:
        ...

class WCAPIConfigureThirdPartyVehicleModeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIPushChargeCommandRequest(_message.Message):
    __slots__ = ('charge_command',)
    CHARGE_COMMAND_FIELD_NUMBER: _ClassVar[int]
    charge_command: WCChargeCommand

    def __init__(self, charge_command: _Optional[_Union[WCChargeCommand, _Mapping]]=...) -> None:
        ...

class WCAPIPushChargeCommandResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIConfigureHomeSiteControllerRequest(_message.Message):
    __slots__ = ('din', 'modbus_node_id', 'config')
    DIN_FIELD_NUMBER: _ClassVar[int]
    MODBUS_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    din: _device_pb2.Din
    modbus_node_id: int
    config: WCVehicleToHomeConfig

    def __init__(self, din: _Optional[_Union[_device_pb2.Din, _Mapping]]=..., modbus_node_id: _Optional[int]=..., config: _Optional[_Union[WCVehicleToHomeConfig, _Mapping]]=...) -> None:
        ...

class WCAPIConfigureHomeSiteControllerResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: WCVehicleToHomeConfig

    def __init__(self, config: _Optional[_Union[WCVehicleToHomeConfig, _Mapping]]=...) -> None:
        ...

class WCAPIConfigureOcppSettingsRequest(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: WCOcppSettings

    def __init__(self, settings: _Optional[_Union[WCOcppSettings, _Mapping]]=...) -> None:
        ...

class WCAPIConfigureOcppSettingsResponse(_message.Message):
    __slots__ = ('settings', 'status')
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    settings: WCOcppSettings
    status: WCOcppStatus

    def __init__(self, settings: _Optional[_Union[WCOcppSettings, _Mapping]]=..., status: _Optional[_Union[WCOcppStatus, str]]=...) -> None:
        ...

class WCAPISetOcppSecurityParameterRequest(_message.Message):
    __slots__ = ('security_parameter_type', 'security_parameter')
    SECURITY_PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    security_parameter_type: WCOcppSecurityParameterType
    security_parameter: bytes

    def __init__(self, security_parameter_type: _Optional[_Union[WCOcppSecurityParameterType, str]]=..., security_parameter: _Optional[bytes]=...) -> None:
        ...

class WCAPISetOcppSecurityParameterResponse(_message.Message):
    __slots__ = ('status',)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: WCOcppStatus

    def __init__(self, status: _Optional[_Union[WCOcppStatus, str]]=...) -> None:
        ...

class WCAPIGetOcppSecurityParameterRequest(_message.Message):
    __slots__ = ('security_parameter_type',)
    SECURITY_PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    security_parameter_type: WCOcppSecurityParameterType

    def __init__(self, security_parameter_type: _Optional[_Union[WCOcppSecurityParameterType, str]]=...) -> None:
        ...

class WCAPIGetOcppSecurityParameterResponse(_message.Message):
    __slots__ = ('security_parameter_type', 'security_parameter')
    SECURITY_PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    security_parameter_type: WCOcppSecurityParameterType
    security_parameter: bytes

    def __init__(self, security_parameter_type: _Optional[_Union[WCOcppSecurityParameterType, str]]=..., security_parameter: _Optional[bytes]=...) -> None:
        ...

class WCAPIGetOcppLocalAuthListRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIGetOcppLocalAuthListResponse(_message.Message):
    __slots__ = ('auth_list',)
    AUTH_LIST_FIELD_NUMBER: _ClassVar[int]
    auth_list: WCOcppAuthorizationList

    def __init__(self, auth_list: _Optional[_Union[WCOcppAuthorizationList, _Mapping]]=...) -> None:
        ...

class WCAPIConfigureCountryCodeSettingsRequest(_message.Message):
    __slots__ = ('country',)
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    country: str

    def __init__(self, country: _Optional[str]=...) -> None:
        ...

class WCAPIConfigureCountryCodeSettingsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCTargetChargePowerParams(_message.Message):
    __slots__ = ('target_charge_power_w', 'max_charge_power_w', 'max_charge_current_a')
    TARGET_CHARGE_POWER_W_FIELD_NUMBER: _ClassVar[int]
    MAX_CHARGE_POWER_W_FIELD_NUMBER: _ClassVar[int]
    MAX_CHARGE_CURRENT_A_FIELD_NUMBER: _ClassVar[int]
    target_charge_power_w: float
    max_charge_power_w: _wrappers_pb2.FloatValue
    max_charge_current_a: int

    def __init__(self, target_charge_power_w: _Optional[float]=..., max_charge_power_w: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., max_charge_current_a: _Optional[int]=...) -> None:
        ...

class WCSmartChargingCommand(_message.Message):
    __slots__ = ('ttl_seconds', 'charge_disallowed', 'target_charge_power_params')
    TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CHARGE_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHARGE_POWER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ttl_seconds: int
    charge_disallowed: bool
    target_charge_power_params: WCTargetChargePowerParams

    def __init__(self, ttl_seconds: _Optional[int]=..., charge_disallowed: bool=..., target_charge_power_params: _Optional[_Union[WCTargetChargePowerParams, _Mapping]]=...) -> None:
        ...

class WCAPIPushSmartChargingCommandRequest(_message.Message):
    __slots__ = ('command',)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: WCSmartChargingCommand

    def __init__(self, command: _Optional[_Union[WCSmartChargingCommand, _Mapping]]=...) -> None:
        ...

class WCAPIPushSmartChargingCommandResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIRegisterCommercialRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WCAPIRegisterCommercialResponse(_message.Message):
    __slots__ = ('failure',)
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    failure: int

    def __init__(self, failure: _Optional[int]=...) -> None:
        ...

class WCAPIPushPowershareCommandRequest(_message.Message):
    __slots__ = ('site_vehicle_request', 'site_evse_request', 'inverter_config', 'ttl_seconds')
    SITE_VEHICLE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SITE_EVSE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    INVERTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    site_vehicle_request: bytes
    site_evse_request: bytes
    inverter_config: bytes
    ttl_seconds: int

    def __init__(self, site_vehicle_request: _Optional[bytes]=..., site_evse_request: _Optional[bytes]=..., inverter_config: _Optional[bytes]=..., ttl_seconds: _Optional[int]=...) -> None:
        ...

class WCAPIPushPowershareCommandResponse(_message.Message):
    __slots__ = ('site_vehicle_response', 'site_evse_response')
    SITE_VEHICLE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SITE_EVSE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    site_vehicle_response: bytes
    site_evse_response: bytes

    def __init__(self, site_vehicle_response: _Optional[bytes]=..., site_evse_response: _Optional[bytes]=...) -> None:
        ...

class WCMessages(_message.Message):
    __slots__ = ('get_vitals_request', 'get_vitals_response', 'get_lifetime_stats_request', 'get_lifetime_stats_response', 'get_config_request', 'get_config_response', 'configure_settings_request', 'configure_settings_response', 'get_system_info_request', 'get_system_info_response', 'get_load_sharing_network_state_request', 'get_load_sharing_network_state_response', 'push_load_sharing_follower_state_request', 'push_load_sharing_follower_state_response', 'push_load_sharing_leader_command_request', 'push_load_sharing_leader_command_response', 'set_load_sharing_network_operation_request', 'set_load_sharing_network_operation_response', 'configure_load_sharing_settings_request', 'configure_load_sharing_settings_response', 'configure_ppu_settings_request', 'configure_ppu_settings_response', 'get_ppu_settings_request', 'get_ppu_settings_response', 'set_provisional_operational_params_request', 'set_provisional_operational_params_response', 'get_provisional_operational_params_request', 'get_provisional_operational_params_response', 'get_access_control_settings_request', 'get_access_control_settings_response', 'configure_access_control_settings_request', 'configure_access_control_settings_response', 'get_recent_vehicles_request', 'get_recent_vehicles_response', 'push_ppu_authorization_state_request', 'push_ppu_authorization_state_response', 'configure_charge_schedule_request', 'configure_charge_schedule_response', 'push_charge_command_request', 'push_charge_command_response', 'configure_third_party_vehicle_mode_request', 'configure_third_party_vehicle_mode_response', 'configure_home_site_controller_request', 'configure_home_site_controller_response', 'configure_ocpp_settings_request', 'configure_ocpp_settings_response', 'set_ocpp_security_parameter_request', 'set_ocpp_security_parameter_response', 'get_ocpp_security_parameter_request', 'get_ocpp_security_parameter_response', 'configure_operational_settings_request', 'configure_operational_settings_response', 'get_operational_settings_request', 'get_operational_settings_response', 'configure_country_code_settings_request', 'configure_country_code_settings_response', 'push_load_sharing_config_request', 'push_load_sharing_config_response', 'push_smart_charging_command_request', 'push_smart_charging_command_response', 'register_commercial_request', 'register_commercial_response', 'get_ocpp_local_auth_list_request', 'get_ocpp_local_auth_list_response', 'push_powershare_command_request', 'push_powershare_command_response')
    GET_VITALS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_VITALS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_LIFETIME_STATS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_LIFETIME_STATS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_CONFIG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_CONFIG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_SYSTEM_INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_SYSTEM_INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_LOAD_SHARING_NETWORK_STATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_LOAD_SHARING_NETWORK_STATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_LOAD_SHARING_FOLLOWER_STATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_LOAD_SHARING_FOLLOWER_STATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_LOAD_SHARING_LEADER_COMMAND_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_LOAD_SHARING_LEADER_COMMAND_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SET_LOAD_SHARING_NETWORK_OPERATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_LOAD_SHARING_NETWORK_OPERATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_LOAD_SHARING_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_LOAD_SHARING_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_PPU_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_PPU_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_PPU_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_PPU_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SET_PROVISIONAL_OPERATIONAL_PARAMS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_PROVISIONAL_OPERATIONAL_PARAMS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_PROVISIONAL_OPERATIONAL_PARAMS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_PROVISIONAL_OPERATIONAL_PARAMS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_ACCESS_CONTROL_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_ACCESS_CONTROL_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_ACCESS_CONTROL_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_ACCESS_CONTROL_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_RECENT_VEHICLES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_RECENT_VEHICLES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_PPU_AUTHORIZATION_STATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_PPU_AUTHORIZATION_STATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_CHARGE_SCHEDULE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_CHARGE_SCHEDULE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_CHARGE_COMMAND_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_CHARGE_COMMAND_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_THIRD_PARTY_VEHICLE_MODE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_THIRD_PARTY_VEHICLE_MODE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_HOME_SITE_CONTROLLER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_HOME_SITE_CONTROLLER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_OCPP_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_OCPP_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SET_OCPP_SECURITY_PARAMETER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_OCPP_SECURITY_PARAMETER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_OCPP_SECURITY_PARAMETER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_OCPP_SECURITY_PARAMETER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_OPERATIONAL_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_OPERATIONAL_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_OPERATIONAL_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_OPERATIONAL_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_COUNTRY_CODE_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_COUNTRY_CODE_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_LOAD_SHARING_CONFIG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_LOAD_SHARING_CONFIG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_SMART_CHARGING_COMMAND_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_SMART_CHARGING_COMMAND_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REGISTER_COMMERCIAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REGISTER_COMMERCIAL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_OCPP_LOCAL_AUTH_LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_OCPP_LOCAL_AUTH_LIST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_POWERSHARE_COMMAND_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_POWERSHARE_COMMAND_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    get_vitals_request: WCAPIGetVitalsRequest
    get_vitals_response: WCAPIGetVitalsResponse
    get_lifetime_stats_request: WCAPIGetLifetimeStatsRequest
    get_lifetime_stats_response: WCAPIGetLifetimeStatsResponse
    get_config_request: WCAPIGetConfigRequest
    get_config_response: WCAPIGetConfigResponse
    configure_settings_request: WCAPIConfigureSettingsRequest
    configure_settings_response: WCAPIConfigureSettingsResponse
    get_system_info_request: WCAPIGetSystemInfoRequest
    get_system_info_response: WCAPIGetSystemInfoResponse
    get_load_sharing_network_state_request: WCAPIGetLoadSharingNetworkStateRequest
    get_load_sharing_network_state_response: WCAPIGetLoadSharingNetworkStateResponse
    push_load_sharing_follower_state_request: WCAPIPushLoadSharingFollowerStateRequest
    push_load_sharing_follower_state_response: WCAPIPushLoadSharingFollowerStateResponse
    push_load_sharing_leader_command_request: WCAPIPushLoadSharingLeaderCommandRequest
    push_load_sharing_leader_command_response: WCAPIPushLoadSharingLeaderCommandResponse
    set_load_sharing_network_operation_request: WCAPISetLoadSharingNetworkOperationRequest
    set_load_sharing_network_operation_response: WCAPISetLoadSharingNetworkOperationResponse
    configure_load_sharing_settings_request: WCAPIConfigureLoadSharingSettingsRequest
    configure_load_sharing_settings_response: WCAPIConfigureLoadSharingSettingsResponse
    configure_ppu_settings_request: WCAPIConfigurePpuSettingsRequest
    configure_ppu_settings_response: WCAPIConfigurePpuSettingsResponse
    get_ppu_settings_request: WCAPIGetPpuSettingsRequest
    get_ppu_settings_response: WCAPIGetPpuSettingsResponse
    set_provisional_operational_params_request: WCAPISetProvisionalOperationalParamsRequest
    set_provisional_operational_params_response: WCAPISetProvisionalOperationalParamsResponse
    get_provisional_operational_params_request: WCAPIGetProvisionalOperationalParamsRequest
    get_provisional_operational_params_response: WCAPIGetProvisionalOperationalParamsResponse
    get_access_control_settings_request: WCAPIGetAccessControlSettingsRequest
    get_access_control_settings_response: WCAPIGetAccessControlSettingsResponse
    configure_access_control_settings_request: WCAPIConfigureAccessControlSettingsRequest
    configure_access_control_settings_response: WCAPIConfigureAccessControlSettingsResponse
    get_recent_vehicles_request: WCAPIGetRecentVehiclesRequest
    get_recent_vehicles_response: WCAPIGetRecentVehiclesResponse
    push_ppu_authorization_state_request: WCAPIPushPpuAuthorizationStateRequest
    push_ppu_authorization_state_response: WCAPIPushPpuAuthorizationStateResponse
    configure_charge_schedule_request: WCAPIConfigureChargeScheduleRequest
    configure_charge_schedule_response: WCAPIConfigureChargeScheduleResponse
    push_charge_command_request: WCAPIPushChargeCommandRequest
    push_charge_command_response: WCAPIPushChargeCommandResponse
    configure_third_party_vehicle_mode_request: WCAPIConfigureThirdPartyVehicleModeRequest
    configure_third_party_vehicle_mode_response: WCAPIConfigureThirdPartyVehicleModeResponse
    configure_home_site_controller_request: WCAPIConfigureHomeSiteControllerRequest
    configure_home_site_controller_response: WCAPIConfigureHomeSiteControllerResponse
    configure_ocpp_settings_request: WCAPIConfigureOcppSettingsRequest
    configure_ocpp_settings_response: WCAPIConfigureOcppSettingsResponse
    set_ocpp_security_parameter_request: WCAPISetOcppSecurityParameterRequest
    set_ocpp_security_parameter_response: WCAPISetOcppSecurityParameterResponse
    get_ocpp_security_parameter_request: WCAPIGetOcppSecurityParameterRequest
    get_ocpp_security_parameter_response: WCAPIGetOcppSecurityParameterResponse
    configure_operational_settings_request: WCAPIConfigureOperationalSettingsRequest
    configure_operational_settings_response: WCAPIConfigureOperationalSettingsResponse
    get_operational_settings_request: WCAPIGetOperationalSettingsRequest
    get_operational_settings_response: WCAPIGetOperationalSettingsResponse
    configure_country_code_settings_request: WCAPIConfigureCountryCodeSettingsRequest
    configure_country_code_settings_response: WCAPIConfigureCountryCodeSettingsResponse
    push_load_sharing_config_request: WCAPIPushLoadSharingConfigRequest
    push_load_sharing_config_response: WCAPIPushLoadSharingConfigResponse
    push_smart_charging_command_request: WCAPIPushSmartChargingCommandRequest
    push_smart_charging_command_response: WCAPIPushSmartChargingCommandResponse
    register_commercial_request: WCAPIRegisterCommercialRequest
    register_commercial_response: WCAPIRegisterCommercialResponse
    get_ocpp_local_auth_list_request: WCAPIGetOcppLocalAuthListRequest
    get_ocpp_local_auth_list_response: WCAPIGetOcppLocalAuthListResponse
    push_powershare_command_request: WCAPIPushPowershareCommandRequest
    push_powershare_command_response: WCAPIPushPowershareCommandResponse

    def __init__(self, get_vitals_request: _Optional[_Union[WCAPIGetVitalsRequest, _Mapping]]=..., get_vitals_response: _Optional[_Union[WCAPIGetVitalsResponse, _Mapping]]=..., get_lifetime_stats_request: _Optional[_Union[WCAPIGetLifetimeStatsRequest, _Mapping]]=..., get_lifetime_stats_response: _Optional[_Union[WCAPIGetLifetimeStatsResponse, _Mapping]]=..., get_config_request: _Optional[_Union[WCAPIGetConfigRequest, _Mapping]]=..., get_config_response: _Optional[_Union[WCAPIGetConfigResponse, _Mapping]]=..., configure_settings_request: _Optional[_Union[WCAPIConfigureSettingsRequest, _Mapping]]=..., configure_settings_response: _Optional[_Union[WCAPIConfigureSettingsResponse, _Mapping]]=..., get_system_info_request: _Optional[_Union[WCAPIGetSystemInfoRequest, _Mapping]]=..., get_system_info_response: _Optional[_Union[WCAPIGetSystemInfoResponse, _Mapping]]=..., get_load_sharing_network_state_request: _Optional[_Union[WCAPIGetLoadSharingNetworkStateRequest, _Mapping]]=..., get_load_sharing_network_state_response: _Optional[_Union[WCAPIGetLoadSharingNetworkStateResponse, _Mapping]]=..., push_load_sharing_follower_state_request: _Optional[_Union[WCAPIPushLoadSharingFollowerStateRequest, _Mapping]]=..., push_load_sharing_follower_state_response: _Optional[_Union[WCAPIPushLoadSharingFollowerStateResponse, _Mapping]]=..., push_load_sharing_leader_command_request: _Optional[_Union[WCAPIPushLoadSharingLeaderCommandRequest, _Mapping]]=..., push_load_sharing_leader_command_response: _Optional[_Union[WCAPIPushLoadSharingLeaderCommandResponse, _Mapping]]=..., set_load_sharing_network_operation_request: _Optional[_Union[WCAPISetLoadSharingNetworkOperationRequest, _Mapping]]=..., set_load_sharing_network_operation_response: _Optional[_Union[WCAPISetLoadSharingNetworkOperationResponse, _Mapping]]=..., configure_load_sharing_settings_request: _Optional[_Union[WCAPIConfigureLoadSharingSettingsRequest, _Mapping]]=..., configure_load_sharing_settings_response: _Optional[_Union[WCAPIConfigureLoadSharingSettingsResponse, _Mapping]]=..., configure_ppu_settings_request: _Optional[_Union[WCAPIConfigurePpuSettingsRequest, _Mapping]]=..., configure_ppu_settings_response: _Optional[_Union[WCAPIConfigurePpuSettingsResponse, _Mapping]]=..., get_ppu_settings_request: _Optional[_Union[WCAPIGetPpuSettingsRequest, _Mapping]]=..., get_ppu_settings_response: _Optional[_Union[WCAPIGetPpuSettingsResponse, _Mapping]]=..., set_provisional_operational_params_request: _Optional[_Union[WCAPISetProvisionalOperationalParamsRequest, _Mapping]]=..., set_provisional_operational_params_response: _Optional[_Union[WCAPISetProvisionalOperationalParamsResponse, _Mapping]]=..., get_provisional_operational_params_request: _Optional[_Union[WCAPIGetProvisionalOperationalParamsRequest, _Mapping]]=..., get_provisional_operational_params_response: _Optional[_Union[WCAPIGetProvisionalOperationalParamsResponse, _Mapping]]=..., get_access_control_settings_request: _Optional[_Union[WCAPIGetAccessControlSettingsRequest, _Mapping]]=..., get_access_control_settings_response: _Optional[_Union[WCAPIGetAccessControlSettingsResponse, _Mapping]]=..., configure_access_control_settings_request: _Optional[_Union[WCAPIConfigureAccessControlSettingsRequest, _Mapping]]=..., configure_access_control_settings_response: _Optional[_Union[WCAPIConfigureAccessControlSettingsResponse, _Mapping]]=..., get_recent_vehicles_request: _Optional[_Union[WCAPIGetRecentVehiclesRequest, _Mapping]]=..., get_recent_vehicles_response: _Optional[_Union[WCAPIGetRecentVehiclesResponse, _Mapping]]=..., push_ppu_authorization_state_request: _Optional[_Union[WCAPIPushPpuAuthorizationStateRequest, _Mapping]]=..., push_ppu_authorization_state_response: _Optional[_Union[WCAPIPushPpuAuthorizationStateResponse, _Mapping]]=..., configure_charge_schedule_request: _Optional[_Union[WCAPIConfigureChargeScheduleRequest, _Mapping]]=..., configure_charge_schedule_response: _Optional[_Union[WCAPIConfigureChargeScheduleResponse, _Mapping]]=..., push_charge_command_request: _Optional[_Union[WCAPIPushChargeCommandRequest, _Mapping]]=..., push_charge_command_response: _Optional[_Union[WCAPIPushChargeCommandResponse, _Mapping]]=..., configure_third_party_vehicle_mode_request: _Optional[_Union[WCAPIConfigureThirdPartyVehicleModeRequest, _Mapping]]=..., configure_third_party_vehicle_mode_response: _Optional[_Union[WCAPIConfigureThirdPartyVehicleModeResponse, _Mapping]]=..., configure_home_site_controller_request: _Optional[_Union[WCAPIConfigureHomeSiteControllerRequest, _Mapping]]=..., configure_home_site_controller_response: _Optional[_Union[WCAPIConfigureHomeSiteControllerResponse, _Mapping]]=..., configure_ocpp_settings_request: _Optional[_Union[WCAPIConfigureOcppSettingsRequest, _Mapping]]=..., configure_ocpp_settings_response: _Optional[_Union[WCAPIConfigureOcppSettingsResponse, _Mapping]]=..., set_ocpp_security_parameter_request: _Optional[_Union[WCAPISetOcppSecurityParameterRequest, _Mapping]]=..., set_ocpp_security_parameter_response: _Optional[_Union[WCAPISetOcppSecurityParameterResponse, _Mapping]]=..., get_ocpp_security_parameter_request: _Optional[_Union[WCAPIGetOcppSecurityParameterRequest, _Mapping]]=..., get_ocpp_security_parameter_response: _Optional[_Union[WCAPIGetOcppSecurityParameterResponse, _Mapping]]=..., configure_operational_settings_request: _Optional[_Union[WCAPIConfigureOperationalSettingsRequest, _Mapping]]=..., configure_operational_settings_response: _Optional[_Union[WCAPIConfigureOperationalSettingsResponse, _Mapping]]=..., get_operational_settings_request: _Optional[_Union[WCAPIGetOperationalSettingsRequest, _Mapping]]=..., get_operational_settings_response: _Optional[_Union[WCAPIGetOperationalSettingsResponse, _Mapping]]=..., configure_country_code_settings_request: _Optional[_Union[WCAPIConfigureCountryCodeSettingsRequest, _Mapping]]=..., configure_country_code_settings_response: _Optional[_Union[WCAPIConfigureCountryCodeSettingsResponse, _Mapping]]=..., push_load_sharing_config_request: _Optional[_Union[WCAPIPushLoadSharingConfigRequest, _Mapping]]=..., push_load_sharing_config_response: _Optional[_Union[WCAPIPushLoadSharingConfigResponse, _Mapping]]=..., push_smart_charging_command_request: _Optional[_Union[WCAPIPushSmartChargingCommandRequest, _Mapping]]=..., push_smart_charging_command_response: _Optional[_Union[WCAPIPushSmartChargingCommandResponse, _Mapping]]=..., register_commercial_request: _Optional[_Union[WCAPIRegisterCommercialRequest, _Mapping]]=..., register_commercial_response: _Optional[_Union[WCAPIRegisterCommercialResponse, _Mapping]]=..., get_ocpp_local_auth_list_request: _Optional[_Union[WCAPIGetOcppLocalAuthListRequest, _Mapping]]=..., get_ocpp_local_auth_list_response: _Optional[_Union[WCAPIGetOcppLocalAuthListResponse, _Mapping]]=..., push_powershare_command_request: _Optional[_Union[WCAPIPushPowershareCommandRequest, _Mapping]]=..., push_powershare_command_response: _Optional[_Union[WCAPIPushPowershareCommandResponse, _Mapping]]=...) -> None:
        ...