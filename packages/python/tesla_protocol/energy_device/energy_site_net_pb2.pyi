from . import device_pb2 as _device_pb2
from . import networking_pb2 as _networking_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EnergySiteNetAdditionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENERGY_SITE_NET_ADDITION_STATUS_INVALID: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_IN_PROGRESS: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_ADDED: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NOT_FOUND: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_CANNOT_JOIN: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NO_RESPONSE: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_BAD_RESPONSE: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_INTERNAL_ERROR: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_CHANGES_PROHIBITED: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_MAX_DEVICES: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NOT_LEADER: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_EXISTS: _ClassVar[EnergySiteNetAdditionStatus]
    ENERGY_SITE_NET_ADDITION_STATUS_FAILED_PROOF_OF_PRESENCE: _ClassVar[EnergySiteNetAdditionStatus]

class EnergySiteNetNetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENERGY_SITE_NET_NETWORK_TYPE_INVALID: _ClassVar[EnergySiteNetNetworkType]
    ENERGY_SITE_NET_NETWORK_TYPE_POWERWALL3: _ClassVar[EnergySiteNetNetworkType]
    ENERGY_SITE_NET_NETWORK_TYPE_SMART_CHARGING: _ClassVar[EnergySiteNetNetworkType]
    ENERGY_SITE_NET_NETWORK_TYPE_LOAD_SHARING: _ClassVar[EnergySiteNetNetworkType]

class EnergySiteNetPairStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENERGY_SITE_NET_PAIR_STATUS_INVALID: _ClassVar[EnergySiteNetPairStatus]
    ENERGY_SITE_NET_PAIR_STATUS_PENDING: _ClassVar[EnergySiteNetPairStatus]
    ENERGY_SITE_NET_PAIR_STATUS_FAILED_INTERNAL_ERROR: _ClassVar[EnergySiteNetPairStatus]
    ENERGY_SITE_NET_PAIR_STATUS_PROOF_OF_PRESENCE_TIMEOUT: _ClassVar[EnergySiteNetPairStatus]

class EnergySiteNetRemovalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENERGY_SITE_NET_REMOVAL_STATUS_INVALID: _ClassVar[EnergySiteNetRemovalStatus]
    ENERGY_SITE_NET_REMOVAL_STATUS_IN_PROGRESS: _ClassVar[EnergySiteNetRemovalStatus]
    ENERGY_SITE_NET_REMOVAL_STATUS_REMOVED: _ClassVar[EnergySiteNetRemovalStatus]
    ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_NO_SUCH_DEVICE: _ClassVar[EnergySiteNetRemovalStatus]
    ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_INTERNAL_ERROR: _ClassVar[EnergySiteNetRemovalStatus]
    ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_CHANGES_PROHIBITED: _ClassVar[EnergySiteNetRemovalStatus]
    ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_AM_LEADER: _ClassVar[EnergySiteNetRemovalStatus]
    ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_AM_SOLO: _ClassVar[EnergySiteNetRemovalStatus]
    ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_NOT_LEADER: _ClassVar[EnergySiteNetRemovalStatus]
    ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_LEADER_AVAILABLE: _ClassVar[EnergySiteNetRemovalStatus]

class IntraSiteServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTRA_SITE_SERVICE_TYPE_INVALID: _ClassVar[IntraSiteServiceType]
    INTRA_SITE_SERVICE_TYPE_MULTI_PW3_FOLLOWER: _ClassVar[IntraSiteServiceType]
    INTRA_SITE_SERVICE_TYPE_WC_LOAD_SHARING_FOLLOWER: _ClassVar[IntraSiteServiceType]
    INTRA_SITE_SERVICE_TYPE_WC_CURRENT_CONTROL: _ClassVar[IntraSiteServiceType]
