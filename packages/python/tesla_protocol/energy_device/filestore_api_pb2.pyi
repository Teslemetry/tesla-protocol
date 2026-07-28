from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FileStoreAPIDomain(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_STORE_API_DOMAIN_INVALID: _ClassVar[FileStoreAPIDomain]
    FILE_STORE_API_DOMAIN_CONFIG_JSON: _ClassVar[FileStoreAPIDomain]
    FILE_STORE_API_DOMAIN_GRID_CODE_REGIONS_CSV: _ClassVar[FileStoreAPIDomain]
    FILE_STORE_API_DOMAIN_CERTIFIED_INSTALLERS_CSV: _ClassVar[FileStoreAPIDomain]
    FILE_STORE_API_DOMAIN_SUPERCHARGER_FILES: _ClassVar[FileStoreAPIDomain]
    FILE_STORE_API_DOMAIN_OPTICASTER_FILES: _ClassVar[FileStoreAPIDomain]
    FILE_STORE_API_DOMAIN_WALLBOX_CONFIG: _ClassVar[FileStoreAPIDomain]
    FILE_STORE_API_DOMAIN_OCPP_CSMS_ROOT_CA: _ClassVar[FileStoreAPIDomain]
    FILE_STORE_API_DOMAIN_OPTIMUS_CHARGER_CONFIG: _ClassVar[FileStoreAPIDomain]
FILE_STORE_API_DOMAIN_INVALID: FileStoreAPIDomain
FILE_STORE_API_DOMAIN_CONFIG_JSON: FileStoreAPIDomain
FILE_STORE_API_DOMAIN_GRID_CODE_REGIONS_CSV: FileStoreAPIDomain
FILE_STORE_API_DOMAIN_CERTIFIED_INSTALLERS_CSV: FileStoreAPIDomain
FILE_STORE_API_DOMAIN_SUPERCHARGER_FILES: FileStoreAPIDomain
FILE_STORE_API_DOMAIN_OPTICASTER_FILES: FileStoreAPIDomain
FILE_STORE_API_DOMAIN_WALLBOX_CONFIG: FileStoreAPIDomain
FILE_STORE_API_DOMAIN_OCPP_CSMS_ROOT_CA: FileStoreAPIDomain
FILE_STORE_API_DOMAIN_OPTIMUS_CHARGER_CONFIG: FileStoreAPIDomain

class FileStoreAPIFile(_message.Message):
    __slots__ = ('name', 'blob')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    name: str
    blob: bytes

    def __init__(self, name: _Optional[str]=..., blob: _Optional[bytes]=...) -> None:
        ...

class FileStoreAPIForceWriteFileRequest(_message.Message):
    __slots__ = ('domain', 'file')
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    domain: FileStoreAPIDomain
    file: FileStoreAPIFile

    def __init__(self, domain: _Optional[_Union[FileStoreAPIDomain, str]]=..., file: _Optional[_Union[FileStoreAPIFile, _Mapping]]=...) -> None:
        ...

class FileStoreAPIForceWriteFileResponse(_message.Message):
    __slots__ = ('hash',)
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: bytes

    def __init__(self, hash: _Optional[bytes]=...) -> None:
        ...

class FileStoreAPIUpdateFileRequest(_message.Message):
    __slots__ = ('domain', 'file', 'hash')
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    domain: FileStoreAPIDomain
    file: FileStoreAPIFile
    hash: bytes

    def __init__(self, domain: _Optional[_Union[FileStoreAPIDomain, str]]=..., file: _Optional[_Union[FileStoreAPIFile, _Mapping]]=..., hash: _Optional[bytes]=...) -> None:
        ...

class FileStoreAPIUpdateFileResponse(_message.Message):
    __slots__ = ('file', 'hash')
    FILE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    file: FileStoreAPIFile
    hash: bytes

    def __init__(self, file: _Optional[_Union[FileStoreAPIFile, _Mapping]]=..., hash: _Optional[bytes]=...) -> None:
        ...

class FileStoreAPIReadFileRequest(_message.Message):
    __slots__ = ('domain', 'name', 'if_different_hash')
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_DIFFERENT_HASH_FIELD_NUMBER: _ClassVar[int]
    domain: FileStoreAPIDomain
    name: str
    if_different_hash: bytes

    def __init__(self, domain: _Optional[_Union[FileStoreAPIDomain, str]]=..., name: _Optional[str]=..., if_different_hash: _Optional[bytes]=...) -> None:
        ...

class FileStoreAPIReadFileResponse(_message.Message):
    __slots__ = ('file', 'hash')
    FILE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    file: FileStoreAPIFile
    hash: bytes

    def __init__(self, file: _Optional[_Union[FileStoreAPIFile, _Mapping]]=..., hash: _Optional[bytes]=...) -> None:
        ...

class FileStoreMessages(_message.Message):
    __slots__ = ('read_file_request', 'read_file_response', 'force_write_file_request', 'force_write_file_response', 'update_file_request', 'update_file_response')
    READ_FILE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    READ_FILE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    FORCE_WRITE_FILE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FORCE_WRITE_FILE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FILE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FILE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    read_file_request: FileStoreAPIReadFileRequest
    read_file_response: FileStoreAPIReadFileResponse
    force_write_file_request: FileStoreAPIForceWriteFileRequest
    force_write_file_response: FileStoreAPIForceWriteFileResponse
    update_file_request: FileStoreAPIUpdateFileRequest
    update_file_response: FileStoreAPIUpdateFileResponse

    def __init__(self, read_file_request: _Optional[_Union[FileStoreAPIReadFileRequest, _Mapping]]=..., read_file_response: _Optional[_Union[FileStoreAPIReadFileResponse, _Mapping]]=..., force_write_file_request: _Optional[_Union[FileStoreAPIForceWriteFileRequest, _Mapping]]=..., force_write_file_response: _Optional[_Union[FileStoreAPIForceWriteFileResponse, _Mapping]]=..., update_file_request: _Optional[_Union[FileStoreAPIUpdateFileRequest, _Mapping]]=..., update_file_response: _Optional[_Union[FileStoreAPIUpdateFileResponse, _Mapping]]=...) -> None:
        ...