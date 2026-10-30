from tesla_protocol.energy_device import energy_pb2 as _energy_pb2
from tesla_protocol.energy_device import update_pb2 as _update_pb2
from tesla_protocol.energy_device import device_pb2 as _device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IslandGridConnected(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISLAND_GRID_CONNECTED_INVALID: _ClassVar[IslandGridConnected]
    ISLAND_GRID_CONNECTED_ISLANDED: _ClassVar[IslandGridConnected]
    ISLAND_GRID_CONNECTED_CONNECTED: _ClassVar[IslandGridConnected]

class IslandRxEnableAdjustableFreqCheck(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_INVALID: _ClassVar[IslandRxEnableAdjustableFreqCheck]
    ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_NORMAL: _ClassVar[IslandRxEnableAdjustableFreqCheck]
    ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_PERMISSIVE: _ClassVar[IslandRxEnableAdjustableFreqCheck]
    ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_RESTRICTIVE: _ClassVar[IslandRxEnableAdjustableFreqCheck]
    ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_SNA: _ClassVar[IslandRxEnableAdjustableFreqCheck]

class IslandRxRelayCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISLAND_RX_RELAY_COMMAND_INVALID: _ClassVar[IslandRxRelayCommand]
    ISLAND_RX_RELAY_COMMAND_NO_CHANGE: _ClassVar[IslandRxRelayCommand]
    ISLAND_RX_RELAY_COMMAND_OPEN: _ClassVar[IslandRxRelayCommand]
    ISLAND_RX_RELAY_COMMAND_CLOSE: _ClassVar[IslandRxRelayCommand]
ISLAND_GRID_CONNECTED_INVALID: IslandGridConnected
ISLAND_GRID_CONNECTED_ISLANDED: IslandGridConnected
ISLAND_GRID_CONNECTED_CONNECTED: IslandGridConnected
ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_INVALID: IslandRxEnableAdjustableFreqCheck
ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_NORMAL: IslandRxEnableAdjustableFreqCheck
ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_PERMISSIVE: IslandRxEnableAdjustableFreqCheck
ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_RESTRICTIVE: IslandRxEnableAdjustableFreqCheck
ISLAND_RX_ENABLE_ADJUSTABLE_FREQ_CHECK_SNA: IslandRxEnableAdjustableFreqCheck
ISLAND_RX_RELAY_COMMAND_INVALID: IslandRxRelayCommand
ISLAND_RX_RELAY_COMMAND_NO_CHANGE: IslandRxRelayCommand
ISLAND_RX_RELAY_COMMAND_OPEN: IslandRxRelayCommand
ISLAND_RX_RELAY_COMMAND_CLOSE: IslandRxRelayCommand

class IslandACMeasurements(_message.Message):
    __slots__ = ("phase", "grid_state", "ready_for_synchronization", "l1l2_phase_delta_deg", "l1l3_phase_delta_deg", "l2l3_phase_delta_deg", "grid_connected", "delay_open", "learned_nominal_voltage_pu")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    GRID_STATE_FIELD_NUMBER: _ClassVar[int]
    READY_FOR_SYNCHRONIZATION_FIELD_NUMBER: _ClassVar[int]
    L1L2_PHASE_DELTA_DEG_FIELD_NUMBER: _ClassVar[int]
    L1L3_PHASE_DELTA_DEG_FIELD_NUMBER: _ClassVar[int]
    L2L3_PHASE_DELTA_DEG_FIELD_NUMBER: _ClassVar[int]
    GRID_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    DELAY_OPEN_FIELD_NUMBER: _ClassVar[int]
    LEARNED_NOMINAL_VOLTAGE_PU_FIELD_NUMBER: _ClassVar[int]
    phase: _containers.RepeatedCompositeFieldContainer[IslandACPhaseMeasuremets]
    grid_state: int
    ready_for_synchronization: bool
    l1l2_phase_delta_deg: float
    l1l3_phase_delta_deg: float
    l2l3_phase_delta_deg: float
    grid_connected: int
    delay_open: bool
    learned_nominal_voltage_pu: float
    def __init__(self, phase: _Optional[_Iterable[_Union[IslandACPhaseMeasuremets, _Mapping]]] = ..., grid_state: _Optional[int] = ..., ready_for_synchronization: _Optional[bool] = ..., l1l2_phase_delta_deg: _Optional[float] = ..., l1l3_phase_delta_deg: _Optional[float] = ..., l2l3_phase_delta_deg: _Optional[float] = ..., grid_connected: _Optional[int] = ..., delay_open: _Optional[bool] = ..., learned_nominal_voltage_pu: _Optional[float] = ...) -> None: ...

class IslandACPhaseMeasuremets(_message.Message):
    __slots__ = ("vl_to_ref_main_vrms", "freq_main_hz", "vl_to_ref_load_vrms", "freq_load_hz", "phase_main_load_deg", "microgrid_ok", "grid_resistance", "grid_reactance")
    VL_TO_REF_MAIN_VRMS_FIELD_NUMBER: _ClassVar[int]
    FREQ_MAIN_HZ_FIELD_NUMBER: _ClassVar[int]
    VL_TO_REF_LOAD_VRMS_FIELD_NUMBER: _ClassVar[int]
    FREQ_LOAD_HZ_FIELD_NUMBER: _ClassVar[int]
    PHASE_MAIN_LOAD_DEG_FIELD_NUMBER: _ClassVar[int]
    MICROGRID_OK_FIELD_NUMBER: _ClassVar[int]
    GRID_RESISTANCE_FIELD_NUMBER: _ClassVar[int]
    GRID_REACTANCE_FIELD_NUMBER: _ClassVar[int]
    vl_to_ref_main_vrms: float
    freq_main_hz: float
    vl_to_ref_load_vrms: float
    freq_load_hz: float
    phase_main_load_deg: float
    microgrid_ok: bool
    grid_resistance: float
    grid_reactance: float
    def __init__(self, vl_to_ref_main_vrms: _Optional[float] = ..., freq_main_hz: _Optional[float] = ..., vl_to_ref_load_vrms: _Optional[float] = ..., freq_load_hz: _Optional[float] = ..., phase_main_load_deg: _Optional[float] = ..., microgrid_ok: _Optional[bool] = ..., grid_resistance: _Optional[float] = ..., grid_reactance: _Optional[float] = ...) -> None: ...

class IslandRxCommand(_message.Message):
    __slots__ = ("relay_command", "disable_close", "disable_trip", "enable_adjustable_freq_check")
    RELAY_COMMAND_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CLOSE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TRIP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ADJUSTABLE_FREQ_CHECK_FIELD_NUMBER: _ClassVar[int]
    relay_command: int
    disable_close: bool
    disable_trip: bool
    enable_adjustable_freq_check: int
    def __init__(self, relay_command: _Optional[int] = ..., disable_close: _Optional[bool] = ..., disable_trip: _Optional[bool] = ..., enable_adjustable_freq_check: _Optional[int] = ...) -> None: ...

class MeterMeasurements(_message.Message):
    __slots__ = ("phase", "lifetime_total_energy_import_wh", "lifetime_total_energy_export_wh", "grid_voltage_l1l2_vrms")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_TOTAL_ENERGY_IMPORT_WH_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_TOTAL_ENERGY_EXPORT_WH_FIELD_NUMBER: _ClassVar[int]
    GRID_VOLTAGE_L1L2_VRMS_FIELD_NUMBER: _ClassVar[int]
    phase: _containers.RepeatedCompositeFieldContainer[MeterPhaseMeasurements]
    lifetime_total_energy_import_wh: _energy_pb2.AccumulatedEnergy
    lifetime_total_energy_export_wh: _energy_pb2.AccumulatedEnergy
    grid_voltage_l1l2_vrms: float
    def __init__(self, phase: _Optional[_Iterable[_Union[MeterPhaseMeasurements, _Mapping]]] = ..., lifetime_total_energy_import_wh: _Optional[_Union[_energy_pb2.AccumulatedEnergy, _Mapping]] = ..., lifetime_total_energy_export_wh: _Optional[_Union[_energy_pb2.AccumulatedEnergy, _Mapping]] = ..., grid_voltage_l1l2_vrms: _Optional[float] = ...) -> None: ...

class MeterPhaseMeasurements(_message.Message):
    __slots__ = ("phase_measurements", "lifetime_phase_energy_import_wh", "lifetime_phase_energy_export_wh")
    PHASE_MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_PHASE_ENERGY_IMPORT_WH_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_PHASE_ENERGY_EXPORT_WH_FIELD_NUMBER: _ClassVar[int]
    phase_measurements: _energy_pb2.InstACMeasurement
    lifetime_phase_energy_import_wh: _energy_pb2.AccumulatedEnergy
    lifetime_phase_energy_export_wh: _energy_pb2.AccumulatedEnergy
    def __init__(self, phase_measurements: _Optional[_Union[_energy_pb2.InstACMeasurement, _Mapping]] = ..., lifetime_phase_energy_import_wh: _Optional[_Union[_energy_pb2.AccumulatedEnergy, _Mapping]] = ..., lifetime_phase_energy_export_wh: _Optional[_Union[_energy_pb2.AccumulatedEnergy, _Mapping]] = ...) -> None: ...

class WMSAAPIGetInfoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WMSAAPIGetInfoResponse(_message.Message):
    __slots__ = ("wmsa_info",)
    WMSA_INFO_FIELD_NUMBER: _ClassVar[int]
    wmsa_info: WmsaInfoMessage
    def __init__(self, wmsa_info: _Optional[_Union[WmsaInfoMessage, _Mapping]] = ...) -> None: ...

class WMSAAPIPushIslandRxCommandRequest(_message.Message):
    __slots__ = ("island_rx",)
    ISLAND_RX_FIELD_NUMBER: _ClassVar[int]
    island_rx: IslandRxCommand
    def __init__(self, island_rx: _Optional[_Union[IslandRxCommand, _Mapping]] = ...) -> None: ...

class WMSAAPIPushIslandRxCommandResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WMSAMessages(_message.Message):
    __slots__ = ("push_island_rx_command_request", "push_island_rx_command_response", "get_info_request", "get_info_response")
    PUSH_ISLAND_RX_COMMAND_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_ISLAND_RX_COMMAND_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    push_island_rx_command_request: WMSAAPIPushIslandRxCommandRequest
    push_island_rx_command_response: WMSAAPIPushIslandRxCommandResponse
    get_info_request: WMSAAPIGetInfoRequest
    get_info_response: WMSAAPIGetInfoResponse
    def __init__(self, push_island_rx_command_request: _Optional[_Union[WMSAAPIPushIslandRxCommandRequest, _Mapping]] = ..., push_island_rx_command_response: _Optional[_Union[WMSAAPIPushIslandRxCommandResponse, _Mapping]] = ..., get_info_request: _Optional[_Union[WMSAAPIGetInfoRequest, _Mapping]] = ..., get_info_response: _Optional[_Union[WMSAAPIGetInfoResponse, _Mapping]] = ...) -> None: ...

class WmsaInfoMessage(_message.Message):
    __slots__ = ("app_crc", "fw_version", "build_config_id", "component_id", "ecu_id", "pcba_id", "assembly_id", "usage_id", "subusage_id")
    APP_CRC_FIELD_NUMBER: _ClassVar[int]
    FW_VERSION_FIELD_NUMBER: _ClassVar[int]
    BUILD_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    ECU_ID_FIELD_NUMBER: _ClassVar[int]
    PCBA_ID_FIELD_NUMBER: _ClassVar[int]
    ASSEMBLY_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBUSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    app_crc: int
    fw_version: _update_pb2.FirmwareVersion
    build_config_id: int
    component_id: int
    ecu_id: _device_pb2.EcuId
    pcba_id: int
    assembly_id: int
    usage_id: int
    subusage_id: int
    def __init__(self, app_crc: _Optional[int] = ..., fw_version: _Optional[_Union[_update_pb2.FirmwareVersion, _Mapping]] = ..., build_config_id: _Optional[int] = ..., component_id: _Optional[int] = ..., ecu_id: _Optional[_Union[_device_pb2.EcuId, _Mapping]] = ..., pcba_id: _Optional[int] = ..., assembly_id: _Optional[int] = ..., usage_id: _Optional[int] = ..., subusage_id: _Optional[int] = ...) -> None: ...

class WmsaStatus(_message.Message):
    __slots__ = ("meter", "island")
    METER_FIELD_NUMBER: _ClassVar[int]
    ISLAND_FIELD_NUMBER: _ClassVar[int]
    meter: MeterMeasurements
    island: IslandACMeasurements
    def __init__(self, meter: _Optional[_Union[MeterMeasurements, _Mapping]] = ..., island: _Optional[_Union[IslandACMeasurements, _Mapping]] = ...) -> None: ...
