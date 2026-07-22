from . import networking_pb2 as _networking_pb2
from . import device_pb2 as _device_pb2
from . import update_pb2 as _update_pb2
from . import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CommonAPIGetSystemInfoRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIGetSystemInfoResponse(_message.Message):
    __slots__ = ('device_id', 'din', 'firmare_version', 'system_update', 'device_type')
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DIN_FIELD_NUMBER: _ClassVar[int]
    FIRMARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    device_id: _device_pb2.EcuId
    din: _device_pb2.Din
    firmare_version: _update_pb2.FirmwareVersion
    system_update: _update_pb2.SystemUpdate
    device_type: _device_pb2.DeviceType

    def __init__(self, device_id: _Optional[_Union[_device_pb2.EcuId, _Mapping]]=..., din: _Optional[_Union[_device_pb2.Din, _Mapping]]=..., firmare_version: _Optional[_Union[_update_pb2.FirmwareVersion, _Mapping]]=..., system_update: _Optional[_Union[_update_pb2.SystemUpdate, _Mapping]]=..., device_type: _Optional[_Union[_device_pb2.DeviceType, str]]=...) -> None:
        ...

class CommonAPISetLocalSiteConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPISetLocalSiteConfigResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIPerformUpdateRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIPerformUpdateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIFactoryResetRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIFactoryResetResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIWifiScanRequest(_message.Message):
    __slots__ = ('max_scan_duration_s', 'desired_security_types', 'maximum_total_aps')
    MAX_SCAN_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    DESIRED_SECURITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_TOTAL_APS_FIELD_NUMBER: _ClassVar[int]
    max_scan_duration_s: int
    desired_security_types: _containers.RepeatedScalarFieldContainer[_networking_pb2.WifiNetworkSecurityType]
    maximum_total_aps: int

    def __init__(self, max_scan_duration_s: _Optional[int]=..., desired_security_types: _Optional[_Iterable[_Union[_networking_pb2.WifiNetworkSecurityType, str]]]=..., maximum_total_aps: _Optional[int]=...) -> None:
        ...

class CommonAPIWifiScanResponse(_message.Message):
    __slots__ = ('wifi_networks',)
    WIFI_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    wifi_networks: _containers.RepeatedCompositeFieldContainer[_networking_pb2.WifiNetwork]

    def __init__(self, wifi_networks: _Optional[_Iterable[_Union[_networking_pb2.WifiNetwork, _Mapping]]]=...) -> None:
        ...

class CommonAPIConfigureWifiRequest(_message.Message):
    __slots__ = ('enabled', 'wifi_config')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WIFI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    wifi_config: _networking_pb2.WifiConfig

    def __init__(self, enabled: bool=..., wifi_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=...) -> None:
        ...

class CommonAPIConfigureWifiResponse(_message.Message):
    __slots__ = ('wifi_config', 'wifi')
    WIFI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    wifi_config: _networking_pb2.WifiConfig
    wifi: _networking_pb2.NetworkInterface

    def __init__(self, wifi_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=...) -> None:
        ...

class CommonAPIConfigureWifiWithEncryptedPasswordRequest(_message.Message):
    __slots__ = ('enabled', 'wifi_config', 'encrypted_password')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WIFI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    wifi_config: _networking_pb2.WifiConfig
    encrypted_password: _device_pb2.EncryptedMessage

    def __init__(self, enabled: bool=..., wifi_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=..., encrypted_password: _Optional[_Union[_device_pb2.EncryptedMessage, _Mapping]]=...) -> None:
        ...

class CommonAPIConfigureWifiWithEncryptedPasswordResponse(_message.Message):
    __slots__ = ('wifi_config', 'wifi', 'result')
    WIFI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    wifi_config: _networking_pb2.WifiConfig
    wifi: _networking_pb2.NetworkInterface
    result: int

    def __init__(self, wifi_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., result: _Optional[int]=...) -> None:
        ...

class CommonAPICheckForUpdateRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPICheckForUpdateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPICheckForUpdateUrgencyRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPICheckForUpdateUrgencyResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIClearUpdateRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIClearUpdateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIDeviceCertRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIDeviceCertResponse(_message.Message):
    __slots__ = ('format', 'device_cert')
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CERT_FIELD_NUMBER: _ClassVar[int]
    format: _device_pb2.DeviceCertFormat
    device_cert: bytes

    def __init__(self, format: _Optional[_Union[_device_pb2.DeviceCertFormat, str]]=..., device_cert: _Optional[bytes]=...) -> None:
        ...

class CommonAPIGetNetworkingStatusRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIGetNetworkingStatusResponse(_message.Message):
    __slots__ = ('wifi_config', 'wifi', 'eth', 'gsm')
    WIFI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    ETH_FIELD_NUMBER: _ClassVar[int]
    GSM_FIELD_NUMBER: _ClassVar[int]
    wifi_config: _networking_pb2.WifiConfig
    wifi: _networking_pb2.NetworkInterface
    eth: _networking_pb2.NetworkInterface
    gsm: _networking_pb2.NetworkInterface

    def __init__(self, wifi_config: _Optional[_Union[_networking_pb2.WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., eth: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., gsm: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=...) -> None:
        ...

class CommonAPIGetCellularInfoRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIGetCellularInfoResponse(_message.Message):
    __slots__ = ('eid', 'supported_profiles')
    EID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PROFILES_FIELD_NUMBER: _ClassVar[int]
    eid: _networking_pb2.CellularEID
    supported_profiles: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, eid: _Optional[_Union[_networking_pb2.CellularEID, _Mapping]]=..., supported_profiles: _Optional[_Iterable[int]]=...) -> None:
        ...

class CommonAPIConfigureEthernetRequest(_message.Message):
    __slots__ = ('ipv4_config',)
    IPV4_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ipv4_config: _networking_pb2.NetworkInterfaceIPv4Config

    def __init__(self, ipv4_config: _Optional[_Union[_networking_pb2.NetworkInterfaceIPv4Config, _Mapping]]=...) -> None:
        ...

class CommonAPIConfigureEthernetResponse(_message.Message):
    __slots__ = ('eth',)
    ETH_FIELD_NUMBER: _ClassVar[int]
    eth: _networking_pb2.NetworkInterface

    def __init__(self, eth: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=...) -> None:
        ...

class CommonAPIForgetWifiNetworkRequest(_message.Message):
    __slots__ = ('ssid',)
    SSID_FIELD_NUMBER: _ClassVar[int]
    ssid: str

    def __init__(self, ssid: _Optional[str]=...) -> None:
        ...

class CommonAPIForgetWifiNetworkResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPICheckInternetRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPICheckInternetResponse(_message.Message):
    __slots__ = ('wifi', 'eth', 'gsm')
    WIFI_FIELD_NUMBER: _ClassVar[int]
    ETH_FIELD_NUMBER: _ClassVar[int]
    GSM_FIELD_NUMBER: _ClassVar[int]
    wifi: _networking_pb2.NetworkInterface
    eth: _networking_pb2.NetworkInterface
    gsm: _networking_pb2.NetworkInterface

    def __init__(self, wifi: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., eth: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=..., gsm: _Optional[_Union[_networking_pb2.NetworkInterface, _Mapping]]=...) -> None:
        ...

class CommonAPINegotiateUpdateWithLocallyAvailablePackagesRequest(_message.Message):
    __slots__ = ('locally_available_packages',)
    LOCALLY_AVAILABLE_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    locally_available_packages: _containers.RepeatedCompositeFieldContainer[_update_pb2.LocallyAvailablePackage]

    def __init__(self, locally_available_packages: _Optional[_Iterable[_Union[_update_pb2.LocallyAvailablePackage, _Mapping]]]=...) -> None:
        ...

class CommonAPINegotiateUpdateWithLocallyAvailablePackagesResponse(_message.Message):
    __slots__ = ('accepted_packages',)
    ACCEPTED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    accepted_packages: _containers.RepeatedCompositeFieldContainer[_update_pb2.AcceptedPackage]

    def __init__(self, accepted_packages: _Optional[_Iterable[_Union[_update_pb2.AcceptedPackage, _Mapping]]]=...) -> None:
        ...

class CommonAPIPerformUpdateFromLocallyAvailablePackagesRequest(_message.Message):
    __slots__ = ('locally_available_packages',)
    LOCALLY_AVAILABLE_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    locally_available_packages: _containers.RepeatedCompositeFieldContainer[_update_pb2.LocallyAvailablePackage]

    def __init__(self, locally_available_packages: _Optional[_Iterable[_Union[_update_pb2.LocallyAvailablePackage, _Mapping]]]=...) -> None:
        ...

class CommonAPIPerformUpdateFromLocallyAvailablePackagesResponse(_message.Message):
    __slots__ = ('accepted_packages',)
    ACCEPTED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    accepted_packages: _containers.RepeatedCompositeFieldContainer[_update_pb2.AcceptedPackage]

    def __init__(self, accepted_packages: _Optional[_Iterable[_Union[_update_pb2.AcceptedPackage, _Mapping]]]=...) -> None:
        ...

class CommonAPIPrepareRegistrationPayloadRequest(_message.Message):
    __slots__ = ('customer_registration_info',)
    CUSTOMER_REGISTRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_registration_info: bytes

    def __init__(self, customer_registration_info: _Optional[bytes]=...) -> None:
        ...

class CommonAPIPrepareRegistrationPayloadResponse(_message.Message):
    __slots__ = ('signed_registration_payload',)
    SIGNED_REGISTRATION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    signed_registration_payload: _device_pb2.DeviceSignedPayload

    def __init__(self, signed_registration_payload: _Optional[_Union[_device_pb2.DeviceSignedPayload, _Mapping]]=...) -> None:
        ...

class CommonMessages(_message.Message):
    __slots__ = ('error_response', 'get_system_info_request', 'get_system_info_response', 'set_local_site_config_request', 'set_local_site_config_response', 'perform_update_request', 'perform_update_response', 'factory_reset_request', 'factory_reset_response', 'wifi_scan_request', 'wifi_scan_response', 'configure_wifi_request', 'configure_wifi_response', 'check_for_update_request', 'check_for_update_response', 'clear_update_request', 'clear_update_response', 'device_cert_request', 'device_cert_response', 'configure_wifi_with_encrypted_password_request', 'configure_wifi_with_encrypted_password_response', 'get_networking_status_request', 'get_networking_status_response', 'get_cellular_info_request', 'get_cellular_info_response', 'configure_ethernet_request', 'configure_ethernet_response', 'forget_wifi_network_request', 'forget_wifi_network_response', 'check_internet_request', 'check_internet_response', 'check_for_update_urgency_request', 'check_for_update_urgency_response', 'negotiate_update_with_locally_available_packages_request', 'negotiate_update_with_locally_available_packages_response', 'prepare_registration_payload_request', 'prepare_registration_payload_response', 'perform_update_from_locally_available_packages_request', 'perform_update_from_locally_available_packages_response')
    ERROR_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_SYSTEM_INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_SYSTEM_INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SET_LOCAL_SITE_CONFIG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_LOCAL_SITE_CONFIG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PERFORM_UPDATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PERFORM_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    FACTORY_RESET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FACTORY_RESET_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    WIFI_SCAN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    WIFI_SCAN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_WIFI_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_WIFI_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECK_FOR_UPDATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHECK_FOR_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_UPDATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CLEAR_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CERT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CERT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_WIFI_WITH_ENCRYPTED_PASSWORD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_WIFI_WITH_ENCRYPTED_PASSWORD_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_NETWORKING_STATUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_NETWORKING_STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_CELLULAR_INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_CELLULAR_INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_ETHERNET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_ETHERNET_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    FORGET_WIFI_NETWORK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FORGET_WIFI_NETWORK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECK_INTERNET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHECK_INTERNET_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECK_FOR_UPDATE_URGENCY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHECK_FOR_UPDATE_URGENCY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    NEGOTIATE_UPDATE_WITH_LOCALLY_AVAILABLE_PACKAGES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    NEGOTIATE_UPDATE_WITH_LOCALLY_AVAILABLE_PACKAGES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_REGISTRATION_PAYLOAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PREPARE_REGISTRATION_PAYLOAD_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PERFORM_UPDATE_FROM_LOCALLY_AVAILABLE_PACKAGES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PERFORM_UPDATE_FROM_LOCALLY_AVAILABLE_PACKAGES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    error_response: _error_pb2.ErrorResponse
    get_system_info_request: CommonAPIGetSystemInfoRequest
    get_system_info_response: CommonAPIGetSystemInfoResponse
    set_local_site_config_request: CommonAPISetLocalSiteConfigRequest
    set_local_site_config_response: CommonAPISetLocalSiteConfigResponse
    perform_update_request: CommonAPIPerformUpdateRequest
    perform_update_response: CommonAPIPerformUpdateResponse
    factory_reset_request: CommonAPIFactoryResetRequest
    factory_reset_response: CommonAPIFactoryResetResponse
    wifi_scan_request: CommonAPIWifiScanRequest
    wifi_scan_response: CommonAPIWifiScanResponse
    configure_wifi_request: CommonAPIConfigureWifiRequest
    configure_wifi_response: CommonAPIConfigureWifiResponse
    check_for_update_request: CommonAPICheckForUpdateRequest
    check_for_update_response: CommonAPICheckForUpdateResponse
    clear_update_request: CommonAPIClearUpdateRequest
    clear_update_response: CommonAPIClearUpdateResponse
    device_cert_request: CommonAPIDeviceCertRequest
    device_cert_response: CommonAPIDeviceCertResponse
    configure_wifi_with_encrypted_password_request: CommonAPIConfigureWifiWithEncryptedPasswordRequest
    configure_wifi_with_encrypted_password_response: CommonAPIConfigureWifiWithEncryptedPasswordResponse
    get_networking_status_request: CommonAPIGetNetworkingStatusRequest
    get_networking_status_response: CommonAPIGetNetworkingStatusResponse
    get_cellular_info_request: CommonAPIGetCellularInfoRequest
    get_cellular_info_response: CommonAPIGetCellularInfoResponse
    configure_ethernet_request: CommonAPIConfigureEthernetRequest
    configure_ethernet_response: CommonAPIConfigureEthernetResponse
    forget_wifi_network_request: CommonAPIForgetWifiNetworkRequest
    forget_wifi_network_response: CommonAPIForgetWifiNetworkResponse
    check_internet_request: CommonAPICheckInternetRequest
    check_internet_response: CommonAPICheckInternetResponse
    check_for_update_urgency_request: CommonAPICheckForUpdateUrgencyRequest
    check_for_update_urgency_response: CommonAPICheckForUpdateUrgencyResponse
    negotiate_update_with_locally_available_packages_request: CommonAPINegotiateUpdateWithLocallyAvailablePackagesRequest
    negotiate_update_with_locally_available_packages_response: CommonAPINegotiateUpdateWithLocallyAvailablePackagesResponse
    prepare_registration_payload_request: CommonAPIPrepareRegistrationPayloadRequest
    prepare_registration_payload_response: CommonAPIPrepareRegistrationPayloadResponse
    perform_update_from_locally_available_packages_request: CommonAPIPerformUpdateFromLocallyAvailablePackagesRequest
    perform_update_from_locally_available_packages_response: CommonAPIPerformUpdateFromLocallyAvailablePackagesResponse

    def __init__(self, error_response: _Optional[_Union[_error_pb2.ErrorResponse, _Mapping]]=..., get_system_info_request: _Optional[_Union[CommonAPIGetSystemInfoRequest, _Mapping]]=..., get_system_info_response: _Optional[_Union[CommonAPIGetSystemInfoResponse, _Mapping]]=..., set_local_site_config_request: _Optional[_Union[CommonAPISetLocalSiteConfigRequest, _Mapping]]=..., set_local_site_config_response: _Optional[_Union[CommonAPISetLocalSiteConfigResponse, _Mapping]]=..., perform_update_request: _Optional[_Union[CommonAPIPerformUpdateRequest, _Mapping]]=..., perform_update_response: _Optional[_Union[CommonAPIPerformUpdateResponse, _Mapping]]=..., factory_reset_request: _Optional[_Union[CommonAPIFactoryResetRequest, _Mapping]]=..., factory_reset_response: _Optional[_Union[CommonAPIFactoryResetResponse, _Mapping]]=..., wifi_scan_request: _Optional[_Union[CommonAPIWifiScanRequest, _Mapping]]=..., wifi_scan_response: _Optional[_Union[CommonAPIWifiScanResponse, _Mapping]]=..., configure_wifi_request: _Optional[_Union[CommonAPIConfigureWifiRequest, _Mapping]]=..., configure_wifi_response: _Optional[_Union[CommonAPIConfigureWifiResponse, _Mapping]]=..., check_for_update_request: _Optional[_Union[CommonAPICheckForUpdateRequest, _Mapping]]=..., check_for_update_response: _Optional[_Union[CommonAPICheckForUpdateResponse, _Mapping]]=..., clear_update_request: _Optional[_Union[CommonAPIClearUpdateRequest, _Mapping]]=..., clear_update_response: _Optional[_Union[CommonAPIClearUpdateResponse, _Mapping]]=..., device_cert_request: _Optional[_Union[CommonAPIDeviceCertRequest, _Mapping]]=..., device_cert_response: _Optional[_Union[CommonAPIDeviceCertResponse, _Mapping]]=..., configure_wifi_with_encrypted_password_request: _Optional[_Union[CommonAPIConfigureWifiWithEncryptedPasswordRequest, _Mapping]]=..., configure_wifi_with_encrypted_password_response: _Optional[_Union[CommonAPIConfigureWifiWithEncryptedPasswordResponse, _Mapping]]=..., get_networking_status_request: _Optional[_Union[CommonAPIGetNetworkingStatusRequest, _Mapping]]=..., get_networking_status_response: _Optional[_Union[CommonAPIGetNetworkingStatusResponse, _Mapping]]=..., get_cellular_info_request: _Optional[_Union[CommonAPIGetCellularInfoRequest, _Mapping]]=..., get_cellular_info_response: _Optional[_Union[CommonAPIGetCellularInfoResponse, _Mapping]]=..., configure_ethernet_request: _Optional[_Union[CommonAPIConfigureEthernetRequest, _Mapping]]=..., configure_ethernet_response: _Optional[_Union[CommonAPIConfigureEthernetResponse, _Mapping]]=..., forget_wifi_network_request: _Optional[_Union[CommonAPIForgetWifiNetworkRequest, _Mapping]]=..., forget_wifi_network_response: _Optional[_Union[CommonAPIForgetWifiNetworkResponse, _Mapping]]=..., check_internet_request: _Optional[_Union[CommonAPICheckInternetRequest, _Mapping]]=..., check_internet_response: _Optional[_Union[CommonAPICheckInternetResponse, _Mapping]]=..., check_for_update_urgency_request: _Optional[_Union[CommonAPICheckForUpdateUrgencyRequest, _Mapping]]=..., check_for_update_urgency_response: _Optional[_Union[CommonAPICheckForUpdateUrgencyResponse, _Mapping]]=..., negotiate_update_with_locally_available_packages_request: _Optional[_Union[CommonAPINegotiateUpdateWithLocallyAvailablePackagesRequest, _Mapping]]=..., negotiate_update_with_locally_available_packages_response: _Optional[_Union[CommonAPINegotiateUpdateWithLocallyAvailablePackagesResponse, _Mapping]]=..., prepare_registration_payload_request: _Optional[_Union[CommonAPIPrepareRegistrationPayloadRequest, _Mapping]]=..., prepare_registration_payload_response: _Optional[_Union[CommonAPIPrepareRegistrationPayloadResponse, _Mapping]]=..., perform_update_from_locally_available_packages_request: _Optional[_Union[CommonAPIPerformUpdateFromLocallyAvailablePackagesRequest, _Mapping]]=..., perform_update_from_locally_available_packages_response: _Optional[_Union[CommonAPIPerformUpdateFromLocallyAvailablePackagesResponse, _Mapping]]=...) -> None:
        ...