"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'dashcam_sei.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11dashcam_sei.proto\x12\nDashcamSei"\xf3\x04\n\x0bSeiMetadata\x12\x0f\n\x07field_1\x18\x01 \x01(\r\x12/\n\tgearState\x18\x02 \x01(\x0e2\x1c.DashcamSei.SeiMetadata.Gear\x12\x12\n\nframeSeqNo\x18\x03 \x01(\x04\x12\x17\n\x0fvehicleSpeedMps\x18\x04 \x01(\x02\x12 \n\x18acceleratorPedalPosition\x18\x05 \x01(\x02\x12\x1a\n\x12steeringWheelAngle\x18\x06 \x01(\x02\x12\x15\n\rblinkerOnLeft\x18\x07 \x01(\x08\x12\x16\n\x0eblinkerOnRight\x18\x08 \x01(\x08\x12\x14\n\x0cbrakeApplied\x18\t \x01(\x08\x12>\n\x0eautopilotState\x18\n \x01(\x0e2&.DashcamSei.SeiMetadata.AutopilotState\x12\x13\n\x0blatitudeDeg\x18\x0b \x01(\x01\x12\x14\n\x0clongitudeDeg\x18\x0c \x01(\x01\x12\x12\n\nheadingDeg\x18\r \x01(\x01\x12\x1f\n\x17linearAccelerationMps2X\x18\x0e \x01(\x01\x12\x1f\n\x17linearAccelerationMps2Y\x18\x0f \x01(\x01\x12\x1f\n\x17linearAccelerationMps2Z\x18\x10 \x01(\x01"I\n\x04Gear\x12\r\n\tGEAR_PARK\x10\x00\x12\x0e\n\nGEAR_DRIVE\x10\x01\x12\x10\n\x0cGEAR_REVERSE\x10\x02\x12\x10\n\x0cGEAR_NEUTRAL\x10\x03"E\n\x0eAutopilotState\x12\x08\n\x04NONE\x10\x00\x12\x10\n\x0cSELF_DRIVING\x10\x01\x12\r\n\tAUTOSTEER\x10\x02\x12\x08\n\x04TACC\x10\x03b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dashcam_sei_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_SEIMETADATA']._serialized_start = 34
    _globals['_SEIMETADATA']._serialized_end = 661
    _globals['_SEIMETADATA_GEAR']._serialized_start = 517
    _globals['_SEIMETADATA_GEAR']._serialized_end = 590
    _globals['_SEIMETADATA_AUTOPILOTSTATE']._serialized_start = 592
    _globals['_SEIMETADATA_AUTOPILOTSTATE']._serialized_end = 661