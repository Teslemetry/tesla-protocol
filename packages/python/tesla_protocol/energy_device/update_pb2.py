"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'update.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cupdate.proto\x12\x1ctesla.proto.energy_device.v1"3\n\x0fFirmwareVersion\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0f\n\x07githash\x18\x02 \x01(\x0c"\xa8\x01\n\x13ServerStagedPackage\x12\x14\n\x0cdownload_url\x18\x01 \x01(\t\x12\x12\n\npackage_id\x18\x02 \x01(\x04\x12\x19\n\x11package_signature\x18\x03 \x01(\x0c\x12L\n\x15server_staged_version\x18\x04 \x01(\x0b2-.tesla.proto.energy_device.v1.FirmwareVersion"\xed\x02\n\x0cSystemUpdate\x12\x18\n\x10handshake_result\x18\x01 \x01(\x05\x12\x15\n\rupdate_status\x18\x02 \x01(\x05\x12L\n\x15server_staged_version\x18\x03 \x01(\x0b2-.tesla.proto.energy_device.v1.FirmwareVersion\x12\x13\n\x0btotal_bytes\x18\x04 \x01(\x04\x12\x14\n\x0cbytes_offset\x18\x05 \x01(\x04\x12"\n\x1aestimated_bytes_per_second\x18\x06 \x01(\x04\x12 \n\x18last_handshake_timestamp\x18\x07 \x01(\x04\x12\x1a\n\x12last_update_result\x18\x08 \x01(\x05\x12Q\n\x16server_staged_packages\x18\t \x03(\x0b21.tesla.proto.energy_device.v1.ServerStagedPackage"Y\n\x0fAcceptedPackage\x12\x12\n\npackage_id\x18\x01 \x01(\x04\x12\x19\n\x11package_signature\x18\x02 \x01(\x0c\x12\x17\n\x0fupload_endpoint\x18\x03 \x01(\t"a\n\x17LocallyAvailablePackage\x12\x12\n\npackage_id\x18\x01 \x01(\x04\x12\x19\n\x11package_signature\x18\x02 \x01(\x0c\x12\x17\n\x0ffile_size_bytes\x18\x03 \x01(\x04*\x98\x01\n\x0cUpdateStatus\x12\x19\n\x15UPDATE_STATUS_INVALID\x10\x00\x12\x16\n\x12UPDATE_STATUS_IDLE\x10\x01\x12\x1d\n\x19UPDATE_STATUS_DOWNLOADING\x10\x02\x12\x1c\n\x18UPDATE_STATUS_DOWNLOADED\x10\x03\x12\x18\n\x14UPDATE_STATUS_STAGED\x10\x04*\xdd\x01\n\x15UpdateHandshakeResult\x12#\n\x1fUPDATE_HANDSHAKE_RESULT_INVALID\x10\x00\x12$\n UPDATE_HANDSHAKE_RESULT_UNDERWAY\x10\x01\x12"\n\x1eUPDATE_HANDSHAKE_RESULT_FAILED\x10\x02\x12*\n&UPDATE_HANDSHAKE_RESULT_NON_ACTIONABLE\x10\x03\x12)\n%UPDATE_HANDSHAKE_RESULT_UPDATE_STAGED\x10\x04*s\n\x10LastUpdateResult\x12\x1e\n\x1aLAST_UPDATE_RESULT_INVALID\x10\x00\x12\x1d\n\x19LAST_UPDATE_RESULT_FAILED\x10\x01\x12 \n\x1cLAST_UPDATE_RESULT_SUCCEEDED\x10\x02Bz\n$com.tesla.generated.energy_device.v1B\x06UpdateZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'update_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x06UpdateZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_UPDATESTATUS']._serialized_start = 829
    _globals['_UPDATESTATUS']._serialized_end = 981
    _globals['_UPDATEHANDSHAKERESULT']._serialized_start = 984
    _globals['_UPDATEHANDSHAKERESULT']._serialized_end = 1205
    _globals['_LASTUPDATERESULT']._serialized_start = 1207
    _globals['_LASTUPDATERESULT']._serialized_end = 1322
    _globals['_FIRMWAREVERSION']._serialized_start = 46
    _globals['_FIRMWAREVERSION']._serialized_end = 97
    _globals['_SERVERSTAGEDPACKAGE']._serialized_start = 100
    _globals['_SERVERSTAGEDPACKAGE']._serialized_end = 268
    _globals['_SYSTEMUPDATE']._serialized_start = 271
    _globals['_SYSTEMUPDATE']._serialized_end = 636
    _globals['_ACCEPTEDPACKAGE']._serialized_start = 638
    _globals['_ACCEPTEDPACKAGE']._serialized_end = 727
    _globals['_LOCALLYAVAILABLEPACKAGE']._serialized_start = 729
    _globals['_LOCALLYAVAILABLEPACKAGE']._serialized_end = 826