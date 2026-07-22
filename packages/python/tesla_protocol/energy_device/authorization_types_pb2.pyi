import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizationRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHORIZATION_ROLE_INVALID: _ClassVar[AuthorizationRole]
    AUTHORIZATION_ROLE_CUSTOMER: _ClassVar[AuthorizationRole]
    AUTHORIZATION_ROLE_VEHICLE: _ClassVar[AuthorizationRole]

class AuthorizedClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHORIZED_CLIENT_TYPE_INVALID: _ClassVar[AuthorizedClientType]
    AUTHORIZED_CLIENT_TYPE_CUSTOMER_MOBILE_APP: _ClassVar[AuthorizedClientType]
    AUTHORIZED_CLIENT_TYPE_VEHICLE: _ClassVar[AuthorizedClientType]

class AuthorizedKeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHORIZED_KEY_TYPE_INVALID: _ClassVar[AuthorizedKeyType]
    AUTHORIZED_KEY_TYPE_RSA: _ClassVar[AuthorizedKeyType]
    AUTHORIZED_KEY_TYPE_ECC: _ClassVar[AuthorizedKeyType]

class AuthorizedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHORIZED_STATE_INVALID: _ClassVar[AuthorizedState]
    AUTHORIZED_STATE_PENDING_VERIFICATION: _ClassVar[AuthorizedState]
    AUTHORIZED_STATE_PENDING_VERIFICATION_TIMEOUT: _ClassVar[AuthorizedState]
    AUTHORIZED_STATE_VERIFIED: _ClassVar[AuthorizedState]
    AUTHORIZED_STATE_REMOVED: _ClassVar[AuthorizedState]

class AuthorizedVerificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHORIZED_VERIFICATION_TYPE_INVALID: _ClassVar[AuthorizedVerificationType]
    AUTHORIZED_VERIFICATION_TYPE_PRESENCE_PROOF: _ClassVar[AuthorizedVerificationType]
    AUTHORIZED_VERIFICATION_TYPE_BLE: _ClassVar[AuthorizedVerificationType]
    AUTHORIZED_VERIFICATION_TYPE_SIGNED: _ClassVar[AuthorizedVerificationType]
    AUTHORIZED_VERIFICATION_TYPE_HERMES_COMMAND: _ClassVar[AuthorizedVerificationType]
AUTHORIZATION_ROLE_INVALID: AuthorizationRole
AUTHORIZATION_ROLE_CUSTOMER: AuthorizationRole
AUTHORIZATION_ROLE_VEHICLE: AuthorizationRole
AUTHORIZED_CLIENT_TYPE_INVALID: AuthorizedClientType
AUTHORIZED_CLIENT_TYPE_CUSTOMER_MOBILE_APP: AuthorizedClientType
AUTHORIZED_CLIENT_TYPE_VEHICLE: AuthorizedClientType
AUTHORIZED_KEY_TYPE_INVALID: AuthorizedKeyType
AUTHORIZED_KEY_TYPE_RSA: AuthorizedKeyType
AUTHORIZED_KEY_TYPE_ECC: AuthorizedKeyType
AUTHORIZED_STATE_INVALID: AuthorizedState
AUTHORIZED_STATE_PENDING_VERIFICATION: AuthorizedState
AUTHORIZED_STATE_PENDING_VERIFICATION_TIMEOUT: AuthorizedState
AUTHORIZED_STATE_VERIFIED: AuthorizedState
AUTHORIZED_STATE_REMOVED: AuthorizedState
AUTHORIZED_VERIFICATION_TYPE_INVALID: AuthorizedVerificationType
AUTHORIZED_VERIFICATION_TYPE_PRESENCE_PROOF: AuthorizedVerificationType
AUTHORIZED_VERIFICATION_TYPE_BLE: AuthorizedVerificationType
AUTHORIZED_VERIFICATION_TYPE_SIGNED: AuthorizedVerificationType
AUTHORIZED_VERIFICATION_TYPE_HERMES_COMMAND: AuthorizedVerificationType

class AuthorizationRecord(_message.Message):
    __slots__ = ('type', 'description', 'key_type', 'public_key', 'roles', 'state', 'verification', 'added_time', 'identifier', 'authorized_by_public_key')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    ADDED_TIME_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_BY_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    type: AuthorizedClientType
    description: str
    key_type: AuthorizedKeyType
    public_key: bytes
    roles: _containers.RepeatedScalarFieldContainer[AuthorizationRole]
    state: AuthorizedState
    verification: AuthorizedVerificationType
    added_time: _timestamp_pb2.Timestamp
    identifier: str
    authorized_by_public_key: bytes

    def __init__(self, type: _Optional[_Union[AuthorizedClientType, str]]=..., description: _Optional[str]=..., key_type: _Optional[_Union[AuthorizedKeyType, str]]=..., public_key: _Optional[bytes]=..., roles: _Optional[_Iterable[_Union[AuthorizationRole, str]]]=..., state: _Optional[_Union[AuthorizedState, str]]=..., verification: _Optional[_Union[AuthorizedVerificationType, str]]=..., added_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., identifier: _Optional[str]=..., authorized_by_public_key: _Optional[bytes]=...) -> None:
        ...