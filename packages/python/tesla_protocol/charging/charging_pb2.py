"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'charging.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0echarging.proto\x12\x1bcom.tesla.proto.charging.v1"6\n\x06Energy\x12\x12\n\nwatt_hours\x18\x01 \x01(\r\x12\x18\n\x10milli_watt_hours\x18\x02 \x01(\r"\\\n\x08StemInfo\x12\x12\n\nfw_githash\x18\x01 \x01(\x0c\x12\x15\n\rserial_number\x18\x02 \x01(\t\x12\x13\n\x0bpart_number\x18\x03 \x01(\t\x12\x10\n\x08meter_id\x18\x04 \x01(\t"W\n\rStemEventInfo\x12\x16\n\x0eevent_occurred\x18\x01 \x01(\x08\x12\x13\n\x0binvalidated\x18\x02 \x01(\x08\x12\x19\n\x11time_synchronized\x18\x03 \x01(\x08"\xd1\x02\n\x17ChargeSessionTimeSeries\x12\x1a\n\x12start_time_epoch_s\x18\x01 \x01(\x04\x12\x18\n\x10end_time_epoch_s\x18\x02 \x01(\x04\x12\x1e\n\x16total_energy_vended_wh\x18\x03 \x01(\r\x12\x19\n\x11bucket_duration_s\x18\x04 \x01(\r\x12\x1f\n\x17first_bucket_duration_s\x18\x05 \x01(\r\x12\x1f\n\x17bucket_energy_vended_wh\x18\x06 \x03(\r\x12@\n\x13total_energy_vended\x18\x07 \x01(\x0b2#.com.tesla.proto.charging.v1.Energy\x12A\n\x14bucket_energy_vended\x18\x08 \x03(\x0b2#.com.tesla.proto.charging.v1.Energy"\x85\x02\n\x06StemUi\x128\n\tstem_info\x18\x01 \x01(\x0b2%.com.tesla.proto.charging.v1.StemInfo\x12\x12\n\nsession_id\x18\x02 \x01(\r\x12\x1b\n\x13system_time_epoch_s\x18\x03 \x01(\x04\x12\x13\n\x0bidle_time_s\x18\x04 \x01(\r\x12\x1a\n\x12start_time_epoch_s\x18\x05 \x01(\x04\x12C\n\x0fstem_event_info\x18\x06 \x01(\x0b2*.com.tesla.proto.charging.v1.StemEventInfo\x12\x1a\n\x12session_energy_kwh\x18\x07 \x01(\x02"\xd3\x02\n\x0bStemBilling\x128\n\tstem_info\x18\x01 \x01(\x0b2%.com.tesla.proto.charging.v1.StemInfo\x12\x12\n\nsession_id\x18\x02 \x01(\r\x12C\n\x0fstem_event_info\x18\x03 \x01(\x0b2*.com.tesla.proto.charging.v1.StemEventInfo\x12!\n\x19lifetime_energy_start_kwh\x18\x04 \x01(\x02\x12\x1f\n\x17lifetime_energy_end_kwh\x18\x05 \x01(\x02\x12\x13\n\x0bidle_time_s\x18\x06 \x01(\r\x12X\n\x1acharge_session_time_series\x18\x07 \x01(\x0b24.com.tesla.proto.charging.v1.ChargeSessionTimeSeriesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'charging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_ENERGY']._serialized_start = 47
    _globals['_ENERGY']._serialized_end = 101
    _globals['_STEMINFO']._serialized_start = 103
    _globals['_STEMINFO']._serialized_end = 195
    _globals['_STEMEVENTINFO']._serialized_start = 197
    _globals['_STEMEVENTINFO']._serialized_end = 284
    _globals['_CHARGESESSIONTIMESERIES']._serialized_start = 287
    _globals['_CHARGESESSIONTIMESERIES']._serialized_end = 624
    _globals['_STEMUI']._serialized_start = 627
    _globals['_STEMUI']._serialized_end = 888
    _globals['_STEMBILLING']._serialized_start = 891
    _globals['_STEMBILLING']._serialized_end = 1230