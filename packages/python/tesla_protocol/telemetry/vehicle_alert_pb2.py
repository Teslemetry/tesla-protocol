"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'vehicle_alert.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13vehicle_alert.proto\x12\x18telemetry.vehicle_alerts\x1a\x1fgoogle/protobuf/timestamp.proto"\x84\x01\n\rVehicleAlerts\x126\n\x06alerts\x18\x01 \x03(\x0b2&.telemetry.vehicle_alerts.VehicleAlert\x12.\n\ncreated_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0b\n\x03vin\x18\x03 \x01(\t"\xb1\x01\n\x0cVehicleAlert\x12\x0c\n\x04name\x18\x01 \x01(\t\x125\n\taudiences\x18\x02 \x03(\x0e2".telemetry.vehicle_alerts.Audience\x12.\n\nstarted_at\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08ended_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp*B\n\x08Audience\x12\x0b\n\x07Unknown\x10\x00\x12\x0c\n\x08Customer\x10\x01\x12\x0b\n\x07Service\x10\x02\x12\x0e\n\nServiceFix\x10\x03B/Z-github.com/teslamotors/fleet-telemetry/protosb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vehicle_alert_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/teslamotors/fleet-telemetry/protos'
    _globals['_AUDIENCE']._serialized_start = 397
    _globals['_AUDIENCE']._serialized_end = 463
    _globals['_VEHICLEALERTS']._serialized_start = 83
    _globals['_VEHICLEALERTS']._serialized_end = 215
    _globals['_VEHICLEALERT']._serialized_start = 218
    _globals['_VEHICLEALERT']._serialized_end = 395