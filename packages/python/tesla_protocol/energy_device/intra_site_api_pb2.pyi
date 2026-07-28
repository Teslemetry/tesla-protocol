from . import networking_pb2 as _networking_pb2
from . import energy_site_net_pb2 as _energy_site_net_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IntraSiteBackhaulInterfaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_BACKHAUL_INTERFACE_TYPE_INVALID: _ClassVar[IntraSiteBackhaulInterfaceType]
    INTRA_SITE_BACKHAUL_INTERFACE_TYPE_WIFI: _ClassVar[IntraSiteBackhaulInterfaceType]
    INTRA_SITE_BACKHAUL_INTERFACE_TYPE_CELL: _ClassVar[IntraSiteBackhaulInterfaceType]

class IntraSiteBackhaulStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_BACKHAUL_STATUS_INVALID: _ClassVar[IntraSiteBackhaulStatus]
    INTRA_SITE_BACKHAUL_STATUS_OFFLINE: _ClassVar[IntraSiteBackhaulStatus]
    INTRA_SITE_BACKHAUL_STATUS_ONLINE: _ClassVar[IntraSiteBackhaulStatus]

class IntraSiteLeaderStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_LEADER_STATUS_INVALID: _ClassVar[IntraSiteLeaderStatus]
    INTRA_SITE_LEADER_STATUS_TEMPORARILY_OFFLINE: _ClassVar[IntraSiteLeaderStatus]
    INTRA_SITE_LEADER_STATUS_ONLINE: _ClassVar[IntraSiteLeaderStatus]

class IntraSiteJoinNetworkResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_JOIN_NETWORK_RESULT_INVALID: _ClassVar[IntraSiteJoinNetworkResult]
    INTRA_SITE_JOIN_NETWORK_RESULT_ACCEPTED: _ClassVar[IntraSiteJoinNetworkResult]
    INTRA_SITE_JOIN_NETWORK_RESULT_REJECTED_ALREADY_JOINED: _ClassVar[IntraSiteJoinNetworkResult]
    INTRA_SITE_JOIN_NETWORK_RESULT_REJECTED_INCOMPATIBLE: _ClassVar[IntraSiteJoinNetworkResult]
    INTRA_SITE_JOIN_NETWORK_RESULT_REJECTED_INTERNAL_ERROR: _ClassVar[IntraSiteJoinNetworkResult]

class IntraSitePairResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_PAIR_RESULT_INVALID: _ClassVar[IntraSitePairResult]
    INTRA_SITE_PAIR_RESULT_ACCEPTED: _ClassVar[IntraSitePairResult]
    INTRA_SITE_PAIR_RESULT_REJECTED_DIFFERENT_NETWORK_ALREADY_JOINED: _ClassVar[IntraSitePairResult]
    INTRA_SITE_PAIR_RESULT_REJECTED_INTERNAL_ERROR: _ClassVar[IntraSitePairResult]
    INTRA_SITE_PAIR_RESULT_REJECTED_UNSUPPORTED_SERVICE_TYPES: _ClassVar[IntraSitePairResult]
    INTRA_SITE_PAIR_RESULT_REJECTED_UNSUPPORTED_LAN_TYPE: _ClassVar[IntraSitePairResult]
    INTRA_SITE_PAIR_RESULT_REJECTED_NO_PROOF_OF_PRESENCE: _ClassVar[IntraSitePairResult]

class IntraSiteUnpairResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_UNPAIR_RESULT_INVALID: _ClassVar[IntraSiteUnpairResult]
    INTRA_SITE_UNPAIR_RESULT_ACCEPTED: _ClassVar[IntraSiteUnpairResult]
    INTRA_SITE_UNPAIR_RESULT_REJECTED_NETWORK_LED_BY_DIFFERENT_LEADER: _ClassVar[IntraSiteUnpairResult]
    INTRA_SITE_UNPAIR_RESULT_REJECTED_DEVICE_IS_LEADER: _ClassVar[IntraSiteUnpairResult]
    INTRA_SITE_UNPAIR_RESULT_REJECTED_UNSUPPORTED_OPERATION: _ClassVar[IntraSiteUnpairResult]

class IntraSiteCompleteUpdateResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_COMPLETE_UPDATE_RESULT_INVALID: _ClassVar[IntraSiteCompleteUpdateResult]
    INTRA_SITE_COMPLETE_UPDATE_RESULT_FIRMWARE_MATCHES: _ClassVar[IntraSiteCompleteUpdateResult]
    INTRA_SITE_COMPLETE_UPDATE_RESULT_TERMINATE_SUCCESS: _ClassVar[IntraSiteCompleteUpdateResult]
    INTRA_SITE_COMPLETE_UPDATE_RESULT_TERMINATE_FAILURE: _ClassVar[IntraSiteCompleteUpdateResult]
    INTRA_SITE_COMPLETE_UPDATE_RESULT_HANDSHAKE_FAILURE: _ClassVar[IntraSiteCompleteUpdateResult]
    INTRA_SITE_COMPLETE_UPDATE_RESULT_UNKNOWN_FAILURE: _ClassVar[IntraSiteCompleteUpdateResult]

class IntraSiteHeartbeatResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_HEARTBEAT_RESULT_INVALID: _ClassVar[IntraSiteHeartbeatResult]
    INTRA_SITE_HEARTBEAT_RESULT_ACCEPTED: _ClassVar[IntraSiteHeartbeatResult]
    INTRA_SITE_HEARTBEAT_RESULT_NOT_ON_MANIFEST: _ClassVar[IntraSiteHeartbeatResult]

class IntraSiteLanType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_LAN_TYPE_INVALID: _ClassVar[IntraSiteLanType]
    INTRA_SITE_LAN_TYPE_SOFT_AP: _ClassVar[IntraSiteLanType]
    INTRA_SITE_LAN_TYPE_PRE_DEFINED: _ClassVar[IntraSiteLanType]
INTRA_SITE_BACKHAUL_INTERFACE_TYPE_INVALID: IntraSiteBackhaulInterfaceType
INTRA_SITE_BACKHAUL_INTERFACE_TYPE_WIFI: IntraSiteBackhaulInterfaceType
INTRA_SITE_BACKHAUL_INTERFACE_TYPE_CELL: IntraSiteBackhaulInterfaceType
INTRA_SITE_BACKHAUL_STATUS_INVALID: IntraSiteBackhaulStatus
INTRA_SITE_BACKHAUL_STATUS_OFFLINE: IntraSiteBackhaulStatus
INTRA_SITE_BACKHAUL_STATUS_ONLINE: IntraSiteBackhaulStatus
INTRA_SITE_LEADER_STATUS_INVALID: IntraSiteLeaderStatus
INTRA_SITE_LEADER_STATUS_TEMPORARILY_OFFLINE: IntraSiteLeaderStatus
INTRA_SITE_LEADER_STATUS_ONLINE: IntraSiteLeaderStatus
INTRA_SITE_JOIN_NETWORK_RESULT_INVALID: IntraSiteJoinNetworkResult
INTRA_SITE_JOIN_NETWORK_RESULT_ACCEPTED: IntraSiteJoinNetworkResult
INTRA_SITE_JOIN_NETWORK_RESULT_REJECTED_ALREADY_JOINED: IntraSiteJoinNetworkResult
INTRA_SITE_JOIN_NETWORK_RESULT_REJECTED_INCOMPATIBLE: IntraSiteJoinNetworkResult
INTRA_SITE_JOIN_NETWORK_RESULT_REJECTED_INTERNAL_ERROR: IntraSiteJoinNetworkResult
INTRA_SITE_PAIR_RESULT_INVALID: IntraSitePairResult
INTRA_SITE_PAIR_RESULT_ACCEPTED: IntraSitePairResult
INTRA_SITE_PAIR_RESULT_REJECTED_DIFFERENT_NETWORK_ALREADY_JOINED: IntraSitePairResult
INTRA_SITE_PAIR_RESULT_REJECTED_INTERNAL_ERROR: IntraSitePairResult
INTRA_SITE_PAIR_RESULT_REJECTED_UNSUPPORTED_SERVICE_TYPES: IntraSitePairResult
INTRA_SITE_PAIR_RESULT_REJECTED_UNSUPPORTED_LAN_TYPE: IntraSitePairResult
INTRA_SITE_PAIR_RESULT_REJECTED_NO_PROOF_OF_PRESENCE: IntraSitePairResult
INTRA_SITE_UNPAIR_RESULT_INVALID: IntraSiteUnpairResult
INTRA_SITE_UNPAIR_RESULT_ACCEPTED: IntraSiteUnpairResult
INTRA_SITE_UNPAIR_RESULT_REJECTED_NETWORK_LED_BY_DIFFERENT_LEADER: IntraSiteUnpairResult
INTRA_SITE_UNPAIR_RESULT_REJECTED_DEVICE_IS_LEADER: IntraSiteUnpairResult
INTRA_SITE_UNPAIR_RESULT_REJECTED_UNSUPPORTED_OPERATION: IntraSiteUnpairResult
INTRA_SITE_COMPLETE_UPDATE_RESULT_INVALID: IntraSiteCompleteUpdateResult
INTRA_SITE_COMPLETE_UPDATE_RESULT_FIRMWARE_MATCHES: IntraSiteCompleteUpdateResult
INTRA_SITE_COMPLETE_UPDATE_RESULT_TERMINATE_SUCCESS: IntraSiteCompleteUpdateResult
INTRA_SITE_COMPLETE_UPDATE_RESULT_TERMINATE_FAILURE: IntraSiteCompleteUpdateResult
INTRA_SITE_COMPLETE_UPDATE_RESULT_HANDSHAKE_FAILURE: IntraSiteCompleteUpdateResult
INTRA_SITE_COMPLETE_UPDATE_RESULT_UNKNOWN_FAILURE: IntraSiteCompleteUpdateResult
INTRA_SITE_HEARTBEAT_RESULT_INVALID: IntraSiteHeartbeatResult
INTRA_SITE_HEARTBEAT_RESULT_ACCEPTED: IntraSiteHeartbeatResult
INTRA_SITE_HEARTBEAT_RESULT_NOT_ON_MANIFEST: IntraSiteHeartbeatResult
INTRA_SITE_LAN_TYPE_INVALID: IntraSiteLanType
INTRA_SITE_LAN_TYPE_SOFT_AP: IntraSiteLanType
INTRA_SITE_LAN_TYPE_PRE_DEFINED: IntraSiteLanType

