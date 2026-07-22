from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WifiNetworkSecurityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIFI_NETWORK_SECURITY_TYPE_INVALID: _ClassVar[WifiNetworkSecurityType]
    WIFI_NETWORK_SECURITY_TYPE_NONE: _ClassVar[WifiNetworkSecurityType]
    WIFI_NETWORK_SECURITY_TYPE_DYNAMIC_WEP: _ClassVar[WifiNetworkSecurityType]
    WIFI_NETWORK_SECURITY_TYPE_WPA2_PERSONAL: _ClassVar[WifiNetworkSecurityType]
    WIFI_NETWORK_SECURITY_TYPE_WPA2_ENTERPRISE: _ClassVar[WifiNetworkSecurityType]

class WifiConfigureResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIFI_CONFIGURE_RESULT_INVALID: _ClassVar[WifiConfigureResult]
    WIFI_CONFIGURE_RESULT_SUCCESS: _ClassVar[WifiConfigureResult]
    WIFI_CONFIGURE_RESULT_FAILURE_GENERIC: _ClassVar[WifiConfigureResult]
    WIFI_CONFIGURE_RESULT_FAILED_WITH_INVALID_CONFIG: _ClassVar[WifiConfigureResult]
    WIFI_CONFIGURE_RESULT_FAILED_TO_CONNECT: _ClassVar[WifiConfigureResult]

class CellularProfileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CELLULAR_PROFILE_TYPE_INVALID: _ClassVar[CellularProfileType]
    CELLULAR_PROFILE_TYPE_TWILIO: _ClassVar[CellularProfileType]
    CELLULAR_PROFILE_TYPE_ATT: _ClassVar[CellularProfileType]
    CELLULAR_PROFILE_TYPE_KPN: _ClassVar[CellularProfileType]
    CELLULAR_PROFILE_TYPE_TELEFONICA: _ClassVar[CellularProfileType]
    CELLULAR_PROFILE_TYPE_TELSTRA: _ClassVar[CellularProfileType]
    CELLULAR_PROFILE_TYPE_TELUS: _ClassVar[CellularProfileType]
    CELLULAR_PROFILE_TYPE_DOCOMO: _ClassVar[CellularProfileType]
    CELLULAR_PROFILE_TYPE_UNICOM: _ClassVar[CellularProfileType]

class NetworkDeviceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_DEVICE_STATE_INVALID: _ClassVar[NetworkDeviceState]
    NETWORK_DEVICE_STATE_UNMANAGED: _ClassVar[NetworkDeviceState]
    NETWORK_DEVICE_STATE_UNAVAILABLE: _ClassVar[NetworkDeviceState]
    NETWORK_DEVICE_STATE_IDLE: _ClassVar[NetworkDeviceState]
    NETWORK_DEVICE_STATE_ASSOCIATION: _ClassVar[NetworkDeviceState]
    NETWORK_DEVICE_STATE_CONFIGURATION: _ClassVar[NetworkDeviceState]
    NETWORK_DEVICE_STATE_READY: _ClassVar[NetworkDeviceState]
    NETWORK_DEVICE_STATE_DISCONNECT: _ClassVar[NetworkDeviceState]
    NETWORK_DEVICE_STATE_FAILURE: _ClassVar[NetworkDeviceState]

class NetworkDeviceStateReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_DEVICE_STATE_REASON_INVALID: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_NONE: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_CONFIG_FAILED: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_DHCP_FAILED: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_IP_ADDRESS_DUPLICATE: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_IP_CONFIG_EXPIRED: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_IP_CONFIG_UNAVAILABLE: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_IP_METHOD_UNSUPPORTED: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_NEW_ACTIVATION: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_NO_SECRETS: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_PPP_FAILED: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_SSID_NOT_FOUND: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_SIM_PIN_INCORRECT: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_SUPPLICANT_FAILED: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_REMOVED: _ClassVar[NetworkDeviceStateReason]
    NETWORK_DEVICE_STATE_REASON_MODEM_FAILED: _ClassVar[NetworkDeviceStateReason]
