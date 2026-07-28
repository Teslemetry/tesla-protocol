import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import device_pb2 as _device_pb2
from . import networking_pb2 as _networking_pb2
from . import common_api_pb2 as _common_api_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TEGIslandMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEG_ISLAND_MODE_INVALID: _ClassVar[TEGIslandMode]
    TEG_ISLAND_MODE_AUTO_ACTIVE: _ClassVar[TEGIslandMode]
    TEG_ISLAND_MODE_READY: _ClassVar[TEGIslandMode]
    TEG_ISLAND_MODE_INTENTIONAL: _ClassVar[TEGIslandMode]
    TEG_ISLAND_MODE_PQ: _ClassVar[TEGIslandMode]
    TEG_ISLAND_MODE_OFF: _ClassVar[TEGIslandMode]
    TEG_ISLAND_MODE_INTENTIONAL_WITH_RECONNECT_FAILSAFE: _ClassVar[TEGIslandMode]

class TEGSetIslandModeResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEG_SET_ISLAND_MODE_RESULT_INVALID: _ClassVar[TEGSetIslandModeResult]
    TEG_SET_ISLAND_MODE_RESULT_ACCEPTED: _ClassVar[TEGSetIslandModeResult]
    TEG_SET_ISLAND_MODE_RESULT_REJECTED_NOT_READY_FOR_ISLANDING: _ClassVar[TEGSetIslandModeResult]
    TEG_SET_ISLAND_MODE_RESULT_REJECTED_LOAD_DROP_EXPECTED: _ClassVar[TEGSetIslandModeResult]
    TEG_SET_ISLAND_MODE_RESULT_REJECTED_LOW_ENERGY: _ClassVar[TEGSetIslandModeResult]
    TEG_SET_ISLAND_MODE_RESULT_REJECTED_EXCESSIVE_SOLAR: _ClassVar[TEGSetIslandModeResult]

class CanvasSiteStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANVAS_SITE_STATUS_INVALID: _ClassVar[CanvasSiteStatus]
    CANVAS_SITE_STATUS_IS_CANVAS: _ClassVar[CanvasSiteStatus]
    CANVAS_SITE_STATUS_NOT_CANVAS: _ClassVar[CanvasSiteStatus]
    CANVAS_SITE_STATUS_NOT_FOUND: _ClassVar[CanvasSiteStatus]
TEG_ISLAND_MODE_INVALID: TEGIslandMode
TEG_ISLAND_MODE_AUTO_ACTIVE: TEGIslandMode
TEG_ISLAND_MODE_READY: TEGIslandMode
TEG_ISLAND_MODE_INTENTIONAL: TEGIslandMode
TEG_ISLAND_MODE_PQ: TEGIslandMode
TEG_ISLAND_MODE_OFF: TEGIslandMode
TEG_ISLAND_MODE_INTENTIONAL_WITH_RECONNECT_FAILSAFE: TEGIslandMode
TEG_SET_ISLAND_MODE_RESULT_INVALID: TEGSetIslandModeResult
TEG_SET_ISLAND_MODE_RESULT_ACCEPTED: TEGSetIslandModeResult
TEG_SET_ISLAND_MODE_RESULT_REJECTED_NOT_READY_FOR_ISLANDING: TEGSetIslandModeResult
TEG_SET_ISLAND_MODE_RESULT_REJECTED_LOAD_DROP_EXPECTED: TEGSetIslandModeResult
TEG_SET_ISLAND_MODE_RESULT_REJECTED_LOW_ENERGY: TEGSetIslandModeResult
TEG_SET_ISLAND_MODE_RESULT_REJECTED_EXCESSIVE_SOLAR: TEGSetIslandModeResult
CANVAS_SITE_STATUS_INVALID: CanvasSiteStatus
CANVAS_SITE_STATUS_IS_CANVAS: CanvasSiteStatus
CANVAS_SITE_STATUS_NOT_CANVAS: CanvasSiteStatus
CANVAS_SITE_STATUS_NOT_FOUND: CanvasSiteStatus

