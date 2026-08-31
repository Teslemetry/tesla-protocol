"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'signed_message.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14signed_message.proto\x12\x1ctesla.proto.energy_device.v1"s\n\x0bDestination\x126\n\x06domain\x18\x01 \x01(\x0e2$.tesla.proto.energy_device.v1.DomainH\x00\x12\x19\n\x0frouting_address\x18\x02 \x01(\x0cH\x00B\x11\n\x0fsub_destination"F\n\x0bKeyIdentity\x12\x14\n\npublic_key\x18\x01 \x01(\x0cH\x00\x12\x10\n\x06handle\x18\x03 \x01(\rH\x00B\x0f\n\ridentity_type"9\n\x10RsaSignatureData\x12\x12\n\nexpires_at\x18\x01 \x01(\x07\x12\x11\n\tsignature\x18\x02 \x01(\x0c"\xa3\x01\n\rSignatureData\x12B\n\x0fsigner_identity\x18\x01 \x01(\x0b2).tesla.proto.energy_device.v1.KeyIdentity\x12B\n\x08rsa_data\x18\x07 \x01(\x0b2..tesla.proto.energy_device.v1.RsaSignatureDataH\x00B\n\n\x08sig_type"T\n\rMessageStatus\x12C\n\rmessage_fault\x18\x01 \x01(\x0e2,.tesla.proto.energy_device.v1.MessageFault_E"\xb2\x03\n\x0fRoutableMessage\x12A\n\x0eto_destination\x18\x06 \x01(\x0b2).tesla.proto.energy_device.v1.Destination\x12C\n\x10from_destination\x18\x07 \x01(\x0b2).tesla.proto.energy_device.v1.Destination\x12#\n\x19protobuf_message_as_bytes\x18\n \x01(\x0cH\x00\x12C\n\x0esignature_data\x18\r \x01(\x0b2+.tesla.proto.energy_device.v1.SignatureData\x12J\n\x15signed_message_status\x18\x0c \x01(\x0b2+.tesla.proto.energy_device.v1.MessageStatus\x12\x14\n\x0crequest_uuid\x182 \x01(\x0c\x12\x0c\n\x04uuid\x183 \x01(\x0c\x122\n\x05flags\x184 \x01(\x0e2#.tesla.proto.energy_device.v1.FlagsB\t\n\x07payload"\x15\n\x04Tail\x12\r\n\x05value\x18\x01 \x01(\x05"{\n\x07Message\x12>\n\x07message\x18\x01 \x01(\x0b2-.tesla.proto.energy_device.v1.RoutableMessage\x120\n\x04tail\x18\x02 \x01(\x0b2".tesla.proto.energy_device.v1.Tail*\x9f\x01\n\x06Domain\x12\x14\n\x10DOMAIN_BROADCAST\x10\x00\x12\x1b\n\x17DOMAIN_VEHICLE_SECURITY\x10\x02\x12\x17\n\x13DOMAIN_INFOTAINMENT\x10\x03\x12\x10\n\x0cDOMAIN_AUTHD\x10\x05\x12\x18\n\x14DOMAIN_ENERGY_DEVICE\x10\x07\x12\x1d\n\x19DOMAIN_ENERGY_DEVICE_AUTH\x10\x08*\xd3\x02\n\rSignatureType\x12\x1a\n\x16SIGNATURE_TYPE_AES_GCM\x10\x00\x12\x18\n\x14SIGNATURE_TYPE_ECDSA\x10\x01\x12\x1e\n\x1aSIGNATURE_TYPE_PRESENT_KEY\x10\x02\x12 \n\x1cSIGNATURE_TYPE_AES_GCM_TOKEN\x10\x03\x12%\n!SIGNATURE_TYPE_ECDSA_PERSONALIZED\x10\x04\x12\'\n#SIGNATURE_TYPE_AES_GCM_PERSONALIZED\x10\x05\x12\x17\n\x13SIGNATURE_TYPE_HMAC\x10\x06\x12\x16\n\x12SIGNATURE_TYPE_RSA\x10\x07\x12$\n SIGNATURE_TYPE_HMAC_PERSONALIZED\x10\x08\x12#\n\x1fSIGNATURE_TYPE_AES_GCM_RESPONSE\x10\t*\xcf\x01\n\x03Tag\x12\x16\n\x12TAG_SIGNATURE_TYPE\x10\x00\x12\x0e\n\nTAG_DOMAIN\x10\x01\x12\x17\n\x13TAG_PERSONALIZATION\x10\x02\x12\r\n\tTAG_EPOCH\x10\x03\x12\x12\n\x0eTAG_EXPIRES_AT\x10\x04\x12\x0f\n\x0bTAG_COUNTER\x10\x05\x12\x11\n\rTAG_CHALLENGE\x10\x06\x12\r\n\tTAG_FLAGS\x10\x07\x12\x14\n\x10TAG_REQUEST_HASH\x10\x08\x12\r\n\tTAG_FAULT\x10\t\x12\x0c\n\x07TAG_END\x10\xff\x01*\x17\n\x05Flags\x12\x0e\n\nFLAGS_NONE\x10\x00*\xc9\x07\n\x0eMessageFault_E\x12\x1b\n\x17MESSAGEFAULT_ERROR_NONE\x10\x00\x12\x1b\n\x17MESSAGEFAULT_ERROR_BUSY\x10\x01\x12\x1e\n\x1aMESSAGEFAULT_ERROR_TIMEOUT\x10\x02\x12%\n!MESSAGEFAULT_ERROR_UNKNOWN_KEY_ID\x10\x03\x12#\n\x1fMESSAGEFAULT_ERROR_INACTIVE_KEY\x10\x04\x12(\n$MESSAGEFAULT_ERROR_INVALID_SIGNATURE\x10\x05\x12/\n+MESSAGEFAULT_ERROR_INVALID_TOKEN_OR_COUNTER\x10\x06\x12.\n*MESSAGEFAULT_ERROR_INSUFFICIENT_PRIVILEGES\x10\x07\x12&\n"MESSAGEFAULT_ERROR_INVALID_DOMAINS\x10\x08\x12&\n"MESSAGEFAULT_ERROR_INVALID_COMMAND\x10\t\x12\x1f\n\x1bMESSAGEFAULT_ERROR_DECODING\x10\n\x12\x1f\n\x1bMESSAGEFAULT_ERROR_INTERNAL\x10\x0b\x12,\n(MESSAGEFAULT_ERROR_WRONG_PERSONALIZATION\x10\x0c\x12$\n MESSAGEFAULT_ERROR_BAD_PARAMETER\x10\r\x12\'\n#MESSAGEFAULT_ERROR_KEYCHAIN_IS_FULL\x10\x0e\x12&\n"MESSAGEFAULT_ERROR_INCORRECT_EPOCH\x10\x0f\x12*\n&MESSAGEFAULT_ERROR_IV_INCORRECT_LENGTH\x10\x10\x12#\n\x1fMESSAGEFAULT_ERROR_TIME_EXPIRED\x10\x11\x124\n0MESSAGEFAULT_ERROR_NOT_PROVISIONED_WITH_IDENTITY\x10\x12\x12.\n*MESSAGEFAULT_ERROR_COULD_NOT_HASH_METADATA\x10\x13\x12,\n(MESSAGEFAULT_ERROR_TIME_TO_LIVE_TOO_LONG\x10\x14\x12-\n)MESSAGEFAULT_ERROR_REMOTE_ACCESS_DISABLED\x10\x15\x12;\n7MESSAGEFAULT_ERROR_REMOTE_SERVICE_REQUEST_NOT_SUPPORTED\x10\x16B\x81\x01\n$com.tesla.generated.energy_device.v1B\rSignedMessageZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'signed_message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\rSignedMessageZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_DOMAIN']._serialized_start = 1140
    _globals['_DOMAIN']._serialized_end = 1299
    _globals['_SIGNATURETYPE']._serialized_start = 1302
    _globals['_SIGNATURETYPE']._serialized_end = 1641
    _globals['_TAG']._serialized_start = 1644
    _globals['_TAG']._serialized_end = 1851
    _globals['_FLAGS']._serialized_start = 1853
    _globals['_FLAGS']._serialized_end = 1876
    _globals['_MESSAGEFAULT_E']._serialized_start = 1879
    _globals['_MESSAGEFAULT_E']._serialized_end = 2848
    _globals['_DESTINATION']._serialized_start = 54
    _globals['_DESTINATION']._serialized_end = 169
    _globals['_KEYIDENTITY']._serialized_start = 171
    _globals['_KEYIDENTITY']._serialized_end = 241
    _globals['_RSASIGNATUREDATA']._serialized_start = 243
    _globals['_RSASIGNATUREDATA']._serialized_end = 300
    _globals['_SIGNATUREDATA']._serialized_start = 303
    _globals['_SIGNATUREDATA']._serialized_end = 466
    _globals['_MESSAGESTATUS']._serialized_start = 468
    _globals['_MESSAGESTATUS']._serialized_end = 552
    _globals['_ROUTABLEMESSAGE']._serialized_start = 555
    _globals['_ROUTABLEMESSAGE']._serialized_end = 989
    _globals['_TAIL']._serialized_start = 991
    _globals['_TAIL']._serialized_end = 1012
    _globals['_MESSAGE']._serialized_start = 1014
    _globals['_MESSAGE']._serialized_end = 1137