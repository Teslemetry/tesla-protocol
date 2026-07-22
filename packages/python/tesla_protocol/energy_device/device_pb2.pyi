from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_TYPE_INVALID: _ClassVar[DeviceType]
    DEVICE_TYPE_GEN3WC: _ClassVar[DeviceType]
    DEVICE_TYPE_PVCOM: _ClassVar[DeviceType]
    DEVICE_TYPE_MSA: _ClassVar[DeviceType]
    DEVICE_TYPE_SITECONTROLLER: _ClassVar[DeviceType]
    DEVICE_TYPE_MEGAPUTER: _ClassVar[DeviceType]
    DEVICE_TYPE_IPM: _ClassVar[DeviceType]

class DeviceCertFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_CERT_FORMAT_INVALID: _ClassVar[DeviceCertFormat]
    DEVICE_CERT_FORMAT_DER: _ClassVar[DeviceCertFormat]
    DEVICE_CERT_FORMAT_PEM: _ClassVar[DeviceCertFormat]

class DeviceSignatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_SIGNATURE_TYPE_INVALID: _ClassVar[DeviceSignatureType]
    DEVICE_SIGNATURE_TYPE_SHA256_ECDSA_ASN1: _ClassVar[DeviceSignatureType]

class Cipher(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CIPHER_INVALID: _ClassVar[Cipher]
    CIPHER_RSA_OAEP_SHA256: _ClassVar[Cipher]

class TEGDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEG_DEVICE_TYPE_INVALID: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_SMC: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_HEC_GATEWAY1: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_TEG_GATEWAY2: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_TEG_POWERWALLPLUS: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_TEG_MP1: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_TEG_SUPERCHARGER: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_TACO_POWERWALL3: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_TEG_PVI: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_TACO_GATEWAY3V: _ClassVar[TEGDeviceType]
    TEG_DEVICE_TYPE_TACO_WALLBOX: _ClassVar[TEGDeviceType]

class iPMDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IPM_DEVICE_TYPE_INVALID: _ClassVar[iPMDeviceType]
    IPM_DEVICE_TYPE_POWERPACK3: _ClassVar[iPMDeviceType]
    IPM_DEVICE_TYPE_SUPERCHARGER4: _ClassVar[iPMDeviceType]
DEVICE_TYPE_INVALID: DeviceType
DEVICE_TYPE_GEN3WC: DeviceType
DEVICE_TYPE_PVCOM: DeviceType
DEVICE_TYPE_MSA: DeviceType
DEVICE_TYPE_SITECONTROLLER: DeviceType
DEVICE_TYPE_MEGAPUTER: DeviceType
DEVICE_TYPE_IPM: DeviceType
DEVICE_CERT_FORMAT_INVALID: DeviceCertFormat
DEVICE_CERT_FORMAT_DER: DeviceCertFormat
DEVICE_CERT_FORMAT_PEM: DeviceCertFormat
DEVICE_SIGNATURE_TYPE_INVALID: DeviceSignatureType
DEVICE_SIGNATURE_TYPE_SHA256_ECDSA_ASN1: DeviceSignatureType
CIPHER_INVALID: Cipher
CIPHER_RSA_OAEP_SHA256: Cipher
TEG_DEVICE_TYPE_INVALID: TEGDeviceType
TEG_DEVICE_TYPE_SMC: TEGDeviceType
TEG_DEVICE_TYPE_HEC_GATEWAY1: TEGDeviceType
TEG_DEVICE_TYPE_TEG_GATEWAY2: TEGDeviceType
TEG_DEVICE_TYPE_TEG_POWERWALLPLUS: TEGDeviceType
TEG_DEVICE_TYPE_TEG_MP1: TEGDeviceType
TEG_DEVICE_TYPE_TEG_SUPERCHARGER: TEGDeviceType
TEG_DEVICE_TYPE_TACO_POWERWALL3: TEGDeviceType
TEG_DEVICE_TYPE_TEG_PVI: TEGDeviceType
TEG_DEVICE_TYPE_TACO_GATEWAY3V: TEGDeviceType
TEG_DEVICE_TYPE_TACO_WALLBOX: TEGDeviceType
IPM_DEVICE_TYPE_INVALID: iPMDeviceType
IPM_DEVICE_TYPE_POWERPACK3: iPMDeviceType
IPM_DEVICE_TYPE_SUPERCHARGER4: iPMDeviceType

class Din(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...

class EcuId(_message.Message):
    __slots__ = ('part_number', 'serial_number')
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    part_number: str
    serial_number: str

    def __init__(self, part_number: _Optional[str]=..., serial_number: _Optional[str]=...) -> None:
        ...

class DeviceSignedPayload(_message.Message):
    __slots__ = ('payload', 'device_signature_type', 'signature', 'device_cert_format', 'device_cert')
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SIGNATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CERT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CERT_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    device_signature_type: DeviceSignatureType
    signature: bytes
    device_cert_format: DeviceCertFormat
    device_cert: bytes

    def __init__(self, payload: _Optional[bytes]=..., device_signature_type: _Optional[_Union[DeviceSignatureType, str]]=..., signature: _Optional[bytes]=..., device_cert_format: _Optional[_Union[DeviceCertFormat, str]]=..., device_cert: _Optional[bytes]=...) -> None:
        ...

class EncryptedMessage(_message.Message):
    __slots__ = ('cipher', 'cipher_text')
    CIPHER_FIELD_NUMBER: _ClassVar[int]
    CIPHER_TEXT_FIELD_NUMBER: _ClassVar[int]
    cipher: Cipher
    cipher_text: bytes

    def __init__(self, cipher: _Optional[_Union[Cipher, str]]=..., cipher_text: _Optional[bytes]=...) -> None:
        ...