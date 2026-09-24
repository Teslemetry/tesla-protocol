from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Tag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TAG_SIGNATURE_TYPE: _ClassVar[Tag]
    TAG_DOMAIN: _ClassVar[Tag]
    TAG_PERSONALIZATION: _ClassVar[Tag]
    TAG_EPOCH: _ClassVar[Tag]
    TAG_EXPIRES_AT: _ClassVar[Tag]
    TAG_COUNTER: _ClassVar[Tag]
    TAG_CHALLENGE: _ClassVar[Tag]
    TAG_FLAGS: _ClassVar[Tag]
    TAG_REQUEST_HASH: _ClassVar[Tag]
    TAG_FAULT: _ClassVar[Tag]
    TAG_COMMAND_PREFIX: _ClassVar[Tag]
    TAG_END: _ClassVar[Tag]

class SignatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_TYPE_AES_GCM: _ClassVar[SignatureType]
    SIGNATURE_TYPE_ECDSA: _ClassVar[SignatureType]
    SIGNATURE_TYPE_PRESENT_KEY: _ClassVar[SignatureType]
    SIGNATURE_TYPE_AES_GCM_TOKEN: _ClassVar[SignatureType]
    SIGNATURE_TYPE_ECDSA_PERSONALIZED: _ClassVar[SignatureType]
    SIGNATURE_TYPE_AES_GCM_PERSONALIZED: _ClassVar[SignatureType]
    SIGNATURE_TYPE_HMAC: _ClassVar[SignatureType]
    SIGNATURE_TYPE_HMAC_PERSONALIZED: _ClassVar[SignatureType]
    SIGNATURE_TYPE_AES_GCM_RESPONSE: _ClassVar[SignatureType]
    SIGNATURE_TYPE_AES_GCM_DETACHED: _ClassVar[SignatureType]
    SIGNATURE_TYPE_CERTIFICATE_ECDSA: _ClassVar[SignatureType]

class IdentifiedKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDENTIFIEDKEY_UNKNOWN: _ClassVar[IdentifiedKey]
    IDENTIFIEDKEY_ROOT_KEY: _ClassVar[IdentifiedKey]

class Session_Info_Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_INFO_STATUS_OK: _ClassVar[Session_Info_Status]
    SESSION_INFO_STATUS_KEY_NOT_ON_WHITELIST: _ClassVar[Session_Info_Status]
    SESSION_INFO_STATUS_INVALID_HANDLE: _ClassVar[Session_Info_Status]
TAG_SIGNATURE_TYPE: Tag
TAG_DOMAIN: Tag
TAG_PERSONALIZATION: Tag
TAG_EPOCH: Tag
TAG_EXPIRES_AT: Tag
TAG_COUNTER: Tag
TAG_CHALLENGE: Tag
TAG_FLAGS: Tag
TAG_REQUEST_HASH: Tag
TAG_FAULT: Tag
TAG_COMMAND_PREFIX: Tag
TAG_END: Tag
SIGNATURE_TYPE_AES_GCM: SignatureType
SIGNATURE_TYPE_ECDSA: SignatureType
SIGNATURE_TYPE_PRESENT_KEY: SignatureType
SIGNATURE_TYPE_AES_GCM_TOKEN: SignatureType
SIGNATURE_TYPE_ECDSA_PERSONALIZED: SignatureType
SIGNATURE_TYPE_AES_GCM_PERSONALIZED: SignatureType
SIGNATURE_TYPE_HMAC: SignatureType
SIGNATURE_TYPE_HMAC_PERSONALIZED: SignatureType
SIGNATURE_TYPE_AES_GCM_RESPONSE: SignatureType
SIGNATURE_TYPE_AES_GCM_DETACHED: SignatureType
SIGNATURE_TYPE_CERTIFICATE_ECDSA: SignatureType
IDENTIFIEDKEY_UNKNOWN: IdentifiedKey
IDENTIFIEDKEY_ROOT_KEY: IdentifiedKey
SESSION_INFO_STATUS_OK: Session_Info_Status
SESSION_INFO_STATUS_KEY_NOT_ON_WHITELIST: Session_Info_Status
SESSION_INFO_STATUS_INVALID_HANDLE: Session_Info_Status

class KeyIdentity(_message.Message):
    __slots__ = ('public_key', 'handle', 'identified_key')
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIED_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    handle: int
    identified_key: IdentifiedKey

    def __init__(self, public_key: _Optional[bytes]=..., handle: _Optional[int]=..., identified_key: _Optional[_Union[IdentifiedKey, str]]=...) -> None:
        ...

class AES_GCM_Personalized_Signature_Data(_message.Message):
    __slots__ = ('epoch', 'nonce', 'counter', 'expires_at', 'tag')
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    epoch: bytes
    nonce: bytes
    counter: int
    expires_at: int
    tag: bytes

    def __init__(self, epoch: _Optional[bytes]=..., nonce: _Optional[bytes]=..., counter: _Optional[int]=..., expires_at: _Optional[int]=..., tag: _Optional[bytes]=...) -> None:
        ...

