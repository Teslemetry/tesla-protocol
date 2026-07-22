import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import authorization_types_pb2 as _authorization_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizationAPIAddAuthorizedClientRequest(_message.Message):
    __slots__ = ('type', 'description', 'key_type', 'public_key')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    type: _authorization_types_pb2.AuthorizedClientType
    description: str
    key_type: _authorization_types_pb2.AuthorizedKeyType
    public_key: bytes

    def __init__(self, type: _Optional[_Union[_authorization_types_pb2.AuthorizedClientType, str]]=..., description: _Optional[str]=..., key_type: _Optional[_Union[_authorization_types_pb2.AuthorizedKeyType, str]]=..., public_key: _Optional[bytes]=...) -> None:
        ...

class AuthorizationAPIAddAuthorizedClientResponse(_message.Message):
    __slots__ = ('client',)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _authorization_types_pb2.AuthorizationRecord

    def __init__(self, client: _Optional[_Union[_authorization_types_pb2.AuthorizationRecord, _Mapping]]=...) -> None:
        ...

class AuthorizationAPIAddAuthorizedClientByTrustedSignatureRequest(_message.Message):
    __slots__ = ('type', 'description', 'key_type', 'public_key', 'roles', 'identifier')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    type: _authorization_types_pb2.AuthorizedClientType
    description: str
    key_type: _authorization_types_pb2.AuthorizedKeyType
    public_key: bytes
    roles: _containers.RepeatedScalarFieldContainer[_authorization_types_pb2.AuthorizationRole]
    identifier: str

    def __init__(self, type: _Optional[_Union[_authorization_types_pb2.AuthorizedClientType, str]]=..., description: _Optional[str]=..., key_type: _Optional[_Union[_authorization_types_pb2.AuthorizedKeyType, str]]=..., public_key: _Optional[bytes]=..., roles: _Optional[_Iterable[_Union[_authorization_types_pb2.AuthorizationRole, str]]]=..., identifier: _Optional[str]=...) -> None:
        ...

class AuthorizationAPIAddAuthorizedClientByTrustedSignatureResponse(_message.Message):
    __slots__ = ('client',)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _authorization_types_pb2.AuthorizationRecord

    def __init__(self, client: _Optional[_Union[_authorization_types_pb2.AuthorizationRecord, _Mapping]]=...) -> None:
        ...

class AuthorizationAPIRemoveAuthorizedClientRequest(_message.Message):
    __slots__ = ('public_key',)
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes

    def __init__(self, public_key: _Optional[bytes]=...) -> None:
        ...

class AuthorizationAPIRemoveAuthorizedClientResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AuthorizationAPIListAuthorizedClientsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AuthorizationAPIListAuthorizedClientsResponse(_message.Message):
    __slots__ = ('clients', 'enable_line_switch_off')
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LINE_SWITCH_OFF_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[_authorization_types_pb2.AuthorizationRecord]
    enable_line_switch_off: bool

    def __init__(self, clients: _Optional[_Iterable[_Union[_authorization_types_pb2.AuthorizationRecord, _Mapping]]]=..., enable_line_switch_off: bool=...) -> None:
        ...

class AuthorizationAPIGetSignedCommandsPublicKeyRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AuthorizationAPIGetSignedCommandsPublicKeyResponse(_message.Message):
    __slots__ = ('pub_key_ecc',)
    PUB_KEY_ECC_FIELD_NUMBER: _ClassVar[int]
    pub_key_ecc: bytes

    def __init__(self, pub_key_ecc: _Optional[bytes]=...) -> None:
        ...

class AuthorizationAPIConfigureRemoteServiceRequest(_message.Message):
    __slots__ = ('duration_seconds', 'session_id', 'requester_email')
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    duration_seconds: int
    session_id: str
    requester_email: str

    def __init__(self, duration_seconds: _Optional[int]=..., session_id: _Optional[str]=..., requester_email: _Optional[str]=...) -> None:
        ...

