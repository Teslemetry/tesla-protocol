from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectedKioskError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTED_KIOSK_ERROR_INVALID: _ClassVar[ConnectedKioskError]
    CONNECTED_KIOSK_ERROR_SITEMANAGER_STARTED: _ClassVar[ConnectedKioskError]
    CONNECTED_KIOSK_ERROR_UNEXPECTED_ERROR: _ClassVar[ConnectedKioskError]

class EcuFirmwareUpdateStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ECU_FIRMWARE_UPDATE_STAGE_INVALID: _ClassVar[EcuFirmwareUpdateStage]
    ECU_FIRMWARE_UPDATE_STAGE_WAITING: _ClassVar[EcuFirmwareUpdateStage]
    ECU_FIRMWARE_UPDATE_STAGE_GET_DEVICE_INFO: _ClassVar[EcuFirmwareUpdateStage]
    ECU_FIRMWARE_UPDATE_STAGE_CHECK_BL_UPDATE_REQUIRED: _ClassVar[EcuFirmwareUpdateStage]
    ECU_FIRMWARE_UPDATE_STAGE_UPDATE_BL: _ClassVar[EcuFirmwareUpdateStage]
    ECU_FIRMWARE_UPDATE_STAGE_CHECK_APP_UPDATE_REQUIRED: _ClassVar[EcuFirmwareUpdateStage]
    ECU_FIRMWARE_UPDATE_STAGE_UPDATE_APP: _ClassVar[EcuFirmwareUpdateStage]
    ECU_FIRMWARE_UPDATE_STAGE_UPDATE_SUBCOMPONENTS: _ClassVar[EcuFirmwareUpdateStage]
    ECU_FIRMWARE_UPDATE_STAGE_PASS: _ClassVar[EcuFirmwareUpdateStage]
    ECU_FIRMWARE_UPDATE_STAGE_FAIL: _ClassVar[EcuFirmwareUpdateStage]

class SetDcMeterCommissionedError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SET_DC_METER_COMMISSIONED_ERROR_INVALID: _ClassVar[SetDcMeterCommissionedError]
    SET_DC_METER_COMMISSIONED_ERROR_INVALID_POST_ID: _ClassVar[SetDcMeterCommissionedError]
    SET_DC_METER_COMMISSIONED_ERROR_DC_METER_NOT_INSTALLED: _ClassVar[SetDcMeterCommissionedError]
    SET_DC_METER_COMMISSIONED_ERROR_UNAVAILABLE: _ClassVar[SetDcMeterCommissionedError]
    SET_DC_METER_COMMISSIONED_ERROR_SECURITY_UNLOCK_FAILED: _ClassVar[SetDcMeterCommissionedError]
    SET_DC_METER_COMMISSIONED_ERROR_WRITE_FAILED: _ClassVar[SetDcMeterCommissionedError]
CONNECTED_KIOSK_ERROR_INVALID: ConnectedKioskError
CONNECTED_KIOSK_ERROR_SITEMANAGER_STARTED: ConnectedKioskError
CONNECTED_KIOSK_ERROR_UNEXPECTED_ERROR: ConnectedKioskError
ECU_FIRMWARE_UPDATE_STAGE_INVALID: EcuFirmwareUpdateStage
ECU_FIRMWARE_UPDATE_STAGE_WAITING: EcuFirmwareUpdateStage
ECU_FIRMWARE_UPDATE_STAGE_GET_DEVICE_INFO: EcuFirmwareUpdateStage
ECU_FIRMWARE_UPDATE_STAGE_CHECK_BL_UPDATE_REQUIRED: EcuFirmwareUpdateStage
ECU_FIRMWARE_UPDATE_STAGE_UPDATE_BL: EcuFirmwareUpdateStage
ECU_FIRMWARE_UPDATE_STAGE_CHECK_APP_UPDATE_REQUIRED: EcuFirmwareUpdateStage
ECU_FIRMWARE_UPDATE_STAGE_UPDATE_APP: EcuFirmwareUpdateStage
ECU_FIRMWARE_UPDATE_STAGE_UPDATE_SUBCOMPONENTS: EcuFirmwareUpdateStage
ECU_FIRMWARE_UPDATE_STAGE_PASS: EcuFirmwareUpdateStage
ECU_FIRMWARE_UPDATE_STAGE_FAIL: EcuFirmwareUpdateStage
SET_DC_METER_COMMISSIONED_ERROR_INVALID: SetDcMeterCommissionedError
SET_DC_METER_COMMISSIONED_ERROR_INVALID_POST_ID: SetDcMeterCommissionedError
SET_DC_METER_COMMISSIONED_ERROR_DC_METER_NOT_INSTALLED: SetDcMeterCommissionedError
SET_DC_METER_COMMISSIONED_ERROR_UNAVAILABLE: SetDcMeterCommissionedError
SET_DC_METER_COMMISSIONED_ERROR_SECURITY_UNLOCK_FAILED: SetDcMeterCommissionedError
SET_DC_METER_COMMISSIONED_ERROR_WRITE_FAILED: SetDcMeterCommissionedError