class TEGSettings(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Powerwall2PhaseDetectionParameters(_message.Message):
    __slots__ = ('din',)
    DIN_FIELD_NUMBER: _ClassVar[int]
    din: str

    def __init__(self, din: _Optional[str]=...) -> None:
        ...

class TEGAPIGetConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetConfigResponse(_message.Message):
    __slots__ = ('settings', 'wifi_config', 'wifi', 'eth', 'gsm', 'device_type')
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    WIFI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    ETH_FIELD_NUMBER: _ClassVar[int]
    GSM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    settings: TEGSettings
    wifi_config: _networking_pb2.WifiConfig
    wifi: _networking_pb2.NetworkInterface
    eth: _networking_pb2.NetworkInterface
    gsm: _networking_pb2.NetworkInterface
    device_type: _device_pb2.DeviceType

    def __init__(self, settings: _Optional[_Union[TEGSettings, _Mapping]]=..., wifi_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., eth: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., gsm: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., device_type: _Optional[_Union[_device_pb2.DeviceType, str]]=...) -> None:
        ...

class TEGAPISetIslandModeRequest(_message.Message):
    __slots__ = ('mode', 'force')
    MODE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    mode: TEGIslandMode
    force: bool

    def __init__(self, mode: _Optional[_Union[TEGIslandMode, str]]=..., force: bool=...) -> None:
        ...

class TEGAPISetIslandModeResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: TEGSetIslandModeResult

    def __init__(self, result: _Optional[_Union[TEGSetIslandModeResult, str]]=...) -> None:
        ...

class TEGAPITriggerIslandingBlackStartRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerIslandingBlackStartResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerAssetManifestUploadRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerAssetManifestUploadResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerPowerwall2EnumerationRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerPowerwall2EnumerationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerEsCanFirmwareUpdateRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerEsCanFirmwareUpdateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerPW3CanFirmwareUpdateRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerPW3CanFirmwareUpdateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerPowerwall3EnumerationRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerPowerwall3EnumerationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIDispatchBatteryPowerRequest_ResumeDeviceOperatingMode(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIDispatchBatteryPowerRequest_RealPowerCommand(_message.Message):
    __slots__ = ('power_watts', 'duration_seconds')
    POWER_WATTS_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    power_watts: float
    duration_seconds: int

    def __init__(self, power_watts: _Optional[float]=..., duration_seconds: _Optional[int]=...) -> None:
        ...

class TEGAPIDispatchBatteryPowerRequest(_message.Message):
    __slots__ = ('resume_device_mode', 'real_power')
    RESUME_DEVICE_MODE_FIELD_NUMBER: _ClassVar[int]
    REAL_POWER_FIELD_NUMBER: _ClassVar[int]
    resume_device_mode: TEGAPIDispatchBatteryPowerRequest_ResumeDeviceOperatingMode
    real_power: TEGAPIDispatchBatteryPowerRequest_RealPowerCommand

    def __init__(self, resume_device_mode: _Optional[_Union[TEGAPIDispatchBatteryPowerRequest_ResumeDeviceOperatingMode, _Mapping]]=..., real_power: _Optional[_Union[TEGAPIDispatchBatteryPowerRequest_RealPowerCommand, _Mapping]]=...) -> None:
        ...

class TEGAPIDispatchBatteryPowerResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIDetectWiredMetersRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIDetectWiredMetersResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIRegisterRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIRegisterResponse(_message.Message):
    __slots__ = ('failure',)
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    failure: int

    def __init__(self, failure: _Optional[int]=...) -> None:
        ...

class TEGAPITriggerPowerwall2PhaseDetectionRequest(_message.Message):
    __slots__ = ('powerwalls',)
    POWERWALLS_FIELD_NUMBER: _ClassVar[int]
    powerwalls: _containers.RepeatedCompositeFieldContainer[Powerwall2PhaseDetectionParameters]

    def __init__(self, powerwalls: _Optional[_Iterable[_Union[Powerwall2PhaseDetectionParameters, _Mapping]]]=...) -> None:
        ...

class TEGAPITriggerPowerwall2PhaseDetectionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIResetPowerwall2PhaseDetectionRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIResetPowerwall2PhaseDetectionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIForceWifiScanRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIForceWifiScanResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIStartPowerwall2InverterSelfTestsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIStartPowerwall2InverterSelfTestsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIStopPowerwall2InverterSelfTestsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIStopPowerwall2InverterSelfTestsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIStartPowerwall2BubbleShedRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIStartPowerwall2BubbleShedResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIClearSolarInverterAlertsRequest(_message.Message):
    __slots__ = ('din',)
    DIN_FIELD_NUMBER: _ClassVar[int]
    din: str

    def __init__(self, din: _Optional[str]=...) -> None:
        ...

class TEGAPIClearSolarInverterAlertsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetWifiConfigWithCredentialsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetWifiConfigWithCredentialsResponse(_message.Message):
    __slots__ = ('wifi_config',)
    WIFI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    wifi_config: _networking_pb2.WifiConfig

    def __init__(self, wifi_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=...) -> None:
        ...

class TEGAPIDisableBatteriesRequest_BatteryDisableRequest(_message.Message):
    __slots__ = ('din', 'disable')
    DIN_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    din: str
    disable: bool

    def __init__(self, din: _Optional[str]=..., disable: bool=...) -> None:
        ...

class TEGAPIDisableBatteriesRequest(_message.Message):
    __slots__ = ('battery_disable_requests',)
    BATTERY_DISABLE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    battery_disable_requests: _containers.RepeatedCompositeFieldContainer[TEGAPIDisableBatteriesRequest_BatteryDisableRequest]

    def __init__(self, battery_disable_requests: _Optional[_Iterable[_Union[TEGAPIDisableBatteriesRequest_BatteryDisableRequest, _Mapping]]]=...) -> None:
        ...

class TEGAPIDisableBatteriesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIBypassBatterySoeAdjustmentConstraintsRequest(_message.Message):
    __slots__ = ('enable', 'duration_hours')
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    DURATION_HOURS_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    duration_hours: int

    def __init__(self, enable: bool=..., duration_hours: _Optional[int]=...) -> None:
        ...

class TEGAPIBypassBatterySoeAdjustmentConstraintsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIEnsureCertificateRequest_CSIPSouthAustraliaPowerNetworks(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIEnsureCertificateRequest_CSIPCitiPowerPowercorUnited(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIEnsureCertificateRequest_CSIPAusNet(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIEnsureCertificateRequest_CSIPJemena(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIEnsureCertificateRequest_CSIPEnergexErgonEnergyQLD(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIEnsureCertificateRequest_CSIPWesternPowerSynergy(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIEnsureCertificateRequest(_message.Message):
    __slots__ = ('force_renew', 'csip_south_australia_power_networks', 'csip_citipower_powercor_united', 'csip_ausnet', 'csip_jemena', 'csip_energex_ergon_energy_qld', 'csip_western_power_synergy')
    FORCE_RENEW_FIELD_NUMBER: _ClassVar[int]
    CSIP_SOUTH_AUSTRALIA_POWER_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    CSIP_CITIPOWER_POWERCOR_UNITED_FIELD_NUMBER: _ClassVar[int]
    CSIP_AUSNET_FIELD_NUMBER: _ClassVar[int]
    CSIP_JEMENA_FIELD_NUMBER: _ClassVar[int]
    CSIP_ENERGEX_ERGON_ENERGY_QLD_FIELD_NUMBER: _ClassVar[int]
    CSIP_WESTERN_POWER_SYNERGY_FIELD_NUMBER: _ClassVar[int]
    force_renew: bool
    csip_south_australia_power_networks: TEGAPIEnsureCertificateRequest_CSIPSouthAustraliaPowerNetworks
    csip_citipower_powercor_united: TEGAPIEnsureCertificateRequest_CSIPCitiPowerPowercorUnited
    csip_ausnet: TEGAPIEnsureCertificateRequest_CSIPAusNet
    csip_jemena: TEGAPIEnsureCertificateRequest_CSIPJemena
    csip_energex_ergon_energy_qld: TEGAPIEnsureCertificateRequest_CSIPEnergexErgonEnergyQLD
    csip_western_power_synergy: TEGAPIEnsureCertificateRequest_CSIPWesternPowerSynergy

    def __init__(self, force_renew: bool=..., csip_south_australia_power_networks: _Optional[_Union[TEGAPIEnsureCertificateRequest_CSIPSouthAustraliaPowerNetworks, _Mapping]]=..., csip_citipower_powercor_united: _Optional[_Union[TEGAPIEnsureCertificateRequest_CSIPCitiPowerPowercorUnited, _Mapping]]=..., csip_ausnet: _Optional[_Union[TEGAPIEnsureCertificateRequest_CSIPAusNet, _Mapping]]=..., csip_jemena: _Optional[_Union[TEGAPIEnsureCertificateRequest_CSIPJemena, _Mapping]]=..., csip_energex_ergon_energy_qld: _Optional[_Union[TEGAPIEnsureCertificateRequest_CSIPEnergexErgonEnergyQLD, _Mapping]]=..., csip_western_power_synergy: _Optional[_Union[TEGAPIEnsureCertificateRequest_CSIPWesternPowerSynergy, _Mapping]]=...) -> None:
        ...

class TEGAPIEnsureCertificateResponse(_message.Message):
    __slots__ = ('certificate_exists',)
    CERTIFICATE_EXISTS_FIELD_NUMBER: _ClassVar[int]
    certificate_exists: bool

    def __init__(self, certificate_exists: bool=...) -> None:
        ...

class ControlEventSchedulingInfo(_message.Message):
    __slots__ = ('start_time', 'duration_seconds', 'priority')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    duration_seconds: int
    priority: int

    def __init__(self, start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., duration_seconds: _Optional[int]=..., priority: _Optional[int]=...) -> None:
        ...

class BackupEvent(_message.Message):
    __slots__ = ('id', 'name', 'sheduling_info')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHEDULING_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    sheduling_info: ControlEventSchedulingInfo

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., sheduling_info: _Optional[_Union[ControlEventSchedulingInfo, _Mapping]]=...) -> None:
        ...

class ManualBackupEvent(_message.Message):
    __slots__ = ('scheduling_info',)
    SCHEDULING_INFO_FIELD_NUMBER: _ClassVar[int]
    scheduling_info: ControlEventSchedulingInfo

    def __init__(self, scheduling_info: _Optional[_Union[ControlEventSchedulingInfo, _Mapping]]=...) -> None:
        ...

class TEGAPIScheduleManualBackupEventRequest(_message.Message):
    __slots__ = ('scheduling_info',)
    SCHEDULING_INFO_FIELD_NUMBER: _ClassVar[int]
    scheduling_info: ControlEventSchedulingInfo

    def __init__(self, scheduling_info: _Optional[_Union[ControlEventSchedulingInfo, _Mapping]]=...) -> None:
        ...

class TEGAPIScheduleManualBackupEventResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPICancelManualBackupEventRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPICancelManualBackupEventResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetBackupEventsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetBackupEventsResponse(_message.Message):
    __slots__ = ('manual_backup_event', 'backup_events')
    MANUAL_BACKUP_EVENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_EVENTS_FIELD_NUMBER: _ClassVar[int]
    manual_backup_event: ManualBackupEvent
    backup_events: _containers.RepeatedCompositeFieldContainer[BackupEvent]

    def __init__(self, manual_backup_event: _Optional[_Union[ManualBackupEvent, _Mapping]]=..., backup_events: _Optional[_Iterable[_Union[BackupEvent, _Mapping]]]=...) -> None:
        ...

class CsmsPropertiesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CsmsProperties(_message.Message):
    __slots__ = ('csms_root_ca', 'csms_url', 'charge_point_operator')
    CSMS_ROOT_CA_FIELD_NUMBER: _ClassVar[int]
    CSMS_URL_FIELD_NUMBER: _ClassVar[int]
    CHARGE_POINT_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    csms_root_ca: bytes
    csms_url: str
    charge_point_operator: str

    def __init__(self, csms_root_ca: _Optional[bytes]=..., csms_url: _Optional[str]=..., charge_point_operator: _Optional[str]=...) -> None:
        ...

class CsmsPropertiesResponse(_message.Message):
    __slots__ = ('canvas_site_status', 'csms_properties')
    CANVAS_SITE_STATUS_FIELD_NUMBER: _ClassVar[int]
    CSMS_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    canvas_site_status: CanvasSiteStatus
    csms_properties: CsmsProperties

    def __init__(self, canvas_site_status: _Optional[_Union[CanvasSiteStatus, str]]=..., csms_properties: _Optional[_Union[CsmsProperties, _Mapping]]=...) -> None:
        ...

class TEGAPIGetCsmsPropertiesRequest(_message.Message):
    __slots__ = ('request',)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: CsmsPropertiesRequest

    def __init__(self, request: _Optional[_Union[CsmsPropertiesRequest, _Mapping]]=...) -> None:
        ...

class TEGAPIGetCsmsPropertiesResponse(_message.Message):
    __slots__ = ('response',)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: CsmsPropertiesResponse

    def __init__(self, response: _Optional[_Union[CsmsPropertiesResponse, _Mapping]]=...) -> None:
        ...

class TEGAPIConfigureOcppRequest(_message.Message):
    __slots__ = ('csms_base_url',)
    CSMS_BASE_URL_FIELD_NUMBER: _ClassVar[int]
    csms_base_url: str

    def __init__(self, csms_base_url: _Optional[str]=...) -> None:
        ...

class TEGAPIConfigureOcppResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIStartProtectionTripSelfTestRequest(_message.Message):
    __slots__ = ('tests_to_run', 'disable_field_limits', 'disable_disconnect_on_failure', 'disable_abort_on_failure', 'fast_forward_to_step_before_nominal', 'repetitions', 'disable_inverter_fast_trips')
    TESTS_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_LIMITS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DISCONNECT_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ABORT_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    FAST_FORWARD_TO_STEP_BEFORE_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    REPETITIONS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_INVERTER_FAST_TRIPS_FIELD_NUMBER: _ClassVar[int]
    tests_to_run: _containers.RepeatedScalarFieldContainer[str]
    disable_field_limits: bool
    disable_disconnect_on_failure: bool
    disable_abort_on_failure: bool
    fast_forward_to_step_before_nominal: int
    repetitions: int
    disable_inverter_fast_trips: bool

    def __init__(self, tests_to_run: _Optional[_Iterable[str]]=..., disable_field_limits: bool=..., disable_disconnect_on_failure: bool=..., disable_abort_on_failure: bool=..., fast_forward_to_step_before_nominal: _Optional[int]=..., repetitions: _Optional[int]=..., disable_inverter_fast_trips: bool=...) -> None:
        ...

class TEGAPIStartProtectionTripSelfTestResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIStopProtectionTripSelfTestRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIStopProtectionTripSelfTestResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIProvisionEatonSmartBreakerRequest(_message.Message):
    __slots__ = ('device_id', 'broadcast_primary_udp_key', 'broadcast_secondary_udp_key', 'unicast_primary_udp_key', 'unicast_secondary_udp_key')
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_PRIMARY_UDP_KEY_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_SECONDARY_UDP_KEY_FIELD_NUMBER: _ClassVar[int]
    UNICAST_PRIMARY_UDP_KEY_FIELD_NUMBER: _ClassVar[int]
    UNICAST_SECONDARY_UDP_KEY_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    broadcast_primary_udp_key: bytes
    broadcast_secondary_udp_key: bytes
    unicast_primary_udp_key: bytes
    unicast_secondary_udp_key: bytes

    def __init__(self, device_id: _Optional[str]=..., broadcast_primary_udp_key: _Optional[bytes]=..., broadcast_secondary_udp_key: _Optional[bytes]=..., unicast_primary_udp_key: _Optional[bytes]=..., unicast_secondary_udp_key: _Optional[bytes]=...) -> None:
        ...

class TEGAPIProvisionEatonSmartBreakerResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIIdentifyEatonSmartBreakerRequest(_message.Message):
    __slots__ = ('device_id',)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str

    def __init__(self, device_id: _Optional[str]=...) -> None:
        ...

class TEGAPIIdentifyEatonSmartBreakerResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerPvacFanSelfTestRequest(_message.Message):
    __slots__ = ('beid',)
    BEID_FIELD_NUMBER: _ClassVar[int]
    beid: int

    def __init__(self, beid: _Optional[int]=...) -> None:
        ...

class TEGAPITriggerPvacFanSelfTestResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIProxyPrepareRegistrationPayloadRequest(_message.Message):
    __slots__ = ('request', 'target_din')
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    TARGET_DIN_FIELD_NUMBER: _ClassVar[int]
    request: _common_api_pb2.CommonAPIPrepareRegistrationPayloadRequest
    target_din: _device_pb2.Din

    def __init__(self, request: _Optional[_Union[_common_api_pb2.CommonAPIPrepareRegistrationPayloadRequest, _Mapping]]=..., target_din: _Optional[_Union[_device_pb2.Din, _Mapping]]=...) -> None:
        ...

class TEGAPIProxyPrepareRegistrationPayloadResponse(_message.Message):
    __slots__ = ('response',)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _common_api_pb2.CommonAPIPrepareRegistrationPayloadResponse

    def __init__(self, response: _Optional[_Union[_common_api_pb2.CommonAPIPrepareRegistrationPayloadResponse, _Mapping]]=...) -> None:
        ...

class TEGAPITriggerWallboxVehicleAbsentSelfTestRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerWallboxVehicleAbsentSelfTestResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPICustomerResetRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPICustomerResetResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIDelayBatteryCalibrationRequest(_message.Message):
    __slots__ = ('delay_hours',)
    DELAY_HOURS_FIELD_NUMBER: _ClassVar[int]
    delay_hours: int

    def __init__(self, delay_hours: _Optional[int]=...) -> None:
        ...

class TEGAPIDelayBatteryCalibrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetDelayBatteryCalibrationStatusRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetDelayBatteryCalibrationStatusResponse(_message.Message):
    __slots__ = ('calibration_delays_left', 'calibration_delay_remaining_seconds', 'max_calibration_delays')
    CALIBRATION_DELAYS_LEFT_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_DELAY_REMAINING_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_CALIBRATION_DELAYS_FIELD_NUMBER: _ClassVar[int]
    calibration_delays_left: int
    calibration_delay_remaining_seconds: int
    max_calibration_delays: int

    def __init__(self, calibration_delays_left: _Optional[int]=..., calibration_delay_remaining_seconds: _Optional[int]=..., max_calibration_delays: _Optional[int]=...) -> None:
        ...

class ControllableDeviceProgram_Key(_message.Message):
    __slots__ = ('device_id', 'priority')

    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIORITY_INVALID: _ClassVar[ControllableDeviceProgram_Key.Priority]
        PRIORITY_CUSTOMER_DEFAULT: _ClassVar[ControllableDeviceProgram_Key.Priority]
        PRIORITY_CUSTOMER_AUTOMATIC: _ClassVar[ControllableDeviceProgram_Key.Priority]
        PRIORITY_CUSTOMER_OVERRIDE: _ClassVar[ControllableDeviceProgram_Key.Priority]
    PRIORITY_INVALID: ControllableDeviceProgram_Key.Priority
    PRIORITY_CUSTOMER_DEFAULT: ControllableDeviceProgram_Key.Priority
    PRIORITY_CUSTOMER_AUTOMATIC: ControllableDeviceProgram_Key.Priority
    PRIORITY_CUSTOMER_OVERRIDE: ControllableDeviceProgram_Key.Priority
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    priority: ControllableDeviceProgram_Key.Priority

    def __init__(self, device_id: _Optional[str]=..., priority: _Optional[_Union[ControllableDeviceProgram_Key.Priority, str]]=...) -> None:
        ...

class ControllableDeviceProgram_Settings(_message.Message):
    __slots__ = ('contactor_state',)

    class ContactorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTACTOR_STATE_INVALID: _ClassVar[ControllableDeviceProgram_Settings.ContactorState]
        CONTACTOR_STATE_OPEN: _ClassVar[ControllableDeviceProgram_Settings.ContactorState]
        CONTACTOR_STATE_CLOSED: _ClassVar[ControllableDeviceProgram_Settings.ContactorState]
    CONTACTOR_STATE_INVALID: ControllableDeviceProgram_Settings.ContactorState
    CONTACTOR_STATE_OPEN: ControllableDeviceProgram_Settings.ContactorState
    CONTACTOR_STATE_CLOSED: ControllableDeviceProgram_Settings.ContactorState
    CONTACTOR_STATE_FIELD_NUMBER: _ClassVar[int]
    contactor_state: ControllableDeviceProgram_Settings.ContactorState

    def __init__(self, contactor_state: _Optional[_Union[ControllableDeviceProgram_Settings.ContactorState, str]]=...) -> None:
        ...

class ControllableDeviceProgram_Schedule_Boundary(_message.Message):
    __slots__ = ('static_condition', 'timestamp', 'islanding_state', 'state_of_energy')

    class StaticCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATIC_CONDITION_INVALID: _ClassVar[ControllableDeviceProgram_Schedule_Boundary.StaticCondition]
        STATIC_CONDITION_ALWAYS: _ClassVar[ControllableDeviceProgram_Schedule_Boundary.StaticCondition]
        STATIC_CONDITION_NEVER: _ClassVar[ControllableDeviceProgram_Schedule_Boundary.StaticCondition]
    STATIC_CONDITION_INVALID: ControllableDeviceProgram_Schedule_Boundary.StaticCondition
    STATIC_CONDITION_ALWAYS: ControllableDeviceProgram_Schedule_Boundary.StaticCondition
    STATIC_CONDITION_NEVER: ControllableDeviceProgram_Schedule_Boundary.StaticCondition

    class IslandingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ISLANDING_STATE_INVALID: _ClassVar[ControllableDeviceProgram_Schedule_Boundary.IslandingState]
        ISLANDING_STATE_ON_GRID: _ClassVar[ControllableDeviceProgram_Schedule_Boundary.IslandingState]
        ISLANDING_STATE_OFF_GRID: _ClassVar[ControllableDeviceProgram_Schedule_Boundary.IslandingState]
    ISLANDING_STATE_INVALID: ControllableDeviceProgram_Schedule_Boundary.IslandingState
    ISLANDING_STATE_ON_GRID: ControllableDeviceProgram_Schedule_Boundary.IslandingState
    ISLANDING_STATE_OFF_GRID: ControllableDeviceProgram_Schedule_Boundary.IslandingState

    class StateOfEnergy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_OF_ENERGY_INVALID: _ClassVar[ControllableDeviceProgram_Schedule_Boundary.StateOfEnergy]
        STATE_OF_ENERGY_ABOVE_BACKUP_RESERVE: _ClassVar[ControllableDeviceProgram_Schedule_Boundary.StateOfEnergy]
        STATE_OF_ENERGY_BELOW_BACKUP_RESERVE: _ClassVar[ControllableDeviceProgram_Schedule_Boundary.StateOfEnergy]
    STATE_OF_ENERGY_INVALID: ControllableDeviceProgram_Schedule_Boundary.StateOfEnergy
    STATE_OF_ENERGY_ABOVE_BACKUP_RESERVE: ControllableDeviceProgram_Schedule_Boundary.StateOfEnergy
    STATE_OF_ENERGY_BELOW_BACKUP_RESERVE: ControllableDeviceProgram_Schedule_Boundary.StateOfEnergy
    STATIC_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ISLANDING_STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_OF_ENERGY_FIELD_NUMBER: _ClassVar[int]
    static_condition: ControllableDeviceProgram_Schedule_Boundary.StaticCondition
    timestamp: _timestamp_pb2.Timestamp
    islanding_state: ControllableDeviceProgram_Schedule_Boundary.IslandingState
    state_of_energy: ControllableDeviceProgram_Schedule_Boundary.StateOfEnergy

    def __init__(self, static_condition: _Optional[_Union[ControllableDeviceProgram_Schedule_Boundary.StaticCondition, str]]=..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., islanding_state: _Optional[_Union[ControllableDeviceProgram_Schedule_Boundary.IslandingState, str]]=..., state_of_energy: _Optional[_Union[ControllableDeviceProgram_Schedule_Boundary.StateOfEnergy, str]]=...) -> None:
        ...

class ControllableDeviceProgram_Schedule(_message.Message):
    __slots__ = ('start', 'end', 'expiry')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    expiry: _timestamp_pb2.Timestamp

    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., expiry: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ControllableDeviceProgram(_message.Message):
    __slots__ = ('key', 'settings', 'schedule')
    KEY_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    key: ControllableDeviceProgram_Key
    settings: ControllableDeviceProgram_Settings
    schedule: ControllableDeviceProgram_Schedule

    def __init__(self, key: _Optional[_Union[ControllableDeviceProgram_Key, _Mapping]]=..., settings: _Optional[_Union[ControllableDeviceProgram_Settings, _Mapping]]=..., schedule: _Optional[_Union[ControllableDeviceProgram_Schedule, _Mapping]]=...) -> None:
        ...

class TEGAPIGetControllableDeviceProgramsRequest(_message.Message):
    __slots__ = ('device_ids',)
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    device_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, device_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class TEGAPIGetControllableDeviceProgramsResponse(_message.Message):
    __slots__ = ('active_programs', 'inactive_programs')
    ACTIVE_PROGRAMS_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_PROGRAMS_FIELD_NUMBER: _ClassVar[int]
    active_programs: _containers.RepeatedCompositeFieldContainer[ControllableDeviceProgram]
    inactive_programs: _containers.RepeatedCompositeFieldContainer[ControllableDeviceProgram]

    def __init__(self, active_programs: _Optional[_Iterable[_Union[ControllableDeviceProgram, _Mapping]]]=..., inactive_programs: _Optional[_Iterable[_Union[ControllableDeviceProgram, _Mapping]]]=...) -> None:
        ...

class TEGAPIUpdateControllableDeviceProgramsRequest(_message.Message):
    __slots__ = ('updated_programs',)
    UPDATED_PROGRAMS_FIELD_NUMBER: _ClassVar[int]
    updated_programs: _containers.RepeatedCompositeFieldContainer[ControllableDeviceProgram]

    def __init__(self, updated_programs: _Optional[_Iterable[_Union[ControllableDeviceProgram, _Mapping]]]=...) -> None:
        ...

class TEGAPIUpdateControllableDeviceProgramsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIDeleteControllableDeviceProgramsRequest(_message.Message):
    __slots__ = ('deletion_keys',)
    DELETION_KEYS_FIELD_NUMBER: _ClassVar[int]
    deletion_keys: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, deletion_keys: _Optional[_Iterable[str]]=...) -> None:
        ...

class TEGAPIDeleteControllableDeviceProgramsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIClearPowerwall3LockoutAlertsRequest(_message.Message):
    __slots__ = ('din',)
    DIN_FIELD_NUMBER: _ClassVar[int]
    din: str

    def __init__(self, din: _Optional[str]=...) -> None:
        ...

class TEGAPIClearPowerwall3LockoutAlertsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIRetrieveSiteUuidRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIRetrieveSiteUuidResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIRetrieveSiteSuggestionRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIRetrieveSiteSuggestionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGMessages(_message.Message):
    __slots__ = ('get_config_request', 'get_config_response', 'set_island_mode_request', 'set_island_mode_response', 'trigger_islanding_black_start_request', 'trigger_islanding_black_start_response', 'trigger_asset_manifest_upload_request', 'trigger_asset_manifest_upload_response', 'trigger_powerwall2_enumeration_request', 'trigger_powerwall2_enumeration_response', 'trigger_es_can_firmware_update_request', 'trigger_es_can_firmware_update_response', 'register_request', 'register_response', 'trigger_powerwall2_phase_detection_request', 'trigger_powerwall2_phase_detection_response', 'reset_powerwall2_phase_detection_request', 'reset_powerwall2_phase_detection_response', 'force_wifi_scan_request', 'force_wifi_scan_response', 'start_powerwall2_inverter_self_tests_request', 'start_powerwall2_inverter_self_tests_response', 'stop_powerwall2_inverter_self_tests_request', 'stop_powerwall2_inverter_self_tests_response', 'start_powerwall2_bubble_shed_request', 'start_powerwall2_bubble_shed_response', 'clear_solar_inverter_alerts_request', 'clear_solar_inverter_alerts_response', 'get_wifi_config_with_credentials_request', 'get_wifi_config_with_credentials_response', 'disable_batteries_request', 'disable_batteries_response', 'trigger_p_w3_can_firmware_update_request', 'trigger_p_w3_can_firmware_update_response', 'trigger_powerwall3_enumeration_request', 'trigger_powerwall3_enumeration_response', 'dispatch_battery_power_request', 'dispatch_battery_power_response', 'detect_wired_meters_request', 'detect_wired_meters_response', 'bypass_battery_soe_adjustment_constraints_request', 'bypass_battery_soe_adjustment_constraints_response', 'ensure_certificate_request', 'ensure_certificate_response', 'schedule_manual_backup_event_request', 'schedule_manual_backup_event_response', 'cancel_manual_backup_event_request', 'cancel_manual_backup_event_response', 'get_backup_events_request', 'get_backup_events_response', 'get_csms_properties_request', 'get_csms_properties_response', 'configure_ocpp_request', 'configure_ocpp_response', 'retrieve_site_uuid_request', 'retrieve_site_uuid_response', 'retrieve_site_suggestion_request', 'retrieve_site_suggestion_response', 'start_protection_trip_self_test_request', 'start_protection_trip_self_test_response', 'stop_protection_trip_self_test_request', 'stop_protection_trip_self_test_response', 'provision_eaton_smart_breaker_request', 'provision_eaton_smart_breaker_response', 'identify_eaton_smart_breaker_request', 'identify_eaton_smart_breaker_response', 'trigger_pvac_fan_self_test_request', 'trigger_pvac_fan_self_test_response', 'proxy_prepare_registration_payload_request', 'proxy_prepare_registration_payload_response', 'trigger_wallbox_vehicle_absent_self_test_request', 'trigger_wallbox_vehicle_absent_self_test_response', 'customer_reset_request', 'customer_reset_response', 'delay_battery_calibration_request', 'delay_battery_calibration_response', 'get_delay_battery_calibration_status_request', 'get_delay_battery_calibration_status_response', 'get_controllable_device_programs_request', 'get_controllable_device_programs_response', 'update_controllable_device_programs_request', 'update_controllable_device_programs_response', 'delete_controllable_device_programs_request', 'delete_controllable_device_programs_response', 'clear_powerwall3_lockout_alerts_request', 'clear_powerwall3_lockout_alerts_response')
    GET_CONFIG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_CONFIG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SET_ISLAND_MODE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_ISLAND_MODE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ISLANDING_BLACK_START_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ISLANDING_BLACK_START_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ASSET_MANIFEST_UPLOAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ASSET_MANIFEST_UPLOAD_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_POWERWALL2_ENUMERATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_POWERWALL2_ENUMERATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ES_CAN_FIRMWARE_UPDATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ES_CAN_FIRMWARE_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REGISTER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REGISTER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_POWERWALL2_PHASE_DETECTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_POWERWALL2_PHASE_DETECTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESET_POWERWALL2_PHASE_DETECTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESET_POWERWALL2_PHASE_DETECTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    FORCE_WIFI_SCAN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FORCE_WIFI_SCAN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    START_POWERWALL2_INVERTER_SELF_TESTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    START_POWERWALL2_INVERTER_SELF_TESTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STOP_POWERWALL2_INVERTER_SELF_TESTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    STOP_POWERWALL2_INVERTER_SELF_TESTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    START_POWERWALL2_BUBBLE_SHED_REQUEST_FIELD_NUMBER: _ClassVar[int]
    START_POWERWALL2_BUBBLE_SHED_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_SOLAR_INVERTER_ALERTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CLEAR_SOLAR_INVERTER_ALERTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_WIFI_CONFIG_WITH_CREDENTIALS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_WIFI_CONFIG_WITH_CREDENTIALS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_BATTERIES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DISABLE_BATTERIES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_P_W3_CAN_FIRMWARE_UPDATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_P_W3_CAN_FIRMWARE_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_POWERWALL3_ENUMERATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_POWERWALL3_ENUMERATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_BATTERY_POWER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_BATTERY_POWER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DETECT_WIRED_METERS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DETECT_WIRED_METERS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BYPASS_BATTERY_SOE_ADJUSTMENT_CONSTRAINTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BYPASS_BATTERY_SOE_ADJUSTMENT_CONSTRAINTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ENSURE_CERTIFICATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ENSURE_CERTIFICATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_MANUAL_BACKUP_EVENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_MANUAL_BACKUP_EVENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_MANUAL_BACKUP_EVENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CANCEL_MANUAL_BACKUP_EVENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_EVENTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_EVENTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_CSMS_PROPERTIES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_CSMS_PROPERTIES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_OCPP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_OCPP_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_SITE_UUID_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_SITE_UUID_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_SITE_SUGGESTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_SITE_SUGGESTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    START_PROTECTION_TRIP_SELF_TEST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    START_PROTECTION_TRIP_SELF_TEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STOP_PROTECTION_TRIP_SELF_TEST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    STOP_PROTECTION_TRIP_SELF_TEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PROVISION_EATON_SMART_BREAKER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROVISION_EATON_SMART_BREAKER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFY_EATON_SMART_BREAKER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    IDENTIFY_EATON_SMART_BREAKER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_PVAC_FAN_SELF_TEST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_PVAC_FAN_SELF_TEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PROXY_PREPARE_REGISTRATION_PAYLOAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROXY_PREPARE_REGISTRATION_PAYLOAD_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_WALLBOX_VEHICLE_ABSENT_SELF_TEST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_WALLBOX_VEHICLE_ABSENT_SELF_TEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_RESET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_RESET_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DELAY_BATTERY_CALIBRATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DELAY_BATTERY_CALIBRATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_DELAY_BATTERY_CALIBRATION_STATUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_DELAY_BATTERY_CALIBRATION_STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_CONTROLLABLE_DEVICE_PROGRAMS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_CONTROLLABLE_DEVICE_PROGRAMS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CONTROLLABLE_DEVICE_PROGRAMS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CONTROLLABLE_DEVICE_PROGRAMS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DELETE_CONTROLLABLE_DEVICE_PROGRAMS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DELETE_CONTROLLABLE_DEVICE_PROGRAMS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_POWERWALL3_LOCKOUT_ALERTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CLEAR_POWERWALL3_LOCKOUT_ALERTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    get_config_request: TEGAPIGetConfigRequest
    get_config_response: TEGAPIGetConfigResponse
    set_island_mode_request: TEGAPISetIslandModeRequest
    set_island_mode_response: TEGAPISetIslandModeResponse
    trigger_islanding_black_start_request: TEGAPITriggerIslandingBlackStartRequest
    trigger_islanding_black_start_response: TEGAPITriggerIslandingBlackStartResponse
    trigger_asset_manifest_upload_request: TEGAPITriggerAssetManifestUploadRequest
    trigger_asset_manifest_upload_response: TEGAPITriggerAssetManifestUploadResponse
    trigger_powerwall2_enumeration_request: TEGAPITriggerPowerwall2EnumerationRequest
    trigger_powerwall2_enumeration_response: TEGAPITriggerPowerwall2EnumerationResponse
    trigger_es_can_firmware_update_request: TEGAPITriggerEsCanFirmwareUpdateRequest
    trigger_es_can_firmware_update_response: TEGAPITriggerEsCanFirmwareUpdateResponse
    register_request: TEGAPIRegisterRequest
    register_response: TEGAPIRegisterResponse
    trigger_powerwall2_phase_detection_request: TEGAPITriggerPowerwall2PhaseDetectionRequest
    trigger_powerwall2_phase_detection_response: TEGAPITriggerPowerwall2PhaseDetectionResponse
    reset_powerwall2_phase_detection_request: TEGAPIResetPowerwall2PhaseDetectionRequest
    reset_powerwall2_phase_detection_response: TEGAPIResetPowerwall2PhaseDetectionResponse
    force_wifi_scan_request: TEGAPIForceWifiScanRequest
    force_wifi_scan_response: TEGAPIForceWifiScanResponse
    start_powerwall2_inverter_self_tests_request: TEGAPIStartPowerwall2InverterSelfTestsRequest
    start_powerwall2_inverter_self_tests_response: TEGAPIStartPowerwall2InverterSelfTestsResponse
    stop_powerwall2_inverter_self_tests_request: TEGAPIStopPowerwall2InverterSelfTestsRequest
    stop_powerwall2_inverter_self_tests_response: TEGAPIStopPowerwall2InverterSelfTestsResponse
    start_powerwall2_bubble_shed_request: TEGAPIStartPowerwall2BubbleShedRequest
    start_powerwall2_bubble_shed_response: TEGAPIStartPowerwall2BubbleShedResponse
    clear_solar_inverter_alerts_request: TEGAPIClearSolarInverterAlertsRequest
    clear_solar_inverter_alerts_response: TEGAPIClearSolarInverterAlertsResponse
    get_wifi_config_with_credentials_request: TEGAPIGetWifiConfigWithCredentialsRequest
    get_wifi_config_with_credentials_response: TEGAPIGetWifiConfigWithCredentialsResponse
    disable_batteries_request: TEGAPIDisableBatteriesRequest
    disable_batteries_response: TEGAPIDisableBatteriesResponse
    trigger_p_w3_can_firmware_update_request: TEGAPITriggerPW3CanFirmwareUpdateRequest
    trigger_p_w3_can_firmware_update_response: TEGAPITriggerPW3CanFirmwareUpdateResponse
    trigger_powerwall3_enumeration_request: TEGAPITriggerPowerwall3EnumerationRequest
    trigger_powerwall3_enumeration_response: TEGAPITriggerPowerwall3EnumerationResponse
    dispatch_battery_power_request: TEGAPIDispatchBatteryPowerRequest
    dispatch_battery_power_response: TEGAPIDispatchBatteryPowerResponse
    detect_wired_meters_request: TEGAPIDetectWiredMetersRequest
    detect_wired_meters_response: TEGAPIDetectWiredMetersResponse
    bypass_battery_soe_adjustment_constraints_request: TEGAPIBypassBatterySoeAdjustmentConstraintsRequest
    bypass_battery_soe_adjustment_constraints_response: TEGAPIBypassBatterySoeAdjustmentConstraintsResponse
    ensure_certificate_request: TEGAPIEnsureCertificateRequest
    ensure_certificate_response: TEGAPIEnsureCertificateResponse
    schedule_manual_backup_event_request: TEGAPIScheduleManualBackupEventRequest
    schedule_manual_backup_event_response: TEGAPIScheduleManualBackupEventResponse
    cancel_manual_backup_event_request: TEGAPICancelManualBackupEventRequest
    cancel_manual_backup_event_response: TEGAPICancelManualBackupEventResponse
    get_backup_events_request: TEGAPIGetBackupEventsRequest
    get_backup_events_response: TEGAPIGetBackupEventsResponse
    get_csms_properties_request: TEGAPIGetCsmsPropertiesRequest
    get_csms_properties_response: TEGAPIGetCsmsPropertiesResponse
    configure_ocpp_request: TEGAPIConfigureOcppRequest
    configure_ocpp_response: TEGAPIConfigureOcppResponse
    retrieve_site_uuid_request: TEGAPIRetrieveSiteUuidRequest
    retrieve_site_uuid_response: TEGAPIRetrieveSiteUuidResponse
    retrieve_site_suggestion_request: TEGAPIRetrieveSiteSuggestionRequest
    retrieve_site_suggestion_response: TEGAPIRetrieveSiteSuggestionResponse
    start_protection_trip_self_test_request: TEGAPIStartProtectionTripSelfTestRequest
    start_protection_trip_self_test_response: TEGAPIStartProtectionTripSelfTestResponse
    stop_protection_trip_self_test_request: TEGAPIStopProtectionTripSelfTestRequest
    stop_protection_trip_self_test_response: TEGAPIStopProtectionTripSelfTestResponse
    provision_eaton_smart_breaker_request: TEGAPIProvisionEatonSmartBreakerRequest
    provision_eaton_smart_breaker_response: TEGAPIProvisionEatonSmartBreakerResponse
    identify_eaton_smart_breaker_request: TEGAPIIdentifyEatonSmartBreakerRequest
    identify_eaton_smart_breaker_response: TEGAPIIdentifyEatonSmartBreakerResponse
    trigger_pvac_fan_self_test_request: TEGAPITriggerPvacFanSelfTestRequest
    trigger_pvac_fan_self_test_response: TEGAPITriggerPvacFanSelfTestResponse
    proxy_prepare_registration_payload_request: TEGAPIProxyPrepareRegistrationPayloadRequest
    proxy_prepare_registration_payload_response: TEGAPIProxyPrepareRegistrationPayloadResponse
    trigger_wallbox_vehicle_absent_self_test_request: TEGAPITriggerWallboxVehicleAbsentSelfTestRequest
    trigger_wallbox_vehicle_absent_self_test_response: TEGAPITriggerWallboxVehicleAbsentSelfTestResponse
    customer_reset_request: TEGAPICustomerResetRequest
    customer_reset_response: TEGAPICustomerResetResponse
    delay_battery_calibration_request: TEGAPIDelayBatteryCalibrationRequest
    delay_battery_calibration_response: TEGAPIDelayBatteryCalibrationResponse
    get_delay_battery_calibration_status_request: TEGAPIGetDelayBatteryCalibrationStatusRequest
    get_delay_battery_calibration_status_response: TEGAPIGetDelayBatteryCalibrationStatusResponse
    get_controllable_device_programs_request: TEGAPIGetControllableDeviceProgramsRequest
    get_controllable_device_programs_response: TEGAPIGetControllableDeviceProgramsResponse
    update_controllable_device_programs_request: TEGAPIUpdateControllableDeviceProgramsRequest
    update_controllable_device_programs_response: TEGAPIUpdateControllableDeviceProgramsResponse
    delete_controllable_device_programs_request: TEGAPIDeleteControllableDeviceProgramsRequest
    delete_controllable_device_programs_response: TEGAPIDeleteControllableDeviceProgramsResponse
    clear_powerwall3_lockout_alerts_request: TEGAPIClearPowerwall3LockoutAlertsRequest
    clear_powerwall3_lockout_alerts_response: TEGAPIClearPowerwall3LockoutAlertsResponse

    def __init__(self, get_config_request: _Optional[_Union[TEGAPIGetConfigRequest, _Mapping]]=..., get_config_response: _Optional[_Union[TEGAPIGetConfigResponse, _Mapping]]=..., set_island_mode_request: _Optional[_Union[TEGAPISetIslandModeRequest, _Mapping]]=..., set_island_mode_response: _Optional[_Union[TEGAPISetIslandModeResponse, _Mapping]]=..., trigger_islanding_black_start_request: _Optional[_Union[TEGAPITriggerIslandingBlackStartRequest, _Mapping]]=..., trigger_islanding_black_start_response: _Optional[_Union[TEGAPITriggerIslandingBlackStartResponse, _Mapping]]=..., trigger_asset_manifest_upload_request: _Optional[_Union[TEGAPITriggerAssetManifestUploadRequest, _Mapping]]=..., trigger_asset_manifest_upload_response: _Optional[_Union[TEGAPITriggerAssetManifestUploadResponse, _Mapping]]=..., trigger_powerwall2_enumeration_request: _Optional[_Union[TEGAPITriggerPowerwall2EnumerationRequest, _Mapping]]=..., trigger_powerwall2_enumeration_response: _Optional[_Union[TEGAPITriggerPowerwall2EnumerationResponse, _Mapping]]=..., trigger_es_can_firmware_update_request: _Optional[_Union[TEGAPITriggerEsCanFirmwareUpdateRequest, _Mapping]]=..., trigger_es_can_firmware_update_response: _Optional[_Union[TEGAPITriggerEsCanFirmwareUpdateResponse, _Mapping]]=..., register_request: _Optional[_Union[TEGAPIRegisterRequest, _Mapping]]=..., register_response: _Optional[_Union[TEGAPIRegisterResponse, _Mapping]]=..., trigger_powerwall2_phase_detection_request: _Optional[_Union[TEGAPITriggerPowerwall2PhaseDetectionRequest, _Mapping]]=..., trigger_powerwall2_phase_detection_response: _Optional[_Union[TEGAPITriggerPowerwall2PhaseDetectionResponse, _Mapping]]=..., reset_powerwall2_phase_detection_request: _Optional[_Union[TEGAPIResetPowerwall2PhaseDetectionRequest, _Mapping]]=..., reset_powerwall2_phase_detection_response: _Optional[_Union[TEGAPIResetPowerwall2PhaseDetectionResponse, _Mapping]]=..., force_wifi_scan_request: _Optional[_Union[TEGAPIForceWifiScanRequest, _Mapping]]=..., force_wifi_scan_response: _Optional[_Union[TEGAPIForceWifiScanResponse, _Mapping]]=..., start_powerwall2_inverter_self_tests_request: _Optional[_Union[TEGAPIStartPowerwall2InverterSelfTestsRequest, _Mapping]]=..., start_powerwall2_inverter_self_tests_response: _Optional[_Union[TEGAPIStartPowerwall2InverterSelfTestsResponse, _Mapping]]=..., stop_powerwall2_inverter_self_tests_request: _Optional[_Union[TEGAPIStopPowerwall2InverterSelfTestsRequest, _Mapping]]=..., stop_powerwall2_inverter_self_tests_response: _Optional[_Union[TEGAPIStopPowerwall2InverterSelfTestsResponse, _Mapping]]=..., start_powerwall2_bubble_shed_request: _Optional[_Union[TEGAPIStartPowerwall2BubbleShedRequest, _Mapping]]=..., start_powerwall2_bubble_shed_response: _Optional[_Union[TEGAPIStartPowerwall2BubbleShedResponse, _Mapping]]=..., clear_solar_inverter_alerts_request: _Optional[_Union[TEGAPIClearSolarInverterAlertsRequest, _Mapping]]=..., clear_solar_inverter_alerts_response: _Optional[_Union[TEGAPIClearSolarInverterAlertsResponse, _Mapping]]=..., get_wifi_config_with_credentials_request: _Optional[_Union[TEGAPIGetWifiConfigWithCredentialsRequest, _Mapping]]=..., get_wifi_config_with_credentials_response: _Optional[_Union[TEGAPIGetWifiConfigWithCredentialsResponse, _Mapping]]=..., disable_batteries_request: _Optional[_Union[TEGAPIDisableBatteriesRequest, _Mapping]]=..., disable_batteries_response: _Optional[_Union[TEGAPIDisableBatteriesResponse, _Mapping]]=..., trigger_p_w3_can_firmware_update_request: _Optional[_Union[TEGAPITriggerPW3CanFirmwareUpdateRequest, _Mapping]]=..., trigger_p_w3_can_firmware_update_response: _Optional[_Union[TEGAPITriggerPW3CanFirmwareUpdateResponse, _Mapping]]=..., trigger_powerwall3_enumeration_request: _Optional[_Union[TEGAPITriggerPowerwall3EnumerationRequest, _Mapping]]=..., trigger_powerwall3_enumeration_response: _Optional[_Union[TEGAPITriggerPowerwall3EnumerationResponse, _Mapping]]=..., dispatch_battery_power_request: _Optional[_Union[TEGAPIDispatchBatteryPowerRequest, _Mapping]]=..., dispatch_battery_power_response: _Optional[_Union[TEGAPIDispatchBatteryPowerResponse, _Mapping]]=..., detect_wired_meters_request: _Optional[_Union[TEGAPIDetectWiredMetersRequest, _Mapping]]=..., detect_wired_meters_response: _Optional[_Union[TEGAPIDetectWiredMetersResponse, _Mapping]]=..., bypass_battery_soe_adjustment_constraints_request: _Optional[_Union[TEGAPIBypassBatterySoeAdjustmentConstraintsRequest, _Mapping]]=..., bypass_battery_soe_adjustment_constraints_response: _Optional[_Union[TEGAPIBypassBatterySoeAdjustmentConstraintsResponse, _Mapping]]=..., ensure_certificate_request: _Optional[_Union[TEGAPIEnsureCertificateRequest, _Mapping]]=..., ensure_certificate_response: _Optional[_Union[TEGAPIEnsureCertificateResponse, _Mapping]]=..., schedule_manual_backup_event_request: _Optional[_Union[TEGAPIScheduleManualBackupEventRequest, _Mapping]]=..., schedule_manual_backup_event_response: _Optional[_Union[TEGAPIScheduleManualBackupEventResponse, _Mapping]]=..., cancel_manual_backup_event_request: _Optional[_Union[TEGAPICancelManualBackupEventRequest, _Mapping]]=..., cancel_manual_backup_event_response: _Optional[_Union[TEGAPICancelManualBackupEventResponse, _Mapping]]=..., get_backup_events_request: _Optional[_Union[TEGAPIGetBackupEventsRequest, _Mapping]]=..., get_backup_events_response: _Optional[_Union[TEGAPIGetBackupEventsResponse, _Mapping]]=..., get_csms_properties_request: _Optional[_Union[TEGAPIGetCsmsPropertiesRequest, _Mapping]]=..., get_csms_properties_response: _Optional[_Union[TEGAPIGetCsmsPropertiesResponse, _Mapping]]=..., configure_ocpp_request: _Optional[_Union[TEGAPIConfigureOcppRequest, _Mapping]]=..., configure_ocpp_response: _Optional[_Union[TEGAPIConfigureOcppResponse, _Mapping]]=..., retrieve_site_uuid_request: _Optional[_Union[TEGAPIRetrieveSiteUuidRequest, _Mapping]]=..., retrieve_site_uuid_response: _Optional[_Union[TEGAPIRetrieveSiteUuidResponse, _Mapping]]=..., retrieve_site_suggestion_request: _Optional[_Union[TEGAPIRetrieveSiteSuggestionRequest, _Mapping]]=..., retrieve_site_suggestion_response: _Optional[_Union[TEGAPIRetrieveSiteSuggestionResponse, _Mapping]]=..., start_protection_trip_self_test_request: _Optional[_Union[TEGAPIStartProtectionTripSelfTestRequest, _Mapping]]=..., start_protection_trip_self_test_response: _Optional[_Union[TEGAPIStartProtectionTripSelfTestResponse, _Mapping]]=..., stop_protection_trip_self_test_request: _Optional[_Union[TEGAPIStopProtectionTripSelfTestRequest, _Mapping]]=..., stop_protection_trip_self_test_response: _Optional[_Union[TEGAPIStopProtectionTripSelfTestResponse, _Mapping]]=..., provision_eaton_smart_breaker_request: _Optional[_Union[TEGAPIProvisionEatonSmartBreakerRequest, _Mapping]]=..., provision_eaton_smart_breaker_response: _Optional[_Union[TEGAPIProvisionEatonSmartBreakerResponse, _Mapping]]=..., identify_eaton_smart_breaker_request: _Optional[_Union[TEGAPIIdentifyEatonSmartBreakerRequest, _Mapping]]=..., identify_eaton_smart_breaker_response: _Optional[_Union[TEGAPIIdentifyEatonSmartBreakerResponse, _Mapping]]=..., trigger_pvac_fan_self_test_request: _Optional[_Union[TEGAPITriggerPvacFanSelfTestRequest, _Mapping]]=..., trigger_pvac_fan_self_test_response: _Optional[_Union[TEGAPITriggerPvacFanSelfTestResponse, _Mapping]]=..., proxy_prepare_registration_payload_request: _Optional[_Union[TEGAPIProxyPrepareRegistrationPayloadRequest, _Mapping]]=..., proxy_prepare_registration_payload_response: _Optional[_Union[TEGAPIProxyPrepareRegistrationPayloadResponse, _Mapping]]=..., trigger_wallbox_vehicle_absent_self_test_request: _Optional[_Union[TEGAPITriggerWallboxVehicleAbsentSelfTestRequest, _Mapping]]=..., trigger_wallbox_vehicle_absent_self_test_response: _Optional[_Union[TEGAPITriggerWallboxVehicleAbsentSelfTestResponse, _Mapping]]=..., customer_reset_request: _Optional[_Union[TEGAPICustomerResetRequest, _Mapping]]=..., customer_reset_response: _Optional[_Union[TEGAPICustomerResetResponse, _Mapping]]=..., delay_battery_calibration_request: _Optional[_Union[TEGAPIDelayBatteryCalibrationRequest, _Mapping]]=..., delay_battery_calibration_response: _Optional[_Union[TEGAPIDelayBatteryCalibrationResponse, _Mapping]]=..., get_delay_battery_calibration_status_request: _Optional[_Union[TEGAPIGetDelayBatteryCalibrationStatusRequest, _Mapping]]=..., get_delay_battery_calibration_status_response: _Optional[_Union[TEGAPIGetDelayBatteryCalibrationStatusResponse, _Mapping]]=..., get_controllable_device_programs_request: _Optional[_Union[TEGAPIGetControllableDeviceProgramsRequest, _Mapping]]=..., get_controllable_device_programs_response: _Optional[_Union[TEGAPIGetControllableDeviceProgramsResponse, _Mapping]]=..., update_controllable_device_programs_request: _Optional[_Union[TEGAPIUpdateControllableDeviceProgramsRequest, _Mapping]]=..., update_controllable_device_programs_response: _Optional[_Union[TEGAPIUpdateControllableDeviceProgramsResponse, _Mapping]]=..., delete_controllable_device_programs_request: _Optional[_Union[TEGAPIDeleteControllableDeviceProgramsRequest, _Mapping]]=..., delete_controllable_device_programs_response: _Optional[_Union[TEGAPIDeleteControllableDeviceProgramsResponse, _Mapping]]=..., clear_powerwall3_lockout_alerts_request: _Optional[_Union[TEGAPIClearPowerwall3LockoutAlertsRequest, _Mapping]]=..., clear_powerwall3_lockout_alerts_response: _Optional[_Union[TEGAPIClearPowerwall3LockoutAlertsResponse, _Mapping]]=...) -> None:
        ...