from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EnergyAccumulationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENERGY_ACCUMULATION_TYPE_INVALID: _ClassVar[EnergyAccumulationType]
    ENERGY_ACCUMULATION_TYPE_LIFETIME: _ClassVar[EnergyAccumulationType]
    ENERGY_ACCUMULATION_TYPE_TODAY: _ClassVar[EnergyAccumulationType]
    ENERGY_ACCUMULATION_TYPE_SESSION: _ClassVar[EnergyAccumulationType]

class GridState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRID_STATE_INVALID: _ClassVar[GridState]
    GRID_STATE_UNCOMPLIANT: _ClassVar[GridState]
    GRID_STATE_QUALIFYING: _ClassVar[GridState]
    GRID_STATE_COMPLIANT: _ClassVar[GridState]
ENERGY_ACCUMULATION_TYPE_INVALID: EnergyAccumulationType
ENERGY_ACCUMULATION_TYPE_LIFETIME: EnergyAccumulationType
ENERGY_ACCUMULATION_TYPE_TODAY: EnergyAccumulationType
ENERGY_ACCUMULATION_TYPE_SESSION: EnergyAccumulationType
GRID_STATE_INVALID: GridState
GRID_STATE_UNCOMPLIANT: GridState
GRID_STATE_QUALIFYING: GridState
GRID_STATE_COMPLIANT: GridState

class AccumulatedEnergy(_message.Message):
    __slots__ = ('energy_wh', 'accumulation_type', 'period_s')
    ENERGY_WH_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERIOD_S_FIELD_NUMBER: _ClassVar[int]
    energy_wh: float
    accumulation_type: EnergyAccumulationType
    period_s: _wrappers_pb2.UInt64Value

    def __init__(self, energy_wh: _Optional[float]=..., accumulation_type: _Optional[_Union[EnergyAccumulationType, str]]=..., period_s: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]]=...) -> None:
        ...

class GridComplianceStatus(_message.Message):
    __slots__ = ('grid_state', 'qualifiying_time_remaining_s')
    GRID_STATE_FIELD_NUMBER: _ClassVar[int]
    QUALIFIYING_TIME_REMAINING_S_FIELD_NUMBER: _ClassVar[int]
    grid_state: GridState
    qualifiying_time_remaining_s: _wrappers_pb2.FloatValue

    def __init__(self, grid_state: _Optional[_Union[GridState, str]]=..., qualifiying_time_remaining_s: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=...) -> None:
        ...

class InstACMeasurement(_message.Message):
    __slots__ = ('voltage_vrms', 'frequency_hz', 'current_arms', 'real_power_w', 'reactive_power_var', 'apparent_power_va')
    VOLTAGE_VRMS_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_HZ_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ARMS_FIELD_NUMBER: _ClassVar[int]
    REAL_POWER_W_FIELD_NUMBER: _ClassVar[int]
    REACTIVE_POWER_VAR_FIELD_NUMBER: _ClassVar[int]
    APPARENT_POWER_VA_FIELD_NUMBER: _ClassVar[int]
    voltage_vrms: float
    frequency_hz: float
    current_arms: _wrappers_pb2.FloatValue
    real_power_w: _wrappers_pb2.FloatValue
    reactive_power_var: _wrappers_pb2.FloatValue
    apparent_power_va: _wrappers_pb2.FloatValue

    def __init__(self, voltage_vrms: _Optional[float]=..., frequency_hz: _Optional[float]=..., current_arms: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., real_power_w: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., reactive_power_var: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., apparent_power_va: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=...) -> None:
        ...

class InstDCMeasurement(_message.Message):
    __slots__ = ('voltage_v', 'current_a')
    VOLTAGE_V_FIELD_NUMBER: _ClassVar[int]
    CURRENT_A_FIELD_NUMBER: _ClassVar[int]
    voltage_v: float
    current_a: _wrappers_pb2.FloatValue

    def __init__(self, voltage_v: _Optional[float]=..., current_a: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=...) -> None:
        ...

class AlertLog(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int

    def __init__(self, data: _Optional[int]=...) -> None:
        ...

class AlertMatrix(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int

    def __init__(self, data: _Optional[int]=...) -> None:
        ...