ENERGY_SITE_NET_ADDITION_STATUS_INVALID: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_IN_PROGRESS: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_ADDED: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NOT_FOUND: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_CANNOT_JOIN: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NO_RESPONSE: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_BAD_RESPONSE: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_INTERNAL_ERROR: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_CHANGES_PROHIBITED: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_MAX_DEVICES: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NOT_LEADER: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_EXISTS: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_ADDITION_STATUS_FAILED_PROOF_OF_PRESENCE: EnergySiteNetAdditionStatus
ENERGY_SITE_NET_NETWORK_TYPE_INVALID: EnergySiteNetNetworkType
ENERGY_SITE_NET_NETWORK_TYPE_POWERWALL3: EnergySiteNetNetworkType
ENERGY_SITE_NET_NETWORK_TYPE_SMART_CHARGING: EnergySiteNetNetworkType
ENERGY_SITE_NET_NETWORK_TYPE_LOAD_SHARING: EnergySiteNetNetworkType
ENERGY_SITE_NET_PAIR_STATUS_INVALID: EnergySiteNetPairStatus
ENERGY_SITE_NET_PAIR_STATUS_PENDING: EnergySiteNetPairStatus
ENERGY_SITE_NET_PAIR_STATUS_FAILED_INTERNAL_ERROR: EnergySiteNetPairStatus
ENERGY_SITE_NET_PAIR_STATUS_PROOF_OF_PRESENCE_TIMEOUT: EnergySiteNetPairStatus
ENERGY_SITE_NET_REMOVAL_STATUS_INVALID: EnergySiteNetRemovalStatus
ENERGY_SITE_NET_REMOVAL_STATUS_IN_PROGRESS: EnergySiteNetRemovalStatus
ENERGY_SITE_NET_REMOVAL_STATUS_REMOVED: EnergySiteNetRemovalStatus
ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_NO_SUCH_DEVICE: EnergySiteNetRemovalStatus
ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_INTERNAL_ERROR: EnergySiteNetRemovalStatus
ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_CHANGES_PROHIBITED: EnergySiteNetRemovalStatus
ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_AM_LEADER: EnergySiteNetRemovalStatus
ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_AM_SOLO: EnergySiteNetRemovalStatus
ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_NOT_LEADER: EnergySiteNetRemovalStatus
ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_LEADER_AVAILABLE: EnergySiteNetRemovalStatus
INTRA_SITE_SERVICE_TYPE_INVALID: IntraSiteServiceType
INTRA_SITE_SERVICE_TYPE_MULTI_PW3_FOLLOWER: IntraSiteServiceType
INTRA_SITE_SERVICE_TYPE_WC_LOAD_SHARING_FOLLOWER: IntraSiteServiceType
INTRA_SITE_SERVICE_TYPE_WC_CURRENT_CONTROL: IntraSiteServiceType

class EnergySiteNetDevice(_message.Message):
    __slots__ = ('din', 'wifi_ap_config', 'service_types')
    DIN_FIELD_NUMBER: _ClassVar[int]
    WIFI_AP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPES_FIELD_NUMBER: _ClassVar[int]
    din: _device_pb2.Din
    wifi_ap_config: _networking_pb2.WifiConfig
    service_types: _containers.RepeatedScalarFieldContainer[IntraSiteServiceType]

    def __init__(self, din: _Optional[_Union[_device_pb2.Din, _Mapping]]=..., wifi_ap_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=..., service_types: _Optional[_Iterable[_Union[IntraSiteServiceType, str]]]=...) -> None:
        ...

class EnergySiteNetRecentlyAddedDevice(_message.Message):
    __slots__ = ('din', 'status')
    DIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    din: _device_pb2.Din
    status: EnergySiteNetAdditionStatus

    def __init__(self, din: _Optional[_Union[_device_pb2.Din, _Mapping]]=..., status: _Optional[_Union[EnergySiteNetAdditionStatus, str]]=...) -> None:
        ...

class EnergySiteNetRecentlyRemovedDevice(_message.Message):
    __slots__ = ('din', 'status')
    DIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    din: _device_pb2.Din
    status: EnergySiteNetRemovalStatus

    def __init__(self, din: _Optional[_Union[_device_pb2.Din, _Mapping]]=..., status: _Optional[_Union[EnergySiteNetRemovalStatus, str]]=...) -> None:
        ...

class EnergySiteNetUnpairedDevice(_message.Message):
    __slots__ = ('din', 'pair_status', 'firmware_version', 'device_type', 'teg_device_type')
    DIN_FIELD_NUMBER: _ClassVar[int]
    PAIR_STATUS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEG_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    din: _device_pb2.Din
    pair_status: EnergySiteNetPairStatus
    firmware_version: str
    device_type: _device_pb2.DeviceType
    teg_device_type: _device_pb2.TEGDeviceType

    def __init__(self, din: _Optional[_Union[_device_pb2.Din, _Mapping]]=..., pair_status: _Optional[_Union[EnergySiteNetPairStatus, str]]=..., firmware_version: _Optional[str]=..., device_type: _Optional[_Union[_device_pb2.DeviceType, str]]=..., teg_device_type: _Optional[_Union[_device_pb2.TEGDeviceType, str]]=...) -> None:
        ...

