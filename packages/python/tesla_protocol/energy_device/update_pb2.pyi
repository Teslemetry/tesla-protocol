from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpdateStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_STATUS_INVALID: _ClassVar[UpdateStatus]
    UPDATE_STATUS_IDLE: _ClassVar[UpdateStatus]
    UPDATE_STATUS_DOWNLOADING: _ClassVar[UpdateStatus]
    UPDATE_STATUS_DOWNLOADED: _ClassVar[UpdateStatus]
    UPDATE_STATUS_STAGED: _ClassVar[UpdateStatus]

class UpdateHandshakeResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_HANDSHAKE_RESULT_INVALID: _ClassVar[UpdateHandshakeResult]
    UPDATE_HANDSHAKE_RESULT_UNDERWAY: _ClassVar[UpdateHandshakeResult]
    UPDATE_HANDSHAKE_RESULT_FAILED: _ClassVar[UpdateHandshakeResult]
    UPDATE_HANDSHAKE_RESULT_NON_ACTIONABLE: _ClassVar[UpdateHandshakeResult]
    UPDATE_HANDSHAKE_RESULT_UPDATE_STAGED: _ClassVar[UpdateHandshakeResult]

class LastUpdateResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LAST_UPDATE_RESULT_INVALID: _ClassVar[LastUpdateResult]
    LAST_UPDATE_RESULT_FAILED: _ClassVar[LastUpdateResult]
    LAST_UPDATE_RESULT_SUCCEEDED: _ClassVar[LastUpdateResult]
UPDATE_STATUS_INVALID: UpdateStatus
UPDATE_STATUS_IDLE: UpdateStatus
UPDATE_STATUS_DOWNLOADING: UpdateStatus
UPDATE_STATUS_DOWNLOADED: UpdateStatus
UPDATE_STATUS_STAGED: UpdateStatus
UPDATE_HANDSHAKE_RESULT_INVALID: UpdateHandshakeResult
UPDATE_HANDSHAKE_RESULT_UNDERWAY: UpdateHandshakeResult
UPDATE_HANDSHAKE_RESULT_FAILED: UpdateHandshakeResult
UPDATE_HANDSHAKE_RESULT_NON_ACTIONABLE: UpdateHandshakeResult
UPDATE_HANDSHAKE_RESULT_UPDATE_STAGED: UpdateHandshakeResult
LAST_UPDATE_RESULT_INVALID: LastUpdateResult
LAST_UPDATE_RESULT_FAILED: LastUpdateResult
LAST_UPDATE_RESULT_SUCCEEDED: LastUpdateResult

class FirmwareVersion(_message.Message):
    __slots__ = ('version', 'githash')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GITHASH_FIELD_NUMBER: _ClassVar[int]
    version: str
    githash: bytes

    def __init__(self, version: _Optional[str]=..., githash: _Optional[bytes]=...) -> None:
        ...

class ServerStagedPackage(_message.Message):
    __slots__ = ('download_url', 'package_id', 'package_signature', 'server_staged_version')
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SERVER_STAGED_VERSION_FIELD_NUMBER: _ClassVar[int]
    download_url: str
    package_id: int
    package_signature: bytes
    server_staged_version: FirmwareVersion

    def __init__(self, download_url: _Optional[str]=..., package_id: _Optional[int]=..., package_signature: _Optional[bytes]=..., server_staged_version: _Optional[_Union[FirmwareVersion, _Mapping]]=...) -> None:
        ...

class SystemUpdate(_message.Message):
    __slots__ = ('handshake_result', 'update_status', 'server_staged_version', 'total_bytes', 'bytes_offset', 'estimated_bytes_per_second', 'last_handshake_timestamp', 'last_update_result', 'server_staged_packages')
    HANDSHAKE_RESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVER_STAGED_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    BYTES_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    LAST_HANDSHAKE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_RESULT_FIELD_NUMBER: _ClassVar[int]
    SERVER_STAGED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    handshake_result: int
    update_status: int
    server_staged_version: FirmwareVersion
    total_bytes: int
    bytes_offset: int
    estimated_bytes_per_second: int
    last_handshake_timestamp: int
    last_update_result: int
    server_staged_packages: _containers.RepeatedCompositeFieldContainer[ServerStagedPackage]

    def __init__(self, handshake_result: _Optional[int]=..., update_status: _Optional[int]=..., server_staged_version: _Optional[_Union[FirmwareVersion, _Mapping]]=..., total_bytes: _Optional[int]=..., bytes_offset: _Optional[int]=..., estimated_bytes_per_second: _Optional[int]=..., last_handshake_timestamp: _Optional[int]=..., last_update_result: _Optional[int]=..., server_staged_packages: _Optional[_Iterable[_Union[ServerStagedPackage, _Mapping]]]=...) -> None:
        ...

class AcceptedPackage(_message.Message):
    __slots__ = ('package_id', 'package_signature', 'upload_endpoint')
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    package_id: int
    package_signature: bytes
    upload_endpoint: str

    def __init__(self, package_id: _Optional[int]=..., package_signature: _Optional[bytes]=..., upload_endpoint: _Optional[str]=...) -> None:
        ...

class LocallyAvailablePackage(_message.Message):
    __slots__ = ('package_id', 'package_signature', 'file_size_bytes')
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    package_id: int
    package_signature: bytes
    file_size_bytes: int

    def __init__(self, package_id: _Optional[int]=..., package_signature: _Optional[bytes]=..., file_size_bytes: _Optional[int]=...) -> None:
        ...