class ConnectedKiosk(_message.Message):
    __slots__ = ("verifone_kiosk",)
    VERIFONE_KIOSK_FIELD_NUMBER: _ClassVar[int]
    verifone_kiosk: VerifoneKiosk
    def __init__(self, verifone_kiosk: _Optional[_Union[VerifoneKiosk, _Mapping]] = ...) -> None: ...

class DcMeterCommissioningStatus(_message.Message):
    __slots__ = ("post_id", "installed", "commissioned")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONED_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    installed: _wrappers_pb2.BoolValue
    commissioned: _wrappers_pb2.BoolValue
    def __init__(self, post_id: _Optional[int] = ..., installed: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., commissioned: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class DeviceIDAndSerialNumber(_message.Message):
    __slots__ = ("serial_number", "device_id")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    device_id: str
    def __init__(self, serial_number: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class EcuFirmwareModuleUpdateResult(_message.Message):
    __slots__ = ("ecu_module", "module_update_status")
    ECU_MODULE_FIELD_NUMBER: _ClassVar[int]
    MODULE_UPDATE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ecu_module: str
    module_update_status: EcuFirmwareModuleUpdateStatus
    def __init__(self, ecu_module: _Optional[str] = ..., module_update_status: _Optional[_Union[EcuFirmwareModuleUpdateStatus, _Mapping]] = ...) -> None: ...

class EcuFirmwareModuleUpdateStatus(_message.Message):
    __slots__ = ("fail", "skipped")
    PASS_FIELD_NUMBER: _ClassVar[int]
    FAIL_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    fail: EcuFirmwareModuleUpdateStatusFail
    skipped: EcuFirmwareModuleUpdateStatusSkipped
    def __init__(self, fail: _Optional[_Union[EcuFirmwareModuleUpdateStatusFail, _Mapping]] = ..., skipped: _Optional[_Union[EcuFirmwareModuleUpdateStatusSkipped, _Mapping]] = ..., **kwargs) -> None: ...

class EcuFirmwareModuleUpdateStatusFail(_message.Message):
    __slots__ = ("reason", "pre_update_version", "post_update_version")
    REASON_FIELD_NUMBER: _ClassVar[int]
    PRE_UPDATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    POST_UPDATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    reason: _wrappers_pb2.StringValue
    pre_update_version: _wrappers_pb2.StringValue
    post_update_version: _wrappers_pb2.StringValue
    def __init__(self, reason: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., pre_update_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., post_update_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class EcuFirmwareModuleUpdateStatusPass(_message.Message):
    __slots__ = ("pre_update_version", "post_update_version")
    PRE_UPDATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    POST_UPDATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    pre_update_version: _wrappers_pb2.StringValue
    post_update_version: _wrappers_pb2.StringValue
    def __init__(self, pre_update_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., post_update_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class EcuFirmwareModuleUpdateStatusSkipped(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: _wrappers_pb2.StringValue
    def __init__(self, reason: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class EcuFirmwareUpdateAttempts(_message.Message):
    __slots__ = ("attempts",)
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    attempts: _containers.RepeatedCompositeFieldContainer[EcuFirmwareUpdateEcuResult]
    def __init__(self, attempts: _Optional[_Iterable[_Union[EcuFirmwareUpdateEcuResult, _Mapping]]] = ...) -> None: ...

class EcuFirmwareUpdateEcuResult(_message.Message):
    __slots__ = ("ecu_name", "module_update_results")
    ECU_NAME_FIELD_NUMBER: _ClassVar[int]
    MODULE_UPDATE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ecu_name: str
    module_update_results: _containers.RepeatedCompositeFieldContainer[EcuFirmwareModuleUpdateResult]
    def __init__(self, ecu_name: _Optional[str] = ..., module_update_results: _Optional[_Iterable[_Union[EcuFirmwareModuleUpdateResult, _Mapping]]] = ...) -> None: ...

class EcuFirmwareUpdateInProgress(_message.Message):
    __slots__ = ("default",)
    class DefaultEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EcuFirmwareUpdateNodeProgress
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EcuFirmwareUpdateNodeProgress, _Mapping]] = ...) -> None: ...
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    default: _containers.MessageMap[str, EcuFirmwareUpdateNodeProgress]
    def __init__(self, default: _Optional[_Mapping[str, EcuFirmwareUpdateNodeProgress]] = ...) -> None: ...

class EcuFirmwareUpdateNodeProgress(_message.Message):
    __slots__ = ("node_path", "stage", "message")
    NODE_PATH_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    node_path: str
    stage: EcuFirmwareUpdateStage
    message: str
    def __init__(self, node_path: _Optional[str] = ..., stage: _Optional[_Union[EcuFirmwareUpdateStage, str]] = ..., message: _Optional[str] = ...) -> None: ...

class EcuFirmwareUpdateResult(_message.Message):
    __slots__ = ("system_update_status", "default")
    class DefaultEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EcuFirmwareUpdateAttempts
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EcuFirmwareUpdateAttempts, _Mapping]] = ...) -> None: ...
    SYSTEM_UPDATE_STATUS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    system_update_status: EcuFirmwareUpdateStatus
    default: _containers.MessageMap[str, EcuFirmwareUpdateAttempts]
    def __init__(self, system_update_status: _Optional[_Union[EcuFirmwareUpdateStatus, _Mapping]] = ..., default: _Optional[_Mapping[str, EcuFirmwareUpdateAttempts]] = ...) -> None: ...