class EnergySiteNetConfig(_message.Message):
    __slots__ = ('devices', 'recently_added', 'recently_removed', 'unpaired_devices')
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    RECENTLY_ADDED_FIELD_NUMBER: _ClassVar[int]
    RECENTLY_REMOVED_FIELD_NUMBER: _ClassVar[int]
    UNPAIRED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[EnergySiteNetDevice]
    recently_added: EnergySiteNetRecentlyAddedDevice
    recently_removed: EnergySiteNetRecentlyRemovedDevice
    unpaired_devices: _containers.RepeatedCompositeFieldContainer[EnergySiteNetUnpairedDevice]

    def __init__(self, devices: _Optional[_Iterable[_Union[EnergySiteNetDevice, _Mapping]]]=..., recently_added: _Optional[_Union[EnergySiteNetRecentlyAddedDevice, _Mapping]]=..., recently_removed: _Optional[_Union[EnergySiteNetRecentlyRemovedDevice, _Mapping]]=..., unpaired_devices: _Optional[_Iterable[_Union[EnergySiteNetUnpairedDevice, _Mapping]]]=...) -> None:
        ...

class EnergySiteNetAPIAddDeviceRequest(_message.Message):
    __slots__ = ('device', 'network_type')
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    device: EnergySiteNetDevice
    network_type: EnergySiteNetNetworkType

    def __init__(self, device: _Optional[_Union[EnergySiteNetDevice, _Mapping]]=..., network_type: _Optional[_Union[EnergySiteNetNetworkType, str]]=...) -> None:
        ...

class EnergySiteNetAPIAddDeviceResponse(_message.Message):
    __slots__ = ('recently_added',)
    RECENTLY_ADDED_FIELD_NUMBER: _ClassVar[int]
    recently_added: EnergySiteNetRecentlyAddedDevice

    def __init__(self, recently_added: _Optional[_Union[EnergySiteNetRecentlyAddedDevice, _Mapping]]=...) -> None:
        ...

class EnergySiteNetAPIRemoveDeviceRequest(_message.Message):
    __slots__ = ('din', 'network_type', 'service_type')
    DIN_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    din: _device_pb2.Din
    network_type: EnergySiteNetNetworkType
    service_type: IntraSiteServiceType

    def __init__(self, din: _Optional[_Union[_device_pb2.Din, _Mapping]]=..., network_type: _Optional[_Union[EnergySiteNetNetworkType, str]]=..., service_type: _Optional[_Union[IntraSiteServiceType, str]]=...) -> None:
        ...

class EnergySiteNetAPIRemoveDeviceResponse(_message.Message):
    __slots__ = ('recently_removed',)
    RECENTLY_REMOVED_FIELD_NUMBER: _ClassVar[int]
    recently_removed: EnergySiteNetRecentlyRemovedDevice

    def __init__(self, recently_removed: _Optional[_Union[EnergySiteNetRecentlyRemovedDevice, _Mapping]]=...) -> None:
        ...

class EnergySiteNetAPIGetConfigRequest(_message.Message):
    __slots__ = ('network_type',)
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    network_type: EnergySiteNetNetworkType

    def __init__(self, network_type: _Optional[_Union[EnergySiteNetNetworkType, str]]=...) -> None:
        ...

class EnergySiteNetAPIGetConfigResponse(_message.Message):
    __slots__ = ('config', 'network_type')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    config: EnergySiteNetConfig
    network_type: EnergySiteNetNetworkType

    def __init__(self, config: _Optional[_Union[EnergySiteNetConfig, _Mapping]]=..., network_type: _Optional[_Union[EnergySiteNetNetworkType, str]]=...) -> None:
        ...

class EnergySiteNetMessages(_message.Message):
    __slots__ = ('add_device_request', 'add_device_response', 'remove_device_request', 'remove_device_response', 'get_config_request', 'get_config_response')
    ADD_DEVICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ADD_DEVICE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_DEVICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REMOVE_DEVICE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_CONFIG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_CONFIG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    add_device_request: EnergySiteNetAPIAddDeviceRequest
    add_device_response: EnergySiteNetAPIAddDeviceResponse
    remove_device_request: EnergySiteNetAPIRemoveDeviceRequest
    remove_device_response: EnergySiteNetAPIRemoveDeviceResponse
    get_config_request: EnergySiteNetAPIGetConfigRequest
    get_config_response: EnergySiteNetAPIGetConfigResponse

    def __init__(self, add_device_request: _Optional[_Union[EnergySiteNetAPIAddDeviceRequest, _Mapping]]=..., add_device_response: _Optional[_Union[EnergySiteNetAPIAddDeviceResponse, _Mapping]]=..., remove_device_request: _Optional[_Union[EnergySiteNetAPIRemoveDeviceRequest, _Mapping]]=..., remove_device_response: _Optional[_Union[EnergySiteNetAPIRemoveDeviceResponse, _Mapping]]=..., get_config_request: _Optional[_Union[EnergySiteNetAPIGetConfigRequest, _Mapping]]=..., get_config_response: _Optional[_Union[EnergySiteNetAPIGetConfigResponse, _Mapping]]=...) -> None:
        ...