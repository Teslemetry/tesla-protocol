"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'authorization_types.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19authorization_types.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xad\x04\n\x13AuthorizationRecord\x12@\n\x04type\x18\x01 \x01(\x0e22.tesla.proto.energy_device.v1.AuthorizedClientType\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12A\n\x08key_type\x18\x03 \x01(\x0e2/.tesla.proto.energy_device.v1.AuthorizedKeyType\x12\x12\n\npublic_key\x18\x04 \x01(\x0c\x12>\n\x05roles\x18\x05 \x03(\x0e2/.tesla.proto.energy_device.v1.AuthorizationRole\x12<\n\x05state\x18\x06 \x01(\x0e2-.tesla.proto.energy_device.v1.AuthorizedState\x12N\n\x0cverification\x18\x07 \x01(\x0e28.tesla.proto.energy_device.v1.AuthorizedVerificationType\x12.\n\nadded_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\nidentifier\x18\t \x01(\tH\x00\x88\x01\x01\x12%\n\x18authorized_by_public_key\x18\n \x01(\x0cH\x01\x88\x01\x01B\r\n\x0b_identifierB\x1b\n\x19_authorized_by_public_key*t\n\x11AuthorizationRole\x12\x1e\n\x1aAUTHORIZATION_ROLE_INVALID\x10\x00\x12\x1f\n\x1bAUTHORIZATION_ROLE_CUSTOMER\x10\x01\x12\x1e\n\x1aAUTHORIZATION_ROLE_VEHICLE\x10\x02*\x8e\x01\n\x14AuthorizedClientType\x12"\n\x1eAUTHORIZED_CLIENT_TYPE_INVALID\x10\x00\x12.\n*AUTHORIZED_CLIENT_TYPE_CUSTOMER_MOBILE_APP\x10\x01\x12"\n\x1eAUTHORIZED_CLIENT_TYPE_VEHICLE\x10\x02*n\n\x11AuthorizedKeyType\x12\x1f\n\x1bAUTHORIZED_KEY_TYPE_INVALID\x10\x00\x12\x1b\n\x17AUTHORIZED_KEY_TYPE_RSA\x10\x01\x12\x1b\n\x17AUTHORIZED_KEY_TYPE_ECC\x10\x02*\xca\x01\n\x0fAuthorizedState\x12\x1c\n\x18AUTHORIZED_STATE_INVALID\x10\x00\x12)\n%AUTHORIZED_STATE_PENDING_VERIFICATION\x10\x01\x121\n-AUTHORIZED_STATE_PENDING_VERIFICATION_TIMEOUT\x10\x02\x12\x1d\n\x19AUTHORIZED_STATE_VERIFIED\x10\x03\x12\x1c\n\x18AUTHORIZED_STATE_REMOVED\x10\x04*\xf7\x01\n\x1aAuthorizedVerificationType\x12(\n$AUTHORIZED_VERIFICATION_TYPE_INVALID\x10\x00\x12/\n+AUTHORIZED_VERIFICATION_TYPE_PRESENCE_PROOF\x10\x01\x12$\n AUTHORIZED_VERIFICATION_TYPE_BLE\x10\x02\x12\'\n#AUTHORIZED_VERIFICATION_TYPE_SIGNED\x10\x03\x12/\n+AUTHORIZED_VERIFICATION_TYPE_HERMES_COMMAND\x10\x04B\x86\x01\n$com.tesla.generated.energy_device.v1B\x12AuthorizationTypesZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authorization_types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x12AuthorizationTypesZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_AUTHORIZATIONROLE']._serialized_start = 652
    _globals['_AUTHORIZATIONROLE']._serialized_end = 768
    _globals['_AUTHORIZEDCLIENTTYPE']._serialized_start = 771
    _globals['_AUTHORIZEDCLIENTTYPE']._serialized_end = 913
    _globals['_AUTHORIZEDKEYTYPE']._serialized_start = 915
    _globals['_AUTHORIZEDKEYTYPE']._serialized_end = 1025
    _globals['_AUTHORIZEDSTATE']._serialized_start = 1028
    _globals['_AUTHORIZEDSTATE']._serialized_end = 1230
    _globals['_AUTHORIZEDVERIFICATIONTYPE']._serialized_start = 1233
    _globals['_AUTHORIZEDVERIFICATIONTYPE']._serialized_end = 1480
    _globals['_AUTHORIZATIONRECORD']._serialized_start = 93
    _globals['_AUTHORIZATIONRECORD']._serialized_end = 650