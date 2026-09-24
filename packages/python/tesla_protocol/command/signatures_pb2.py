"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 5, '', 'signatures.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10signatures.proto\x12\nSignatures"\x81\x01\n\x0bKeyIdentity\x12\x14\n\npublic_key\x18\x01 \x01(\x0cH\x00\x12\x10\n\x06handle\x18\x03 \x01(\rH\x00\x123\n\x0eidentified_key\x18\x04 \x01(\x0e2\x19.Signatures.IdentifiedKeyH\x00B\x0f\n\ridentity_typeJ\x04\x08\x02\x10\x03"u\n#AES_GCM_Personalized_Signature_Data\x12\r\n\x05epoch\x18\x01 \x01(\x0c\x12\r\n\x05nonce\x18\x02 \x01(\x0c\x12\x0f\n\x07counter\x18\x03 \x01(\r\x12\x12\n\nexpires_at\x18\x04 \x01(\x07\x12\x0b\n\x03tag\x18\x05 \x01(\x0c"N\n\x1fAES_GCM_Response_Signature_Data\x12\r\n\x05nonce\x18\x01 \x01(\x0c\x12\x0f\n\x07counter\x18\x02 \x01(\r\x12\x0b\n\x03tag\x18\x03 \x01(\x0c"0\n\x1aPresent_Key_Signature_Data\x12\x12\n\nauth_token\x18\x01 \x01(\x0c"q\n\x1fAES_GCM_Detached_Signature_Data\x12\r\n\x05epoch\x18\x01 \x01(\x0c\x12\x0f\n\x07counter\x18\x02 \x01(\r\x12\x12\n\nexpires_at\x18\x03 \x01(\x07\x12\r\n\x05nonce\x18\x04 \x01(\x0c\x12\x0b\n\x03tag\x18\x05 \x01(\x0c"T\n Certificate_ECDSA_Signature_Data\x12\x1d\n\x15certificate_chain_der\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c""\n\x13HMAC_Signature_Data\x12\x0b\n\x03tag\x18\x01 \x01(\x0c"c\n HMAC_Personalized_Signature_Data\x12\r\n\x05epoch\x18\x01 \x01(\x0c\x12\x0f\n\x07counter\x18\x02 \x01(\r\x12\x12\n\nexpires_at\x18\x03 \x01(\x07\x12\x0b\n\x03tag\x18\x04 \x01(\x0c"\xe6\x04\n\rSignatureData\x120\n\x0fsigner_identity\x18\x01 \x01(\x0b2\x17.Signatures.KeyIdentity\x12B\n\x10Present_Key_data\x18\x02 \x01(\x0b2&.Signatures.Present_Key_Signature_DataH\x00\x12T\n\x19AES_GCM_Personalized_data\x18\x05 \x01(\x0b2/.Signatures.AES_GCM_Personalized_Signature_DataH\x00\x12;\n\x10session_info_tag\x18\x06 \x01(\x0b2\x1f.Signatures.HMAC_Signature_DataH\x00\x12N\n\x16HMAC_Personalized_data\x18\x08 \x01(\x0b2,.Signatures.HMAC_Personalized_Signature_DataH\x00\x12L\n\x15AES_GCM_Response_data\x18\t \x01(\x0b2+.Signatures.AES_GCM_Response_Signature_DataH\x00\x12L\n\x15AES_GCM_Detached_data\x18\n \x01(\x0b2+.Signatures.AES_GCM_Detached_Signature_DataH\x00\x12N\n\x16Certificate_ECDSA_data\x18\x0b \x01(\x0b2,.Signatures.Certificate_ECDSA_Signature_DataH\x00B\n\n\x08sig_typeJ\x04\x08\x07\x10\x08"F\n\x15GetSessionInfoRequest\x12-\n\x0ckey_identity\x18\x01 \x01(\x0b2\x17.Signatures.KeyIdentity"\xa6\x01\n\x0bSessionInfo\x12\x0f\n\x07counter\x18\x01 \x01(\r\x12\x11\n\tpublicKey\x18\x02 \x01(\x0c\x12\r\n\x05epoch\x18\x03 \x01(\x0c\x12\x12\n\nclock_time\x18\x04 \x01(\x07\x12/\n\x06status\x18\x05 \x01(\x0e2\x1f.Signatures.Session_Info_Status\x12\x0e\n\x06handle\x18\x06 \x01(\r\x12\x0f\n\x07field_7\x18\x07 \x01(\r*\xe7\x01\n\x03Tag\x12\x16\n\x12TAG_SIGNATURE_TYPE\x10\x00\x12\x0e\n\nTAG_DOMAIN\x10\x01\x12\x17\n\x13TAG_PERSONALIZATION\x10\x02\x12\r\n\tTAG_EPOCH\x10\x03\x12\x12\n\x0eTAG_EXPIRES_AT\x10\x04\x12\x0f\n\x0bTAG_COUNTER\x10\x05\x12\x11\n\rTAG_CHALLENGE\x10\x06\x12\r\n\tTAG_FLAGS\x10\x07\x12\x14\n\x10TAG_REQUEST_HASH\x10\x08\x12\r\n\tTAG_FAULT\x10\t\x12\x16\n\x12TAG_COMMAND_PREFIX\x10\n\x12\x0c\n\x07TAG_END\x10\xff\x01*\x8c\x03\n\rSignatureType\x12\x1a\n\x16SIGNATURE_TYPE_AES_GCM\x10\x00\x12\x18\n\x14SIGNATURE_TYPE_ECDSA\x10\x01\x12\x1e\n\x1aSIGNATURE_TYPE_PRESENT_KEY\x10\x02\x12 \n\x1cSIGNATURE_TYPE_AES_GCM_TOKEN\x10\x03\x12%\n!SIGNATURE_TYPE_ECDSA_PERSONALIZED\x10\x04\x12\'\n#SIGNATURE_TYPE_AES_GCM_PERSONALIZED\x10\x05\x12\x17\n\x13SIGNATURE_TYPE_HMAC\x10\x06\x12$\n SIGNATURE_TYPE_HMAC_PERSONALIZED\x10\x08\x12#\n\x1fSIGNATURE_TYPE_AES_GCM_RESPONSE\x10\t\x12#\n\x1fSIGNATURE_TYPE_AES_GCM_DETACHED\x10\n\x12$\n SIGNATURE_TYPE_CERTIFICATE_ECDSA\x10\x0b"\x04\x08\x07\x10\x07*F\n\rIdentifiedKey\x12\x19\n\x15IDENTIFIEDKEY_UNKNOWN\x10\x00\x12\x1a\n\x16IDENTIFIEDKEY_ROOT_KEY\x10\x01*\x87\x01\n\x13Session_Info_Status\x12\x1a\n\x16SESSION_INFO_STATUS_OK\x10\x00\x12,\n(SESSION_INFO_STATUS_KEY_NOT_ON_WHITELIST\x10\x01\x12&\n"SESSION_INFO_STATUS_INVALID_HANDLE\x10\x02Bi\n\x1ecom.tesla.generated.signaturesZGgithub.com/teslamotors/vehicle-command/pkg/protocol/protobuf/signaturesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'signatures_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.tesla.generated.signaturesZGgithub.com/teslamotors/vehicle-command/pkg/protocol/protobuf/signatures'
    _globals['_TAG']._serialized_start = 1610
    _globals['_TAG']._serialized_end = 1841
    _globals['_SIGNATURETYPE']._serialized_start = 1844
    _globals['_SIGNATURETYPE']._serialized_end = 2240
    _globals['_IDENTIFIEDKEY']._serialized_start = 2242
    _globals['_IDENTIFIEDKEY']._serialized_end = 2312
    _globals['_SESSION_INFO_STATUS']._serialized_start = 2315
    _globals['_SESSION_INFO_STATUS']._serialized_end = 2450
    _globals['_KEYIDENTITY']._serialized_start = 33
    _globals['_KEYIDENTITY']._serialized_end = 162
    _globals['_AES_GCM_PERSONALIZED_SIGNATURE_DATA']._serialized_start = 164
    _globals['_AES_GCM_PERSONALIZED_SIGNATURE_DATA']._serialized_end = 281
    _globals['_AES_GCM_RESPONSE_SIGNATURE_DATA']._serialized_start = 283
    _globals['_AES_GCM_RESPONSE_SIGNATURE_DATA']._serialized_end = 361
    _globals['_PRESENT_KEY_SIGNATURE_DATA']._serialized_start = 363
    _globals['_PRESENT_KEY_SIGNATURE_DATA']._serialized_end = 411
    _globals['_AES_GCM_DETACHED_SIGNATURE_DATA']._serialized_start = 413
    _globals['_AES_GCM_DETACHED_SIGNATURE_DATA']._serialized_end = 526
    _globals['_CERTIFICATE_ECDSA_SIGNATURE_DATA']._serialized_start = 528
    _globals['_CERTIFICATE_ECDSA_SIGNATURE_DATA']._serialized_end = 612
    _globals['_HMAC_SIGNATURE_DATA']._serialized_start = 614
    _globals['_HMAC_SIGNATURE_DATA']._serialized_end = 648
    _globals['_HMAC_PERSONALIZED_SIGNATURE_DATA']._serialized_start = 650
    _globals['_HMAC_PERSONALIZED_SIGNATURE_DATA']._serialized_end = 749
    _globals['_SIGNATUREDATA']._serialized_start = 752
    _globals['_SIGNATUREDATA']._serialized_end = 1366
    _globals['_GETSESSIONINFOREQUEST']._serialized_start = 1368
    _globals['_GETSESSIONINFOREQUEST']._serialized_end = 1438
    _globals['_SESSIONINFO']._serialized_start = 1441
    _globals['_SESSIONINFO']._serialized_end = 1607