class AuthorizationAPIConfigureRemoteServiceResponse(_message.Message):
    __slots__ = ('begin_time', 'expiry_time')
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    begin_time: _timestamp_pb2.Timestamp
    expiry_time: _timestamp_pb2.Timestamp

    def __init__(self, begin_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., expiry_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AuthorizationMessages(_message.Message):
    __slots__ = ('add_authorized_client_request', 'add_authorized_client_response', 'remove_authorized_client_request', 'remove_authorized_client_response', 'list_authorized_clients_request', 'list_authorized_clients_response', 'get_signed_commands_public_key_request', 'get_signed_commands_public_key_response', 'add_authorized_client_by_trusted_signature_request', 'add_authorized_client_by_trusted_signature_response', 'configure_remote_service_request', 'configure_remote_service_response')
    ADD_AUTHORIZED_CLIENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ADD_AUTHORIZED_CLIENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_AUTHORIZED_CLIENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REMOVE_AUTHORIZED_CLIENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    LIST_AUTHORIZED_CLIENTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LIST_AUTHORIZED_CLIENTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_SIGNED_COMMANDS_PUBLIC_KEY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_SIGNED_COMMANDS_PUBLIC_KEY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ADD_AUTHORIZED_CLIENT_BY_TRUSTED_SIGNATURE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ADD_AUTHORIZED_CLIENT_BY_TRUSTED_SIGNATURE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_REMOTE_SERVICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_REMOTE_SERVICE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    add_authorized_client_request: AuthorizationAPIAddAuthorizedClientRequest
    add_authorized_client_response: AuthorizationAPIAddAuthorizedClientResponse
    remove_authorized_client_request: AuthorizationAPIRemoveAuthorizedClientRequest
    remove_authorized_client_response: AuthorizationAPIRemoveAuthorizedClientResponse
    list_authorized_clients_request: AuthorizationAPIListAuthorizedClientsRequest
    list_authorized_clients_response: AuthorizationAPIListAuthorizedClientsResponse
    get_signed_commands_public_key_request: AuthorizationAPIGetSignedCommandsPublicKeyRequest
    get_signed_commands_public_key_response: AuthorizationAPIGetSignedCommandsPublicKeyResponse
    add_authorized_client_by_trusted_signature_request: AuthorizationAPIAddAuthorizedClientByTrustedSignatureRequest
    add_authorized_client_by_trusted_signature_response: AuthorizationAPIAddAuthorizedClientByTrustedSignatureResponse
    configure_remote_service_request: AuthorizationAPIConfigureRemoteServiceRequest
    configure_remote_service_response: AuthorizationAPIConfigureRemoteServiceResponse

    def __init__(self, add_authorized_client_request: _Optional[_Union[AuthorizationAPIAddAuthorizedClientRequest, _Mapping]]=..., add_authorized_client_response: _Optional[_Union[AuthorizationAPIAddAuthorizedClientResponse, _Mapping]]=..., remove_authorized_client_request: _Optional[_Union[AuthorizationAPIRemoveAuthorizedClientRequest, _Mapping]]=..., remove_authorized_client_response: _Optional[_Union[AuthorizationAPIRemoveAuthorizedClientResponse, _Mapping]]=..., list_authorized_clients_request: _Optional[_Union[AuthorizationAPIListAuthorizedClientsRequest, _Mapping]]=..., list_authorized_clients_response: _Optional[_Union[AuthorizationAPIListAuthorizedClientsResponse, _Mapping]]=..., get_signed_commands_public_key_request: _Optional[_Union[AuthorizationAPIGetSignedCommandsPublicKeyRequest, _Mapping]]=..., get_signed_commands_public_key_response: _Optional[_Union[AuthorizationAPIGetSignedCommandsPublicKeyResponse, _Mapping]]=..., add_authorized_client_by_trusted_signature_request: _Optional[_Union[AuthorizationAPIAddAuthorizedClientByTrustedSignatureRequest, _Mapping]]=..., add_authorized_client_by_trusted_signature_response: _Optional[_Union[AuthorizationAPIAddAuthorizedClientByTrustedSignatureResponse, _Mapping]]=..., configure_remote_service_request: _Optional[_Union[AuthorizationAPIConfigureRemoteServiceRequest, _Mapping]]=..., configure_remote_service_response: _Optional[_Union[AuthorizationAPIConfigureRemoteServiceResponse, _Mapping]]=...) -> None:
        ...