class AES_GCM_Response_Signature_Data(_message.Message):
    __slots__ = ('nonce', 'counter', 'tag')
    NONCE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    nonce: bytes
    counter: int
    tag: bytes

    def __init__(self, nonce: _Optional[bytes]=..., counter: _Optional[int]=..., tag: _Optional[bytes]=...) -> None:
        ...

class Present_Key_Signature_Data(_message.Message):
    __slots__ = ('auth_token',)
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    auth_token: bytes

    def __init__(self, auth_token: _Optional[bytes]=...) -> None:
        ...

class AES_GCM_Detached_Signature_Data(_message.Message):
    __slots__ = ('epoch', 'counter', 'expires_at', 'nonce', 'tag')
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    epoch: bytes
    counter: int
    expires_at: int
    nonce: bytes
    tag: bytes

    def __init__(self, epoch: _Optional[bytes]=..., counter: _Optional[int]=..., expires_at: _Optional[int]=..., nonce: _Optional[bytes]=..., tag: _Optional[bytes]=...) -> None:
        ...

class Certificate_ECDSA_Signature_Data(_message.Message):
    __slots__ = ('certificate_chain_der', 'signature')
    CERTIFICATE_CHAIN_DER_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    certificate_chain_der: bytes
    signature: bytes

    def __init__(self, certificate_chain_der: _Optional[bytes]=..., signature: _Optional[bytes]=...) -> None:
        ...

class HMAC_Signature_Data(_message.Message):
    __slots__ = ('tag',)
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: bytes

    def __init__(self, tag: _Optional[bytes]=...) -> None:
        ...

class HMAC_Personalized_Signature_Data(_message.Message):
    __slots__ = ('epoch', 'counter', 'expires_at', 'tag')
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    epoch: bytes
    counter: int
    expires_at: int
    tag: bytes

    def __init__(self, epoch: _Optional[bytes]=..., counter: _Optional[int]=..., expires_at: _Optional[int]=..., tag: _Optional[bytes]=...) -> None:
        ...

class SignatureData(_message.Message):
    __slots__ = ('signer_identity', 'Present_Key_data', 'AES_GCM_Personalized_data', 'session_info_tag', 'HMAC_Personalized_data', 'AES_GCM_Response_data', 'AES_GCM_Detached_data', 'Certificate_ECDSA_data')
    SIGNER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    PRESENT_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    AES_GCM_PERSONALIZED_DATA_FIELD_NUMBER: _ClassVar[int]
    SESSION_INFO_TAG_FIELD_NUMBER: _ClassVar[int]
    HMAC_PERSONALIZED_DATA_FIELD_NUMBER: _ClassVar[int]
    AES_GCM_RESPONSE_DATA_FIELD_NUMBER: _ClassVar[int]
    AES_GCM_DETACHED_DATA_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_ECDSA_DATA_FIELD_NUMBER: _ClassVar[int]
    signer_identity: KeyIdentity
    Present_Key_data: Present_Key_Signature_Data
    AES_GCM_Personalized_data: AES_GCM_Personalized_Signature_Data
    session_info_tag: HMAC_Signature_Data
    HMAC_Personalized_data: HMAC_Personalized_Signature_Data
    AES_GCM_Response_data: AES_GCM_Response_Signature_Data
    AES_GCM_Detached_data: AES_GCM_Detached_Signature_Data
    Certificate_ECDSA_data: Certificate_ECDSA_Signature_Data

    def __init__(self, signer_identity: _Optional[_Union[KeyIdentity, _Mapping]]=..., Present_Key_data: _Optional[_Union[Present_Key_Signature_Data, _Mapping]]=..., AES_GCM_Personalized_data: _Optional[_Union[AES_GCM_Personalized_Signature_Data, _Mapping]]=..., session_info_tag: _Optional[_Union[HMAC_Signature_Data, _Mapping]]=..., HMAC_Personalized_data: _Optional[_Union[HMAC_Personalized_Signature_Data, _Mapping]]=..., AES_GCM_Response_data: _Optional[_Union[AES_GCM_Response_Signature_Data, _Mapping]]=..., AES_GCM_Detached_data: _Optional[_Union[AES_GCM_Detached_Signature_Data, _Mapping]]=..., Certificate_ECDSA_data: _Optional[_Union[Certificate_ECDSA_Signature_Data, _Mapping]]=...) -> None:
        ...

class GetSessionInfoRequest(_message.Message):
    __slots__ = ('key_identity',)
    KEY_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    key_identity: KeyIdentity

    def __init__(self, key_identity: _Optional[_Union[KeyIdentity, _Mapping]]=...) -> None:
        ...

class SessionInfo(_message.Message):
    __slots__ = ('counter', 'publicKey', 'epoch', 'clock_time', 'status', 'handle', 'field_7')
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    CLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    FIELD_7_FIELD_NUMBER: _ClassVar[int]
    counter: int
    publicKey: bytes
    epoch: bytes
    clock_time: int
    status: Session_Info_Status
    handle: int
    field_7: int

    def __init__(self, counter: _Optional[int]=..., publicKey: _Optional[bytes]=..., epoch: _Optional[bytes]=..., clock_time: _Optional[int]=..., status: _Optional[_Union[Session_Info_Status, str]]=..., handle: _Optional[int]=..., field_7: _Optional[int]=...) -> None:
        ...