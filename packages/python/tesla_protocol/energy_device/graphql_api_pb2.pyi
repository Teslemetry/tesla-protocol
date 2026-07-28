from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GraphQLQueryFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRAPH_QL_QUERY_FORMAT_INVALID: _ClassVar[GraphQLQueryFormat]
    GRAPH_QL_QUERY_FORMAT_RAW: _ClassVar[GraphQLQueryFormat]
    GRAPH_QL_QUERY_FORMAT_SIGNED_SHA256_ECDSA_ASN1: _ClassVar[GraphQLQueryFormat]

class GraphQLStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRAPH_QL_STATUS_INVALID: _ClassVar[GraphQLStatus]
    GRAPH_QL_STATUS_SUCCESS: _ClassVar[GraphQLStatus]
    GRAPH_QL_STATUS_ERROR_PARTIAL: _ClassVar[GraphQLStatus]
    GRAPH_QL_STATUS_ERROR_FULL: _ClassVar[GraphQLStatus]

class GraphQLErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRAPH_QL_ERROR_CODE_INVALID: _ClassVar[GraphQLErrorCode]
    GRAPH_QL_ERROR_CODE_FIELD_NOT_FOUND: _ClassVar[GraphQLErrorCode]
    GRAPH_QL_ERROR_CODE_UNAUTHORIZED: _ClassVar[GraphQLErrorCode]
    GRAPH_QL_ERROR_CODE_RESOLVER_PROCESS_UNRESPONSIVE: _ClassVar[GraphQLErrorCode]
    GRAPH_QL_ERROR_CODE_RESPONSE_TOO_BIG: _ClassVar[GraphQLErrorCode]
GRAPH_QL_QUERY_FORMAT_INVALID: GraphQLQueryFormat
GRAPH_QL_QUERY_FORMAT_RAW: GraphQLQueryFormat
GRAPH_QL_QUERY_FORMAT_SIGNED_SHA256_ECDSA_ASN1: GraphQLQueryFormat
GRAPH_QL_STATUS_INVALID: GraphQLStatus
GRAPH_QL_STATUS_SUCCESS: GraphQLStatus
GRAPH_QL_STATUS_ERROR_PARTIAL: GraphQLStatus
GRAPH_QL_STATUS_ERROR_FULL: GraphQLStatus
GRAPH_QL_ERROR_CODE_INVALID: GraphQLErrorCode
GRAPH_QL_ERROR_CODE_FIELD_NOT_FOUND: GraphQLErrorCode
GRAPH_QL_ERROR_CODE_UNAUTHORIZED: GraphQLErrorCode
GRAPH_QL_ERROR_CODE_RESOLVER_PROCESS_UNRESPONSIVE: GraphQLErrorCode
GRAPH_QL_ERROR_CODE_RESPONSE_TOO_BIG: GraphQLErrorCode

class SignedGraphQLQuery(_message.Message):
    __slots__ = ('version', 'query')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    version: int
    query: bytes

    def __init__(self, version: _Optional[int]=..., query: _Optional[bytes]=...) -> None:
        ...

class GraphQLError(_message.Message):
    __slots__ = ('path', 'code', 'message')
    PATH_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    path: _containers.RepeatedScalarFieldContainer[str]
    code: GraphQLErrorCode
    message: str

    def __init__(self, path: _Optional[_Iterable[str]]=..., code: _Optional[_Union[GraphQLErrorCode, str]]=..., message: _Optional[str]=...) -> None:
        ...

class GraphQLAPIQueryRequest(_message.Message):
    __slots__ = ('format', 'query', 'signature', 'variables_json')
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_JSON_FIELD_NUMBER: _ClassVar[int]
    format: GraphQLQueryFormat
    query: bytes
    signature: bytes
    variables_json: _wrappers_pb2.StringValue

    def __init__(self, format: _Optional[_Union[GraphQLQueryFormat, str]]=..., query: _Optional[bytes]=..., signature: _Optional[bytes]=..., variables_json: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=...) -> None:
        ...

class GraphQLAPIQueryResponse(_message.Message):
    __slots__ = ('status', 'data', 'errors')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    status: GraphQLStatus
    data: str
    errors: _containers.RepeatedCompositeFieldContainer[GraphQLError]

    def __init__(self, status: _Optional[_Union[GraphQLStatus, str]]=..., data: _Optional[str]=..., errors: _Optional[_Iterable[_Union[GraphQLError, _Mapping]]]=...) -> None:
        ...

class GraphQLMessages(_message.Message):
    __slots__ = ('query_request', 'query_response')
    QUERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    query_request: GraphQLAPIQueryRequest
    query_response: GraphQLAPIQueryResponse

    def __init__(self, query_request: _Optional[_Union[GraphQLAPIQueryRequest, _Mapping]]=..., query_response: _Optional[_Union[GraphQLAPIQueryResponse, _Mapping]]=...) -> None:
        ...