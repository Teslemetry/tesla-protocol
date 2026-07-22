"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'device.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cdevice.proto\x12\x1ctesla.proto.energy_device.v1"\x14\n\x03Din\x12\r\n\x05value\x18\x01 \x01(\t"3\n\x05EcuId\x12\x13\n\x0bpart_number\x18\x01 \x01(\t\x12\x15\n\rserial_number\x18\x02 \x01(\t"\xec\x01\n\x13DeviceSignedPayload\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12P\n\x15device_signature_type\x18\x02 \x01(\x0e21.tesla.proto.energy_device.v1.DeviceSignatureType\x12\x11\n\tsignature\x18\x03 \x01(\x0c\x12J\n\x12device_cert_format\x18\x04 \x01(\x0e2..tesla.proto.energy_device.v1.DeviceCertFormat\x12\x13\n\x0bdevice_cert\x18\x05 \x01(\x0c"]\n\x10EncryptedMessage\x124\n\x06cipher\x18\x01 \x01(\x0e2$.tesla.proto.energy_device.v1.Cipher\x12\x13\n\x0bcipher_text\x18\x02 \x01(\x0c*\xb9\x01\n\nDeviceType\x12\x17\n\x13DEVICE_TYPE_INVALID\x10\x00\x12\x16\n\x12DEVICE_TYPE_GEN3WC\x10\x01\x12\x15\n\x11DEVICE_TYPE_PVCOM\x10\x02\x12\x13\n\x0fDEVICE_TYPE_MSA\x10\x03\x12\x1e\n\x1aDEVICE_TYPE_SITECONTROLLER\x10\x04\x12\x19\n\x15DEVICE_TYPE_MEGAPUTER\x10\x05\x12\x13\n\x0fDEVICE_TYPE_IPM\x10\x06*j\n\x10DeviceCertFormat\x12\x1e\n\x1aDEVICE_CERT_FORMAT_INVALID\x10\x00\x12\x1a\n\x16DEVICE_CERT_FORMAT_DER\x10\x01\x12\x1a\n\x16DEVICE_CERT_FORMAT_PEM\x10\x02*e\n\x13DeviceSignatureType\x12!\n\x1dDEVICE_SIGNATURE_TYPE_INVALID\x10\x00\x12+\n\'DEVICE_SIGNATURE_TYPE_SHA256_ECDSA_ASN1\x10\x01*8\n\x06Cipher\x12\x12\n\x0eCIPHER_INVALID\x10\x00\x12\x1a\n\x16CIPHER_RSA_OAEP_SHA256\x10\x02*\xfb\x02\n\rTEGDeviceType\x12\x1b\n\x17TEG_DEVICE_TYPE_INVALID\x10\x00\x12\x17\n\x13TEG_DEVICE_TYPE_SMC\x10\x01\x12 \n\x1cTEG_DEVICE_TYPE_HEC_GATEWAY1\x10\x02\x12 \n\x1cTEG_DEVICE_TYPE_TEG_GATEWAY2\x10\x03\x12%\n!TEG_DEVICE_TYPE_TEG_POWERWALLPLUS\x10\x04\x12\x1b\n\x17TEG_DEVICE_TYPE_TEG_MP1\x10\x05\x12$\n TEG_DEVICE_TYPE_TEG_SUPERCHARGER\x10\x06\x12#\n\x1fTEG_DEVICE_TYPE_TACO_POWERWALL3\x10\x07\x12\x1b\n\x17TEG_DEVICE_TYPE_TEG_PVI\x10\x08\x12"\n\x1eTEG_DEVICE_TYPE_TACO_GATEWAY3V\x10\t\x12 \n\x1cTEG_DEVICE_TYPE_TACO_WALLBOX\x10\n*o\n\riPMDeviceType\x12\x1b\n\x17IPM_DEVICE_TYPE_INVALID\x10\x00\x12\x1e\n\x1aIPM_DEVICE_TYPE_POWERPACK3\x10\x01\x12!\n\x1dIPM_DEVICE_TYPE_SUPERCHARGER4\x10\x02Bz\n$com.tesla.generated.energy_device.v1B\x06DeviceZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'device_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x06DeviceZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_DEVICETYPE']._serialized_start = 456
    _globals['_DEVICETYPE']._serialized_end = 641
    _globals['_DEVICECERTFORMAT']._serialized_start = 643
    _globals['_DEVICECERTFORMAT']._serialized_end = 749
    _globals['_DEVICESIGNATURETYPE']._serialized_start = 751
    _globals['_DEVICESIGNATURETYPE']._serialized_end = 852
    _globals['_CIPHER']._serialized_start = 854
    _globals['_CIPHER']._serialized_end = 910
    _globals['_TEGDEVICETYPE']._serialized_start = 913
    _globals['_TEGDEVICETYPE']._serialized_end = 1292
    _globals['_IPMDEVICETYPE']._serialized_start = 1294
    _globals['_IPMDEVICETYPE']._serialized_end = 1405
    _globals['_DIN']._serialized_start = 46
    _globals['_DIN']._serialized_end = 66
    _globals['_ECUID']._serialized_start = 68
    _globals['_ECUID']._serialized_end = 119
    _globals['_DEVICESIGNEDPAYLOAD']._serialized_start = 122
    _globals['_DEVICESIGNEDPAYLOAD']._serialized_end = 358
    _globals['_ENCRYPTEDMESSAGE']._serialized_start = 360
    _globals['_ENCRYPTEDMESSAGE']._serialized_end = 453