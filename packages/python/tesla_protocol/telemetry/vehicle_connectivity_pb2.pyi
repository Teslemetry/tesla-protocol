import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectivityEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[ConnectivityEvent]
    CONNECTED: _ClassVar[ConnectivityEvent]
    DISCONNECTED: _ClassVar[ConnectivityEvent]
UNKNOWN: ConnectivityEvent
CONNECTED: ConnectivityEvent
DISCONNECTED: ConnectivityEvent

class VehicleConnectivity(_message.Message):
    __slots__ = ("vin", "connection_id", "status", "created_at", "network_interface")
    VIN_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    vin: str
    connection_id: str
    status: ConnectivityEvent
    created_at: _timestamp_pb2.Timestamp
    network_interface: str
    def __init__(self, vin: _Optional[str] = ..., connection_id: _Optional[str] = ..., status: _Optional[_Union[ConnectivityEvent, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., network_interface: _Optional[str] = ...) -> None: ...
