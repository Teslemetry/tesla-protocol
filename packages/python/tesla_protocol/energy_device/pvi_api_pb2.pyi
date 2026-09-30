from google.protobuf import wrappers_pb2 as _wrappers_pb2
from . import device_pb2 as _device_pb2
from . import networking_pb2 as _networking_pb2
from . import update_pb2 as _update_pb2
from . import energy_pb2 as _energy_pb2
from . import neurio_meter_api_pb2 as _neurio_meter_api_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PVInverterSolarInstallationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PV_INVERTER_SOLAR_INSTALLATION_TYPE_INVALID: _ClassVar[PVInverterSolarInstallationType]
    PV_INVERTER_SOLAR_INSTALLATION_TYPE_PV_PANEL: _ClassVar[PVInverterSolarInstallationType]
    PV_INVERTER_SOLAR_INSTALLATION_TYPE_SOLARGLASS: _ClassVar[PVInverterSolarInstallationType]

class PVInverterPowerStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PV_INVERTER_POWER_STATUS_INVALID: _ClassVar[PVInverterPowerStatus]
    PV_INVERTER_POWER_STATUS_OFF: _ClassVar[PVInverterPowerStatus]
    PV_INVERTER_POWER_STATUS_DC_CONNECTED: _ClassVar[PVInverterPowerStatus]
    PV_INVERTER_POWER_STATUS_AC_PRODUCING: _ClassVar[PVInverterPowerStatus]

class PVInverterEcuResetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PV_INVERTER_ECU_RESET_STATUS_INVALID: _ClassVar[PVInverterEcuResetStatus]
    PV_INVERTER_ECU_RESET_STATUS_NONE: _ClassVar[PVInverterEcuResetStatus]
    PV_INVERTER_ECU_RESET_STATUS_SUCCESS: _ClassVar[PVInverterEcuResetStatus]
    PV_INVERTER_ECU_RESET_STATUS_PROCESSING: _ClassVar[PVInverterEcuResetStatus]
    PV_INVERTER_ECU_RESET_STATUS_UNKNOWN_FAILURE: _ClassVar[PVInverterEcuResetStatus]

