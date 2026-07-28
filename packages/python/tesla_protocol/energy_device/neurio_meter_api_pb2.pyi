from . import networking_pb2 as _networking_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PowerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POWER_TYPE_INVALID: _ClassVar[PowerType]
    POWER_TYPE_AC_1_PHASE: _ClassVar[PowerType]
    POWER_TYPE_AC_3_PHASE: _ClassVar[PowerType]
    POWER_TYPE_DC: _ClassVar[PowerType]

class ConnectorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTOR_TYPE_INVALID: _ClassVar[ConnectorType]
    CONNECTOR_TYPE_CCS1: _ClassVar[ConnectorType]
    CONNECTOR_TYPE_CCS2: _ClassVar[ConnectorType]
    CONNECTOR_TYPE_GB: _ClassVar[ConnectorType]
    CONNECTOR_TYPE_NA: _ClassVar[ConnectorType]
    CONNECTOR_TYPE_TYPE_2: _ClassVar[ConnectorType]
    CONNECTOR_TYPE_J1772: _ClassVar[ConnectorType]
    CONNECTOR_TYPE_INDISTINGUISHABLE_DUAL_HANDLE: _ClassVar[ConnectorType]
    CONNECTOR_TYPE_UNKNOWN: _ClassVar[ConnectorType]
    CONNECTOR_TYPE_MCS: _ClassVar[ConnectorType]

class NeurioConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NEURIO_CONNECTION_STATUS_INVALID: _ClassVar[NeurioConnectionStatus]
    NEURIO_CONNECTION_STATUS_NO_COMMS: _ClassVar[NeurioConnectionStatus]
    NEURIO_CONNECTION_STATUS_PAIRING: _ClassVar[NeurioConnectionStatus]
    NEURIO_CONNECTION_STATUS_CONNECTED: _ClassVar[NeurioConnectionStatus]
    NEURIO_CONNECTION_STATUS_CONFIG_CHANGE_UNDERWAY: _ClassVar[NeurioConnectionStatus]

class NeurioConnectionError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NEURIO_CONNECTION_ERROR_INVALID: _ClassVar[NeurioConnectionError]
    NEURIO_CONNECTION_ERROR_NONE: _ClassVar[NeurioConnectionError]
    NEURIO_CONNECTION_ERROR_UNKNOWN: _ClassVar[NeurioConnectionError]
    NEURIO_CONNECTION_ERROR_WIFI_AP: _ClassVar[NeurioConnectionError]
    NEURIO_CONNECTION_ERROR_PAIRING_COMMAND: _ClassVar[NeurioConnectionError]
    NEURIO_CONNECTION_ERROR_REBOOT_COMMAND: _ClassVar[NeurioConnectionError]

class NeurioCtType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NEURIO_CT_TYPE_INVALID: _ClassVar[NeurioCtType]
    NEURIO_CT_TYPE_MISSING: _ClassVar[NeurioCtType]
    NEURIO_CT_TYPE_200A: _ClassVar[NeurioCtType]
    NEURIO_CT_TYPE_800A: _ClassVar[NeurioCtType]
    NEURIO_CT_TYPE_UNIVERSAL: _ClassVar[NeurioCtType]

class NeurioCtConfigRequestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NEURIO_CT_CONFIG_REQUEST_STATUS_INVALID: _ClassVar[NeurioCtConfigRequestStatus]
    NEURIO_CT_CONFIG_REQUEST_STATUS_SUCCESS: _ClassVar[NeurioCtConfigRequestStatus]
    NEURIO_CT_CONFIG_REQUEST_STATUS_FAILED_NETWORK: _ClassVar[NeurioCtConfigRequestStatus]
    NEURIO_CT_CONFIG_REQUEST_STATUS_FAILED_HTTP: _ClassVar[NeurioCtConfigRequestStatus]

class NeurioCompatibleMeterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NEURIO_COMPATIBLE_METER_TYPE_INVALID: _ClassVar[NeurioCompatibleMeterType]
    NEURIO_COMPATIBLE_METER_TYPE_NEURIO: _ClassVar[NeurioCompatibleMeterType]
    NEURIO_COMPATIBLE_METER_TYPE_TRM: _ClassVar[NeurioCompatibleMeterType]
