from tesla_protocol.energy_device import authorization_types_pb2 as _authorization_types_pb2
from tesla_protocol.energy_device import device_pb2 as _device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFCProofOfPresence(_message.Message):
    __slots__ = ("client_public_key", "nfc_nonce", "nonce_proof", "key_type", "roles", "client_type")
    CLIENT_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    NFC_NONCE_FIELD_NUMBER: _ClassVar[int]
    NONCE_PROOF_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    client_public_key: bytes
    nfc_nonce: bytes
    nonce_proof: bytes
    key_type: _authorization_types_pb2.AuthorizedKeyType
    roles: _containers.RepeatedScalarFieldContainer[_authorization_types_pb2.AuthorizationRole]
    client_type: _authorization_types_pb2.AuthorizedClientType
    def __init__(self, client_public_key: _Optional[bytes] = ..., nfc_nonce: _Optional[bytes] = ..., nonce_proof: _Optional[bytes] = ..., key_type: _Optional[_Union[_authorization_types_pb2.AuthorizedKeyType, str]] = ..., roles: _Optional[_Iterable[_Union[_authorization_types_pb2.AuthorizationRole, str]]] = ..., client_type: _Optional[_Union[_authorization_types_pb2.AuthorizedClientType, str]] = ...) -> None: ...

class NFCAck(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SPAKE2PlusClientHello(_message.Message):
    __slots__ = ("client_public_key", "client_public_share", "profile", "key_type", "roles", "client_type")
    CLIENT_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PUBLIC_SHARE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    client_public_key: bytes
    client_public_share: bytes
    profile: _authorization_types_pb2.SPAKE2PlusProfile
    key_type: _authorization_types_pb2.AuthorizedKeyType
    roles: _containers.RepeatedScalarFieldContainer[_authorization_types_pb2.AuthorizationRole]
    client_type: _authorization_types_pb2.AuthorizedClientType
    def __init__(self, client_public_key: _Optional[bytes] = ..., client_public_share: _Optional[bytes] = ..., profile: _Optional[_Union[_authorization_types_pb2.SPAKE2PlusProfile, str]] = ..., key_type: _Optional[_Union[_authorization_types_pb2.AuthorizedKeyType, str]] = ..., roles: _Optional[_Iterable[_Union[_authorization_types_pb2.AuthorizationRole, str]]] = ..., client_type: _Optional[_Union[_authorization_types_pb2.AuthorizedClientType, str]] = ...) -> None: ...

class SPAKE2PlusServerHello(_message.Message):
    __slots__ = ("server_public_share", "server_confirmation", "session_uuid", "profile")
    SERVER_PUBLIC_SHARE_FIELD_NUMBER: _ClassVar[int]
    SERVER_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_UUID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    server_public_share: bytes
    server_confirmation: bytes
    session_uuid: _device_pb2.UUIDv4Bytes
    profile: _authorization_types_pb2.SPAKE2PlusProfile
    def __init__(self, server_public_share: _Optional[bytes] = ..., server_confirmation: _Optional[bytes] = ..., session_uuid: _Optional[_Union[_device_pb2.UUIDv4Bytes, _Mapping]] = ..., profile: _Optional[_Union[_authorization_types_pb2.SPAKE2PlusProfile, str]] = ...) -> None: ...

class SPAKE2PlusConfirmRequest(_message.Message):
    __slots__ = ("client_confirmation",)
    CLIENT_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    client_confirmation: bytes
    def __init__(self, client_confirmation: _Optional[bytes] = ...) -> None: ...

class SPAKE2PlusConfirmAck(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResumeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResumeAck(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceAttestation(_message.Message):
    __slots__ = ("cert_chain", "signature")
    CERT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    cert_chain: _containers.RepeatedScalarFieldContainer[bytes]
    signature: bytes
    def __init__(self, cert_chain: _Optional[_Iterable[bytes]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class BLEAPIPairRequest(_message.Message):
    __slots__ = ("nfc", "spake2_plus_hello", "spake2_plus_confirm", "resume")
    NFC_FIELD_NUMBER: _ClassVar[int]
    SPAKE2_PLUS_HELLO_FIELD_NUMBER: _ClassVar[int]
    SPAKE2_PLUS_CONFIRM_FIELD_NUMBER: _ClassVar[int]
    RESUME_FIELD_NUMBER: _ClassVar[int]
    nfc: NFCProofOfPresence
    spake2_plus_hello: SPAKE2PlusClientHello
    spake2_plus_confirm: SPAKE2PlusConfirmRequest
    resume: ResumeRequest
    def __init__(self, nfc: _Optional[_Union[NFCProofOfPresence, _Mapping]] = ..., spake2_plus_hello: _Optional[_Union[SPAKE2PlusClientHello, _Mapping]] = ..., spake2_plus_confirm: _Optional[_Union[SPAKE2PlusConfirmRequest, _Mapping]] = ..., resume: _Optional[_Union[ResumeRequest, _Mapping]] = ...) -> None: ...

class BLEAPIPairResponse(_message.Message):
    __slots__ = ("attestation", "nfc", "spake2_plus_hello", "spake2_plus_confirm", "resume")
    ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    NFC_FIELD_NUMBER: _ClassVar[int]
    SPAKE2_PLUS_HELLO_FIELD_NUMBER: _ClassVar[int]
    SPAKE2_PLUS_CONFIRM_FIELD_NUMBER: _ClassVar[int]
    RESUME_FIELD_NUMBER: _ClassVar[int]
    attestation: DeviceAttestation
    nfc: NFCAck
    spake2_plus_hello: SPAKE2PlusServerHello
    spake2_plus_confirm: SPAKE2PlusConfirmAck
    resume: ResumeAck
    def __init__(self, attestation: _Optional[_Union[DeviceAttestation, _Mapping]] = ..., nfc: _Optional[_Union[NFCAck, _Mapping]] = ..., spake2_plus_hello: _Optional[_Union[SPAKE2PlusServerHello, _Mapping]] = ..., spake2_plus_confirm: _Optional[_Union[SPAKE2PlusConfirmAck, _Mapping]] = ..., resume: _Optional[_Union[ResumeAck, _Mapping]] = ...) -> None: ...

class BLEMessages(_message.Message):
    __slots__ = ("pair_request", "pair_response")
    PAIR_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PAIR_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    pair_request: BLEAPIPairRequest
    pair_response: BLEAPIPairResponse
    def __init__(self, pair_request: _Optional[_Union[BLEAPIPairRequest, _Mapping]] = ..., pair_response: _Optional[_Union[BLEAPIPairResponse, _Mapping]] = ...) -> None: ...
