"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'networking.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10networking.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x1egoogle/protobuf/wrappers.proto"T\n\x04Rssi\x12\r\n\x05value\x18\x01 \x01(\x11\x12=\n\x17signal_strength_percent\x18\x02 \x01(\x0b2\x1c.google.protobuf.UInt32Value"\x1d\n\x0cWifiPassword\x12\r\n\x05value\x18\x01 \x01(\t"\xa6\x01\n\nWifiConfig\x12\x0c\n\x04ssid\x18\x01 \x01(\t\x12<\n\x08password\x18\x02 \x01(\x0b2*.tesla.proto.energy_device.v1.WifiPassword\x12L\n\rsecurity_type\x18\x03 \x01(\x0e25.tesla.proto.energy_device.v1.WifiNetworkSecurityType"\xad\x01\n\x0bWifiNetwork\x12\x0c\n\x04ssid\x18\x01 \x01(\t\x12\x11\n\trssiValue\x18\x02 \x01(\x11\x120\n\x04rssi\x18\x03 \x01(\x0b2".tesla.proto.energy_device.v1.Rssi\x12K\n\x0csecurityType\x18\x04 \x01(\x0e25.tesla.proto.energy_device.v1.WifiNetworkSecurityType"|\n\x1aNetworkInterfaceIPv4Config\x12\x14\n\x0cdhcp_enabled\x18\x02 \x01(\x08\x12\x0f\n\x07address\x18\x03 \x01(\x07\x12\x13\n\x0bsubnet_mask\x18\x04 \x01(\x07\x12\x0f\n\x07gateway\x18\x05 \x01(\x07\x12\x0b\n\x03dns\x18\x06 \x03(\x07J\x04\x08\x01\x10\x02"\xc8\x01\n\x19NetworkConnectivityStatus\x12\x1a\n\x12connected_physical\x18\x01 \x01(\x08\x12\x1a\n\x12connected_internet\x18\x02 \x01(\x08\x12\x17\n\x0fconnected_tesla\x18\x03 \x01(\x08\x120\n\x04rssi\x18\x04 \x01(\x0b2".tesla.proto.energy_device.v1.Rssi\x12(\n\x03snr\x18\x05 \x01(\x0b2\x1b.google.protobuf.Int32Value"\xf3\x01\n\x10NetworkInterface\x12\x13\n\x0bmac_address\x18\x01 \x01(\x0c\x12\x0f\n\x07enabled\x18\x02 \x01(\x08\x12\x14\n\x0cactive_route\x18\x03 \x01(\x08\x12M\n\x0bipv4_config\x18\x04 \x01(\x0b28.tesla.proto.energy_device.v1.NetworkInterfaceIPv4Config\x12T\n\x13connectivity_status\x18\x05 \x01(\x0b27.tesla.proto.energy_device.v1.NetworkConnectivityStatus"\x1c\n\x0bCellularEID\x12\r\n\x05value\x18\x01 \x01(\t*\xf0\x01\n\x17WifiNetworkSecurityType\x12&\n"WIFI_NETWORK_SECURITY_TYPE_INVALID\x10\x00\x12#\n\x1fWIFI_NETWORK_SECURITY_TYPE_NONE\x10\x01\x12*\n&WIFI_NETWORK_SECURITY_TYPE_DYNAMIC_WEP\x10\x02\x12,\n(WIFI_NETWORK_SECURITY_TYPE_WPA2_PERSONAL\x10\x03\x12.\n*WIFI_NETWORK_SECURITY_TYPE_WPA2_ENTERPRISE\x10\x04*\xe9\x01\n\x13WifiConfigureResult\x12!\n\x1dWIFI_CONFIGURE_RESULT_INVALID\x10\x00\x12!\n\x1dWIFI_CONFIGURE_RESULT_SUCCESS\x10\x01\x12)\n%WIFI_CONFIGURE_RESULT_FAILURE_GENERIC\x10\x02\x124\n0WIFI_CONFIGURE_RESULT_FAILED_WITH_INVALID_CONFIG\x10\x03\x12+\n\'WIFI_CONFIGURE_RESULT_FAILED_TO_CONNECT\x10\x04*\xc6\x02\n\x13CellularProfileType\x12!\n\x1dCELLULAR_PROFILE_TYPE_INVALID\x10\x00\x12 \n\x1cCELLULAR_PROFILE_TYPE_TWILIO\x10\x01\x12\x1d\n\x19CELLULAR_PROFILE_TYPE_ATT\x10\x02\x12\x1d\n\x19CELLULAR_PROFILE_TYPE_KPN\x10\x03\x12$\n CELLULAR_PROFILE_TYPE_TELEFONICA\x10\x04\x12!\n\x1dCELLULAR_PROFILE_TYPE_TELSTRA\x10\x05\x12\x1f\n\x1bCELLULAR_PROFILE_TYPE_TELUS\x10\x06\x12 \n\x1cCELLULAR_PROFILE_TYPE_DOCOMO\x10\x07\x12 \n\x1cCELLULAR_PROFILE_TYPE_UNICOM\x10\x08*\xd4\x02\n\x12NetworkDeviceState\x12 \n\x1cNETWORK_DEVICE_STATE_INVALID\x10\x00\x12"\n\x1eNETWORK_DEVICE_STATE_UNMANAGED\x10\x01\x12$\n NETWORK_DEVICE_STATE_UNAVAILABLE\x10\x02\x12\x1d\n\x19NETWORK_DEVICE_STATE_IDLE\x10\x03\x12$\n NETWORK_DEVICE_STATE_ASSOCIATION\x10\x04\x12&\n"NETWORK_DEVICE_STATE_CONFIGURATION\x10\x05\x12\x1e\n\x1aNETWORK_DEVICE_STATE_READY\x10\x06\x12#\n\x1fNETWORK_DEVICE_STATE_DISCONNECT\x10\x07\x12 \n\x1cNETWORK_DEVICE_STATE_FAILURE\x10\x08*\x91\x06\n\x18NetworkDeviceStateReason\x12\'\n#NETWORK_DEVICE_STATE_REASON_INVALID\x10\x00\x12$\n NETWORK_DEVICE_STATE_REASON_NONE\x10\x01\x12-\n)NETWORK_DEVICE_STATE_REASON_CONFIG_FAILED\x10\x02\x12+\n\'NETWORK_DEVICE_STATE_REASON_DHCP_FAILED\x10\x03\x124\n0NETWORK_DEVICE_STATE_REASON_IP_ADDRESS_DUPLICATE\x10\x04\x121\n-NETWORK_DEVICE_STATE_REASON_IP_CONFIG_EXPIRED\x10\x05\x125\n1NETWORK_DEVICE_STATE_REASON_IP_CONFIG_UNAVAILABLE\x10\x06\x125\n1NETWORK_DEVICE_STATE_REASON_IP_METHOD_UNSUPPORTED\x10\x07\x12.\n*NETWORK_DEVICE_STATE_REASON_NEW_ACTIVATION\x10\x08\x12*\n&NETWORK_DEVICE_STATE_REASON_NO_SECRETS\x10\t\x12*\n&NETWORK_DEVICE_STATE_REASON_PPP_FAILED\x10\n\x12.\n*NETWORK_DEVICE_STATE_REASON_SSID_NOT_FOUND\x10\x0b\x121\n-NETWORK_DEVICE_STATE_REASON_SIM_PIN_INCORRECT\x10\x0c\x121\n-NETWORK_DEVICE_STATE_REASON_SUPPLICANT_FAILED\x10\r\x12\'\n#NETWORK_DEVICE_STATE_REASON_REMOVED\x10\x0e\x12,\n(NETWORK_DEVICE_STATE_REASON_MODEM_FAILED\x10\x0fB~\n$com.tesla.generated.energy_device.v1B\nNetworkingZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'networking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\nNetworkingZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_WIFINETWORKSECURITYTYPE']._serialized_start = 1150
    _globals['_WIFINETWORKSECURITYTYPE']._serialized_end = 1390
    _globals['_WIFICONFIGURERESULT']._serialized_start = 1393
    _globals['_WIFICONFIGURERESULT']._serialized_end = 1626
    _globals['_CELLULARPROFILETYPE']._serialized_start = 1629
    _globals['_CELLULARPROFILETYPE']._serialized_end = 1955
    _globals['_NETWORKDEVICESTATE']._serialized_start = 1958
    _globals['_NETWORKDEVICESTATE']._serialized_end = 2298
    _globals['_NETWORKDEVICESTATEREASON']._serialized_start = 2301
    _globals['_NETWORKDEVICESTATEREASON']._serialized_end = 3086
    _globals['_RSSI']._serialized_start = 82
    _globals['_RSSI']._serialized_end = 166
    _globals['_WIFIPASSWORD']._serialized_start = 168
    _globals['_WIFIPASSWORD']._serialized_end = 197
    _globals['_WIFICONFIG']._serialized_start = 200
    _globals['_WIFICONFIG']._serialized_end = 366
    _globals['_WIFINETWORK']._serialized_start = 369
    _globals['_WIFINETWORK']._serialized_end = 542
    _globals['_NETWORKINTERFACEIPV4CONFIG']._serialized_start = 544
    _globals['_NETWORKINTERFACEIPV4CONFIG']._serialized_end = 668
    _globals['_NETWORKCONNECTIVITYSTATUS']._serialized_start = 671
    _globals['_NETWORKCONNECTIVITYSTATUS']._serialized_end = 871
    _globals['_NETWORKINTERFACE']._serialized_start = 874
    _globals['_NETWORKINTERFACE']._serialized_end = 1117
    _globals['_CELLULAREID']._serialized_start = 1119
    _globals['_CELLULAREID']._serialized_end = 1147