POWER_TYPE_INVALID: PowerType
POWER_TYPE_AC_1_PHASE: PowerType
POWER_TYPE_AC_3_PHASE: PowerType
POWER_TYPE_DC: PowerType
CONNECTOR_TYPE_INVALID: ConnectorType
CONNECTOR_TYPE_CCS1: ConnectorType
CONNECTOR_TYPE_CCS2: ConnectorType
CONNECTOR_TYPE_GB: ConnectorType
CONNECTOR_TYPE_NA: ConnectorType
CONNECTOR_TYPE_TYPE_2: ConnectorType
CONNECTOR_TYPE_J1772: ConnectorType
CONNECTOR_TYPE_INDISTINGUISHABLE_DUAL_HANDLE: ConnectorType
CONNECTOR_TYPE_UNKNOWN: ConnectorType
CONNECTOR_TYPE_MCS: ConnectorType
NEURIO_CONNECTION_STATUS_INVALID: NeurioConnectionStatus
NEURIO_CONNECTION_STATUS_NO_COMMS: NeurioConnectionStatus
NEURIO_CONNECTION_STATUS_PAIRING: NeurioConnectionStatus
NEURIO_CONNECTION_STATUS_CONNECTED: NeurioConnectionStatus
NEURIO_CONNECTION_STATUS_CONFIG_CHANGE_UNDERWAY: NeurioConnectionStatus
NEURIO_CONNECTION_ERROR_INVALID: NeurioConnectionError
NEURIO_CONNECTION_ERROR_NONE: NeurioConnectionError
NEURIO_CONNECTION_ERROR_UNKNOWN: NeurioConnectionError
NEURIO_CONNECTION_ERROR_WIFI_AP: NeurioConnectionError
NEURIO_CONNECTION_ERROR_PAIRING_COMMAND: NeurioConnectionError
NEURIO_CONNECTION_ERROR_REBOOT_COMMAND: NeurioConnectionError
NEURIO_CT_TYPE_INVALID: NeurioCtType
NEURIO_CT_TYPE_MISSING: NeurioCtType
NEURIO_CT_TYPE_200A: NeurioCtType
NEURIO_CT_TYPE_800A: NeurioCtType
NEURIO_CT_TYPE_UNIVERSAL: NeurioCtType
NEURIO_CT_CONFIG_REQUEST_STATUS_INVALID: NeurioCtConfigRequestStatus
NEURIO_CT_CONFIG_REQUEST_STATUS_SUCCESS: NeurioCtConfigRequestStatus
NEURIO_CT_CONFIG_REQUEST_STATUS_FAILED_NETWORK: NeurioCtConfigRequestStatus
NEURIO_CT_CONFIG_REQUEST_STATUS_FAILED_HTTP: NeurioCtConfigRequestStatus
NEURIO_COMPATIBLE_METER_TYPE_INVALID: NeurioCompatibleMeterType
NEURIO_COMPATIBLE_METER_TYPE_NEURIO: NeurioCompatibleMeterType
NEURIO_COMPATIBLE_METER_TYPE_TRM: NeurioCompatibleMeterType

class NeurioCTConfig(_message.Message):
    __slots__ = ('location', 'real_power_scale_factor')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    REAL_POWER_SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    location: int
    real_power_scale_factor: float

    def __init__(self, location: _Optional[int]=..., real_power_scale_factor: _Optional[float]=...) -> None:
        ...

class NeurioCTReading(_message.Message):
    __slots__ = ('real_power_w', 'scaled_real_power_w', 'current_amps')
    REAL_POWER_W_FIELD_NUMBER: _ClassVar[int]
    SCALED_REAL_POWER_W_FIELD_NUMBER: _ClassVar[int]
    CURRENT_AMPS_FIELD_NUMBER: _ClassVar[int]
    real_power_w: float
    scaled_real_power_w: float
    current_amps: float

    def __init__(self, real_power_w: _Optional[float]=..., scaled_real_power_w: _Optional[float]=..., current_amps: _Optional[float]=...) -> None:
        ...

class NeurioMeterReadings(_message.Message):
    __slots__ = ('ct_readings',)
    CT_READINGS_FIELD_NUMBER: _ClassVar[int]
    ct_readings: _containers.RepeatedCompositeFieldContainer[NeurioCTReading]

    def __init__(self, ct_readings: _Optional[_Iterable[_Union[NeurioCTReading, _Mapping]]]=...) -> None:
        ...

class NeurioMeterConnection(_message.Message):
    __slots__ = ('connection_status', 'connection_error', 'rssi', 'firmware_version', 'meter_readings')
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ERROR_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    METER_READINGS_FIELD_NUMBER: _ClassVar[int]
    connection_status: NeurioConnectionStatus
    connection_error: NeurioConnectionError
    rssi: _networking_pb2.Rssi
    firmware_version: str
    meter_readings: NeurioMeterReadings

    def __init__(self, connection_status: _Optional[_Union[NeurioConnectionStatus, str]]=..., connection_error: _Optional[_Union[NeurioConnectionError, str]]=..., rssi: _Optional[_Union[_networking_pb2.Rssi, _Mapping]]=..., firmware_version: _Optional[str]=..., meter_readings: _Optional[_Union[NeurioMeterReadings, _Mapping]]=...) -> None:
        ...

