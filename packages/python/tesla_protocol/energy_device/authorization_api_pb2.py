"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'authorization_api.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import authorization_types_pb2 as authorization__types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17authorization_api.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19authorization_types.proto"\xda\x01\n*AuthorizationAPIAddAuthorizedClientRequest\x12@\n\x04type\x18\x01 \x01(\x0e22.tesla.proto.energy_device.v1.AuthorizedClientType\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12A\n\x08key_type\x18\x03 \x01(\x0e2/.tesla.proto.energy_device.v1.AuthorizedKeyType\x12\x12\n\npublic_key\x18\x04 \x01(\x0c"p\n+AuthorizationAPIAddAuthorizedClientResponse\x12A\n\x06client\x18\x01 \x01(\x0b21.tesla.proto.energy_device.v1.AuthorizationRecord"\xc0\x02\n<AuthorizationAPIAddAuthorizedClientByTrustedSignatureRequest\x12@\n\x04type\x18\x01 \x01(\x0e22.tesla.proto.energy_device.v1.AuthorizedClientType\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12A\n\x08key_type\x18\x03 \x01(\x0e2/.tesla.proto.energy_device.v1.AuthorizedKeyType\x12\x12\n\npublic_key\x18\x04 \x01(\x0c\x12>\n\x05roles\x18\x05 \x03(\x0e2/.tesla.proto.energy_device.v1.AuthorizationRole\x12\x12\n\nidentifier\x18\x06 \x01(\t"\x82\x01\n=AuthorizationAPIAddAuthorizedClientByTrustedSignatureResponse\x12A\n\x06client\x18\x01 \x01(\x0b21.tesla.proto.energy_device.v1.AuthorizationRecord"C\n-AuthorizationAPIRemoveAuthorizedClientRequest\x12\x12\n\npublic_key\x18\x01 \x01(\x0c"0\n.AuthorizationAPIRemoveAuthorizedClientResponse".\n,AuthorizationAPIListAuthorizedClientsRequest"\x93\x01\n-AuthorizationAPIListAuthorizedClientsResponse\x12B\n\x07clients\x18\x01 \x03(\x0b21.tesla.proto.energy_device.v1.AuthorizationRecord\x12\x1e\n\x16enable_line_switch_off\x18\x02 \x01(\x08"3\n1AuthorizationAPIGetSignedCommandsPublicKeyRequest"I\n2AuthorizationAPIGetSignedCommandsPublicKeyResponse\x12\x13\n\x0bpub_key_ecc\x18\x01 \x01(\x0c"v\n-AuthorizationAPIConfigureRemoteServiceRequest\x12\x18\n\x10duration_seconds\x18\x01 \x01(\r\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x17\n\x0frequester_email\x18\x03 \x01(\t"\x91\x01\n.AuthorizationAPIConfigureRemoteServiceResponse\x12.\n\nbegin_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bexpiry_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xa4\x0c\n\x15AuthorizationMessages\x12q\n\x1dadd_authorized_client_request\x18\x01 \x01(\x0b2H.tesla.proto.energy_device.v1.AuthorizationAPIAddAuthorizedClientRequestH\x00\x12s\n\x1eadd_authorized_client_response\x18\x02 \x01(\x0b2I.tesla.proto.energy_device.v1.AuthorizationAPIAddAuthorizedClientResponseH\x00\x12w\n remove_authorized_client_request\x18\x03 \x01(\x0b2K.tesla.proto.energy_device.v1.AuthorizationAPIRemoveAuthorizedClientRequestH\x00\x12y\n!remove_authorized_client_response\x18\x04 \x01(\x0b2L.tesla.proto.energy_device.v1.AuthorizationAPIRemoveAuthorizedClientResponseH\x00\x12u\n\x1flist_authorized_clients_request\x18\x05 \x01(\x0b2J.tesla.proto.energy_device.v1.AuthorizationAPIListAuthorizedClientsRequestH\x00\x12w\n list_authorized_clients_response\x18\x06 \x01(\x0b2K.tesla.proto.energy_device.v1.AuthorizationAPIListAuthorizedClientsResponseH\x00\x12\x81\x01\n&get_signed_commands_public_key_request\x18\x07 \x01(\x0b2O.tesla.proto.energy_device.v1.AuthorizationAPIGetSignedCommandsPublicKeyRequestH\x00\x12\x83\x01\n\'get_signed_commands_public_key_response\x18\x08 \x01(\x0b2P.tesla.proto.energy_device.v1.AuthorizationAPIGetSignedCommandsPublicKeyResponseH\x00\x12\x98\x01\n2add_authorized_client_by_trusted_signature_request\x18\t \x01(\x0b2Z.tesla.proto.energy_device.v1.AuthorizationAPIAddAuthorizedClientByTrustedSignatureRequestH\x00\x12\x9a\x01\n3add_authorized_client_by_trusted_signature_response\x18\n \x01(\x0b2[.tesla.proto.energy_device.v1.AuthorizationAPIAddAuthorizedClientByTrustedSignatureResponseH\x00\x12w\n configure_remote_service_request\x18\x0b \x01(\x0b2K.tesla.proto.energy_device.v1.AuthorizationAPIConfigureRemoteServiceRequestH\x00\x12y\n!configure_remote_service_response\x18\x0c \x01(\x0b2L.tesla.proto.energy_device.v1.AuthorizationAPIConfigureRemoteServiceResponseH\x00B\t\n\x07messageB\x84\x01\n$com.tesla.generated.energy_device.v1B\x10AuthorizationApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authorization_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x10AuthorizationApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_AUTHORIZATIONAPIADDAUTHORIZEDCLIENTREQUEST']._serialized_start = 118
    _globals['_AUTHORIZATIONAPIADDAUTHORIZEDCLIENTREQUEST']._serialized_end = 336
    _globals['_AUTHORIZATIONAPIADDAUTHORIZEDCLIENTRESPONSE']._serialized_start = 338
    _globals['_AUTHORIZATIONAPIADDAUTHORIZEDCLIENTRESPONSE']._serialized_end = 450
    _globals['_AUTHORIZATIONAPIADDAUTHORIZEDCLIENTBYTRUSTEDSIGNATUREREQUEST']._serialized_start = 453
    _globals['_AUTHORIZATIONAPIADDAUTHORIZEDCLIENTBYTRUSTEDSIGNATUREREQUEST']._serialized_end = 773
    _globals['_AUTHORIZATIONAPIADDAUTHORIZEDCLIENTBYTRUSTEDSIGNATURERESPONSE']._serialized_start = 776
    _globals['_AUTHORIZATIONAPIADDAUTHORIZEDCLIENTBYTRUSTEDSIGNATURERESPONSE']._serialized_end = 906
    _globals['_AUTHORIZATIONAPIREMOVEAUTHORIZEDCLIENTREQUEST']._serialized_start = 908
    _globals['_AUTHORIZATIONAPIREMOVEAUTHORIZEDCLIENTREQUEST']._serialized_end = 975
    _globals['_AUTHORIZATIONAPIREMOVEAUTHORIZEDCLIENTRESPONSE']._serialized_start = 977
    _globals['_AUTHORIZATIONAPIREMOVEAUTHORIZEDCLIENTRESPONSE']._serialized_end = 1025
    _globals['_AUTHORIZATIONAPILISTAUTHORIZEDCLIENTSREQUEST']._serialized_start = 1027
    _globals['_AUTHORIZATIONAPILISTAUTHORIZEDCLIENTSREQUEST']._serialized_end = 1073
    _globals['_AUTHORIZATIONAPILISTAUTHORIZEDCLIENTSRESPONSE']._serialized_start = 1076
    _globals['_AUTHORIZATIONAPILISTAUTHORIZEDCLIENTSRESPONSE']._serialized_end = 1223
    _globals['_AUTHORIZATIONAPIGETSIGNEDCOMMANDSPUBLICKEYREQUEST']._serialized_start = 1225
    _globals['_AUTHORIZATIONAPIGETSIGNEDCOMMANDSPUBLICKEYREQUEST']._serialized_end = 1276
    _globals['_AUTHORIZATIONAPIGETSIGNEDCOMMANDSPUBLICKEYRESPONSE']._serialized_start = 1278
    _globals['_AUTHORIZATIONAPIGETSIGNEDCOMMANDSPUBLICKEYRESPONSE']._serialized_end = 1351
    _globals['_AUTHORIZATIONAPICONFIGUREREMOTESERVICEREQUEST']._serialized_start = 1353
    _globals['_AUTHORIZATIONAPICONFIGUREREMOTESERVICEREQUEST']._serialized_end = 1471
    _globals['_AUTHORIZATIONAPICONFIGUREREMOTESERVICERESPONSE']._serialized_start = 1474
    _globals['_AUTHORIZATIONAPICONFIGUREREMOTESERVICERESPONSE']._serialized_end = 1619
    _globals['_AUTHORIZATIONMESSAGES']._serialized_start = 1622
    _globals['_AUTHORIZATIONMESSAGES']._serialized_end = 3194