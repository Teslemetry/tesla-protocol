from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Energy(_message.Message):
    __slots__ = ('watt_hours', 'milli_watt_hours')
    WATT_HOURS_FIELD_NUMBER: _ClassVar[int]
    MILLI_WATT_HOURS_FIELD_NUMBER: _ClassVar[int]
    watt_hours: int
    milli_watt_hours: int

    def __init__(self, watt_hours: _Optional[int]=..., milli_watt_hours: _Optional[int]=...) -> None:
        ...

class StemInfo(_message.Message):
    __slots__ = ('fw_githash', 'serial_number', 'part_number', 'meter_id')
    FW_GITHASH_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    METER_ID_FIELD_NUMBER: _ClassVar[int]
    fw_githash: bytes
    serial_number: str
    part_number: str
    meter_id: str

    def __init__(self, fw_githash: _Optional[bytes]=..., serial_number: _Optional[str]=..., part_number: _Optional[str]=..., meter_id: _Optional[str]=...) -> None:
        ...

class StemEventInfo(_message.Message):
    __slots__ = ('event_occurred', 'invalidated', 'time_synchronized')
    EVENT_OCCURRED_FIELD_NUMBER: _ClassVar[int]
    INVALIDATED_FIELD_NUMBER: _ClassVar[int]
    TIME_SYNCHRONIZED_FIELD_NUMBER: _ClassVar[int]
    event_occurred: bool
    invalidated: bool
    time_synchronized: bool

    def __init__(self, event_occurred: bool=..., invalidated: bool=..., time_synchronized: bool=...) -> None:
        ...

class ChargeSessionTimeSeries(_message.Message):
    __slots__ = ('start_time_epoch_s', 'end_time_epoch_s', 'total_energy_vended_wh', 'bucket_duration_s', 'first_bucket_duration_s', 'bucket_energy_vended_wh', 'total_energy_vended', 'bucket_energy_vended')
    START_TIME_EPOCH_S_FIELD_NUMBER: _ClassVar[int]
    END_TIME_EPOCH_S_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ENERGY_VENDED_WH_FIELD_NUMBER: _ClassVar[int]
    BUCKET_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    FIRST_BUCKET_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ENERGY_VENDED_WH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ENERGY_VENDED_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ENERGY_VENDED_FIELD_NUMBER: _ClassVar[int]
    start_time_epoch_s: int
    end_time_epoch_s: int
    total_energy_vended_wh: int
    bucket_duration_s: int
    first_bucket_duration_s: int
    bucket_energy_vended_wh: _containers.RepeatedScalarFieldContainer[int]
    total_energy_vended: Energy
    bucket_energy_vended: _containers.RepeatedCompositeFieldContainer[Energy]

    def __init__(self, start_time_epoch_s: _Optional[int]=..., end_time_epoch_s: _Optional[int]=..., total_energy_vended_wh: _Optional[int]=..., bucket_duration_s: _Optional[int]=..., first_bucket_duration_s: _Optional[int]=..., bucket_energy_vended_wh: _Optional[_Iterable[int]]=..., total_energy_vended: _Optional[_Union[Energy, _Mapping]]=..., bucket_energy_vended: _Optional[_Iterable[_Union[Energy, _Mapping]]]=...) -> None:
        ...

class StemUi(_message.Message):
    __slots__ = ('stem_info', 'session_id', 'system_time_epoch_s', 'idle_time_s', 'start_time_epoch_s', 'stem_event_info', 'session_energy_kwh')
    STEM_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_TIME_EPOCH_S_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIME_S_FIELD_NUMBER: _ClassVar[int]
    START_TIME_EPOCH_S_FIELD_NUMBER: _ClassVar[int]
    STEM_EVENT_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENERGY_KWH_FIELD_NUMBER: _ClassVar[int]
    stem_info: StemInfo
    session_id: int
    system_time_epoch_s: int
    idle_time_s: int
    start_time_epoch_s: int
    stem_event_info: StemEventInfo
    session_energy_kwh: float

    def __init__(self, stem_info: _Optional[_Union[StemInfo, _Mapping]]=..., session_id: _Optional[int]=..., system_time_epoch_s: _Optional[int]=..., idle_time_s: _Optional[int]=..., start_time_epoch_s: _Optional[int]=..., stem_event_info: _Optional[_Union[StemEventInfo, _Mapping]]=..., session_energy_kwh: _Optional[float]=...) -> None:
        ...

class StemBilling(_message.Message):
    __slots__ = ('stem_info', 'session_id', 'stem_event_info', 'lifetime_energy_start_kwh', 'lifetime_energy_end_kwh', 'idle_time_s', 'charge_session_time_series')
    STEM_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STEM_EVENT_INFO_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_ENERGY_START_KWH_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_ENERGY_END_KWH_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIME_S_FIELD_NUMBER: _ClassVar[int]
    CHARGE_SESSION_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    stem_info: StemInfo
    session_id: int
    stem_event_info: StemEventInfo
    lifetime_energy_start_kwh: float
    lifetime_energy_end_kwh: float
    idle_time_s: int
    charge_session_time_series: ChargeSessionTimeSeries

    def __init__(self, stem_info: _Optional[_Union[StemInfo, _Mapping]]=..., session_id: _Optional[int]=..., stem_event_info: _Optional[_Union[StemEventInfo, _Mapping]]=..., lifetime_energy_start_kwh: _Optional[float]=..., lifetime_energy_end_kwh: _Optional[float]=..., idle_time_s: _Optional[int]=..., charge_session_time_series: _Optional[_Union[ChargeSessionTimeSeries, _Mapping]]=...) -> None:
        ...