WIFI_NETWORK_SECURITY_TYPE_INVALID: WifiNetworkSecurityType
WIFI_NETWORK_SECURITY_TYPE_NONE: WifiNetworkSecurityType
WIFI_NETWORK_SECURITY_TYPE_DYNAMIC_WEP: WifiNetworkSecurityType
WIFI_NETWORK_SECURITY_TYPE_WPA2_PERSONAL: WifiNetworkSecurityType
WIFI_NETWORK_SECURITY_TYPE_WPA2_ENTERPRISE: WifiNetworkSecurityType
WIFI_CONFIGURE_RESULT_INVALID: WifiConfigureResult
WIFI_CONFIGURE_RESULT_SUCCESS: WifiConfigureResult
WIFI_CONFIGURE_RESULT_FAILURE_GENERIC: WifiConfigureResult
WIFI_CONFIGURE_RESULT_FAILED_WITH_INVALID_CONFIG: WifiConfigureResult
WIFI_CONFIGURE_RESULT_FAILED_TO_CONNECT: WifiConfigureResult
CELLULAR_PROFILE_TYPE_INVALID: CellularProfileType
CELLULAR_PROFILE_TYPE_TWILIO: CellularProfileType
CELLULAR_PROFILE_TYPE_ATT: CellularProfileType
CELLULAR_PROFILE_TYPE_KPN: CellularProfileType
CELLULAR_PROFILE_TYPE_TELEFONICA: CellularProfileType
CELLULAR_PROFILE_TYPE_TELSTRA: CellularProfileType
CELLULAR_PROFILE_TYPE_TELUS: CellularProfileType
CELLULAR_PROFILE_TYPE_DOCOMO: CellularProfileType
CELLULAR_PROFILE_TYPE_UNICOM: CellularProfileType
NETWORK_DEVICE_STATE_INVALID: NetworkDeviceState
NETWORK_DEVICE_STATE_UNMANAGED: NetworkDeviceState
NETWORK_DEVICE_STATE_UNAVAILABLE: NetworkDeviceState
NETWORK_DEVICE_STATE_IDLE: NetworkDeviceState
NETWORK_DEVICE_STATE_ASSOCIATION: NetworkDeviceState
NETWORK_DEVICE_STATE_CONFIGURATION: NetworkDeviceState
NETWORK_DEVICE_STATE_READY: NetworkDeviceState
NETWORK_DEVICE_STATE_DISCONNECT: NetworkDeviceState
NETWORK_DEVICE_STATE_FAILURE: NetworkDeviceState
NETWORK_DEVICE_STATE_REASON_INVALID: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_NONE: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_CONFIG_FAILED: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_DHCP_FAILED: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_IP_ADDRESS_DUPLICATE: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_IP_CONFIG_EXPIRED: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_IP_CONFIG_UNAVAILABLE: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_IP_METHOD_UNSUPPORTED: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_NEW_ACTIVATION: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_NO_SECRETS: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_PPP_FAILED: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_SSID_NOT_FOUND: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_SIM_PIN_INCORRECT: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_SUPPLICANT_FAILED: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_REMOVED: NetworkDeviceStateReason
NETWORK_DEVICE_STATE_REASON_MODEM_FAILED: NetworkDeviceStateReason

class Rssi(_message.Message):
    __slots__ = ('value', 'signal_strength_percent')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_STRENGTH_PERCENT_FIELD_NUMBER: _ClassVar[int]
    value: int
    signal_strength_percent: _wrappers_pb2.UInt32Value

    def __init__(self, value: _Optional[int]=..., signal_strength_percent: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]]=...) -> None:
        ...

class WifiPassword(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...

class WifiConfig(_message.Message):
    __slots__ = ('ssid', 'password', 'security_type')
    SSID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ssid: str
    password: WifiPassword
    security_type: WifiNetworkSecurityType

    def __init__(self, ssid: _Optional[str]=..., password: _Optional[_Union[WifiPassword, _Mapping]]=..., security_type: _Optional[_Union[WifiNetworkSecurityType, str]]=...) -> None:
        ...

class WifiNetwork(_message.Message):
    __slots__ = ('ssid', 'rssiValue', 'rssi', 'securityType')
    SSID_FIELD_NUMBER: _ClassVar[int]
    RSSIVALUE_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    ssid: str
    rssiValue: int
    rssi: Rssi
    securityType: WifiNetworkSecurityType

    def __init__(self, ssid: _Optional[str]=..., rssiValue: _Optional[int]=..., rssi: _Optional[_Union[Rssi, _Mapping]]=..., securityType: _Optional[_Union[WifiNetworkSecurityType, str]]=...) -> None:
        ...

class NetworkInterfaceIPv4Config(_message.Message):
    __slots__ = ('dhcp_enabled', 'address', 'subnet_mask', 'gateway', 'dns')
    DHCP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_MASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    dhcp_enabled: bool
    address: int
    subnet_mask: int
    gateway: int
    dns: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, dhcp_enabled: bool=..., address: _Optional[int]=..., subnet_mask: _Optional[int]=..., gateway: _Optional[int]=..., dns: _Optional[_Iterable[int]]=...) -> None:
        ...

class NetworkConnectivityStatus(_message.Message):
    __slots__ = ('connected_physical', 'connected_internet', 'connected_tesla', 'rssi', 'snr')
    CONNECTED_PHYSICAL_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_INTERNET_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_TESLA_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    connected_physical: bool
    connected_internet: bool
    connected_tesla: bool
    rssi: Rssi
    snr: _wrappers_pb2.Int32Value

    def __init__(self, connected_physical: bool=..., connected_internet: bool=..., connected_tesla: bool=..., rssi: _Optional[_Union[Rssi, _Mapping]]=..., snr: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=...) -> None:
        ...

class NetworkInterface(_message.Message):
    __slots__ = ('mac_address', 'enabled', 'active_route', 'ipv4_config', 'connectivity_status')
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_FIELD_NUMBER: _ClassVar[int]
    IPV4_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONNECTIVITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    mac_address: bytes
    enabled: bool
    active_route: bool
    ipv4_config: NetworkInterfaceIPv4Config
    connectivity_status: NetworkConnectivityStatus

    def __init__(self, mac_address: _Optional[bytes]=..., enabled: bool=..., active_route: bool=..., ipv4_config: _Optional[_Union[NetworkInterfaceIPv4Config, _Mapping]]=..., connectivity_status: _Optional[_Union[NetworkConnectivityStatus, _Mapping]]=...) -> None:
        ...

class CellularEID(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...