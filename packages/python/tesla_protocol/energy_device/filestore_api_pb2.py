"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 5, '', 'filestore_api.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13filestore_api.proto\x12\x1ctesla.proto.energy_device.v1".\n\x10FileStoreAPIFile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04blob\x18d \x01(\x0c"\xa3\x01\n!FileStoreAPIForceWriteFileRequest\x12@\n\x06domain\x18\x01 \x01(\x0e20.tesla.proto.energy_device.v1.FileStoreAPIDomain\x12<\n\x04file\x18\x02 \x01(\x0b2..tesla.proto.energy_device.v1.FileStoreAPIFile"2\n"FileStoreAPIForceWriteFileResponse\x12\x0c\n\x04hash\x18\x01 \x01(\x0c"\xad\x01\n\x1dFileStoreAPIUpdateFileRequest\x12@\n\x06domain\x18\x01 \x01(\x0e20.tesla.proto.energy_device.v1.FileStoreAPIDomain\x12<\n\x04file\x18\x02 \x01(\x0b2..tesla.proto.energy_device.v1.FileStoreAPIFile\x12\x0c\n\x04hash\x18\x03 \x01(\x0c"l\n\x1eFileStoreAPIUpdateFileResponse\x12<\n\x04file\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.FileStoreAPIFile\x12\x0c\n\x04hash\x18\x02 \x01(\x0c"\x88\x01\n\x1bFileStoreAPIReadFileRequest\x12@\n\x06domain\x18\x01 \x01(\x0e20.tesla.proto.energy_device.v1.FileStoreAPIDomain\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11if_different_hash\x18\x03 \x01(\x0c"j\n\x1cFileStoreAPIReadFileResponse\x12<\n\x04file\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.FileStoreAPIFile\x12\x0c\n\x04hash\x18\x02 \x01(\x0c"\xd6\x04\n\x11FileStoreMessages\x12V\n\x11read_file_request\x18\x01 \x01(\x0b29.tesla.proto.energy_device.v1.FileStoreAPIReadFileRequestH\x00\x12X\n\x12read_file_response\x18\x02 \x01(\x0b2:.tesla.proto.energy_device.v1.FileStoreAPIReadFileResponseH\x00\x12c\n\x18force_write_file_request\x18\x03 \x01(\x0b2?.tesla.proto.energy_device.v1.FileStoreAPIForceWriteFileRequestH\x00\x12e\n\x19force_write_file_response\x18\x04 \x01(\x0b2@.tesla.proto.energy_device.v1.FileStoreAPIForceWriteFileResponseH\x00\x12Z\n\x13update_file_request\x18\x05 \x01(\x0b2;.tesla.proto.energy_device.v1.FileStoreAPIUpdateFileRequestH\x00\x12\\\n\x14update_file_response\x18\x06 \x01(\x0b2<.tesla.proto.energy_device.v1.FileStoreAPIUpdateFileResponseH\x00B\t\n\x07message*\xa6\x03\n\x12FileStoreAPIDomain\x12!\n\x1dFILE_STORE_API_DOMAIN_INVALID\x10\x00\x12%\n!FILE_STORE_API_DOMAIN_CONFIG_JSON\x10\x01\x12/\n+FILE_STORE_API_DOMAIN_GRID_CODE_REGIONS_CSV\x10\x02\x122\n.FILE_STORE_API_DOMAIN_CERTIFIED_INSTALLERS_CSV\x10\x03\x12,\n(FILE_STORE_API_DOMAIN_SUPERCHARGER_FILES\x10\x04\x12*\n&FILE_STORE_API_DOMAIN_OPTICASTER_FILES\x10\x05\x12(\n$FILE_STORE_API_DOMAIN_WALLBOX_CONFIG\x10\x06\x12+\n\'FILE_STORE_API_DOMAIN_OCPP_CSMS_ROOT_CA\x10\x07\x120\n,FILE_STORE_API_DOMAIN_OPTIMUS_CHARGER_CONFIG\x10\tB\x80\x01\n$com.tesla.generated.energy_device.v1B\x0cFileStoreApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'filestore_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x0cFileStoreApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_FILESTOREAPIDOMAIN']._serialized_start = 1454
    _globals['_FILESTOREAPIDOMAIN']._serialized_end = 1876
    _globals['_FILESTOREAPIFILE']._serialized_start = 53
    _globals['_FILESTOREAPIFILE']._serialized_end = 99
    _globals['_FILESTOREAPIFORCEWRITEFILEREQUEST']._serialized_start = 102
    _globals['_FILESTOREAPIFORCEWRITEFILEREQUEST']._serialized_end = 265
    _globals['_FILESTOREAPIFORCEWRITEFILERESPONSE']._serialized_start = 267
    _globals['_FILESTOREAPIFORCEWRITEFILERESPONSE']._serialized_end = 317
    _globals['_FILESTOREAPIUPDATEFILEREQUEST']._serialized_start = 320
    _globals['_FILESTOREAPIUPDATEFILEREQUEST']._serialized_end = 493
    _globals['_FILESTOREAPIUPDATEFILERESPONSE']._serialized_start = 495
    _globals['_FILESTOREAPIUPDATEFILERESPONSE']._serialized_end = 603
    _globals['_FILESTOREAPIREADFILEREQUEST']._serialized_start = 606
    _globals['_FILESTOREAPIREADFILEREQUEST']._serialized_end = 742
    _globals['_FILESTOREAPIREADFILERESPONSE']._serialized_start = 744
    _globals['_FILESTOREAPIREADFILERESPONSE']._serialized_end = 850
    _globals['_FILESTOREMESSAGES']._serialized_start = 853
    _globals['_FILESTOREMESSAGES']._serialized_end = 1451