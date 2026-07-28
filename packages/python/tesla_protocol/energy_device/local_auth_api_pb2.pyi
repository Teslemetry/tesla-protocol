from . import networking_pb2 as _networking_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LocalAuthResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCAL_AUTH_RESULT_INVALID: _ClassVar[LocalAuthResult]
    LOCAL_AUTH_RESULT_SUCCESS: _ClassVar[LocalAuthResult]
    LOCAL_AUTH_RESULT_INVALID_PARAMETERS: _ClassVar[LocalAuthResult]
    LOCAL_AUTH_RESULT_INVALID_PASSWORD: _ClassVar[LocalAuthResult]
    LOCAL_AUTH_RESULT_PRESENCE_PROOF_REQUIRED: _ClassVar[LocalAuthResult]
    LOCAL_AUTH_RESULT_PRESENCE_PROOF_TIMED_OUT: _ClassVar[LocalAuthResult]
LOCAL_AUTH_RESULT_INVALID: LocalAuthResult
LOCAL_AUTH_RESULT_SUCCESS: LocalAuthResult
LOCAL_AUTH_RESULT_INVALID_PARAMETERS: LocalAuthResult
LOCAL_AUTH_RESULT_INVALID_PASSWORD: LocalAuthResult
LOCAL_AUTH_RESULT_PRESENCE_PROOF_REQUIRED: LocalAuthResult
LOCAL_AUTH_RESULT_PRESENCE_PROOF_TIMED_OUT: LocalAuthResult

class LocalAuthAPIRequiredFactorsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LocalAuthAPIRequiredFactorsResponse(_message.Message):
    __slots__ = ('password', 'presence')
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    password: bool
    presence: bool

    def __init__(self, password: bool=..., presence: bool=...) -> None:
        ...

class LocalAuthAPILoginRequest(_message.Message):
    __slots__ = ('participant', 'email', 'password')
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    participant: int
    email: str
    password: _networking_pb2.WifiPassword

    def __init__(self, participant: _Optional[int]=..., email: _Optional[str]=..., password: _Optional[_Union[_networking_pb2.WifiPassword, _Mapping]]=...) -> None:
        ...

class LocalAuthAPILoginResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: LocalAuthResult

    def __init__(self, result: _Optional[_Union[LocalAuthResult, str]]=...) -> None:
        ...

class LocalAuthAPILogoutRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LocalAuthAPILogoutResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LocalAuthAPICheckAuthStatusRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LocalAuthAPICheckAuthStatusResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: LocalAuthResult

    def __init__(self, result: _Optional[_Union[LocalAuthResult, str]]=...) -> None:
        ...

class LocalAuthMessages(_message.Message):
    __slots__ = ('required_factors_request', 'required_factors_response', 'login_request', 'login_response', 'logout_request', 'logout_response', 'check_auth_status_request', 'check_auth_status_response')
    REQUIRED_FACTORS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FACTORS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    LOGIN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LOGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECK_AUTH_STATUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHECK_AUTH_STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    required_factors_request: LocalAuthAPIRequiredFactorsRequest
    required_factors_response: LocalAuthAPIRequiredFactorsResponse
    login_request: LocalAuthAPILoginRequest
    login_response: LocalAuthAPILoginResponse
    logout_request: LocalAuthAPILogoutRequest
    logout_response: LocalAuthAPILogoutResponse
    check_auth_status_request: LocalAuthAPICheckAuthStatusRequest
    check_auth_status_response: LocalAuthAPICheckAuthStatusResponse

    def __init__(self, required_factors_request: _Optional[_Union[LocalAuthAPIRequiredFactorsRequest, _Mapping]]=..., required_factors_response: _Optional[_Union[LocalAuthAPIRequiredFactorsResponse, _Mapping]]=..., login_request: _Optional[_Union[LocalAuthAPILoginRequest, _Mapping]]=..., login_response: _Optional[_Union[LocalAuthAPILoginResponse, _Mapping]]=..., logout_request: _Optional[_Union[LocalAuthAPILogoutRequest, _Mapping]]=..., logout_response: _Optional[_Union[LocalAuthAPILogoutResponse, _Mapping]]=..., check_auth_status_request: _Optional[_Union[LocalAuthAPICheckAuthStatusRequest, _Mapping]]=..., check_auth_status_response: _Optional[_Union[LocalAuthAPICheckAuthStatusResponse, _Mapping]]=...) -> None:
        ...