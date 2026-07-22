"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'identifier_type.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15identifier_type.proto\x12\x1dtesla.proto.energy.command.v1*\xbd\x01\n\x0eIdentifierType\x12\x1b\n\x17IDENTIFIER_TYPE_INVALID\x10\x00\x12\x1f\n\x1bIDENTIFIER_TYPE_GATEWAY_DIN\x10\x01\x12\x1d\n\x19IDENTIFIER_TYPE_SITE_UUID\x10\x02\x12&\n"IDENTIFIER_TYPE_SOLAR_INVERTER_DIN\x10\x03\x12&\n"IDENTIFIER_TYPE_WALL_CONNECTOR_DIN\x10\x04B\x85\x01\n%com.tesla.generated.energy.command.v1B\x0eIdentifierTypeZLgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energy/command/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'identifier_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.tesla.generated.energy.command.v1B\x0eIdentifierTypeZLgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energy/command/v1'
    _globals['_IDENTIFIERTYPE']._serialized_start = 57
    _globals['_IDENTIFIERTYPE']._serialized_end = 246