"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 5, '', 'graphql_api.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11graphql_api.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x1egoogle/protobuf/wrappers.proto"4\n\x12SignedGraphQLQuery\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\r\n\x05query\x18\x02 \x01(\x0c"k\n\x0cGraphQLError\x12\x0c\n\x04path\x18\x01 \x03(\t\x12<\n\x04code\x18\x02 \x01(\x0e2..tesla.proto.energy_device.v1.GraphQLErrorCode\x12\x0f\n\x07message\x18\x03 \x01(\t"\xb2\x01\n\x16GraphQLAPIQueryRequest\x12@\n\x06format\x18\x01 \x01(\x0e20.tesla.proto.energy_device.v1.GraphQLQueryFormat\x12\r\n\x05query\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\x124\n\x0evariables_json\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue"\xa0\x01\n\x17GraphQLAPIQueryResponse\x12;\n\x06status\x18\x01 \x01(\x0e2+.tesla.proto.energy_device.v1.GraphQLStatus\x12\x0c\n\x04data\x18\x02 \x01(\t\x12:\n\x06errors\x18\x03 \x03(\x0b2*.tesla.proto.energy_device.v1.GraphQLError"\xbc\x01\n\x0fGraphQLMessages\x12M\n\rquery_request\x18\x01 \x01(\x0b24.tesla.proto.energy_device.v1.GraphQLAPIQueryRequestH\x00\x12O\n\x0equery_response\x18\x02 \x01(\x0b25.tesla.proto.energy_device.v1.GraphQLAPIQueryResponseH\x00B\t\n\x07message*\x8a\x01\n\x12GraphQLQueryFormat\x12!\n\x1dGRAPH_QL_QUERY_FORMAT_INVALID\x10\x00\x12\x1d\n\x19GRAPH_QL_QUERY_FORMAT_RAW\x10\x01\x122\n.GRAPH_QL_QUERY_FORMAT_SIGNED_SHA256_ECDSA_ASN1\x10\x02*\x8c\x01\n\rGraphQLStatus\x12\x1b\n\x17GRAPH_QL_STATUS_INVALID\x10\x00\x12\x1b\n\x17GRAPH_QL_STATUS_SUCCESS\x10\x01\x12!\n\x1dGRAPH_QL_STATUS_ERROR_PARTIAL\x10\x02\x12\x1e\n\x1aGRAPH_QL_STATUS_ERROR_FULL\x10\x03*\xe3\x01\n\x10GraphQLErrorCode\x12\x1f\n\x1bGRAPH_QL_ERROR_CODE_INVALID\x10\x00\x12\'\n#GRAPH_QL_ERROR_CODE_FIELD_NOT_FOUND\x10\x01\x12$\n GRAPH_QL_ERROR_CODE_UNAUTHORIZED\x10\x02\x125\n1GRAPH_QL_ERROR_CODE_RESOLVER_PROCESS_UNRESPONSIVE\x10\x03\x12(\n$GRAPH_QL_ERROR_CODE_RESPONSE_TOO_BIG\x10\x04B~\n$com.tesla.generated.energy_device.v1B\nGraphQLApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'graphql_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\nGraphQLApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_GRAPHQLQUERYFORMAT']._serialized_start = 782
    _globals['_GRAPHQLQUERYFORMAT']._serialized_end = 920
    _globals['_GRAPHQLSTATUS']._serialized_start = 923
    _globals['_GRAPHQLSTATUS']._serialized_end = 1063
    _globals['_GRAPHQLERRORCODE']._serialized_start = 1066
    _globals['_GRAPHQLERRORCODE']._serialized_end = 1293
    _globals['_SIGNEDGRAPHQLQUERY']._serialized_start = 83
    _globals['_SIGNEDGRAPHQLQUERY']._serialized_end = 135
    _globals['_GRAPHQLERROR']._serialized_start = 137
    _globals['_GRAPHQLERROR']._serialized_end = 244
    _globals['_GRAPHQLAPIQUERYREQUEST']._serialized_start = 247
    _globals['_GRAPHQLAPIQUERYREQUEST']._serialized_end = 425
    _globals['_GRAPHQLAPIQUERYRESPONSE']._serialized_start = 428
    _globals['_GRAPHQLAPIQUERYRESPONSE']._serialized_end = 588
    _globals['_GRAPHQLMESSAGES']._serialized_start = 591
    _globals['_GRAPHQLMESSAGES']._serialized_end = 779