class NeurioMeterConfig(_message.Message):
    __slots__ = ('short_id', 'serial', 'ct_config', 'meter_type')
    SHORT_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    CT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    METER_TYPE_FIELD_NUMBER: _ClassVar[int]
    short_id: str
    serial: str
    ct_config: _containers.RepeatedCompositeFieldContainer[NeurioCTConfig]
    meter_type: NeurioCompatibleMeterType

    def __init__(self, short_id: _Optional[str]=..., serial: _Optional[str]=..., ct_config: _Optional[_Iterable[_Union[NeurioCTConfig, _Mapping]]]=..., meter_type: _Optional[_Union[NeurioCompatibleMeterType, str]]=...) -> None:
        ...

class NeurioMeterInterface(_message.Message):
    __slots__ = ('config', 'connection')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    config: NeurioMeterConfig
    connection: NeurioMeterConnection

    def __init__(self, config: _Optional[_Union[NeurioMeterConfig, _Mapping]]=..., connection: _Optional[_Union[NeurioMeterConnection, _Mapping]]=...) -> None:
        ...

class NeurioMeterAPIAddMeterRequest(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: NeurioMeterConfig

    def __init__(self, config: _Optional[_Union[NeurioMeterConfig, _Mapping]]=...) -> None:
        ...

class NeurioMeterAPIAddMeterResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: NeurioMeterConfig

    def __init__(self, config: _Optional[_Union[NeurioMeterConfig, _Mapping]]=...) -> None:
        ...

class NeurioMeterAPIRemoveMeterRequest(_message.Message):
    __slots__ = ('serial',)
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    serial: str

    def __init__(self, serial: _Optional[str]=...) -> None:
        ...

class NeurioMeterAPIRemoveMeterResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class NeurioMeterAPIConfigureCtsRequest(_message.Message):
    __slots__ = ('serial', 'ct_config')
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    CT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    serial: str
    ct_config: _containers.RepeatedCompositeFieldContainer[NeurioCTConfig]

    def __init__(self, serial: _Optional[str]=..., ct_config: _Optional[_Iterable[_Union[NeurioCTConfig, _Mapping]]]=...) -> None:
        ...

class NeurioMeterAPIConfigureCtsResponse(_message.Message):
    __slots__ = ('ct_config',)
    CT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ct_config: _containers.RepeatedCompositeFieldContainer[NeurioCTConfig]

    def __init__(self, ct_config: _Optional[_Iterable[_Union[NeurioCTConfig, _Mapping]]]=...) -> None:
        ...

class NeurioMeterAPIDetectWiredRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class NeurioMeterAPIDetectWiredResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class NeurioMeterAPIGetNeurioCtTypeRequest(_message.Message):
    __slots__ = ('serial',)
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    serial: str

    def __init__(self, serial: _Optional[str]=...) -> None:
        ...

class NeurioMeterAPIGetNeurioCtTypeResponse(_message.Message):
    __slots__ = ('serial', 'status', 'ct1_type', 'ct2_type', 'ct3_type', 'ct4_type')
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CT1_TYPE_FIELD_NUMBER: _ClassVar[int]
    CT2_TYPE_FIELD_NUMBER: _ClassVar[int]
    CT3_TYPE_FIELD_NUMBER: _ClassVar[int]
    CT4_TYPE_FIELD_NUMBER: _ClassVar[int]
    serial: str
    status: NeurioCtConfigRequestStatus
    ct1_type: NeurioCtType
    ct2_type: NeurioCtType
    ct3_type: NeurioCtType
    ct4_type: NeurioCtType

    def __init__(self, serial: _Optional[str]=..., status: _Optional[_Union[NeurioCtConfigRequestStatus, str]]=..., ct1_type: _Optional[_Union[NeurioCtType, str]]=..., ct2_type: _Optional[_Union[NeurioCtType, str]]=..., ct3_type: _Optional[_Union[NeurioCtType, str]]=..., ct4_type: _Optional[_Union[NeurioCtType, str]]=...) -> None:
        ...

class NeurioMeterAPISetNeurioCtTypeRequest(_message.Message):
    __slots__ = ('serial', 'ct1_type', 'ct2_type', 'ct3_type', 'ct4_type')
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    CT1_TYPE_FIELD_NUMBER: _ClassVar[int]
    CT2_TYPE_FIELD_NUMBER: _ClassVar[int]
    CT3_TYPE_FIELD_NUMBER: _ClassVar[int]
    CT4_TYPE_FIELD_NUMBER: _ClassVar[int]
    serial: str
    ct1_type: NeurioCtType
    ct2_type: NeurioCtType
    ct3_type: NeurioCtType
    ct4_type: NeurioCtType

    def __init__(self, serial: _Optional[str]=..., ct1_type: _Optional[_Union[NeurioCtType, str]]=..., ct2_type: _Optional[_Union[NeurioCtType, str]]=..., ct3_type: _Optional[_Union[NeurioCtType, str]]=..., ct4_type: _Optional[_Union[NeurioCtType, str]]=...) -> None:
        ...

class NeurioMeterAPISetNeurioCtTypeResponse(_message.Message):
    __slots__ = ('serial', 'status', 'ct1_type', 'ct2_type', 'ct3_type', 'ct4_type')
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CT1_TYPE_FIELD_NUMBER: _ClassVar[int]
    CT2_TYPE_FIELD_NUMBER: _ClassVar[int]
    CT3_TYPE_FIELD_NUMBER: _ClassVar[int]
    CT4_TYPE_FIELD_NUMBER: _ClassVar[int]
    serial: str
    status: NeurioCtConfigRequestStatus
    ct1_type: NeurioCtType
    ct2_type: NeurioCtType
    ct3_type: NeurioCtType
    ct4_type: NeurioCtType

    def __init__(self, serial: _Optional[str]=..., status: _Optional[_Union[NeurioCtConfigRequestStatus, str]]=..., ct1_type: _Optional[_Union[NeurioCtType, str]]=..., ct2_type: _Optional[_Union[NeurioCtType, str]]=..., ct3_type: _Optional[_Union[NeurioCtType, str]]=..., ct4_type: _Optional[_Union[NeurioCtType, str]]=...) -> None:
        ...

class NeurioMeterMessages(_message.Message):
    __slots__ = ('add_meter_request', 'add_meter_response', 'remove_meter_request', 'remove_meter_response', 'configure_cts_request', 'configure_cts_response', 'detect_wired_request', 'detect_wired_response', 'get_neurio_ct_type_request', 'get_neurio_ct_type_response', 'set_neurio_ct_type_request', 'set_neurio_ct_type_response')
    ADD_METER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ADD_METER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_METER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REMOVE_METER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_CTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_CTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DETECT_WIRED_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DETECT_WIRED_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_NEURIO_CT_TYPE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_NEURIO_CT_TYPE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SET_NEURIO_CT_TYPE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_NEURIO_CT_TYPE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    add_meter_request: NeurioMeterAPIAddMeterRequest
    add_meter_response: NeurioMeterAPIAddMeterResponse
    remove_meter_request: NeurioMeterAPIRemoveMeterRequest
    remove_meter_response: NeurioMeterAPIRemoveMeterResponse
    configure_cts_request: NeurioMeterAPIConfigureCtsRequest
    configure_cts_response: NeurioMeterAPIConfigureCtsResponse
    detect_wired_request: NeurioMeterAPIDetectWiredRequest
    detect_wired_response: NeurioMeterAPIDetectWiredResponse
    get_neurio_ct_type_request: NeurioMeterAPIGetNeurioCtTypeRequest
    get_neurio_ct_type_response: NeurioMeterAPIGetNeurioCtTypeResponse
    set_neurio_ct_type_request: NeurioMeterAPISetNeurioCtTypeRequest
    set_neurio_ct_type_response: NeurioMeterAPISetNeurioCtTypeResponse

    def __init__(self, add_meter_request: _Optional[_Union[NeurioMeterAPIAddMeterRequest, _Mapping]]=..., add_meter_response: _Optional[_Union[NeurioMeterAPIAddMeterResponse, _Mapping]]=..., remove_meter_request: _Optional[_Union[NeurioMeterAPIRemoveMeterRequest, _Mapping]]=..., remove_meter_response: _Optional[_Union[NeurioMeterAPIRemoveMeterResponse, _Mapping]]=..., configure_cts_request: _Optional[_Union[NeurioMeterAPIConfigureCtsRequest, _Mapping]]=..., configure_cts_response: _Optional[_Union[NeurioMeterAPIConfigureCtsResponse, _Mapping]]=..., detect_wired_request: _Optional[_Union[NeurioMeterAPIDetectWiredRequest, _Mapping]]=..., detect_wired_response: _Optional[_Union[NeurioMeterAPIDetectWiredResponse, _Mapping]]=..., get_neurio_ct_type_request: _Optional[_Union[NeurioMeterAPIGetNeurioCtTypeRequest, _Mapping]]=..., get_neurio_ct_type_response: _Optional[_Union[NeurioMeterAPIGetNeurioCtTypeResponse, _Mapping]]=..., set_neurio_ct_type_request: _Optional[_Union[NeurioMeterAPISetNeurioCtTypeRequest, _Mapping]]=..., set_neurio_ct_type_response: _Optional[_Union[NeurioMeterAPISetNeurioCtTypeResponse, _Mapping]]=...) -> None:
        ...