class IntraSiteConfig(_message.Message):
    __slots__ = ('last_changed_timestamp', 'site_config', 'backhaul_interface_type', 'site_wifi', 'leader', 'service_types', 'lan_type')
    LAST_CHANGED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SITE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BACKHAUL_INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SITE_WIFI_FIELD_NUMBER: _ClassVar[int]
    LEADER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPES_FIELD_NUMBER: _ClassVar[int]
    LAN_TYPE_FIELD_NUMBER: _ClassVar[int]
    last_changed_timestamp: int
    site_config: _energy_site_net_pb2.EnergySiteNetConfig
    backhaul_interface_type: IntraSiteBackhaulInterfaceType
    site_wifi: _networking_pb2.WifiConfig
    leader: _energy_site_net_pb2.EnergySiteNetDevice
    service_types: _containers.RepeatedScalarFieldContainer[_energy_site_net_pb2.IntraSiteServiceType]
    lan_type: IntraSiteLanType

    def __init__(self, last_changed_timestamp: _Optional[int]=..., site_config: _Optional[_Union[_energy_site_net_pb2.EnergySiteNetConfig, _Mapping]]=..., backhaul_interface_type: _Optional[_Union[IntraSiteBackhaulInterfaceType, str]]=..., site_wifi: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=..., leader: _Optional[_Union[_energy_site_net_pb2.EnergySiteNetDevice, _Mapping]]=..., service_types: _Optional[_Iterable[_Union[_energy_site_net_pb2.IntraSiteServiceType, str]]]=..., lan_type: _Optional[_Union[IntraSiteLanType, str]]=...) -> None:
        ...

class IntraSiteAPIPairRequest(_message.Message):
    __slots__ = ('site',)
    SITE_FIELD_NUMBER: _ClassVar[int]
    site: IntraSiteConfig

    def __init__(self, site: _Optional[_Union[IntraSiteConfig, _Mapping]]=...) -> None:
        ...

class IntraSiteAPIPairResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: IntraSitePairResult

    def __init__(self, result: _Optional[_Union[IntraSitePairResult, str]]=...) -> None:
        ...

class IntraSiteAPIUnpairRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IntraSiteAPIUnpairResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: IntraSiteUnpairResult

    def __init__(self, result: _Optional[_Union[IntraSiteUnpairResult, str]]=...) -> None:
        ...

class IntraSiteAPIJoinNetworkRequest(_message.Message):
    __slots__ = ('site',)
    SITE_FIELD_NUMBER: _ClassVar[int]
    site: IntraSiteConfig

    def __init__(self, site: _Optional[_Union[IntraSiteConfig, _Mapping]]=...) -> None:
        ...

class IntraSiteAPIJoinNetworkResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: IntraSiteJoinNetworkResult

    def __init__(self, result: _Optional[_Union[IntraSiteJoinNetworkResult, str]]=...) -> None:
        ...

class IntraSiteAPIAddDeviceRequest(_message.Message):
    __slots__ = ('device', 'site')
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    device: _energy_site_net_pb2.EnergySiteNetDevice
    site: IntraSiteConfig

    def __init__(self, device: _Optional[_Union[_energy_site_net_pb2.EnergySiteNetDevice, _Mapping]]=..., site: _Optional[_Union[IntraSiteConfig, _Mapping]]=...) -> None:
        ...

class IntraSiteAPIAddDeviceResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _energy_site_net_pb2.EnergySiteNetAdditionStatus

    def __init__(self, result: _Optional[_Union[_energy_site_net_pb2.EnergySiteNetAdditionStatus, str]]=...) -> None:
        ...

class IntraSiteAPIPushAddDeviceResultRequest(_message.Message):
    __slots__ = ('device', 'result')
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    device: _energy_site_net_pb2.EnergySiteNetDevice
    result: _energy_site_net_pb2.EnergySiteNetAdditionStatus

    def __init__(self, device: _Optional[_Union[_energy_site_net_pb2.EnergySiteNetDevice, _Mapping]]=..., result: _Optional[_Union[_energy_site_net_pb2.EnergySiteNetAdditionStatus, str]]=...) -> None:
        ...

class IntraSiteAPIPushAddDeviceResultResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IntraSiteAPILeaveNetworkRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IntraSiteAPILeaveNetworkResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IntraSiteAPIPushHeartbeatRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IntraSiteAPIPushHeartbeatResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: IntraSiteHeartbeatResult

    def __init__(self, result: _Optional[_Union[IntraSiteHeartbeatResult, str]]=...) -> None:
        ...

class IntraSiteAPIPushConfigRequest(_message.Message):
    __slots__ = ('site',)
    SITE_FIELD_NUMBER: _ClassVar[int]
    site: IntraSiteConfig

    def __init__(self, site: _Optional[_Union[IntraSiteConfig, _Mapping]]=...) -> None:
        ...

class IntraSiteAPIPushConfigResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IntraSiteAPIPushBackhaulStatusRequest(_message.Message):
    __slots__ = ('backhaul_interface_type', 'backhaul_status')
    BACKHAUL_INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKHAUL_STATUS_FIELD_NUMBER: _ClassVar[int]
    backhaul_interface_type: IntraSiteBackhaulInterfaceType
    backhaul_status: IntraSiteBackhaulStatus

    def __init__(self, backhaul_interface_type: _Optional[_Union[IntraSiteBackhaulInterfaceType, str]]=..., backhaul_status: _Optional[_Union[IntraSiteBackhaulStatus, str]]=...) -> None:
        ...

class IntraSiteAPIPushBackhaulStatusResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IntraSiteAPIPushLeaderStatusRequest(_message.Message):
    __slots__ = ('status', 'expected_duration_s')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    status: IntraSiteLeaderStatus
    expected_duration_s: int

    def __init__(self, status: _Optional[_Union[IntraSiteLeaderStatus, str]]=..., expected_duration_s: _Optional[int]=...) -> None:
        ...

class IntraSiteAPIPushLeaderStatusResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IntraSiteAPIRequestUpdateRequest(_message.Message):
    __slots__ = ('din',)
    DIN_FIELD_NUMBER: _ClassVar[int]
    din: str

    def __init__(self, din: _Optional[str]=...) -> None:
        ...

class IntraSiteAPIRequestUpdateResponse(_message.Message):
    __slots__ = ('signature',)
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signature: str

    def __init__(self, signature: _Optional[str]=...) -> None:
        ...

class IntraSiteAPICompleteUpdateRequest(_message.Message):
    __slots__ = ('din', 'result')
    DIN_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    din: str
    result: IntraSiteCompleteUpdateResult

    def __init__(self, din: _Optional[str]=..., result: _Optional[_Union[IntraSiteCompleteUpdateResult, str]]=...) -> None:
        ...

class IntraSiteAPICompleteUpdateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IntraSiteMessages(_message.Message):
    __slots__ = ('join_network_request', 'join_network_response', 'add_device_request', 'add_device_response', 'push_add_device_result_request', 'push_add_device_result_response', 'leave_network_request', 'leave_network_response', 'push_heartbeat_request', 'push_heartbeat_response', 'push_config_request', 'push_config_response', 'push_backhaul_status_request', 'push_backhaul_status_response', 'push_leader_status_request', 'push_leader_status_response', 'request_update_request', 'request_update_response', 'complete_update_request', 'complete_update_response', 'pair_request', 'pair_response', 'unpair_request', 'unpair_response')
    JOIN_NETWORK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    JOIN_NETWORK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ADD_DEVICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ADD_DEVICE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_ADD_DEVICE_RESULT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_ADD_DEVICE_RESULT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    LEAVE_NETWORK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LEAVE_NETWORK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_HEARTBEAT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_HEARTBEAT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_CONFIG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_CONFIG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_BACKHAUL_STATUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_BACKHAUL_STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUSH_LEADER_STATUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_LEADER_STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_UPDATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_UPDATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PAIR_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PAIR_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UNPAIR_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UNPAIR_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    join_network_request: IntraSiteAPIJoinNetworkRequest
    join_network_response: IntraSiteAPIJoinNetworkResponse
    add_device_request: IntraSiteAPIAddDeviceRequest
    add_device_response: IntraSiteAPIAddDeviceResponse
    push_add_device_result_request: IntraSiteAPIPushAddDeviceResultRequest
    push_add_device_result_response: IntraSiteAPIPushAddDeviceResultResponse
    leave_network_request: IntraSiteAPILeaveNetworkRequest
    leave_network_response: IntraSiteAPILeaveNetworkResponse
    push_heartbeat_request: IntraSiteAPIPushHeartbeatRequest
    push_heartbeat_response: IntraSiteAPIPushHeartbeatResponse
    push_config_request: IntraSiteAPIPushConfigRequest
    push_config_response: IntraSiteAPIPushConfigResponse
    push_backhaul_status_request: IntraSiteAPIPushBackhaulStatusRequest
    push_backhaul_status_response: IntraSiteAPIPushBackhaulStatusResponse
    push_leader_status_request: IntraSiteAPIPushLeaderStatusRequest
    push_leader_status_response: IntraSiteAPIPushLeaderStatusResponse
    request_update_request: IntraSiteAPIRequestUpdateRequest
    request_update_response: IntraSiteAPIRequestUpdateResponse
    complete_update_request: IntraSiteAPICompleteUpdateRequest
    complete_update_response: IntraSiteAPICompleteUpdateResponse
    pair_request: IntraSiteAPIPairRequest
    pair_response: IntraSiteAPIPairResponse
    unpair_request: IntraSiteAPIUnpairRequest
    unpair_response: IntraSiteAPIUnpairResponse

    def __init__(self, join_network_request: _Optional[_Union[IntraSiteAPIJoinNetworkRequest, _Mapping]]=..., join_network_response: _Optional[_Union[IntraSiteAPIJoinNetworkResponse, _Mapping]]=..., add_device_request: _Optional[_Union[IntraSiteAPIAddDeviceRequest, _Mapping]]=..., add_device_response: _Optional[_Union[IntraSiteAPIAddDeviceResponse, _Mapping]]=..., push_add_device_result_request: _Optional[_Union[IntraSiteAPIPushAddDeviceResultRequest, _Mapping]]=..., push_add_device_result_response: _Optional[_Union[IntraSiteAPIPushAddDeviceResultResponse, _Mapping]]=..., leave_network_request: _Optional[_Union[IntraSiteAPILeaveNetworkRequest, _Mapping]]=..., leave_network_response: _Optional[_Union[IntraSiteAPILeaveNetworkResponse, _Mapping]]=..., push_heartbeat_request: _Optional[_Union[IntraSiteAPIPushHeartbeatRequest, _Mapping]]=..., push_heartbeat_response: _Optional[_Union[IntraSiteAPIPushHeartbeatResponse, _Mapping]]=..., push_config_request: _Optional[_Union[IntraSiteAPIPushConfigRequest, _Mapping]]=..., push_config_response: _Optional[_Union[IntraSiteAPIPushConfigResponse, _Mapping]]=..., push_backhaul_status_request: _Optional[_Union[IntraSiteAPIPushBackhaulStatusRequest, _Mapping]]=..., push_backhaul_status_response: _Optional[_Union[IntraSiteAPIPushBackhaulStatusResponse, _Mapping]]=..., push_leader_status_request: _Optional[_Union[IntraSiteAPIPushLeaderStatusRequest, _Mapping]]=..., push_leader_status_response: _Optional[_Union[IntraSiteAPIPushLeaderStatusResponse, _Mapping]]=..., request_update_request: _Optional[_Union[IntraSiteAPIRequestUpdateRequest, _Mapping]]=..., request_update_response: _Optional[_Union[IntraSiteAPIRequestUpdateResponse, _Mapping]]=..., complete_update_request: _Optional[_Union[IntraSiteAPICompleteUpdateRequest, _Mapping]]=..., complete_update_response: _Optional[_Union[IntraSiteAPICompleteUpdateResponse, _Mapping]]=..., pair_request: _Optional[_Union[IntraSiteAPIPairRequest, _Mapping]]=..., pair_response: _Optional[_Union[IntraSiteAPIPairResponse, _Mapping]]=..., unpair_request: _Optional[_Union[IntraSiteAPIUnpairRequest, _Mapping]]=..., unpair_response: _Optional[_Union[IntraSiteAPIUnpairResponse, _Mapping]]=...) -> None:
        ...