"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'teg_api.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rteg_api.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x1fgoogle/protobuf/timestamp.proto"x\n\x1aControlEventSchedulingInfo\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x18\n\x10duration_seconds\x18\x02 \x01(\r\x12\x10\n\x08priority\x18\x03 \x01(\x04"y\n\x0bBackupEvent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12P\n\x0esheduling_info\x18\x03 \x01(\x0b28.tesla.proto.energy_device.v1.ControlEventSchedulingInfo"f\n\x11ManualBackupEvent\x12Q\n\x0fscheduling_info\x18\x01 \x01(\x0b28.tesla.proto.energy_device.v1.ControlEventSchedulingInfo"{\n&TEGAPIScheduleManualBackupEventRequest\x12Q\n\x0fscheduling_info\x18\x01 \x01(\x0b28.tesla.proto.energy_device.v1.ControlEventSchedulingInfo")\n\'TEGAPIScheduleManualBackupEventResponse"&\n$TEGAPICancelManualBackupEventRequest"\'\n%TEGAPICancelManualBackupEventResponse"\x1e\n\x1cTEGAPIGetBackupEventsRequest"\xaf\x01\n\x1dTEGAPIGetBackupEventsResponse\x12L\n\x13manual_backup_event\x18\x01 \x01(\x0b2/.tesla.proto.energy_device.v1.ManualBackupEvent\x12@\n\rbackup_events\x18\x02 \x03(\x0b2).tesla.proto.energy_device.v1.BackupEvent"\x17\n\x15TEGAPIRegisterRequest"\x18\n\x16TEGAPIRegisterResponse"\xb0\x05\n\x0bTEGMessages\x12t\n$schedule_manual_backup_event_request\x18- \x01(\x0b2D.tesla.proto.energy_device.v1.TEGAPIScheduleManualBackupEventRequestH\x00\x12v\n%schedule_manual_backup_event_response\x18. \x01(\x0b2E.tesla.proto.energy_device.v1.TEGAPIScheduleManualBackupEventResponseH\x00\x12p\n"cancel_manual_backup_event_request\x18/ \x01(\x0b2B.tesla.proto.energy_device.v1.TEGAPICancelManualBackupEventRequestH\x00\x12r\n#cancel_manual_backup_event_response\x180 \x01(\x0b2C.tesla.proto.energy_device.v1.TEGAPICancelManualBackupEventResponseH\x00\x12_\n\x19get_backup_events_request\x181 \x01(\x0b2:.tesla.proto.energy_device.v1.TEGAPIGetBackupEventsRequestH\x00\x12a\n\x1aget_backup_events_response\x182 \x01(\x0b2;.tesla.proto.energy_device.v1.TEGAPIGetBackupEventsResponseH\x00B\t\n\x07messageBz\n$com.tesla.generated.energy_device.v1B\x06TegApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'teg_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x06TegApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_CONTROLEVENTSCHEDULINGINFO']._serialized_start = 80
    _globals['_CONTROLEVENTSCHEDULINGINFO']._serialized_end = 200
    _globals['_BACKUPEVENT']._serialized_start = 202
    _globals['_BACKUPEVENT']._serialized_end = 323
    _globals['_MANUALBACKUPEVENT']._serialized_start = 325
    _globals['_MANUALBACKUPEVENT']._serialized_end = 427
    _globals['_TEGAPISCHEDULEMANUALBACKUPEVENTREQUEST']._serialized_start = 429
    _globals['_TEGAPISCHEDULEMANUALBACKUPEVENTREQUEST']._serialized_end = 552
    _globals['_TEGAPISCHEDULEMANUALBACKUPEVENTRESPONSE']._serialized_start = 554
    _globals['_TEGAPISCHEDULEMANUALBACKUPEVENTRESPONSE']._serialized_end = 595
    _globals['_TEGAPICANCELMANUALBACKUPEVENTREQUEST']._serialized_start = 597
    _globals['_TEGAPICANCELMANUALBACKUPEVENTREQUEST']._serialized_end = 635
    _globals['_TEGAPICANCELMANUALBACKUPEVENTRESPONSE']._serialized_start = 637
    _globals['_TEGAPICANCELMANUALBACKUPEVENTRESPONSE']._serialized_end = 676
    _globals['_TEGAPIGETBACKUPEVENTSREQUEST']._serialized_start = 678
    _globals['_TEGAPIGETBACKUPEVENTSREQUEST']._serialized_end = 708
    _globals['_TEGAPIGETBACKUPEVENTSRESPONSE']._serialized_start = 711
    _globals['_TEGAPIGETBACKUPEVENTSRESPONSE']._serialized_end = 886
    _globals['_TEGAPIREGISTERREQUEST']._serialized_start = 888
    _globals['_TEGAPIREGISTERREQUEST']._serialized_end = 911
    _globals['_TEGAPIREGISTERRESPONSE']._serialized_start = 913
    _globals['_TEGAPIREGISTERRESPONSE']._serialized_end = 937
    _globals['_TEGMESSAGES']._serialized_start = 940
    _globals['_TEGMESSAGES']._serialized_end = 1628