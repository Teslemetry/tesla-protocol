"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'session.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsession.proto\x12\x07Session\x1a\x1fgoogle/protobuf/timestamp.proto"x\n\x0cSessionStore\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\r\n\x05epoch\x18\x02 \x01(\x0c\x12\r\n\x05delta\x18\x03 \x01(\r\x12-\n\x04lock\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x88\x01\x01B\x07\n\x05_lockb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_SESSIONSTORE']._serialized_start = 59
    _globals['_SESSIONSTORE']._serialized_end = 179