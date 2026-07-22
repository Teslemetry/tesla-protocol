import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ControlEventSchedulingInfo(_message.Message):
    __slots__ = ('start_time', 'duration_seconds', 'priority')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    duration_seconds: int
    priority: int

    def __init__(self, start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., duration_seconds: _Optional[int]=..., priority: _Optional[int]=...) -> None:
        ...

class BackupEvent(_message.Message):
    __slots__ = ('id', 'name', 'sheduling_info')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHEDULING_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    sheduling_info: ControlEventSchedulingInfo

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., sheduling_info: _Optional[_Union[ControlEventSchedulingInfo, _Mapping]]=...) -> None:
        ...

class ManualBackupEvent(_message.Message):
    __slots__ = ('scheduling_info',)
    SCHEDULING_INFO_FIELD_NUMBER: _ClassVar[int]
    scheduling_info: ControlEventSchedulingInfo

    def __init__(self, scheduling_info: _Optional[_Union[ControlEventSchedulingInfo, _Mapping]]=...) -> None:
        ...

class TEGAPIScheduleManualBackupEventRequest(_message.Message):
    __slots__ = ('scheduling_info',)
    SCHEDULING_INFO_FIELD_NUMBER: _ClassVar[int]
    scheduling_info: ControlEventSchedulingInfo

    def __init__(self, scheduling_info: _Optional[_Union[ControlEventSchedulingInfo, _Mapping]]=...) -> None:
        ...

class TEGAPIScheduleManualBackupEventResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPICancelManualBackupEventRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPICancelManualBackupEventResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetBackupEventsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetBackupEventsResponse(_message.Message):
    __slots__ = ('manual_backup_event', 'backup_events')
    MANUAL_BACKUP_EVENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_EVENTS_FIELD_NUMBER: _ClassVar[int]
    manual_backup_event: ManualBackupEvent
    backup_events: _containers.RepeatedCompositeFieldContainer[BackupEvent]

    def __init__(self, manual_backup_event: _Optional[_Union[ManualBackupEvent, _Mapping]]=..., backup_events: _Optional[_Iterable[_Union[BackupEvent, _Mapping]]]=...) -> None:
        ...

class TEGAPIRegisterRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIRegisterResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGMessages(_message.Message):
    __slots__ = ('schedule_manual_backup_event_request', 'schedule_manual_backup_event_response', 'cancel_manual_backup_event_request', 'cancel_manual_backup_event_response', 'get_backup_events_request', 'get_backup_events_response')
    SCHEDULE_MANUAL_BACKUP_EVENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_MANUAL_BACKUP_EVENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_MANUAL_BACKUP_EVENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CANCEL_MANUAL_BACKUP_EVENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_EVENTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_EVENTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    schedule_manual_backup_event_request: TEGAPIScheduleManualBackupEventRequest
    schedule_manual_backup_event_response: TEGAPIScheduleManualBackupEventResponse
    cancel_manual_backup_event_request: TEGAPICancelManualBackupEventRequest
    cancel_manual_backup_event_response: TEGAPICancelManualBackupEventResponse
    get_backup_events_request: TEGAPIGetBackupEventsRequest
    get_backup_events_response: TEGAPIGetBackupEventsResponse

    def __init__(self, schedule_manual_backup_event_request: _Optional[_Union[TEGAPIScheduleManualBackupEventRequest, _Mapping]]=..., schedule_manual_backup_event_response: _Optional[_Union[TEGAPIScheduleManualBackupEventResponse, _Mapping]]=..., cancel_manual_backup_event_request: _Optional[_Union[TEGAPICancelManualBackupEventRequest, _Mapping]]=..., cancel_manual_backup_event_response: _Optional[_Union[TEGAPICancelManualBackupEventResponse, _Mapping]]=..., get_backup_events_request: _Optional[_Union[TEGAPIGetBackupEventsRequest, _Mapping]]=..., get_backup_events_response: _Optional[_Union[TEGAPIGetBackupEventsResponse, _Mapping]]=...) -> None:
        ...