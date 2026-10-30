import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceAlertRecord(_message.Message):
    __slots__ = ("timestamp", "interface_type", "interface_instance", "bus_id", "bc_part_number", "bc_serial_number", "ecu_part_number", "ecu_serial_number", "ecu_type", "git_hash", "alert_name", "decoded_alert", "alert_raw", "alert_is_fault")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    BUS_ID_FIELD_NUMBER: _ClassVar[int]
    BC_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BC_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ECU_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ECU_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ECU_TYPE_FIELD_NUMBER: _ClassVar[int]
    GIT_HASH_FIELD_NUMBER: _ClassVar[int]
    ALERT_NAME_FIELD_NUMBER: _ClassVar[int]
    DECODED_ALERT_FIELD_NUMBER: _ClassVar[int]
    ALERT_RAW_FIELD_NUMBER: _ClassVar[int]
    ALERT_IS_FAULT_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    interface_type: str
    interface_instance: str
    bus_id: str
    bc_part_number: str
    bc_serial_number: str
    ecu_part_number: str
    ecu_serial_number: str
    ecu_type: str
    git_hash: str
    alert_name: str
    decoded_alert: str
    alert_raw: int
    alert_is_fault: bool
    def __init__(self, timestamp: _Optional[int] = ..., interface_type: _Optional[str] = ..., interface_instance: _Optional[str] = ..., bus_id: _Optional[str] = ..., bc_part_number: _Optional[str] = ..., bc_serial_number: _Optional[str] = ..., ecu_part_number: _Optional[str] = ..., ecu_serial_number: _Optional[str] = ..., ecu_type: _Optional[str] = ..., git_hash: _Optional[str] = ..., alert_name: _Optional[str] = ..., decoded_alert: _Optional[str] = ..., alert_raw: _Optional[int] = ..., alert_is_fault: _Optional[bool] = ...) -> None: ...

class DeviceTelemetryRecord(_message.Message):
    __slots__ = ("timestamp", "interface_type", "interface_instance", "bus_id", "bc_part_number", "bc_serial_number", "ecu_part_number", "ecu_serial_number", "ecu_type", "git_hash", "signal_name", "signal_value", "signal_value_text", "signal_unit")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    BUS_ID_FIELD_NUMBER: _ClassVar[int]
    BC_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BC_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ECU_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ECU_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ECU_TYPE_FIELD_NUMBER: _ClassVar[int]
    GIT_HASH_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_VALUE_TEXT_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_UNIT_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    interface_type: str
    interface_instance: str
    bus_id: str
    bc_part_number: str
    bc_serial_number: str
    ecu_part_number: str
    ecu_serial_number: str
    ecu_type: str
    git_hash: str
    signal_name: str
    signal_value: float
    signal_value_text: str
    signal_unit: str
    def __init__(self, timestamp: _Optional[int] = ..., interface_type: _Optional[str] = ..., interface_instance: _Optional[str] = ..., bus_id: _Optional[str] = ..., bc_part_number: _Optional[str] = ..., bc_serial_number: _Optional[str] = ..., ecu_part_number: _Optional[str] = ..., ecu_serial_number: _Optional[str] = ..., ecu_type: _Optional[str] = ..., git_hash: _Optional[str] = ..., signal_name: _Optional[str] = ..., signal_value: _Optional[float] = ..., signal_value_text: _Optional[str] = ..., signal_unit: _Optional[str] = ...) -> None: ...

class LogRecord(_message.Message):
    __slots__ = ("time", "ecu_type", "githash", "signal", "version_major", "version_minor", "version_patch", "version_dev")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ECU_TYPE_FIELD_NUMBER: _ClassVar[int]
    GITHASH_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_MINOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_PATCH_FIELD_NUMBER: _ClassVar[int]
    VERSION_DEV_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    ecu_type: str
    githash: str
    signal: _containers.RepeatedCompositeFieldContainer[Signal]
    version_major: int
    version_minor: int
    version_patch: int
    version_dev: int
    def __init__(self, time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ecu_type: _Optional[str] = ..., githash: _Optional[str] = ..., signal: _Optional[_Iterable[_Union[Signal, _Mapping]]] = ..., version_major: _Optional[int] = ..., version_minor: _Optional[int] = ..., version_patch: _Optional[int] = ..., version_dev: _Optional[int] = ...) -> None: ...

class MP2LogRecord(_message.Message):
    __slots__ = ("time", "interface_type", "interface_instance", "bus_id", "bc_part_number", "bc_serial_number", "ecu_part_number", "ecu_serial_number", "ecu_type", "git_hash", "signal", "version_major", "version_minor", "version_patch", "version_dev")
    TIME_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    BUS_ID_FIELD_NUMBER: _ClassVar[int]
    BC_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BC_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ECU_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ECU_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ECU_TYPE_FIELD_NUMBER: _ClassVar[int]
    GIT_HASH_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_MINOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_PATCH_FIELD_NUMBER: _ClassVar[int]
    VERSION_DEV_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    interface_type: str
    interface_instance: str
    bus_id: str
    bc_part_number: str
    bc_serial_number: str
    ecu_part_number: str
    ecu_serial_number: str
    ecu_type: str
    git_hash: str
    signal: _containers.RepeatedCompositeFieldContainer[Signal]
    version_major: int
    version_minor: int
    version_patch: int
    version_dev: int
    def __init__(self, time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., interface_type: _Optional[str] = ..., interface_instance: _Optional[str] = ..., bus_id: _Optional[str] = ..., bc_part_number: _Optional[str] = ..., bc_serial_number: _Optional[str] = ..., ecu_part_number: _Optional[str] = ..., ecu_serial_number: _Optional[str] = ..., ecu_type: _Optional[str] = ..., git_hash: _Optional[str] = ..., signal: _Optional[_Iterable[_Union[Signal, _Mapping]]] = ..., version_major: _Optional[int] = ..., version_minor: _Optional[int] = ..., version_patch: _Optional[int] = ..., version_dev: _Optional[int] = ...) -> None: ...

class Signal(_message.Message):
    __slots__ = ("signal_name", "signal_unit", "signal_value_integer", "signal_value", "signal_value_text")
    SIGNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_UNIT_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_VALUE_INTEGER_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_VALUE_TEXT_FIELD_NUMBER: _ClassVar[int]
    signal_name: str
    signal_unit: str
    signal_value_integer: int
    signal_value: float
    signal_value_text: str
    def __init__(self, signal_name: _Optional[str] = ..., signal_unit: _Optional[str] = ..., signal_value_integer: _Optional[int] = ..., signal_value: _Optional[float] = ..., signal_value_text: _Optional[str] = ...) -> None: ...
