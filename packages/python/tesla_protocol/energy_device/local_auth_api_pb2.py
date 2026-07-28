"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'local_auth_api.proto')
_sym_db = _symbol_database.Default()
from . import networking_pb2 as networking__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14local_auth_api.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x10networking.proto"$\n"LocalAuthAPIRequiredFactorsRequest"I\n#LocalAuthAPIRequiredFactorsResponse\x12\x10\n\x08password\x18\x01 \x01(\x08\x12\x10\n\x08presence\x18\x02 \x01(\x08"|\n\x18LocalAuthAPILoginRequest\x12\x13\n\x0bparticipant\x18\x01 \x01(\x05\x12\r\n\x05email\x18\x02 \x01(\t\x12<\n\x08password\x18\x03 \x01(\x0b2*.tesla.proto.energy_device.v1.WifiPassword"Z\n\x19LocalAuthAPILoginResponse\x12=\n\x06result\x18\x01 \x01(\x0e2-.tesla.proto.energy_device.v1.LocalAuthResult"\x1b\n\x19LocalAuthAPILogoutRequest"\x1c\n\x1aLocalAuthAPILogoutResponse"$\n"LocalAuthAPICheckAuthStatusRequest"d\n#LocalAuthAPICheckAuthStatusResponse\x12=\n\x06result\x18\x01 \x01(\x0e2-.tesla.proto.energy_device.v1.LocalAuthResult"\x88\x06\n\x11LocalAuthMessages\x12d\n\x18required_factors_request\x18\x01 \x01(\x0b2@.tesla.proto.energy_device.v1.LocalAuthAPIRequiredFactorsRequestH\x00\x12f\n\x19required_factors_response\x18\x02 \x01(\x0b2A.tesla.proto.energy_device.v1.LocalAuthAPIRequiredFactorsResponseH\x00\x12O\n\rlogin_request\x18\x03 \x01(\x0b26.tesla.proto.energy_device.v1.LocalAuthAPILoginRequestH\x00\x12Q\n\x0elogin_response\x18\x04 \x01(\x0b27.tesla.proto.energy_device.v1.LocalAuthAPILoginResponseH\x00\x12Q\n\x0elogout_request\x18\x05 \x01(\x0b27.tesla.proto.energy_device.v1.LocalAuthAPILogoutRequestH\x00\x12S\n\x0flogout_response\x18\x06 \x01(\x0b28.tesla.proto.energy_device.v1.LocalAuthAPILogoutResponseH\x00\x12e\n\x19check_auth_status_request\x18\x07 \x01(\x0b2@.tesla.proto.energy_device.v1.LocalAuthAPICheckAuthStatusRequestH\x00\x12g\n\x1acheck_auth_status_response\x18\x08 \x01(\x0b2A.tesla.proto.energy_device.v1.LocalAuthAPICheckAuthStatusResponseH\x00B\t\n\x07message*\x80\x02\n\x0fLocalAuthResult\x12\x1d\n\x19LOCAL_AUTH_RESULT_INVALID\x10\x00\x12\x1d\n\x19LOCAL_AUTH_RESULT_SUCCESS\x10\x01\x12(\n$LOCAL_AUTH_RESULT_INVALID_PARAMETERS\x10\x02\x12&\n"LOCAL_AUTH_RESULT_INVALID_PASSWORD\x10\x03\x12-\n)LOCAL_AUTH_RESULT_PRESENCE_PROOF_REQUIRED\x10\x04\x12.\n*LOCAL_AUTH_RESULT_PRESENCE_PROOF_TIMED_OUT\x10\x05B\x80\x01\n$com.tesla.generated.energy_device.v1B\x0cLocalAuthApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'local_auth_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x0cLocalAuthApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_LOCALAUTHRESULT']._serialized_start = 1382
    _globals['_LOCALAUTHRESULT']._serialized_end = 1638
    _globals['_LOCALAUTHAPIREQUIREDFACTORSREQUEST']._serialized_start = 72
    _globals['_LOCALAUTHAPIREQUIREDFACTORSREQUEST']._serialized_end = 108
    _globals['_LOCALAUTHAPIREQUIREDFACTORSRESPONSE']._serialized_start = 110
    _globals['_LOCALAUTHAPIREQUIREDFACTORSRESPONSE']._serialized_end = 183
    _globals['_LOCALAUTHAPILOGINREQUEST']._serialized_start = 185
    _globals['_LOCALAUTHAPILOGINREQUEST']._serialized_end = 309
    _globals['_LOCALAUTHAPILOGINRESPONSE']._serialized_start = 311
    _globals['_LOCALAUTHAPILOGINRESPONSE']._serialized_end = 401
    _globals['_LOCALAUTHAPILOGOUTREQUEST']._serialized_start = 403
    _globals['_LOCALAUTHAPILOGOUTREQUEST']._serialized_end = 430
    _globals['_LOCALAUTHAPILOGOUTRESPONSE']._serialized_start = 432
    _globals['_LOCALAUTHAPILOGOUTRESPONSE']._serialized_end = 460
    _globals['_LOCALAUTHAPICHECKAUTHSTATUSREQUEST']._serialized_start = 462
    _globals['_LOCALAUTHAPICHECKAUTHSTATUSREQUEST']._serialized_end = 498
    _globals['_LOCALAUTHAPICHECKAUTHSTATUSRESPONSE']._serialized_start = 500
    _globals['_LOCALAUTHAPICHECKAUTHSTATUSRESPONSE']._serialized_end = 600
    _globals['_LOCALAUTHMESSAGES']._serialized_start = 603
    _globals['_LOCALAUTHMESSAGES']._serialized_end = 1379