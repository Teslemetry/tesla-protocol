import datetime
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExternalAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXTERNAL_AUTH_TYPE_INVALID: _ClassVar[ExternalAuthType]
    EXTERNAL_AUTH_TYPE_PRESENCE: _ClassVar[ExternalAuthType]
    EXTERNAL_AUTH_TYPE_MTLS: _ClassVar[ExternalAuthType]
    EXTERNAL_AUTH_TYPE_HERMES_COMMAND: _ClassVar[ExternalAuthType]

class DeliveryChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DELIVERY_CHANNEL_INVALID: _ClassVar[DeliveryChannel]
    DELIVERY_CHANNEL_LOCAL_HTTPS: _ClassVar[DeliveryChannel]
    DELIVERY_CHANNEL_HERMES_COMMAND: _ClassVar[DeliveryChannel]
    DELIVERY_CHANNEL_BLE: _ClassVar[DeliveryChannel]

class TeslaService(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TESLA_SERVICE_INVALID: _ClassVar[TeslaService]
    TESLA_SERVICE_COMMAND: _ClassVar[TeslaService]
EXTERNAL_AUTH_TYPE_INVALID: ExternalAuthType
EXTERNAL_AUTH_TYPE_PRESENCE: ExternalAuthType
EXTERNAL_AUTH_TYPE_MTLS: ExternalAuthType
EXTERNAL_AUTH_TYPE_HERMES_COMMAND: ExternalAuthType
DELIVERY_CHANNEL_INVALID: DeliveryChannel
DELIVERY_CHANNEL_LOCAL_HTTPS: DeliveryChannel
DELIVERY_CHANNEL_HERMES_COMMAND: DeliveryChannel
DELIVERY_CHANNEL_BLE: DeliveryChannel
TESLA_SERVICE_INVALID: TeslaService
TESLA_SERVICE_COMMAND: TeslaService

class ExternalAuth(_message.Message):
    __slots__ = ('type',)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ExternalAuthType

    def __init__(self, type: _Optional[_Union[ExternalAuthType, str]]=...) -> None:
        ...

class Participant(_message.Message):
    __slots__ = ('din', 'teslaService', 'local', 'authorizedClient')
    DIN_FIELD_NUMBER: _ClassVar[int]
    TESLASERVICE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZEDCLIENT_FIELD_NUMBER: _ClassVar[int]
    din: str
    teslaService: int
    local: int
    authorizedClient: int

    def __init__(self, din: _Optional[str]=..., teslaService: _Optional[int]=..., local: _Optional[int]=..., authorizedClient: _Optional[int]=...) -> None:
        ...

class EcuId(_message.Message):
    __slots__ = ('partNumber', 'serialNumber')
    PARTNUMBER_FIELD_NUMBER: _ClassVar[int]
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    partNumber: str
    serialNumber: str

    def __init__(self, partNumber: _Optional[str]=..., serialNumber: _Optional[str]=...) -> None:
        ...

class Din(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...

class FirmwareVersion(_message.Message):
    __slots__ = ('version', 'githash')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GITHASH_FIELD_NUMBER: _ClassVar[int]
    version: str
    githash: str

    def __init__(self, version: _Optional[str]=..., githash: _Optional[str]=...) -> None:
        ...

class AccumulatedEnergy(_message.Message):
    __slots__ = ('energyWh', 'accumulationType', 'periodS')
    ENERGYWH_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    PERIODS_FIELD_NUMBER: _ClassVar[int]
    energyWh: float
    accumulationType: int
    periodS: UInt64Value

    def __init__(self, energyWh: _Optional[float]=..., accumulationType: _Optional[int]=..., periodS: _Optional[_Union[UInt64Value, _Mapping]]=...) -> None:
        ...

class InstACMeasurement(_message.Message):
    __slots__ = ('voltageVrms', 'frequencyHz', 'currentArms', 'realPowerW', 'reactivePowerVar', 'apparentPowerVa')
    VOLTAGEVRMS_FIELD_NUMBER: _ClassVar[int]
    FREQUENCYHZ_FIELD_NUMBER: _ClassVar[int]
    CURRENTARMS_FIELD_NUMBER: _ClassVar[int]
    REALPOWERW_FIELD_NUMBER: _ClassVar[int]
    REACTIVEPOWERVAR_FIELD_NUMBER: _ClassVar[int]
    APPARENTPOWERVA_FIELD_NUMBER: _ClassVar[int]
    voltageVrms: float
    frequencyHz: float
    currentArms: FloatValue
    realPowerW: FloatValue
    reactivePowerVar: FloatValue
    apparentPowerVa: FloatValue

    def __init__(self, voltageVrms: _Optional[float]=..., frequencyHz: _Optional[float]=..., currentArms: _Optional[_Union[FloatValue, _Mapping]]=..., realPowerW: _Optional[_Union[FloatValue, _Mapping]]=..., reactivePowerVar: _Optional[_Union[FloatValue, _Mapping]]=..., apparentPowerVa: _Optional[_Union[FloatValue, _Mapping]]=...) -> None:
        ...

class InstDCMeasurement(_message.Message):
    __slots__ = ('voltageV', 'currentA')
    VOLTAGEV_FIELD_NUMBER: _ClassVar[int]
    CURRENTA_FIELD_NUMBER: _ClassVar[int]
    voltageV: float
    currentA: FloatValue

    def __init__(self, voltageV: _Optional[float]=..., currentA: _Optional[_Union[FloatValue, _Mapping]]=...) -> None:
        ...

class GridComplianceStatus(_message.Message):
    __slots__ = ('gridState', 'qualifyingTimeRemainingS')
    GRIDSTATE_FIELD_NUMBER: _ClassVar[int]
    QUALIFYINGTIMEREMAININGS_FIELD_NUMBER: _ClassVar[int]
    gridState: int
    qualifyingTimeRemainingS: UInt32Value

    def __init__(self, gridState: _Optional[int]=..., qualifyingTimeRemainingS: _Optional[_Union[UInt32Value, _Mapping]]=...) -> None:
        ...

class NetworkInterfaceIPv4Config(_message.Message):
    __slots__ = ('dhcpEnabled', 'address', 'subnetMask', 'gateway', 'dns')
    DHCPENABLED_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUBNETMASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    dhcpEnabled: bool
    address: int
    subnetMask: int
    gateway: int
    dns: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, dhcpEnabled: bool=..., address: _Optional[int]=..., subnetMask: _Optional[int]=..., gateway: _Optional[int]=..., dns: _Optional[_Iterable[int]]=...) -> None:
        ...

class Rssi(_message.Message):
    __slots__ = ('value', 'signalStrengthPercent')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SIGNALSTRENGTHPERCENT_FIELD_NUMBER: _ClassVar[int]
    value: int
    signalStrengthPercent: UInt32Value

    def __init__(self, value: _Optional[int]=..., signalStrengthPercent: _Optional[_Union[UInt32Value, _Mapping]]=...) -> None:
        ...

class NetworkConnectivityStatus(_message.Message):
    __slots__ = ('connectedPhysical', 'connectedInternet', 'connectedTesla', 'rssi', 'snr')
    CONNECTEDPHYSICAL_FIELD_NUMBER: _ClassVar[int]
    CONNECTEDINTERNET_FIELD_NUMBER: _ClassVar[int]
    CONNECTEDTESLA_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    connectedPhysical: bool
    connectedInternet: bool
    connectedTesla: bool
    rssi: Rssi
    snr: Int32Value

    def __init__(self, connectedPhysical: bool=..., connectedInternet: bool=..., connectedTesla: bool=..., rssi: _Optional[_Union[Rssi, _Mapping]]=..., snr: _Optional[_Union[Int32Value, _Mapping]]=...) -> None:
        ...

class NetworkInterface(_message.Message):
    __slots__ = ('macAddress', 'enabled', 'activeRoute', 'ipv4Config', 'connectivityStatus')
    MACADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACTIVEROUTE_FIELD_NUMBER: _ClassVar[int]
    IPV4CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONNECTIVITYSTATUS_FIELD_NUMBER: _ClassVar[int]
    macAddress: bytes
    enabled: bool
    activeRoute: bool
    ipv4Config: NetworkInterfaceIPv4Config
    connectivityStatus: NetworkConnectivityStatus

    def __init__(self, macAddress: _Optional[bytes]=..., enabled: bool=..., activeRoute: bool=..., ipv4Config: _Optional[_Union[NetworkInterfaceIPv4Config, _Mapping]]=..., connectivityStatus: _Optional[_Union[NetworkConnectivityStatus, _Mapping]]=...) -> None:
        ...

class WifiPassword(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...

class EncryptedMessage(_message.Message):
    __slots__ = ('cipher', 'ciphertext')
    CIPHER_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    cipher: int
    ciphertext: bytes

    def __init__(self, cipher: _Optional[int]=..., ciphertext: _Optional[bytes]=...) -> None:
        ...

class WifiConfig(_message.Message):
    __slots__ = ('ssid', 'password', 'securityType')
    SSID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    ssid: str
    password: str
    securityType: int

    def __init__(self, ssid: _Optional[str]=..., password: _Optional[str]=..., securityType: _Optional[int]=...) -> None:
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
    securityType: int

    def __init__(self, ssid: _Optional[str]=..., rssiValue: _Optional[int]=..., rssi: _Optional[_Union[Rssi, _Mapping]]=..., securityType: _Optional[int]=...) -> None:
        ...

class SystemUpdate(_message.Message):
    __slots__ = ('handshakeResult', 'updateStatus', 'serverStagedVersion', 'totalBytes', 'bytesOffset', 'estimatedBytesPerSecond', 'lastHandshakeTimestamp', 'lastUpdateResult')
    HANDSHAKERESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATESTATUS_FIELD_NUMBER: _ClassVar[int]
    SERVERSTAGEDVERSION_FIELD_NUMBER: _ClassVar[int]
    TOTALBYTES_FIELD_NUMBER: _ClassVar[int]
    BYTESOFFSET_FIELD_NUMBER: _ClassVar[int]
    ESTIMATEDBYTESPERSECOND_FIELD_NUMBER: _ClassVar[int]
    LASTHANDSHAKETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATERESULT_FIELD_NUMBER: _ClassVar[int]
    handshakeResult: int
    updateStatus: int
    serverStagedVersion: FirmwareVersion
    totalBytes: int
    bytesOffset: int
    estimatedBytesPerSecond: int
    lastHandshakeTimestamp: int
    lastUpdateResult: int

    def __init__(self, handshakeResult: _Optional[int]=..., updateStatus: _Optional[int]=..., serverStagedVersion: _Optional[_Union[FirmwareVersion, _Mapping]]=..., totalBytes: _Optional[int]=..., bytesOffset: _Optional[int]=..., estimatedBytesPerSecond: _Optional[int]=..., lastHandshakeTimestamp: _Optional[int]=..., lastUpdateResult: _Optional[int]=...) -> None:
        ...

class ErrorResponse(_message.Message):
    __slots__ = ('status',)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status

    def __init__(self, status: _Optional[_Union[Status, _Mapping]]=...) -> None:
        ...

class CommonAPIGetSystemInfoRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIGetSystemInfoResponse(_message.Message):
    __slots__ = ('deviceId', 'din', 'firmwareVersion', 'systemUpdate')
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DIN_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREVERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEMUPDATE_FIELD_NUMBER: _ClassVar[int]
    deviceId: EcuId
    din: str
    firmwareVersion: FirmwareVersion
    systemUpdate: SystemUpdate

    def __init__(self, deviceId: _Optional[_Union[EcuId, _Mapping]]=..., din: _Optional[str]=..., firmwareVersion: _Optional[_Union[FirmwareVersion, _Mapping]]=..., systemUpdate: _Optional[_Union[SystemUpdate, _Mapping]]=...) -> None:
        ...

class CommonAPISetLocalSiteConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPISetLocalSiteConfigResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPICheckForUpdateRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPICheckForUpdateResponse(_message.Message):
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

class CommonAPIGetNetworkingStatusRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIGetNetworkingStatusResponse(_message.Message):
    __slots__ = ('wifiConfig', 'wifi', 'eth', 'gsm')
    WIFICONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    ETH_FIELD_NUMBER: _ClassVar[int]
    GSM_FIELD_NUMBER: _ClassVar[int]
    wifiConfig: WifiConfig
    wifi: NetworkInterface
    eth: NetworkInterface
    gsm: NetworkInterface

    def __init__(self, wifiConfig: _Optional[_Union[WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[NetworkInterface, _Mapping]]=..., eth: _Optional[_Union[NetworkInterface, _Mapping]]=..., gsm: _Optional[_Union[NetworkInterface, _Mapping]]=...) -> None:
        ...

class CommonAPIWifiScanRequest(_message.Message):
    __slots__ = ('maxScanDurationS', 'desiredSecurityTypes', 'maximumTotalAps')
    MAXSCANDURATIONS_FIELD_NUMBER: _ClassVar[int]
    DESIREDSECURITYTYPES_FIELD_NUMBER: _ClassVar[int]
    MAXIMUMTOTALAPS_FIELD_NUMBER: _ClassVar[int]
    maxScanDurationS: int
    desiredSecurityTypes: _containers.RepeatedScalarFieldContainer[int]
    maximumTotalAps: int

    def __init__(self, maxScanDurationS: _Optional[int]=..., desiredSecurityTypes: _Optional[_Iterable[int]]=..., maximumTotalAps: _Optional[int]=...) -> None:
        ...

class CommonAPIWifiScanResponse(_message.Message):
    __slots__ = ('wifiNetworks',)
    WIFINETWORKS_FIELD_NUMBER: _ClassVar[int]
    wifiNetworks: _containers.RepeatedCompositeFieldContainer[WifiNetwork]

    def __init__(self, wifiNetworks: _Optional[_Iterable[_Union[WifiNetwork, _Mapping]]]=...) -> None:
        ...

class CommonAPIConfigureWifiRequest(_message.Message):
    __slots__ = ('enabled', 'wifiConfig')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WIFICONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    wifiConfig: WifiConfig

    def __init__(self, enabled: bool=..., wifiConfig: _Optional[_Union[WifiConfig, _Mapping]]=...) -> None:
        ...

class CommonAPIConfigureWifiResponse(_message.Message):
    __slots__ = ('wifiConfig', 'wifi')
    WIFICONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    wifiConfig: WifiConfig
    wifi: NetworkInterface

    def __init__(self, wifiConfig: _Optional[_Union[WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[NetworkInterface, _Mapping]]=...) -> None:
        ...

class CommonAPIConfigureWifiWithEncryptedPasswordRequest(_message.Message):
    __slots__ = ('enabled', 'wifiConfig', 'encryptedPassword')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WIFICONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTEDPASSWORD_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    wifiConfig: WifiConfig
    encryptedPassword: EncryptedMessage

    def __init__(self, enabled: bool=..., wifiConfig: _Optional[_Union[WifiConfig, _Mapping]]=..., encryptedPassword: _Optional[_Union[EncryptedMessage, _Mapping]]=...) -> None:
        ...

class CommonAPIConfigureWifiWithEncryptedPasswordResponse(_message.Message):
    __slots__ = ('wifiConfig', 'wifi', 'result')
    WIFICONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    wifiConfig: WifiConfig
    wifi: NetworkInterface
    result: int

    def __init__(self, wifiConfig: _Optional[_Union[WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[NetworkInterface, _Mapping]]=..., result: _Optional[int]=...) -> None:
        ...

class CommonAPIDeviceCertRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommonAPIDeviceCertResponse(_message.Message):
    __slots__ = ('format', 'deviceCert')
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DEVICECERT_FIELD_NUMBER: _ClassVar[int]
    format: int
    deviceCert: bytes

    def __init__(self, format: _Optional[int]=..., deviceCert: _Optional[bytes]=...) -> None:
        ...

class AlertLog(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int

    def __init__(self, data: _Optional[int]=...) -> None:
        ...

class AlertMatrix(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int

    def __init__(self, data: _Optional[int]=...) -> None:
        ...

class EnergySiteNetDevice(_message.Message):
    __slots__ = ('din', 'wifiApConfig')
    DIN_FIELD_NUMBER: _ClassVar[int]
    WIFIAPCONFIG_FIELD_NUMBER: _ClassVar[int]
    din: Din
    wifiApConfig: WifiConfig

    def __init__(self, din: _Optional[_Union[Din, _Mapping]]=..., wifiApConfig: _Optional[_Union[WifiConfig, _Mapping]]=...) -> None:
        ...

class EnergySiteNetRecentlyAddedDevice(_message.Message):
    __slots__ = ('din', 'status')
    DIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    din: Din
    status: int

    def __init__(self, din: _Optional[_Union[Din, _Mapping]]=..., status: _Optional[int]=...) -> None:
        ...

class EnergySiteNetRecentlyRemovedDevice(_message.Message):
    __slots__ = ('din', 'status')
    DIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    din: Din
    status: int

    def __init__(self, din: _Optional[_Union[Din, _Mapping]]=..., status: _Optional[int]=...) -> None:
        ...

class EnergySiteNetConfig(_message.Message):
    __slots__ = ('devices', 'recentlyAdded', 'recentlyRemoved')
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    RECENTLYADDED_FIELD_NUMBER: _ClassVar[int]
    RECENTLYREMOVED_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[EnergySiteNetDevice]
    recentlyAdded: _containers.RepeatedCompositeFieldContainer[EnergySiteNetRecentlyAddedDevice]
    recentlyRemoved: _containers.RepeatedCompositeFieldContainer[EnergySiteNetRecentlyRemovedDevice]

    def __init__(self, devices: _Optional[_Iterable[_Union[EnergySiteNetDevice, _Mapping]]]=..., recentlyAdded: _Optional[_Iterable[_Union[EnergySiteNetRecentlyAddedDevice, _Mapping]]]=..., recentlyRemoved: _Optional[_Iterable[_Union[EnergySiteNetRecentlyRemovedDevice, _Mapping]]]=...) -> None:
        ...

class EnergySiteNetAPIAddDeviceRequest(_message.Message):
    __slots__ = ('device',)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: EnergySiteNetDevice

    def __init__(self, device: _Optional[_Union[EnergySiteNetDevice, _Mapping]]=...) -> None:
        ...

class EnergySiteNetAPIAddDeviceResponse(_message.Message):
    __slots__ = ('recentlyAdded',)
    RECENTLYADDED_FIELD_NUMBER: _ClassVar[int]
    recentlyAdded: EnergySiteNetRecentlyAddedDevice

    def __init__(self, recentlyAdded: _Optional[_Union[EnergySiteNetRecentlyAddedDevice, _Mapping]]=...) -> None:
        ...

class EnergySiteNetAPIRemoveDeviceRequest(_message.Message):
    __slots__ = ('din',)
    DIN_FIELD_NUMBER: _ClassVar[int]
    din: Din

    def __init__(self, din: _Optional[_Union[Din, _Mapping]]=...) -> None:
        ...

class EnergySiteNetAPIRemoveDeviceResponse(_message.Message):
    __slots__ = ('recentlyRemoved',)
    RECENTLYREMOVED_FIELD_NUMBER: _ClassVar[int]
    recentlyRemoved: EnergySiteNetRecentlyRemovedDevice

    def __init__(self, recentlyRemoved: _Optional[_Union[EnergySiteNetRecentlyRemovedDevice, _Mapping]]=...) -> None:
        ...

class EnergySiteNetAPIGetConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EnergySiteNetAPIGetConfigResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: EnergySiteNetConfig

    def __init__(self, config: _Optional[_Union[EnergySiteNetConfig, _Mapping]]=...) -> None:
        ...

class DeviceVital(_message.Message):
    __slots__ = ('name', 'intValue', 'floatValue', 'stringValue', 'boolValue')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    intValue: int
    floatValue: float
    stringValue: str
    boolValue: bool

    def __init__(self, name: _Optional[str]=..., intValue: _Optional[int]=..., floatValue: _Optional[float]=..., stringValue: _Optional[str]=..., boolValue: bool=...) -> None:
        ...

class StringValue(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...

class UInt32Value(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int

    def __init__(self, value: _Optional[int]=...) -> None:
        ...

class Int32Value(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int

    def __init__(self, value: _Optional[int]=...) -> None:
        ...

class UInt64Value(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int

    def __init__(self, value: _Optional[int]=...) -> None:
        ...

class FloatValue(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float

    def __init__(self, value: _Optional[float]=...) -> None:
        ...

class ConnectionParameters(_message.Message):
    __slots__ = ('ipAddress', 'serialPort', 'serialBaud', 'modbusId')
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERIALPORT_FIELD_NUMBER: _ClassVar[int]
    SERIALBAUD_FIELD_NUMBER: _ClassVar[int]
    MODBUSID_FIELD_NUMBER: _ClassVar[int]
    ipAddress: StringValue
    serialPort: StringValue
    serialBaud: int
    modbusId: int

    def __init__(self, ipAddress: _Optional[_Union[StringValue, _Mapping]]=..., serialPort: _Optional[_Union[StringValue, _Mapping]]=..., serialBaud: _Optional[int]=..., modbusId: _Optional[int]=...) -> None:
        ...

class TeslaHardwareId(_message.Message):
    __slots__ = ('pcbaId', 'assemblyId', 'usageId')
    PCBAID_FIELD_NUMBER: _ClassVar[int]
    ASSEMBLYID_FIELD_NUMBER: _ClassVar[int]
    USAGEID_FIELD_NUMBER: _ClassVar[int]
    pcbaId: UInt32Value
    assemblyId: UInt32Value
    usageId: UInt32Value

    def __init__(self, pcbaId: _Optional[_Union[UInt32Value, _Mapping]]=..., assemblyId: _Optional[_Union[UInt32Value, _Mapping]]=..., usageId: _Optional[_Union[UInt32Value, _Mapping]]=...) -> None:
        ...

class TeslaEnergyEcuAttributes(_message.Message):
    __slots__ = ('ecuType', 'hardwareId', 'pvInverterAttributes', 'meterAttributes')
    ECUTYPE_FIELD_NUMBER: _ClassVar[int]
    HARDWAREID_FIELD_NUMBER: _ClassVar[int]
    PVINVERTERATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    METERATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ecuType: int
    hardwareId: TeslaHardwareId
    pvInverterAttributes: PVInverterAttributes
    meterAttributes: MeterAttributes

    def __init__(self, ecuType: _Optional[int]=..., hardwareId: _Optional[_Union[TeslaHardwareId, _Mapping]]=..., pvInverterAttributes: _Optional[_Union[PVInverterAttributes, _Mapping]]=..., meterAttributes: _Optional[_Union[MeterAttributes, _Mapping]]=...) -> None:
        ...

class GeneratorAttributes(_message.Message):
    __slots__ = ('nameplateRealPowerW', 'nameplateApparentPowerVa')
    NAMEPLATEREALPOWERW_FIELD_NUMBER: _ClassVar[int]
    NAMEPLATEAPPARENTPOWERVA_FIELD_NUMBER: _ClassVar[int]
    nameplateRealPowerW: int
    nameplateApparentPowerVa: int

    def __init__(self, nameplateRealPowerW: _Optional[int]=..., nameplateApparentPowerVa: _Optional[int]=...) -> None:
        ...

class PVInverterAttributes(_message.Message):
    __slots__ = ('nameplateRealPowerW',)
    NAMEPLATEREALPOWERW_FIELD_NUMBER: _ClassVar[int]
    nameplateRealPowerW: int

    def __init__(self, nameplateRealPowerW: _Optional[int]=...) -> None:
        ...

class MeterAttributes(_message.Message):
    __slots__ = ('meterLocation',)
    METERLOCATION_FIELD_NUMBER: _ClassVar[int]
    meterLocation: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, meterLocation: _Optional[_Iterable[int]]=...) -> None:
        ...

class DeviceAttributes(_message.Message):
    __slots__ = ('teslaEnergyEcuAttributes', 'generatorAttributes', 'pvInverterAttributes', 'meterAttributes')
    TESLAENERGYECUATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    GENERATORATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PVINVERTERATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    METERATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    teslaEnergyEcuAttributes: TeslaEnergyEcuAttributes
    generatorAttributes: GeneratorAttributes
    pvInverterAttributes: PVInverterAttributes
    meterAttributes: MeterAttributes

    def __init__(self, teslaEnergyEcuAttributes: _Optional[_Union[TeslaEnergyEcuAttributes, _Mapping]]=..., generatorAttributes: _Optional[_Union[GeneratorAttributes, _Mapping]]=..., pvInverterAttributes: _Optional[_Union[PVInverterAttributes, _Mapping]]=..., meterAttributes: _Optional[_Union[MeterAttributes, _Mapping]]=...) -> None:
        ...

class Device(_message.Message):
    __slots__ = ('din', 'partNumber', 'serialNumber', 'manufacturer', 'siteLabel', 'componentParentDin', 'firmwareVersion', 'firstCommunicationTime', 'lastCommunicationTime', 'connectionParameters', 'deviceAttributes')
    DIN_FIELD_NUMBER: _ClassVar[int]
    PARTNUMBER_FIELD_NUMBER: _ClassVar[int]
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    SITELABEL_FIELD_NUMBER: _ClassVar[int]
    COMPONENTPARENTDIN_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREVERSION_FIELD_NUMBER: _ClassVar[int]
    FIRSTCOMMUNICATIONTIME_FIELD_NUMBER: _ClassVar[int]
    LASTCOMMUNICATIONTIME_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DEVICEATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    din: StringValue
    partNumber: StringValue
    serialNumber: StringValue
    manufacturer: StringValue
    siteLabel: StringValue
    componentParentDin: StringValue
    firmwareVersion: StringValue
    firstCommunicationTime: _timestamp_pb2.Timestamp
    lastCommunicationTime: _timestamp_pb2.Timestamp
    connectionParameters: ConnectionParameters
    deviceAttributes: DeviceAttributes

    def __init__(self, din: _Optional[_Union[StringValue, _Mapping]]=..., partNumber: _Optional[_Union[StringValue, _Mapping]]=..., serialNumber: _Optional[_Union[StringValue, _Mapping]]=..., manufacturer: _Optional[_Union[StringValue, _Mapping]]=..., siteLabel: _Optional[_Union[StringValue, _Mapping]]=..., componentParentDin: _Optional[_Union[StringValue, _Mapping]]=..., firmwareVersion: _Optional[_Union[StringValue, _Mapping]]=..., firstCommunicationTime: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., lastCommunicationTime: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., connectionParameters: _Optional[_Union[ConnectionParameters, _Mapping]]=..., deviceAttributes: _Optional[_Union[DeviceAttributes, _Mapping]]=...) -> None:
        ...

class SiteControllerConnectedDevice(_message.Message):
    __slots__ = ('device',)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: Device

    def __init__(self, device: _Optional[_Union[Device, _Mapping]]=...) -> None:
        ...

class SiteControllerConnectedDeviceWithVitals(_message.Message):
    __slots__ = ('device', 'vitals', 'alerts')
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    VITALS_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    device: SiteControllerConnectedDevice
    vitals: _containers.RepeatedCompositeFieldContainer[DeviceVital]
    alerts: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, device: _Optional[_Union[SiteControllerConnectedDevice, _Mapping]]=..., vitals: _Optional[_Iterable[_Union[DeviceVital, _Mapping]]]=..., alerts: _Optional[_Iterable[str]]=...) -> None:
        ...

class DevicesWithVitals(_message.Message):
    __slots__ = ('devices',)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[SiteControllerConnectedDeviceWithVitals]

    def __init__(self, devices: _Optional[_Iterable[_Union[SiteControllerConnectedDeviceWithVitals, _Mapping]]]=...) -> None:
        ...

class SiteControllerConnectedDeviceStore(_message.Message):
    __slots__ = ('siteControllerConnectedDevice',)
    SITECONTROLLERCONNECTEDDEVICE_FIELD_NUMBER: _ClassVar[int]
    siteControllerConnectedDevice: _containers.RepeatedCompositeFieldContainer[SiteControllerConnectedDevice]

    def __init__(self, siteControllerConnectedDevice: _Optional[_Iterable[_Union[SiteControllerConnectedDevice, _Mapping]]]=...) -> None:
        ...

class BatterySystemCapabilities(_message.Message):
    __slots__ = ('nominalEnergyWh', 'nominalPowerW')
    NOMINALENERGYWH_FIELD_NUMBER: _ClassVar[int]
    NOMINALPOWERW_FIELD_NUMBER: _ClassVar[int]
    nominalEnergyWh: int
    nominalPowerW: int

    def __init__(self, nominalEnergyWh: _Optional[int]=..., nominalPowerW: _Optional[int]=...) -> None:
        ...

class Status(_message.Message):
    __slots__ = ('code', 'message', 'details')
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    details: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]

    def __init__(self, code: _Optional[int]=..., message: _Optional[str]=..., details: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]]=...) -> None:
        ...

class Manifest(_message.Message):
    __slots__ = ('gatewayDin', 'trigger', 'generatedTime', 'device', 'batterySystemCapabilities', 'gatewayFirmwareVersion')
    GATEWAYDIN_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    GENERATEDTIME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    BATTERYSYSTEMCAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    GATEWAYFIRMWAREVERSION_FIELD_NUMBER: _ClassVar[int]
    gatewayDin: str
    trigger: int
    generatedTime: _timestamp_pb2.Timestamp
    device: _containers.RepeatedCompositeFieldContainer[Device]
    batterySystemCapabilities: BatterySystemCapabilities
    gatewayFirmwareVersion: StringValue

    def __init__(self, gatewayDin: _Optional[str]=..., trigger: _Optional[int]=..., generatedTime: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., device: _Optional[_Iterable[_Union[Device, _Mapping]]]=..., batterySystemCapabilities: _Optional[_Union[BatterySystemCapabilities, _Mapping]]=..., gatewayFirmwareVersion: _Optional[_Union[StringValue, _Mapping]]=...) -> None:
        ...

class MessageEnvelope(_message.Message):
    __slots__ = ('deliveryChannel', 'sender', 'recipient', 'common', 'teg', 'energysitenet')
    DELIVERYCHANNEL_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    COMMON_FIELD_NUMBER: _ClassVar[int]
    TEG_FIELD_NUMBER: _ClassVar[int]
    ENERGYSITENET_FIELD_NUMBER: _ClassVar[int]
    deliveryChannel: int
    sender: Participant
    recipient: Participant
    common: CommonMessages
    teg: TEGMessages
    energysitenet: EnergySiteNetMessages

    def __init__(self, deliveryChannel: _Optional[int]=..., sender: _Optional[_Union[Participant, _Mapping]]=..., recipient: _Optional[_Union[Participant, _Mapping]]=..., common: _Optional[_Union[CommonMessages, _Mapping]]=..., teg: _Optional[_Union[TEGMessages, _Mapping]]=..., energysitenet: _Optional[_Union[EnergySiteNetMessages, _Mapping]]=...) -> None:
        ...

class CommonMessages(_message.Message):
    __slots__ = ('errorResponse', 'getSystemInfoRequest', 'getSystemInfoResponse', 'setLocalSiteConfigRequest', 'setLocalSiteConfigResponse', 'performUpdateRequest', 'performUpdateResponse', 'factoryResetRequest', 'factoryResetResponse', 'wifiScanRequest', 'wifiScanResponse', 'configureWifiRequest', 'configureWifiResponse', 'checkForUpdateRequest', 'checkForUpdateResponse', 'clearUpdateRequest', 'clearUpdateResponse', 'deviceCertRequest', 'deviceCertResponse', 'configureWifiWithEncryptedPasswordRequest', 'configureWifiWithEncryptedPasswordResponse', 'getNetworkingStatusRequest', 'getNetworkingStatusResponse')
    ERRORRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETSYSTEMINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETSYSTEMINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    SETLOCALSITECONFIGREQUEST_FIELD_NUMBER: _ClassVar[int]
    SETLOCALSITECONFIGRESPONSE_FIELD_NUMBER: _ClassVar[int]
    PERFORMUPDATEREQUEST_FIELD_NUMBER: _ClassVar[int]
    PERFORMUPDATERESPONSE_FIELD_NUMBER: _ClassVar[int]
    FACTORYRESETREQUEST_FIELD_NUMBER: _ClassVar[int]
    FACTORYRESETRESPONSE_FIELD_NUMBER: _ClassVar[int]
    WIFISCANREQUEST_FIELD_NUMBER: _ClassVar[int]
    WIFISCANRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGUREWIFIREQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGUREWIFIRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECKFORUPDATEREQUEST_FIELD_NUMBER: _ClassVar[int]
    CHECKFORUPDATERESPONSE_FIELD_NUMBER: _ClassVar[int]
    CLEARUPDATEREQUEST_FIELD_NUMBER: _ClassVar[int]
    CLEARUPDATERESPONSE_FIELD_NUMBER: _ClassVar[int]
    DEVICECERTREQUEST_FIELD_NUMBER: _ClassVar[int]
    DEVICECERTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGUREWIFIWITHENCRYPTEDPASSWORDREQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIGUREWIFIWITHENCRYPTEDPASSWORDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETNETWORKINGSTATUSREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETNETWORKINGSTATUSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    errorResponse: int
    getSystemInfoRequest: CommonAPIGetSystemInfoRequest
    getSystemInfoResponse: CommonAPIGetSystemInfoResponse
    setLocalSiteConfigRequest: CommonAPISetLocalSiteConfigRequest
    setLocalSiteConfigResponse: CommonAPISetLocalSiteConfigResponse
    performUpdateRequest: CommonAPIPerformUpdateRequest
    performUpdateResponse: CommonAPIPerformUpdateResponse
    factoryResetRequest: CommonAPIFactoryResetRequest
    factoryResetResponse: CommonAPIFactoryResetResponse
    wifiScanRequest: CommonAPIWifiScanRequest
    wifiScanResponse: CommonAPIWifiScanResponse
    configureWifiRequest: CommonAPIConfigureWifiRequest
    configureWifiResponse: CommonAPIConfigureWifiResponse
    checkForUpdateRequest: CommonAPICheckForUpdateRequest
    checkForUpdateResponse: CommonAPICheckForUpdateResponse
    clearUpdateRequest: CommonAPIClearUpdateRequest
    clearUpdateResponse: CommonAPIClearUpdateResponse
    deviceCertRequest: CommonAPIDeviceCertRequest
    deviceCertResponse: CommonAPIDeviceCertResponse
    configureWifiWithEncryptedPasswordRequest: CommonAPIConfigureWifiWithEncryptedPasswordRequest
    configureWifiWithEncryptedPasswordResponse: CommonAPIConfigureWifiWithEncryptedPasswordResponse
    getNetworkingStatusRequest: CommonAPIGetNetworkingStatusRequest
    getNetworkingStatusResponse: CommonAPIGetNetworkingStatusResponse

    def __init__(self, errorResponse: _Optional[int]=..., getSystemInfoRequest: _Optional[_Union[CommonAPIGetSystemInfoRequest, _Mapping]]=..., getSystemInfoResponse: _Optional[_Union[CommonAPIGetSystemInfoResponse, _Mapping]]=..., setLocalSiteConfigRequest: _Optional[_Union[CommonAPISetLocalSiteConfigRequest, _Mapping]]=..., setLocalSiteConfigResponse: _Optional[_Union[CommonAPISetLocalSiteConfigResponse, _Mapping]]=..., performUpdateRequest: _Optional[_Union[CommonAPIPerformUpdateRequest, _Mapping]]=..., performUpdateResponse: _Optional[_Union[CommonAPIPerformUpdateResponse, _Mapping]]=..., factoryResetRequest: _Optional[_Union[CommonAPIFactoryResetRequest, _Mapping]]=..., factoryResetResponse: _Optional[_Union[CommonAPIFactoryResetResponse, _Mapping]]=..., wifiScanRequest: _Optional[_Union[CommonAPIWifiScanRequest, _Mapping]]=..., wifiScanResponse: _Optional[_Union[CommonAPIWifiScanResponse, _Mapping]]=..., configureWifiRequest: _Optional[_Union[CommonAPIConfigureWifiRequest, _Mapping]]=..., configureWifiResponse: _Optional[_Union[CommonAPIConfigureWifiResponse, _Mapping]]=..., checkForUpdateRequest: _Optional[_Union[CommonAPICheckForUpdateRequest, _Mapping]]=..., checkForUpdateResponse: _Optional[_Union[CommonAPICheckForUpdateResponse, _Mapping]]=..., clearUpdateRequest: _Optional[_Union[CommonAPIClearUpdateRequest, _Mapping]]=..., clearUpdateResponse: _Optional[_Union[CommonAPIClearUpdateResponse, _Mapping]]=..., deviceCertRequest: _Optional[_Union[CommonAPIDeviceCertRequest, _Mapping]]=..., deviceCertResponse: _Optional[_Union[CommonAPIDeviceCertResponse, _Mapping]]=..., configureWifiWithEncryptedPasswordRequest: _Optional[_Union[CommonAPIConfigureWifiWithEncryptedPasswordRequest, _Mapping]]=..., configureWifiWithEncryptedPasswordResponse: _Optional[_Union[CommonAPIConfigureWifiWithEncryptedPasswordResponse, _Mapping]]=..., getNetworkingStatusRequest: _Optional[_Union[CommonAPIGetNetworkingStatusRequest, _Mapping]]=..., getNetworkingStatusResponse: _Optional[_Union[CommonAPIGetNetworkingStatusResponse, _Mapping]]=...) -> None:
        ...

class TEGMessages(_message.Message):
    __slots__ = ('getConfigRequest', 'getConfigResponse', 'setIslandModeRequest', 'setIslandModeResponse', 'triggerIslandingBlackStartRequest', 'triggerIslandingBlackStartResponse', 'triggerAssetManifestUploadRequest', 'triggerAssetManifestUploadResponse')
    GETCONFIGREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETCONFIGRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SETISLANDMODEREQUEST_FIELD_NUMBER: _ClassVar[int]
    SETISLANDMODERESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGERISLANDINGBLACKSTARTREQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGERISLANDINGBLACKSTARTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRIGGERASSETMANIFESTUPLOADREQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGERASSETMANIFESTUPLOADRESPONSE_FIELD_NUMBER: _ClassVar[int]
    getConfigRequest: TEGAPIGetConfigRequest
    getConfigResponse: TEGAPIGetConfigResponse
    setIslandModeRequest: TEGAPISetIslandModeRequest
    setIslandModeResponse: TEGAPISetIslandModeResponse
    triggerIslandingBlackStartRequest: TEGAPITriggerIslandingBlackStartRequest
    triggerIslandingBlackStartResponse: TEGAPITriggerIslandingBlackStartResponse
    triggerAssetManifestUploadRequest: TEGAPITriggerAssetManifestUploadRequest
    triggerAssetManifestUploadResponse: TEGAPITriggerAssetManifestUploadResponse

    def __init__(self, getConfigRequest: _Optional[_Union[TEGAPIGetConfigRequest, _Mapping]]=..., getConfigResponse: _Optional[_Union[TEGAPIGetConfigResponse, _Mapping]]=..., setIslandModeRequest: _Optional[_Union[TEGAPISetIslandModeRequest, _Mapping]]=..., setIslandModeResponse: _Optional[_Union[TEGAPISetIslandModeResponse, _Mapping]]=..., triggerIslandingBlackStartRequest: _Optional[_Union[TEGAPITriggerIslandingBlackStartRequest, _Mapping]]=..., triggerIslandingBlackStartResponse: _Optional[_Union[TEGAPITriggerIslandingBlackStartResponse, _Mapping]]=..., triggerAssetManifestUploadRequest: _Optional[_Union[TEGAPITriggerAssetManifestUploadRequest, _Mapping]]=..., triggerAssetManifestUploadResponse: _Optional[_Union[TEGAPITriggerAssetManifestUploadResponse, _Mapping]]=...) -> None:
        ...

class TEGSettings(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPIGetConfigResponse(_message.Message):
    __slots__ = ('settings', 'wifiConfig', 'wifi', 'eth', 'gsm')
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    WIFICONFIG_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    ETH_FIELD_NUMBER: _ClassVar[int]
    GSM_FIELD_NUMBER: _ClassVar[int]
    settings: TEGSettings
    wifiConfig: WifiConfig
    wifi: NetworkInterface
    eth: NetworkInterface
    gsm: NetworkInterface

    def __init__(self, settings: _Optional[_Union[TEGSettings, _Mapping]]=..., wifiConfig: _Optional[_Union[WifiConfig, _Mapping]]=..., wifi: _Optional[_Union[NetworkInterface, _Mapping]]=..., eth: _Optional[_Union[NetworkInterface, _Mapping]]=..., gsm: _Optional[_Union[NetworkInterface, _Mapping]]=...) -> None:
        ...

class TEGAPITriggerIslandingBlackStartRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerIslandingBlackStartResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPISetIslandModeRequest(_message.Message):
    __slots__ = ('mode', 'force')
    MODE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    mode: int
    force: bool

    def __init__(self, mode: _Optional[int]=..., force: bool=...) -> None:
        ...

class TEGAPISetIslandModeResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int

    def __init__(self, result: _Optional[int]=...) -> None:
        ...

class TEGAPITriggerAssetManifestUploadRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TEGAPITriggerAssetManifestUploadResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EnergySiteNetMessages(_message.Message):
    __slots__ = ('addDeviceRequest', 'addDeviceResponse', 'removeDeviceRequest', 'removeDeviceResponse', 'getConfigRequest', 'getConfigResponse')
    ADDDEVICEREQUEST_FIELD_NUMBER: _ClassVar[int]
    ADDDEVICERESPONSE_FIELD_NUMBER: _ClassVar[int]
    REMOVEDEVICEREQUEST_FIELD_NUMBER: _ClassVar[int]
    REMOVEDEVICERESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETCONFIGREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETCONFIGRESPONSE_FIELD_NUMBER: _ClassVar[int]
    addDeviceRequest: EnergySiteNetAPIAddDeviceRequest
    addDeviceResponse: EnergySiteNetAPIAddDeviceResponse
    removeDeviceRequest: EnergySiteNetAPIRemoveDeviceRequest
    removeDeviceResponse: EnergySiteNetAPIRemoveDeviceResponse
    getConfigRequest: EnergySiteNetAPIGetConfigRequest
    getConfigResponse: EnergySiteNetAPIGetConfigResponse

    def __init__(self, addDeviceRequest: _Optional[_Union[EnergySiteNetAPIAddDeviceRequest, _Mapping]]=..., addDeviceResponse: _Optional[_Union[EnergySiteNetAPIAddDeviceResponse, _Mapping]]=..., removeDeviceRequest: _Optional[_Union[EnergySiteNetAPIRemoveDeviceRequest, _Mapping]]=..., removeDeviceResponse: _Optional[_Union[EnergySiteNetAPIRemoveDeviceResponse, _Mapping]]=..., getConfigRequest: _Optional[_Union[EnergySiteNetAPIGetConfigRequest, _Mapping]]=..., getConfigResponse: _Optional[_Union[EnergySiteNetAPIGetConfigResponse, _Mapping]]=...) -> None:
        ...

class LocalAuthAPIRequiredFactorsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LocalAuthAPIRequiredFactorsResponse(_message.Message):
    __slots__ = ('password', 'presence')
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    password: bool
    presence: bool

    def __init__(self, password: bool=..., presence: bool=...) -> None:
        ...

class LocalAuthAPILoginRequest(_message.Message):
    __slots__ = ('Participant', 'email', 'password')
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    Participant: int
    email: str
    password: WifiPassword

    def __init__(self, Participant: _Optional[int]=..., email: _Optional[str]=..., password: _Optional[_Union[WifiPassword, _Mapping]]=...) -> None:
        ...

class LocalAuthAPILoginResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int

    def __init__(self, result: _Optional[int]=...) -> None:
        ...

class LocalAuthAPILogoutRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LocalAuthAPILogoutResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LocalAuthAPICheckAuthStatusRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LocalAuthAPICheckAuthStatusResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int

    def __init__(self, result: _Optional[int]=...) -> None:
        ...