class EcuFirmwareUpdateStatus(_message.Message):
    __slots__ = ("fail",)
    PASS_FIELD_NUMBER: _ClassVar[int]
    FAIL_FIELD_NUMBER: _ClassVar[int]
    fail: EcuFirmwareUpdateStatusFail
    def __init__(self, fail: _Optional[_Union[EcuFirmwareUpdateStatusFail, _Mapping]] = ..., **kwargs) -> None: ...

class EcuFirmwareUpdateStatusFail(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class EcuFirmwareUpdateStatusPass(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PayterPostStatus(_message.Message):
    __slots__ = ("post_index", "serial_number", "activated")
    POST_INDEX_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    post_index: int
    serial_number: str
    activated: bool
    def __init__(self, post_index: _Optional[int] = ..., serial_number: _Optional[str] = ..., activated: _Optional[bool] = ...) -> None: ...

class SuperchargerAPIGetConnectedKiosksRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuperchargerAPIGetConnectedKiosksResponse(_message.Message):
    __slots__ = ("error", "connected_kiosks")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_KIOSKS_FIELD_NUMBER: _ClassVar[int]
    error: ConnectedKioskError
    connected_kiosks: _containers.RepeatedCompositeFieldContainer[ConnectedKiosk]
    def __init__(self, error: _Optional[_Union[ConnectedKioskError, str]] = ..., connected_kiosks: _Optional[_Iterable[_Union[ConnectedKiosk, _Mapping]]] = ...) -> None: ...

class SuperchargerAPIGetDcMetersCommissioningRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuperchargerAPIGetDcMetersCommissioningResponse(_message.Message):
    __slots__ = ("dc_meters", "error")
    DC_METERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    dc_meters: _containers.RepeatedCompositeFieldContainer[DcMeterCommissioningStatus]
    error: int
    def __init__(self, dc_meters: _Optional[_Iterable[_Union[DcMeterCommissioningStatus, _Mapping]]] = ..., error: _Optional[int] = ...) -> None: ...

class SuperchargerAPIGetEcuFirmwareUpdateProgressRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuperchargerAPIGetEcuFirmwareUpdateProgressResponse(_message.Message):
    __slots__ = ("finished", "in_progress")
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    finished: EcuFirmwareUpdateResult
    in_progress: EcuFirmwareUpdateInProgress
    def __init__(self, finished: _Optional[_Union[EcuFirmwareUpdateResult, _Mapping]] = ..., in_progress: _Optional[_Union[EcuFirmwareUpdateInProgress, _Mapping]] = ...) -> None: ...

class SuperchargerAPIGetPayterPostStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuperchargerAPIGetPayterPostStatusResponse(_message.Message):
    __slots__ = ("payter_devices",)
    PAYTER_DEVICES_FIELD_NUMBER: _ClassVar[int]
    payter_devices: _containers.RepeatedCompositeFieldContainer[PayterPostStatus]
    def __init__(self, payter_devices: _Optional[_Iterable[_Union[PayterPostStatus, _Mapping]]] = ...) -> None: ...

class SuperchargerAPIGetVerifoneKioskDeviceIdsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuperchargerAPIGetVerifoneKioskDeviceIdsResponse(_message.Message):
    __slots__ = ("device_ids",)
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    device_ids: _containers.RepeatedCompositeFieldContainer[DeviceIDAndSerialNumber]
    def __init__(self, device_ids: _Optional[_Iterable[_Union[DeviceIDAndSerialNumber, _Mapping]]] = ...) -> None: ...

class SuperchargerAPIOdinCommandRequest(_message.Message):
    __slots__ = ("command", "args")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    command: str
    args: bytes
    def __init__(self, command: _Optional[str] = ..., args: _Optional[bytes] = ...) -> None: ...

class SuperchargerAPIOdinCommandResponse(_message.Message):
    __slots__ = ("response", "error")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    response: bytes
    error: str
    def __init__(self, response: _Optional[bytes] = ..., error: _Optional[str] = ...) -> None: ...

class SuperchargerAPISetDcMeterCommissionedRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...

class SuperchargerAPISetDcMeterCommissionedResponse(_message.Message):
    __slots__ = ("success", "error", "error_message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: SetDcMeterCommissionedError
    error_message: str
    def __init__(self, success: _Optional[bool] = ..., error: _Optional[_Union[SetDcMeterCommissionedError, str]] = ..., error_message: _Optional[str] = ...) -> None: ...

class SuperchargerAPIUnlockMagicDockRequest(_message.Message):
    __slots__ = ("cabinet_id", "post_id")
    CABINET_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    cabinet_id: str
    post_id: int
    def __init__(self, cabinet_id: _Optional[str] = ..., post_id: _Optional[int] = ...) -> None: ...

class SuperchargerAPIUnlockMagicDockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuperchargerAPIUpdateFollowersRequest(_message.Message):
    __slots__ = ("dins",)
    DINS_FIELD_NUMBER: _ClassVar[int]
    dins: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dins: _Optional[_Iterable[str]] = ...) -> None: ...

class SuperchargerAPIUpdateFollowersResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuperchargerMessages(_message.Message):
    __slots__ = ("unlock_magic_dock_request", "unlock_magic_dock_response", "get_connected_kiosks_request", "get_connected_kiosks_response", "get_verifone_kiosk_device_ids_request", "get_verifone_kiosk_device_ids_response", "update_followers_request", "update_followers_response", "get_dc_meters_commissioning_request", "get_dc_meters_commissioning_response", "set_dc_meter_commissioned_request", "set_dc_meter_commissioned_response", "odin_command_request", "odin_command_response", "get_payter_post_status_request", "get_payter_post_status_response", "get_ecu_firmware_update_progress_request", "get_ecu_firmware_update_progress_response")
    UNLOCK_MAGIC_DOCK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_MAGIC_DOCK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_CONNECTED_KIOSKS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_CONNECTED_KIOSKS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_VERIFONE_KIOSK_DEVICE_IDS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_VERIFONE_KIOSK_DEVICE_IDS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FOLLOWERS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FOLLOWERS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_DC_METERS_COMMISSIONING_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_DC_METERS_COMMISSIONING_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SET_DC_METER_COMMISSIONED_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_DC_METER_COMMISSIONED_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ODIN_COMMAND_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ODIN_COMMAND_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_PAYTER_POST_STATUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_PAYTER_POST_STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_ECU_FIRMWARE_UPDATE_PROGRESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_ECU_FIRMWARE_UPDATE_PROGRESS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    unlock_magic_dock_request: SuperchargerAPIUnlockMagicDockRequest
    unlock_magic_dock_response: SuperchargerAPIUnlockMagicDockResponse
    get_connected_kiosks_request: SuperchargerAPIGetConnectedKiosksRequest
    get_connected_kiosks_response: SuperchargerAPIGetConnectedKiosksResponse
    get_verifone_kiosk_device_ids_request: SuperchargerAPIGetVerifoneKioskDeviceIdsRequest
    get_verifone_kiosk_device_ids_response: SuperchargerAPIGetVerifoneKioskDeviceIdsResponse
    update_followers_request: SuperchargerAPIUpdateFollowersRequest
    update_followers_response: SuperchargerAPIUpdateFollowersResponse
    get_dc_meters_commissioning_request: SuperchargerAPIGetDcMetersCommissioningRequest
    get_dc_meters_commissioning_response: SuperchargerAPIGetDcMetersCommissioningResponse
    set_dc_meter_commissioned_request: SuperchargerAPISetDcMeterCommissionedRequest
    set_dc_meter_commissioned_response: SuperchargerAPISetDcMeterCommissionedResponse
    odin_command_request: SuperchargerAPIOdinCommandRequest
    odin_command_response: SuperchargerAPIOdinCommandResponse
    get_payter_post_status_request: SuperchargerAPIGetPayterPostStatusRequest
    get_payter_post_status_response: SuperchargerAPIGetPayterPostStatusResponse
    get_ecu_firmware_update_progress_request: SuperchargerAPIGetEcuFirmwareUpdateProgressRequest
    get_ecu_firmware_update_progress_response: SuperchargerAPIGetEcuFirmwareUpdateProgressResponse
    def __init__(self, unlock_magic_dock_request: _Optional[_Union[SuperchargerAPIUnlockMagicDockRequest, _Mapping]] = ..., unlock_magic_dock_response: _Optional[_Union[SuperchargerAPIUnlockMagicDockResponse, _Mapping]] = ..., get_connected_kiosks_request: _Optional[_Union[SuperchargerAPIGetConnectedKiosksRequest, _Mapping]] = ..., get_connected_kiosks_response: _Optional[_Union[SuperchargerAPIGetConnectedKiosksResponse, _Mapping]] = ..., get_verifone_kiosk_device_ids_request: _Optional[_Union[SuperchargerAPIGetVerifoneKioskDeviceIdsRequest, _Mapping]] = ..., get_verifone_kiosk_device_ids_response: _Optional[_Union[SuperchargerAPIGetVerifoneKioskDeviceIdsResponse, _Mapping]] = ..., update_followers_request: _Optional[_Union[SuperchargerAPIUpdateFollowersRequest, _Mapping]] = ..., update_followers_response: _Optional[_Union[SuperchargerAPIUpdateFollowersResponse, _Mapping]] = ..., get_dc_meters_commissioning_request: _Optional[_Union[SuperchargerAPIGetDcMetersCommissioningRequest, _Mapping]] = ..., get_dc_meters_commissioning_response: _Optional[_Union[SuperchargerAPIGetDcMetersCommissioningResponse, _Mapping]] = ..., set_dc_meter_commissioned_request: _Optional[_Union[SuperchargerAPISetDcMeterCommissionedRequest, _Mapping]] = ..., set_dc_meter_commissioned_response: _Optional[_Union[SuperchargerAPISetDcMeterCommissionedResponse, _Mapping]] = ..., odin_command_request: _Optional[_Union[SuperchargerAPIOdinCommandRequest, _Mapping]] = ..., odin_command_response: _Optional[_Union[SuperchargerAPIOdinCommandResponse, _Mapping]] = ..., get_payter_post_status_request: _Optional[_Union[SuperchargerAPIGetPayterPostStatusRequest, _Mapping]] = ..., get_payter_post_status_response: _Optional[_Union[SuperchargerAPIGetPayterPostStatusResponse, _Mapping]] = ..., get_ecu_firmware_update_progress_request: _Optional[_Union[SuperchargerAPIGetEcuFirmwareUpdateProgressRequest, _Mapping]] = ..., get_ecu_firmware_update_progress_response: _Optional[_Union[SuperchargerAPIGetEcuFirmwareUpdateProgressResponse, _Mapping]] = ...) -> None: ...

class VerifoneKiosk(_message.Message):
    __slots__ = ("serial_number", "subject_key_identifer")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_KEY_IDENTIFER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    subject_key_identifer: str
    def __init__(self, serial_number: _Optional[str] = ..., subject_key_identifer: _Optional[str] = ...) -> None: ...
