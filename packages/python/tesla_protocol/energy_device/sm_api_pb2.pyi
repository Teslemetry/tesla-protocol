from tesla_protocol.energy_device import energy_pb2 as _energy_pb2
from tesla_protocol.energy_device import wmsa_api_pb2 as _wmsa_api_pb2
from tesla_protocol.energy_device import energy_telemetry_pb2 as _energy_telemetry_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SMAPILogSignalsRequest(_message.Message):
    __slots__ = ("log_record",)
    LOG_RECORD_FIELD_NUMBER: _ClassVar[int]
    log_record: _energy_telemetry_pb2.LogRecord
    def __init__(self, log_record: _Optional[_Union[_energy_telemetry_pb2.LogRecord, _Mapping]] = ...) -> None: ...

class SMAPILogSignalsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SMAPIPushWmsaAlertLogRequest(_message.Message):
    __slots__ = ("log",)
    LOG_FIELD_NUMBER: _ClassVar[int]
    log: _energy_pb2.AlertLog
    def __init__(self, log: _Optional[_Union[_energy_pb2.AlertLog, _Mapping]] = ...) -> None: ...

class SMAPIPushWmsaAlertLogResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SMAPIPushWmsaAlertMatrixRequest(_message.Message):
    __slots__ = ("matrix",)
    MATRIX_FIELD_NUMBER: _ClassVar[int]
    matrix: _energy_pb2.AlertMatrix
    def __init__(self, matrix: _Optional[_Union[_energy_pb2.AlertMatrix, _Mapping]] = ...) -> None: ...

class SMAPIPushWmsaAlertMatrixResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SMAPIPushWmsaStatusRequest(_message.Message):
    __slots__ = ("wmsa_status",)
    WMSA_STATUS_FIELD_NUMBER: _ClassVar[int]
    wmsa_status: _wmsa_api_pb2.WmsaStatus
    def __init__(self, wmsa_status: _Optional[_Union[_wmsa_api_pb2.WmsaStatus, _Mapping]] = ...) -> None: ...

class SMAPIPushWmsaStatusResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SMMessages(_message.Message):
    __slots__ = ("push_wmsa_status_request", "push_wmsa_status_response", "push_wmsa_alert_log_request", "push_wmsa_alert_log_response", "push_wmsa_alert_matrix_request", "push_wmsa_alert_matrix_response", "log_signals_request", "log_signals_response")
    PUSH_WMSA_STATUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_WMSA_STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_WMSA_ALERT_LOG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_WMSA_ALERT_LOG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_WMSA_ALERT_MATRIX_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_WMSA_ALERT_MATRIX_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    LOG_SIGNALS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LOG_SIGNALS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    push_wmsa_status_request: SMAPIPushWmsaStatusRequest
    push_wmsa_status_response: SMAPIPushWmsaStatusResponse
    push_wmsa_alert_log_request: SMAPIPushWmsaAlertLogRequest
    push_wmsa_alert_log_response: SMAPIPushWmsaAlertLogResponse
    push_wmsa_alert_matrix_request: SMAPIPushWmsaAlertMatrixRequest
    push_wmsa_alert_matrix_response: SMAPIPushWmsaAlertMatrixResponse
    log_signals_request: SMAPILogSignalsRequest
    log_signals_response: SMAPILogSignalsResponse
    def __init__(self, push_wmsa_status_request: _Optional[_Union[SMAPIPushWmsaStatusRequest, _Mapping]] = ..., push_wmsa_status_response: _Optional[_Union[SMAPIPushWmsaStatusResponse, _Mapping]] = ..., push_wmsa_alert_log_request: _Optional[_Union[SMAPIPushWmsaAlertLogRequest, _Mapping]] = ..., push_wmsa_alert_log_response: _Optional[_Union[SMAPIPushWmsaAlertLogResponse, _Mapping]] = ..., push_wmsa_alert_matrix_request: _Optional[_Union[SMAPIPushWmsaAlertMatrixRequest, _Mapping]] = ..., push_wmsa_alert_matrix_response: _Optional[_Union[SMAPIPushWmsaAlertMatrixResponse, _Mapping]] = ..., log_signals_request: _Optional[_Union[SMAPILogSignalsRequest, _Mapping]] = ..., log_signals_response: _Optional[_Union[SMAPILogSignalsResponse, _Mapping]] = ...) -> None: ...
