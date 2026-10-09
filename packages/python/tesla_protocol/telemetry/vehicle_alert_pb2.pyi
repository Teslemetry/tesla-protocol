import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Audience(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unknown: _ClassVar[Audience]
    Customer: _ClassVar[Audience]
    Service: _ClassVar[Audience]
    ServiceFix: _ClassVar[Audience]
Unknown: Audience
Customer: Audience
Service: Audience
ServiceFix: Audience

class VehicleAlerts(_message.Message):
    __slots__ = ("alerts", "created_at", "vin")
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    alerts: _containers.RepeatedCompositeFieldContainer[VehicleAlert]
    created_at: _timestamp_pb2.Timestamp
    vin: str
    def __init__(self, alerts: _Optional[_Iterable[_Union[VehicleAlert, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., vin: _Optional[str] = ...) -> None: ...

class VehicleAlert(_message.Message):
    __slots__ = ("name", "audiences", "started_at", "ended_at")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUDIENCES_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    audiences: _containers.RepeatedScalarFieldContainer[Audience]
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., audiences: _Optional[_Iterable[_Union[Audience, str]]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