class PVInverterEcu(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PV_INVERTER_ECU_INVALID: _ClassVar[PVInverterEcu]
    PV_INVERTER_ECU_PVCOM: _ClassVar[PVInverterEcu]
    PV_INVERTER_ECU_PVAC: _ClassVar[PVInverterEcu]
    PV_INVERTER_ECU_PVS: _ClassVar[PVInverterEcu]

class PVInverterClearLogsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PV_INVERTER_CLEAR_LOGS_STATUS_INVALID: _ClassVar[PVInverterClearLogsStatus]
    PV_INVERTER_CLEAR_LOGS_STATUS_NONE: _ClassVar[PVInverterClearLogsStatus]
    PV_INVERTER_CLEAR_LOGS_STATUS_FAILURE: _ClassVar[PVInverterClearLogsStatus]
    PV_INVERTER_CLEAR_LOGS_STATUS_SUCCESS: _ClassVar[PVInverterClearLogsStatus]
    PV_INVERTER_CLEAR_LOGS_STATUS_ATTEMPTED: _ClassVar[PVInverterClearLogsStatus]
PV_INVERTER_SOLAR_INSTALLATION_TYPE_INVALID: PVInverterSolarInstallationType
PV_INVERTER_SOLAR_INSTALLATION_TYPE_PV_PANEL: PVInverterSolarInstallationType
PV_INVERTER_SOLAR_INSTALLATION_TYPE_SOLARGLASS: PVInverterSolarInstallationType
PV_INVERTER_POWER_STATUS_INVALID: PVInverterPowerStatus
PV_INVERTER_POWER_STATUS_OFF: PVInverterPowerStatus
PV_INVERTER_POWER_STATUS_DC_CONNECTED: PVInverterPowerStatus
PV_INVERTER_POWER_STATUS_AC_PRODUCING: PVInverterPowerStatus
PV_INVERTER_ECU_RESET_STATUS_INVALID: PVInverterEcuResetStatus
PV_INVERTER_ECU_RESET_STATUS_NONE: PVInverterEcuResetStatus
PV_INVERTER_ECU_RESET_STATUS_SUCCESS: PVInverterEcuResetStatus
PV_INVERTER_ECU_RESET_STATUS_PROCESSING: PVInverterEcuResetStatus
PV_INVERTER_ECU_RESET_STATUS_UNKNOWN_FAILURE: PVInverterEcuResetStatus
PV_INVERTER_ECU_INVALID: PVInverterEcu
PV_INVERTER_ECU_PVCOM: PVInverterEcu
PV_INVERTER_ECU_PVAC: PVInverterEcu
PV_INVERTER_ECU_PVS: PVInverterEcu
PV_INVERTER_CLEAR_LOGS_STATUS_INVALID: PVInverterClearLogsStatus
PV_INVERTER_CLEAR_LOGS_STATUS_NONE: PVInverterClearLogsStatus
PV_INVERTER_CLEAR_LOGS_STATUS_FAILURE: PVInverterClearLogsStatus
PV_INVERTER_CLEAR_LOGS_STATUS_SUCCESS: PVInverterClearLogsStatus
PV_INVERTER_CLEAR_LOGS_STATUS_ATTEMPTED: PVInverterClearLogsStatus

class PVStringVitals(_message.Message):
    __slots__ = ('dc_measurement', 'string_id', 'connected', 'locked_out')
    DC_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    STRING_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_OUT_FIELD_NUMBER: _ClassVar[int]
    dc_measurement: _energy_pb2.InstDCMeasurement
    string_id: int
    connected: bool
    locked_out: bool

    def __init__(self, dc_measurement: _Optional[_Union[_energy_pb2.InstDCMeasurement, _Mapping]]=..., string_id: _Optional[int]=..., connected: bool=..., locked_out: bool=...) -> None:
        ...

class PVInverterVitals(_message.Message):
    __slots__ = ('uptime_s', 'pvac_faults', 'pvs_faults', 'ac_measurement_pvac', 'site_shutdown_switch_open', 'energy_today', 'pv_string_vitals', 'ac_measurement_site', 'pvac_inv_state', 'pvac_state', 'grid_compliance_status', 'pvac_warnings', 'pvs_warnings', 'pvs_state', 'ac_measurement_solar_rgm')
    UPTIME_S_FIELD_NUMBER: _ClassVar[int]
    PVAC_FAULTS_FIELD_NUMBER: _ClassVar[int]
    PVS_FAULTS_FIELD_NUMBER: _ClassVar[int]
    AC_MEASUREMENT_PVAC_FIELD_NUMBER: _ClassVar[int]
    SITE_SHUTDOWN_SWITCH_OPEN_FIELD_NUMBER: _ClassVar[int]
    ENERGY_TODAY_FIELD_NUMBER: _ClassVar[int]
    PV_STRING_VITALS_FIELD_NUMBER: _ClassVar[int]
    AC_MEASUREMENT_SITE_FIELD_NUMBER: _ClassVar[int]
    PVAC_INV_STATE_FIELD_NUMBER: _ClassVar[int]
    PVAC_STATE_FIELD_NUMBER: _ClassVar[int]
    GRID_COMPLIANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    PVAC_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    PVS_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    PVS_STATE_FIELD_NUMBER: _ClassVar[int]
    AC_MEASUREMENT_SOLAR_RGM_FIELD_NUMBER: _ClassVar[int]
    uptime_s: int
    pvac_faults: _containers.RepeatedScalarFieldContainer[int]
    pvs_faults: _containers.RepeatedScalarFieldContainer[int]
    ac_measurement_pvac: _energy_pb2.InstACMeasurement
    site_shutdown_switch_open: bool
    energy_today: _energy_pb2.AccumulatedEnergy
    pv_string_vitals: _containers.RepeatedCompositeFieldContainer[PVStringVitals]
    ac_measurement_site: _energy_pb2.InstACMeasurement
    pvac_inv_state: int
    pvac_state: int
    grid_compliance_status: _energy_pb2.GridComplianceStatus
    pvac_warnings: _containers.RepeatedScalarFieldContainer[int]
    pvs_warnings: _containers.RepeatedScalarFieldContainer[int]
    pvs_state: int
    ac_measurement_solar_rgm: _energy_pb2.InstACMeasurement

    def __init__(self, uptime_s: _Optional[int]=..., pvac_faults: _Optional[_Iterable[int]]=..., pvs_faults: _Optional[_Iterable[int]]=..., ac_measurement_pvac: _Optional[_Union[_energy_pb2.InstACMeasurement, _Mapping]]=..., site_shutdown_switch_open: bool=..., energy_today: _Optional[_Union[_energy_pb2.AccumulatedEnergy, _Mapping]]=..., pv_string_vitals: _Optional[_Iterable[_Union[PVStringVitals, _Mapping]]]=..., ac_measurement_site: _Optional[_Union[_energy_pb2.InstACMeasurement, _Mapping]]=..., pvac_inv_state: _Optional[int]=..., pvac_state: _Optional[int]=..., grid_compliance_status: _Optional[_Union[_energy_pb2.GridComplianceStatus, _Mapping]]=..., pvac_warnings: _Optional[_Iterable[int]]=..., pvs_warnings: _Optional[_Iterable[int]]=..., pvs_state: _Optional[int]=..., ac_measurement_solar_rgm: _Optional[_Union[_energy_pb2.InstACMeasurement, _Mapping]]=...) -> None:
        ...

class PVInverterLifetimeStats(_message.Message):
    __slots__ = ('uptime_s', 'alert_count', 'energy_lifetime')
    UPTIME_S_FIELD_NUMBER: _ClassVar[int]
    ALERT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENERGY_LIFETIME_FIELD_NUMBER: _ClassVar[int]
    uptime_s: int
    alert_count: int
    energy_lifetime: _energy_pb2.AccumulatedEnergy

    def __init__(self, uptime_s: _Optional[int]=..., alert_count: _Optional[int]=..., energy_lifetime: _Optional[_Union[_energy_pb2.AccumulatedEnergy, _Mapping]]=...) -> None:
        ...

class PVMeterInterface(_message.Message):
    __slots__ = ('neurio',)
    NEURIO_FIELD_NUMBER: _ClassVar[int]
    neurio: _neurio_meter_api_pb2.NeurioMeterInterface

    def __init__(self, neurio: _Optional[_Union[_neurio_meter_api_pb2.NeurioMeterInterface, _Mapping]]=...) -> None:
        ...

class PVGridCodeConfig(_message.Message):
    __slots__ = ('grid_code', 'region_info')
    GRID_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_INFO_FIELD_NUMBER: _ClassVar[int]
    grid_code: str
    region_info: str

    def __init__(self, grid_code: _Optional[str]=..., region_info: _Optional[str]=...) -> None:
        ...

class PVInverterSettings(_message.Message):
    __slots__ = ('grid_code', 'meters', 'solar_installation_type', 'current_rating_override_a')
    GRID_CODE_FIELD_NUMBER: _ClassVar[int]
    METERS_FIELD_NUMBER: _ClassVar[int]
    SOLAR_INSTALLATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RATING_OVERRIDE_A_FIELD_NUMBER: _ClassVar[int]
    grid_code: PVGridCodeConfig
    meters: _containers.RepeatedCompositeFieldContainer[PVMeterInterface]
    solar_installation_type: PVInverterSolarInstallationType
    current_rating_override_a: _wrappers_pb2.FloatValue

    def __init__(self, grid_code: _Optional[_Union[PVGridCodeConfig, _Mapping]]=..., meters: _Optional[_Iterable[_Union[PVMeterInterface, _Mapping]]]=..., solar_installation_type: _Optional[_Union[PVInverterSolarInstallationType, str]]=..., current_rating_override_a: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=...) -> None:
        ...

class PVInverterCanMessage(_message.Message):
    __slots__ = ('can_id', 'can_payload')
    CAN_ID_FIELD_NUMBER: _ClassVar[int]
    CAN_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    can_id: int
    can_payload: bytes

    def __init__(self, can_id: _Optional[int]=..., can_payload: _Optional[bytes]=...) -> None:
        ...

class PVIAPIGetSystemInfoRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPIGetSystemInfoResponse(_message.Message):
    __slots__ = ('pvcom_id', 'pvac_id', 'pvs_id', 'firmware_version', 'nominal_current_amps', 'nominal_apparent_power_va')
    PVCOM_ID_FIELD_NUMBER: _ClassVar[int]
    PVAC_ID_FIELD_NUMBER: _ClassVar[int]
    PVS_ID_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_CURRENT_AMPS_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_APPARENT_POWER_VA_FIELD_NUMBER: _ClassVar[int]
    pvcom_id: _device_pb2.EcuId
    pvac_id: _device_pb2.EcuId
    pvs_id: _device_pb2.EcuId
    firmware_version: _update_pb2.FirmwareVersion
    nominal_current_amps: float
    nominal_apparent_power_va: float

    def __init__(self, pvcom_id: _Optional[_Union[_device_pb2.EcuId, _Mapping]]=..., pvac_id: _Optional[_Union[_device_pb2.EcuId, _Mapping]]=..., pvs_id: _Optional[_Union[_device_pb2.EcuId, _Mapping]]=..., firmware_version: _Optional[_Union[_update_pb2.FirmwareVersion, _Mapping]]=..., nominal_current_amps: _Optional[float]=..., nominal_apparent_power_va: _Optional[float]=...) -> None:
        ...

class PVIAPIGetVitalsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPIGetVitalsResponse(_message.Message):
    __slots__ = ('vitals',)
    VITALS_FIELD_NUMBER: _ClassVar[int]
    vitals: PVInverterVitals

    def __init__(self, vitals: _Optional[_Union[PVInverterVitals, _Mapping]]=...) -> None:
        ...

class PVIAPIGetLifetimeStatsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPIGetLifetimeStatsResponse(_message.Message):
    __slots__ = ('lifetime_stats',)
    LIFETIME_STATS_FIELD_NUMBER: _ClassVar[int]
    lifetime_stats: PVInverterLifetimeStats

    def __init__(self, lifetime_stats: _Optional[_Union[PVInverterLifetimeStats, _Mapping]]=...) -> None:
        ...

class PVIAPIGetConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPIGetConfigResponse(_message.Message):
    __slots__ = ('settings', 'wifi_config', 'wifi', 'eth', 'gsm', 'power_status')
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    WIFI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    ETH_FIELD_NUMBER: _ClassVar[int]
    GSM_FIELD_NUMBER: _ClassVar[int]
    POWER_STATUS_FIELD_NUMBER: _ClassVar[int]
    settings: PVInverterSettings
    wifi_config: _networking_pb2.WifiConfig
    wifi: _networking_pb2.NetworkInterface
    eth: _networking_pb2.NetworkInterface
    gsm: _networking_pb2.NetworkInterface
    power_status: PVInverterPowerStatus

    def __init__(self, settings: _Optional[_Union[PVInverterSettings, _Mapping]]=..., wifi_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., eth: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., gsm: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., power_status: _Optional[_Union[PVInverterPowerStatus, str]]=...) -> None:
        ...

class PVIAPIConfigureSettingsRequest(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: PVInverterSettings

    def __init__(self, settings: _Optional[_Union[PVInverterSettings, _Mapping]]=...) -> None:
        ...

class PVIAPIConfigureSettingsResponse(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: PVInverterSettings

    def __init__(self, settings: _Optional[_Union[PVInverterSettings, _Mapping]]=...) -> None:
        ...

class PVIAPIConfigureEthernetRequest(_message.Message):
    __slots__ = ('ip4_config',)
    IP4_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ip4_config: _networking_pb2.NetworkInterfaceIPv4Config

    def __init__(self, ip4_config: _Optional[_Union[_networking_pb2.NetworkInterfaceIPv4Config, _Mapping]]=...) -> None:
        ...

class PVIAPIConfigureEthernetResponse(_message.Message):
    __slots__ = ('eth',)
    ETH_FIELD_NUMBER: _ClassVar[int]
    eth: _networking_pb2.NetworkInterface

    def __init__(self, eth: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=...) -> None:
        ...

class PVIAPIConfigureGsmRequest(_message.Message):
    __slots__ = ('enabled',)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool

    def __init__(self, enabled: bool=...) -> None:
        ...

class PVIAPIConfigureGsmResponse(_message.Message):
    __slots__ = ('gsm',)
    GSM_FIELD_NUMBER: _ClassVar[int]
    gsm: _networking_pb2.NetworkInterface

    def __init__(self, gsm: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=...) -> None:
        ...

class PVIAPIInverterResetRequest(_message.Message):
    __slots__ = ('reset_pvcom', 'reset_pvac', 'reset_pvs')
    RESET_PVCOM_FIELD_NUMBER: _ClassVar[int]
    RESET_PVAC_FIELD_NUMBER: _ClassVar[int]
    RESET_PVS_FIELD_NUMBER: _ClassVar[int]
    reset_pvcom: bool
    reset_pvac: bool
    reset_pvs: bool

    def __init__(self, reset_pvcom: bool=..., reset_pvac: bool=..., reset_pvs: bool=...) -> None:
        ...

class PVIAPIInverterResetResponse(_message.Message):
    __slots__ = ('pvcom_status', 'pvac_status', 'pvs_status')
    PVCOM_STATUS_FIELD_NUMBER: _ClassVar[int]
    PVAC_STATUS_FIELD_NUMBER: _ClassVar[int]
    PVS_STATUS_FIELD_NUMBER: _ClassVar[int]
    pvcom_status: PVInverterEcuResetStatus
    pvac_status: PVInverterEcuResetStatus
    pvs_status: PVInverterEcuResetStatus

    def __init__(self, pvcom_status: _Optional[_Union[PVInverterEcuResetStatus, str]]=..., pvac_status: _Optional[_Union[PVInverterEcuResetStatus, str]]=..., pvs_status: _Optional[_Union[PVInverterEcuResetStatus, str]]=...) -> None:
        ...

class PVIAPISetOperationParamsRequest(_message.Message):
    __slots__ = ('power_status', 'active_power_limit_w')
    POWER_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_POWER_LIMIT_W_FIELD_NUMBER: _ClassVar[int]
    power_status: PVInverterPowerStatus
    active_power_limit_w: _wrappers_pb2.FloatValue

    def __init__(self, power_status: _Optional[_Union[PVInverterPowerStatus, str]]=..., active_power_limit_w: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=...) -> None:
        ...

class PVIAPISetOperationParamsResponse(_message.Message):
    __slots__ = ('power_status', 'active_power_limit_w')
    POWER_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_POWER_LIMIT_W_FIELD_NUMBER: _ClassVar[int]
    power_status: PVInverterPowerStatus
    active_power_limit_w: _wrappers_pb2.FloatValue

    def __init__(self, power_status: _Optional[_Union[PVInverterPowerStatus, str]]=..., active_power_limit_w: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=...) -> None:
        ...

class PVIAPISendCanMessageRequest(_message.Message):
    __slots__ = ('can_message',)
    CAN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    can_message: PVInverterCanMessage

    def __init__(self, can_message: _Optional[_Union[PVInverterCanMessage, _Mapping]]=...) -> None:
        ...

class PVIAPISendCanMessageResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPIUdsWriteDataByIdentifierRequest(_message.Message):
    __slots__ = ('ecu', 'did', 'payload')
    ECU_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ecu: PVInverterEcu
    did: int
    payload: bytes

    def __init__(self, ecu: _Optional[_Union[PVInverterEcu, str]]=..., did: _Optional[int]=..., payload: _Optional[bytes]=...) -> None:
        ...

class PVIAPIUdsWriteDataByIdentifierResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPICheckInternetRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPICheckInternetResponse(_message.Message):
    __slots__ = ('wifi', 'eth', 'gsm')
    WIFI_FIELD_NUMBER: _ClassVar[int]
    ETH_FIELD_NUMBER: _ClassVar[int]
    GSM_FIELD_NUMBER: _ClassVar[int]
    wifi: _networking_pb2.NetworkInterface
    eth: _networking_pb2.NetworkInterface
    gsm: _networking_pb2.NetworkInterface

    def __init__(self, wifi: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., eth: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., gsm: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=...) -> None:
        ...

class PVIAPIConfigureGridCodeRequest(_message.Message):
    __slots__ = ('grid_code',)
    GRID_CODE_FIELD_NUMBER: _ClassVar[int]
    grid_code: PVGridCodeConfig

    def __init__(self, grid_code: _Optional[_Union[PVGridCodeConfig, _Mapping]]=...) -> None:
        ...

class PVIAPIConfigureGridCodeResponse(_message.Message):
    __slots__ = ('grid_code',)
    GRID_CODE_FIELD_NUMBER: _ClassVar[int]
    grid_code: PVGridCodeConfig

    def __init__(self, grid_code: _Optional[_Union[PVGridCodeConfig, _Mapping]]=...) -> None:
        ...

class PVIAPIClearAlertsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPIClearAlertsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPITriggerDrLogRequest(_message.Message):
    __slots__ = ('pvac', 'pvs')
    PVAC_FIELD_NUMBER: _ClassVar[int]
    PVS_FIELD_NUMBER: _ClassVar[int]
    pvac: bool
    pvs: bool

    def __init__(self, pvac: bool=..., pvs: bool=...) -> None:
        ...

class PVIAPITriggerDrLogResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPIClearLogsRequest(_message.Message):
    __slots__ = ('telemetry', 'alerts', 'drlog')
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    DRLOG_FIELD_NUMBER: _ClassVar[int]
    telemetry: bool
    alerts: bool
    drlog: bool

    def __init__(self, telemetry: bool=..., alerts: bool=..., drlog: bool=...) -> None:
        ...

class PVIAPIClearLogsResponse(_message.Message):
    __slots__ = ('telemetry', 'alerts', 'drlog')
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    DRLOG_FIELD_NUMBER: _ClassVar[int]
    telemetry: PVInverterClearLogsStatus
    alerts: PVInverterClearLogsStatus
    drlog: PVInverterClearLogsStatus

    def __init__(self, telemetry: _Optional[_Union[PVInverterClearLogsStatus, str]]=..., alerts: _Optional[_Union[PVInverterClearLogsStatus, str]]=..., drlog: _Optional[_Union[PVInverterClearLogsStatus, str]]=...) -> None:
        ...

class PVIAPIConfigureSolarInstallationTypeRequest(_message.Message):
    __slots__ = ('solar_installation_type',)
    SOLAR_INSTALLATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    solar_installation_type: PVInverterSolarInstallationType

    def __init__(self, solar_installation_type: _Optional[_Union[PVInverterSolarInstallationType, str]]=...) -> None:
        ...

class PVIAPIConfigureSolarInstallationTypeResponse(_message.Message):
    __slots__ = ('solar_installation_type',)
    SOLAR_INSTALLATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    solar_installation_type: PVInverterSolarInstallationType

    def __init__(self, solar_installation_type: _Optional[_Union[PVInverterSolarInstallationType, str]]=...) -> None:
        ...

class PVIAPIConfigureCurrentRatingOverrideRequest(_message.Message):
    __slots__ = ('current_rating_override_a',)
    CURRENT_RATING_OVERRIDE_A_FIELD_NUMBER: _ClassVar[int]
    current_rating_override_a: float

    def __init__(self, current_rating_override_a: _Optional[float]=...) -> None:
        ...

class PVIAPIConfigureCurrentRatingOverrideResponse(_message.Message):
    __slots__ = ('current_rating_override_a',)
    CURRENT_RATING_OVERRIDE_A_FIELD_NUMBER: _ClassVar[int]
    current_rating_override_a: float

    def __init__(self, current_rating_override_a: _Optional[float]=...) -> None:
        ...

class PVIAPIRemoveCurrentRatingOverrideRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIAPIRemoveCurrentRatingOverrideResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PVIMessages(_message.Message):
    __slots__ = ('get_system_info_request', 'get_system_info_response', 'get_vitals_request', 'get_vitals_response', 'get_lifetime_stats_request', 'get_lifetime_stats_response', 'get_config_request', 'get_config_response', 'configure_settings_request', 'configure_settings_response', 'configure_ethernet_request', 'configure_ethernet_response', 'configure_gsm_request', 'configure_gsm_response', 'inverter_reset_request', 'inverter_reset_response', 'set_operation_params_request', 'set_operation_params_response', 'send_can_message_request', 'send_can_message_response', 'uds_write_data_by_identifier_request', 'uds_write_data_by_identifier_response', 'check_internet_request', 'check_internet_response', 'configure_grid_code_request', 'configure_grid_code_response', 'clear_alerts_request', 'clear_alerts_response', 'trigger_dr_log_request', 'trigger_dr_log_response', 'clear_logs_request', 'clear_logs_response', 'configure_solar_installation_type_request', 'configure_solar_installation_type_response', 'configure_current_rating_override_request', 'configure_current_rating_override_response', 'remove_current_rating_override_request', 'remove_current_rating_override_response')
    GET_SYSTEM_INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_SYSTEM_INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_VITALS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_VITALS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_LIFETIME_STATS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_LIFETIME_STATS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_CONFIG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_CONFIG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_SETTINGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_ETHERNET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_ETHERNET_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_GSM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_GSM_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INVERTER_RESET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    INVERTER_RESET_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SET_OPERATION_PARAMS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_OPERATION_PARAMS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEND_CAN_MESSAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SEND_CAN_MESSAGE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UDS_WRITE_DATA_BY_IDENTIFIER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UDS_WRITE_DATA_BY_IDENTIFIER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECK_INTERNET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHECK_INTERNET_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_GRID_CODE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_GRID_CODE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_ALERTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CLEAR_ALERTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_DR_LOG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_DR_LOG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_LOGS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CLEAR_LOGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_SOLAR_INSTALLATION_TYPE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_SOLAR_INSTALLATION_TYPE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_CURRENT_RATING_OVERRIDE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_CURRENT_RATING_OVERRIDE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_CURRENT_RATING_OVERRIDE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REMOVE_CURRENT_RATING_OVERRIDE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    get_system_info_request: PVIAPIGetSystemInfoRequest
    get_system_info_response: PVIAPIGetSystemInfoResponse
    get_vitals_request: PVIAPIGetVitalsRequest
    get_vitals_response: PVIAPIGetVitalsResponse
    get_lifetime_stats_request: PVIAPIGetLifetimeStatsRequest
    get_lifetime_stats_response: PVIAPIGetLifetimeStatsResponse
    get_config_request: PVIAPIGetConfigRequest
    get_config_response: PVIAPIGetConfigResponse
    configure_settings_request: PVIAPIConfigureSettingsRequest
    configure_settings_response: PVIAPIConfigureSettingsResponse
    configure_ethernet_request: PVIAPIConfigureEthernetRequest
    configure_ethernet_response: PVIAPIConfigureEthernetResponse
    configure_gsm_request: PVIAPIConfigureGsmRequest
    configure_gsm_response: PVIAPIConfigureGsmResponse
    inverter_reset_request: PVIAPIInverterResetRequest
    inverter_reset_response: PVIAPIInverterResetResponse
    set_operation_params_request: PVIAPISetOperationParamsRequest
    set_operation_params_response: PVIAPISetOperationParamsResponse
    send_can_message_request: PVIAPISendCanMessageRequest
    send_can_message_response: PVIAPISendCanMessageResponse
    uds_write_data_by_identifier_request: PVIAPIUdsWriteDataByIdentifierRequest
    uds_write_data_by_identifier_response: PVIAPIUdsWriteDataByIdentifierResponse
    check_internet_request: PVIAPICheckInternetRequest
    check_internet_response: PVIAPICheckInternetResponse
    configure_grid_code_request: PVIAPIConfigureGridCodeRequest
    configure_grid_code_response: PVIAPIConfigureGridCodeResponse
    clear_alerts_request: PVIAPIClearAlertsRequest
    clear_alerts_response: PVIAPIClearAlertsResponse
    trigger_dr_log_request: PVIAPITriggerDrLogRequest
    trigger_dr_log_response: PVIAPITriggerDrLogResponse
    clear_logs_request: PVIAPIClearLogsRequest
    clear_logs_response: PVIAPIClearLogsResponse
    configure_solar_installation_type_request: PVIAPIConfigureSolarInstallationTypeRequest
    configure_solar_installation_type_response: PVIAPIConfigureSolarInstallationTypeResponse
    configure_current_rating_override_request: PVIAPIConfigureCurrentRatingOverrideRequest
    configure_current_rating_override_response: PVIAPIConfigureCurrentRatingOverrideResponse
    remove_current_rating_override_request: PVIAPIRemoveCurrentRatingOverrideRequest
    remove_current_rating_override_response: PVIAPIRemoveCurrentRatingOverrideResponse

    def __init__(self, get_system_info_request: _Optional[_Union[PVIAPIGetSystemInfoRequest, _Mapping]]=..., get_system_info_response: _Optional[_Union[PVIAPIGetSystemInfoResponse, _Mapping]]=..., get_vitals_request: _Optional[_Union[PVIAPIGetVitalsRequest, _Mapping]]=..., get_vitals_response: _Optional[_Union[PVIAPIGetVitalsResponse, _Mapping]]=..., get_lifetime_stats_request: _Optional[_Union[PVIAPIGetLifetimeStatsRequest, _Mapping]]=..., get_lifetime_stats_response: _Optional[_Union[PVIAPIGetLifetimeStatsResponse, _Mapping]]=..., get_config_request: _Optional[_Union[PVIAPIGetConfigRequest, _Mapping]]=..., get_config_response: _Optional[_Union[PVIAPIGetConfigResponse, _Mapping]]=..., configure_settings_request: _Optional[_Union[PVIAPIConfigureSettingsRequest, _Mapping]]=..., configure_settings_response: _Optional[_Union[PVIAPIConfigureSettingsResponse, _Mapping]]=..., configure_ethernet_request: _Optional[_Union[PVIAPIConfigureEthernetRequest, _Mapping]]=..., configure_ethernet_response: _Optional[_Union[PVIAPIConfigureEthernetResponse, _Mapping]]=..., configure_gsm_request: _Optional[_Union[PVIAPIConfigureGsmRequest, _Mapping]]=..., configure_gsm_response: _Optional[_Union[PVIAPIConfigureGsmResponse, _Mapping]]=..., inverter_reset_request: _Optional[_Union[PVIAPIInverterResetRequest, _Mapping]]=..., inverter_reset_response: _Optional[_Union[PVIAPIInverterResetResponse, _Mapping]]=..., set_operation_params_request: _Optional[_Union[PVIAPISetOperationParamsRequest, _Mapping]]=..., set_operation_params_response: _Optional[_Union[PVIAPISetOperationParamsResponse, _Mapping]]=..., send_can_message_request: _Optional[_Union[PVIAPISendCanMessageRequest, _Mapping]]=..., send_can_message_response: _Optional[_Union[PVIAPISendCanMessageResponse, _Mapping]]=..., uds_write_data_by_identifier_request: _Optional[_Union[PVIAPIUdsWriteDataByIdentifierRequest, _Mapping]]=..., uds_write_data_by_identifier_response: _Optional[_Union[PVIAPIUdsWriteDataByIdentifierResponse, _Mapping]]=..., check_internet_request: _Optional[_Union[PVIAPICheckInternetRequest, _Mapping]]=..., check_internet_response: _Optional[_Union[PVIAPICheckInternetResponse, _Mapping]]=..., configure_grid_code_request: _Optional[_Union[PVIAPIConfigureGridCodeRequest, _Mapping]]=..., configure_grid_code_response: _Optional[_Union[PVIAPIConfigureGridCodeResponse, _Mapping]]=..., clear_alerts_request: _Optional[_Union[PVIAPIClearAlertsRequest, _Mapping]]=..., clear_alerts_response: _Optional[_Union[PVIAPIClearAlertsResponse, _Mapping]]=..., trigger_dr_log_request: _Optional[_Union[PVIAPITriggerDrLogRequest, _Mapping]]=..., trigger_dr_log_response: _Optional[_Union[PVIAPITriggerDrLogResponse, _Mapping]]=..., clear_logs_request: _Optional[_Union[PVIAPIClearLogsRequest, _Mapping]]=..., clear_logs_response: _Optional[_Union[PVIAPIClearLogsResponse, _Mapping]]=..., configure_solar_installation_type_request: _Optional[_Union[PVIAPIConfigureSolarInstallationTypeRequest, _Mapping]]=..., configure_solar_installation_type_response: _Optional[_Union[PVIAPIConfigureSolarInstallationTypeResponse, _Mapping]]=..., configure_current_rating_override_request: _Optional[_Union[PVIAPIConfigureCurrentRatingOverrideRequest, _Mapping]]=..., configure_current_rating_override_response: _Optional[_Union[PVIAPIConfigureCurrentRatingOverrideResponse, _Mapping]]=..., remove_current_rating_override_request: _Optional[_Union[PVIAPIRemoveCurrentRatingOverrideRequest, _Mapping]]=..., remove_current_rating_override_response: _Optional[_Union[PVIAPIRemoveCurrentRatingOverrideResponse, _Mapping]]=...) -> None:
        ...