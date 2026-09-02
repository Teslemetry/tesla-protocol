"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 5, '', 'common_api.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import networking_pb2 as networking__pb2
from . import device_pb2 as device__pb2
from . import update_pb2 as update__pb2
from . import error_pb2 as error__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10common_api.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x10networking.proto\x1a\x0cdevice.proto\x1a\x0cupdate.proto\x1a\x0berror.proto"\x1f\n\x1dCommonAPIGetSystemInfoRequest"\xd3\x01\n\x15RadioLegalInformation\x122\n\x0cmanufacturer\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12+\n\x05model\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12,\n\x06fcc_id\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValue\x12+\n\x05ic_id\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue"m\n\x15ComplianceInformation\x12T\n\x17radio_legal_information\x18\x01 \x03(\x0b23.tesla.proto.energy_device.v1.RadioLegalInformation"\xd2\x02\n\x1eCommonAPIGetSystemInfoResponse\x126\n\tdevice_id\x18\x01 \x01(\x0b2#.tesla.proto.energy_device.v1.EcuId\x12.\n\x03din\x18\x02 \x01(\x0b2!.tesla.proto.energy_device.v1.Din\x12F\n\x0ffirmare_version\x18\x03 \x01(\x0b2-.tesla.proto.energy_device.v1.FirmwareVersion\x12A\n\rsystem_update\x18\x04 \x01(\x0b2*.tesla.proto.energy_device.v1.SystemUpdate\x12=\n\x0bdevice_type\x18\x05 \x01(\x0e2(.tesla.proto.energy_device.v1.DeviceType"$\n"CommonAPISetLocalSiteConfigRequest"%\n#CommonAPISetLocalSiteConfigResponse"\x1f\n\x1dCommonAPIPerformUpdateRequest" \n\x1eCommonAPIPerformUpdateResponse"\x1e\n\x1cCommonAPIFactoryResetRequest"\x1f\n\x1dCommonAPIFactoryResetResponse"\xa9\x01\n\x18CommonAPIWifiScanRequest\x12\x1b\n\x13max_scan_duration_s\x18\x01 \x01(\r\x12U\n\x16desired_security_types\x18\x02 \x03(\x0e25.tesla.proto.energy_device.v1.WifiNetworkSecurityType\x12\x19\n\x11maximum_total_aps\x18\x03 \x01(\r"]\n\x19CommonAPIWifiScanResponse\x12@\n\rwifi_networks\x18\x01 \x03(\x0b2).tesla.proto.energy_device.v1.WifiNetwork"o\n\x1dCommonAPIConfigureWifiRequest\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12=\n\x0bwifi_config\x18\x02 \x01(\x0b2(.tesla.proto.energy_device.v1.WifiConfig"\x9d\x01\n\x1eCommonAPIConfigureWifiResponse\x12=\n\x0bwifi_config\x18\x01 \x01(\x0b2(.tesla.proto.energy_device.v1.WifiConfig\x12<\n\x04wifi\x18\x02 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface"\xd0\x01\n2CommonAPIConfigureWifiWithEncryptedPasswordRequest\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12=\n\x0bwifi_config\x18\x02 \x01(\x0b2(.tesla.proto.energy_device.v1.WifiConfig\x12J\n\x12encrypted_password\x18\x03 \x01(\x0b2..tesla.proto.energy_device.v1.EncryptedMessage"\xc2\x01\n3CommonAPIConfigureWifiWithEncryptedPasswordResponse\x12=\n\x0bwifi_config\x18\x01 \x01(\x0b2(.tesla.proto.energy_device.v1.WifiConfig\x12<\n\x04wifi\x18\x02 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12\x0e\n\x06result\x18\x03 \x01(\x05"?\n\x1eCommonAPICheckForUpdateRequest\x12\x1d\n\x15download_if_available\x18\x01 \x01(\x08"!\n\x1fCommonAPICheckForUpdateResponse"\'\n%CommonAPICheckForUpdateUrgencyRequest"(\n&CommonAPICheckForUpdateUrgencyResponse"\x1d\n\x1bCommonAPIClearUpdateRequest"\x1e\n\x1cCommonAPIClearUpdateResponse"\x1c\n\x1aCommonAPIDeviceCertRequest"r\n\x1bCommonAPIDeviceCertResponse\x12>\n\x06format\x18\x01 \x01(\x0e2..tesla.proto.energy_device.v1.DeviceCertFormat\x12\x13\n\x0bdevice_cert\x18\x02 \x01(\x0c"%\n#CommonAPIGetNetworkingStatusRequest"\x9d\x02\n$CommonAPIGetNetworkingStatusResponse\x12=\n\x0bwifi_config\x18\x01 \x01(\x0b2(.tesla.proto.energy_device.v1.WifiConfig\x12<\n\x04wifi\x18\x02 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12;\n\x03eth\x18\x03 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12;\n\x03gsm\x18\x04 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface"!\n\x1fCommonAPIGetCellularInfoRequest"v\n CommonAPIGetCellularInfoResponse\x126\n\x03eid\x18\x01 \x01(\x0b2).tesla.proto.energy_device.v1.CellularEID\x12\x1a\n\x12supported_profiles\x18\x02 \x03(\x05"r\n!CommonAPIConfigureEthernetRequest\x12M\n\x0bipv4_config\x18\x01 \x01(\x0b28.tesla.proto.energy_device.v1.NetworkInterfaceIPv4Config"a\n"CommonAPIConfigureEthernetResponse\x12;\n\x03eth\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface"1\n!CommonAPIForgetWifiNetworkRequest\x12\x0c\n\x04ssid\x18\x01 \x01(\t"$\n"CommonAPIForgetWifiNetworkResponse"\x1f\n\x1dCommonAPICheckInternetRequest"\xd8\x01\n\x1eCommonAPICheckInternetResponse\x12<\n\x04wifi\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12;\n\x03eth\x18\x02 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12;\n\x03gsm\x18\x03 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface"\x98\x01\n;CommonAPINegotiateUpdateWithLocallyAvailablePackagesRequest\x12Y\n\x1alocally_available_packages\x18\x01 \x03(\x0b25.tesla.proto.energy_device.v1.LocallyAvailablePackage"\x88\x01\n<CommonAPINegotiateUpdateWithLocallyAvailablePackagesResponse\x12H\n\x11accepted_packages\x18\x01 \x03(\x0b2-.tesla.proto.energy_device.v1.AcceptedPackage"\x96\x01\n9CommonAPIPerformUpdateFromLocallyAvailablePackagesRequest\x12Y\n\x1alocally_available_packages\x18\x01 \x03(\x0b25.tesla.proto.energy_device.v1.LocallyAvailablePackage"\x86\x01\n:CommonAPIPerformUpdateFromLocallyAvailablePackagesResponse\x12H\n\x11accepted_packages\x18\x01 \x03(\x0b2-.tesla.proto.energy_device.v1.AcceptedPackage"P\n*CommonAPIPrepareRegistrationPayloadRequest\x12"\n\x1acustomer_registration_info\x18\x01 \x01(\x0c"\x85\x01\n+CommonAPIPrepareRegistrationPayloadResponse\x12V\n\x1bsigned_registration_payload\x18\x01 \x01(\x0b21.tesla.proto.energy_device.v1.DeviceSignedPayload"\xcd\x01\n\x0bTcpdumpInfo\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0b\n\x03pid\x18\x02 \x01(\x03\x12\x11\n\tinterface\x18\x03 \x01(\t\x12\x12\n\nexpression\x18\x04 \x01(\t\x12+\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12/\n\x0cmax_duration\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0c\n\x04size\x18\x07 \x01(\x04\x12\x10\n\x08max_size\x18\x08 \x01(\x04"\x96\x01\n\x1cCommonAPIStartTcpdumpRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tinterface\x18\x02 \x01(\t\x12\x12\n\nexpression\x18\x03 \x01(\t\x12/\n\x0cmax_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x10\n\x08max_size\x18\x05 \x01(\x04"\x1f\n\x1dCommonAPIStartTcpdumpResponse";\n\x1bCommonAPIStopTcpdumpRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06remove\x18\x02 \x01(\x08"\x1e\n\x1cCommonAPIStopTcpdumpResponse" \n\x1eCommonAPIGetTcpdumpInfoRequest"n\n\x1fCommonAPIGetTcpdumpInfoResponse\x127\n\x04list\x18\x01 \x03(\x0b2).tesla.proto.energy_device.v1.TcpdumpInfo\x12\x12\n\ndisk_quota\x18\x02 \x01(\x03"\xc6%\n\x0eCommonMessages\x12C\n\x0eerror_response\x18\x01 \x01(\x0b2+.tesla.proto.energy_device.v1.ErrorResponse\x12^\n\x17get_system_info_request\x18\x02 \x01(\x0b2;.tesla.proto.energy_device.v1.CommonAPIGetSystemInfoRequestH\x00\x12`\n\x18get_system_info_response\x18\x03 \x01(\x0b2<.tesla.proto.energy_device.v1.CommonAPIGetSystemInfoResponseH\x00\x12i\n\x1dset_local_site_config_request\x18\x04 \x01(\x0b2@.tesla.proto.energy_device.v1.CommonAPISetLocalSiteConfigRequestH\x00\x12k\n\x1eset_local_site_config_response\x18\x05 \x01(\x0b2A.tesla.proto.energy_device.v1.CommonAPISetLocalSiteConfigResponseH\x00\x12]\n\x16perform_update_request\x18\x06 \x01(\x0b2;.tesla.proto.energy_device.v1.CommonAPIPerformUpdateRequestH\x00\x12_\n\x17perform_update_response\x18\x07 \x01(\x0b2<.tesla.proto.energy_device.v1.CommonAPIPerformUpdateResponseH\x00\x12[\n\x15factory_reset_request\x18\x08 \x01(\x0b2:.tesla.proto.energy_device.v1.CommonAPIFactoryResetRequestH\x00\x12]\n\x16factory_reset_response\x18\t \x01(\x0b2;.tesla.proto.energy_device.v1.CommonAPIFactoryResetResponseH\x00\x12S\n\x11wifi_scan_request\x18\n \x01(\x0b26.tesla.proto.energy_device.v1.CommonAPIWifiScanRequestH\x00\x12U\n\x12wifi_scan_response\x18\x0b \x01(\x0b27.tesla.proto.energy_device.v1.CommonAPIWifiScanResponseH\x00\x12]\n\x16configure_wifi_request\x18\x0c \x01(\x0b2;.tesla.proto.energy_device.v1.CommonAPIConfigureWifiRequestH\x00\x12_\n\x17configure_wifi_response\x18\r \x01(\x0b2<.tesla.proto.energy_device.v1.CommonAPIConfigureWifiResponseH\x00\x12`\n\x18check_for_update_request\x18\x0e \x01(\x0b2<.tesla.proto.energy_device.v1.CommonAPICheckForUpdateRequestH\x00\x12b\n\x19check_for_update_response\x18\x0f \x01(\x0b2=.tesla.proto.energy_device.v1.CommonAPICheckForUpdateResponseH\x00\x12Y\n\x14clear_update_request\x18\x10 \x01(\x0b29.tesla.proto.energy_device.v1.CommonAPIClearUpdateRequestH\x00\x12[\n\x15clear_update_response\x18\x11 \x01(\x0b2:.tesla.proto.energy_device.v1.CommonAPIClearUpdateResponseH\x00\x12W\n\x13device_cert_request\x18\x12 \x01(\x0b28.tesla.proto.energy_device.v1.CommonAPIDeviceCertRequestH\x00\x12Y\n\x14device_cert_response\x18\x13 \x01(\x0b29.tesla.proto.energy_device.v1.CommonAPIDeviceCertResponseH\x00\x12\x8a\x01\n.configure_wifi_with_encrypted_password_request\x18\x14 \x01(\x0b2P.tesla.proto.energy_device.v1.CommonAPIConfigureWifiWithEncryptedPasswordRequestH\x00\x12\x8c\x01\n/configure_wifi_with_encrypted_password_response\x18\x15 \x01(\x0b2Q.tesla.proto.energy_device.v1.CommonAPIConfigureWifiWithEncryptedPasswordResponseH\x00\x12j\n\x1dget_networking_status_request\x18\x16 \x01(\x0b2A.tesla.proto.energy_device.v1.CommonAPIGetNetworkingStatusRequestH\x00\x12l\n\x1eget_networking_status_response\x18\x17 \x01(\x0b2B.tesla.proto.energy_device.v1.CommonAPIGetNetworkingStatusResponseH\x00\x12b\n\x19get_cellular_info_request\x18\x18 \x01(\x0b2=.tesla.proto.energy_device.v1.CommonAPIGetCellularInfoRequestH\x00\x12d\n\x1aget_cellular_info_response\x18\x19 \x01(\x0b2>.tesla.proto.energy_device.v1.CommonAPIGetCellularInfoResponseH\x00\x12e\n\x1aconfigure_ethernet_request\x18\x1a \x01(\x0b2?.tesla.proto.energy_device.v1.CommonAPIConfigureEthernetRequestH\x00\x12g\n\x1bconfigure_ethernet_response\x18\x1b \x01(\x0b2@.tesla.proto.energy_device.v1.CommonAPIConfigureEthernetResponseH\x00\x12f\n\x1bforget_wifi_network_request\x18\x1c \x01(\x0b2?.tesla.proto.energy_device.v1.CommonAPIForgetWifiNetworkRequestH\x00\x12h\n\x1cforget_wifi_network_response\x18\x1d \x01(\x0b2@.tesla.proto.energy_device.v1.CommonAPIForgetWifiNetworkResponseH\x00\x12]\n\x16check_internet_request\x18\x1e \x01(\x0b2;.tesla.proto.energy_device.v1.CommonAPICheckInternetRequestH\x00\x12_\n\x17check_internet_response\x18\x1f \x01(\x0b2<.tesla.proto.energy_device.v1.CommonAPICheckInternetResponseH\x00\x12o\n check_for_update_urgency_request\x18  \x01(\x0b2C.tesla.proto.energy_device.v1.CommonAPICheckForUpdateUrgencyRequestH\x00\x12q\n!check_for_update_urgency_response\x18! \x01(\x0b2D.tesla.proto.energy_device.v1.CommonAPICheckForUpdateUrgencyResponseH\x00\x12\x9d\x01\n8negotiate_update_with_locally_available_packages_request\x18" \x01(\x0b2Y.tesla.proto.energy_device.v1.CommonAPINegotiateUpdateWithLocallyAvailablePackagesRequestH\x00\x12\x9f\x01\n9negotiate_update_with_locally_available_packages_response\x18# \x01(\x0b2Z.tesla.proto.energy_device.v1.CommonAPINegotiateUpdateWithLocallyAvailablePackagesResponseH\x00\x12x\n$prepare_registration_payload_request\x18$ \x01(\x0b2H.tesla.proto.energy_device.v1.CommonAPIPrepareRegistrationPayloadRequestH\x00\x12z\n%prepare_registration_payload_response\x18% \x01(\x0b2I.tesla.proto.energy_device.v1.CommonAPIPrepareRegistrationPayloadResponseH\x00\x12\x99\x01\n6perform_update_from_locally_available_packages_request\x18& \x01(\x0b2W.tesla.proto.energy_device.v1.CommonAPIPerformUpdateFromLocallyAvailablePackagesRequestH\x00\x12\x9b\x01\n7perform_update_from_locally_available_packages_response\x18\' \x01(\x0b2X.tesla.proto.energy_device.v1.CommonAPIPerformUpdateFromLocallyAvailablePackagesResponseH\x00\x12[\n\x15start_tcpdump_request\x18. \x01(\x0b2:.tesla.proto.energy_device.v1.CommonAPIStartTcpdumpRequestH\x00\x12]\n\x16start_tcpdump_response\x18/ \x01(\x0b2;.tesla.proto.energy_device.v1.CommonAPIStartTcpdumpResponseH\x00\x12Y\n\x14stop_tcpdump_request\x180 \x01(\x0b29.tesla.proto.energy_device.v1.CommonAPIStopTcpdumpRequestH\x00\x12[\n\x15stop_tcpdump_response\x181 \x01(\x0b2:.tesla.proto.energy_device.v1.CommonAPIStopTcpdumpResponseH\x00\x12`\n\x18get_tcpdump_info_request\x182 \x01(\x0b2<.tesla.proto.energy_device.v1.CommonAPIGetTcpdumpInfoRequestH\x00\x12b\n\x19get_tcpdump_info_response\x183 \x01(\x0b2=.tesla.proto.energy_device.v1.CommonAPIGetTcpdumpInfoResponseH\x00B\t\n\x07messageB}\n$com.tesla.generated.energy_device.v1B\tCommonApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\tCommonApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_COMMONAPIGETSYSTEMINFOREQUEST']._serialized_start = 173
    _globals['_COMMONAPIGETSYSTEMINFOREQUEST']._serialized_end = 204
    _globals['_RADIOLEGALINFORMATION']._serialized_start = 207
    _globals['_RADIOLEGALINFORMATION']._serialized_end = 418
    _globals['_COMPLIANCEINFORMATION']._serialized_start = 420
    _globals['_COMPLIANCEINFORMATION']._serialized_end = 529
    _globals['_COMMONAPIGETSYSTEMINFORESPONSE']._serialized_start = 532
    _globals['_COMMONAPIGETSYSTEMINFORESPONSE']._serialized_end = 870
    _globals['_COMMONAPISETLOCALSITECONFIGREQUEST']._serialized_start = 872
    _globals['_COMMONAPISETLOCALSITECONFIGREQUEST']._serialized_end = 908
    _globals['_COMMONAPISETLOCALSITECONFIGRESPONSE']._serialized_start = 910
    _globals['_COMMONAPISETLOCALSITECONFIGRESPONSE']._serialized_end = 947
    _globals['_COMMONAPIPERFORMUPDATEREQUEST']._serialized_start = 949
    _globals['_COMMONAPIPERFORMUPDATEREQUEST']._serialized_end = 980
    _globals['_COMMONAPIPERFORMUPDATERESPONSE']._serialized_start = 982
    _globals['_COMMONAPIPERFORMUPDATERESPONSE']._serialized_end = 1014
    _globals['_COMMONAPIFACTORYRESETREQUEST']._serialized_start = 1016
    _globals['_COMMONAPIFACTORYRESETREQUEST']._serialized_end = 1046
    _globals['_COMMONAPIFACTORYRESETRESPONSE']._serialized_start = 1048
    _globals['_COMMONAPIFACTORYRESETRESPONSE']._serialized_end = 1079
    _globals['_COMMONAPIWIFISCANREQUEST']._serialized_start = 1082
    _globals['_COMMONAPIWIFISCANREQUEST']._serialized_end = 1251
    _globals['_COMMONAPIWIFISCANRESPONSE']._serialized_start = 1253
    _globals['_COMMONAPIWIFISCANRESPONSE']._serialized_end = 1346
    _globals['_COMMONAPICONFIGUREWIFIREQUEST']._serialized_start = 1348
    _globals['_COMMONAPICONFIGUREWIFIREQUEST']._serialized_end = 1459
    _globals['_COMMONAPICONFIGUREWIFIRESPONSE']._serialized_start = 1462
    _globals['_COMMONAPICONFIGUREWIFIRESPONSE']._serialized_end = 1619
    _globals['_COMMONAPICONFIGUREWIFIWITHENCRYPTEDPASSWORDREQUEST']._serialized_start = 1622
    _globals['_COMMONAPICONFIGUREWIFIWITHENCRYPTEDPASSWORDREQUEST']._serialized_end = 1830
    _globals['_COMMONAPICONFIGUREWIFIWITHENCRYPTEDPASSWORDRESPONSE']._serialized_start = 1833
    _globals['_COMMONAPICONFIGUREWIFIWITHENCRYPTEDPASSWORDRESPONSE']._serialized_end = 2027
    _globals['_COMMONAPICHECKFORUPDATEREQUEST']._serialized_start = 2029
    _globals['_COMMONAPICHECKFORUPDATEREQUEST']._serialized_end = 2092
    _globals['_COMMONAPICHECKFORUPDATERESPONSE']._serialized_start = 2094
    _globals['_COMMONAPICHECKFORUPDATERESPONSE']._serialized_end = 2127
    _globals['_COMMONAPICHECKFORUPDATEURGENCYREQUEST']._serialized_start = 2129
    _globals['_COMMONAPICHECKFORUPDATEURGENCYREQUEST']._serialized_end = 2168
    _globals['_COMMONAPICHECKFORUPDATEURGENCYRESPONSE']._serialized_start = 2170
    _globals['_COMMONAPICHECKFORUPDATEURGENCYRESPONSE']._serialized_end = 2210
    _globals['_COMMONAPICLEARUPDATEREQUEST']._serialized_start = 2212
    _globals['_COMMONAPICLEARUPDATEREQUEST']._serialized_end = 2241
    _globals['_COMMONAPICLEARUPDATERESPONSE']._serialized_start = 2243
    _globals['_COMMONAPICLEARUPDATERESPONSE']._serialized_end = 2273
    _globals['_COMMONAPIDEVICECERTREQUEST']._serialized_start = 2275
    _globals['_COMMONAPIDEVICECERTREQUEST']._serialized_end = 2303
    _globals['_COMMONAPIDEVICECERTRESPONSE']._serialized_start = 2305
    _globals['_COMMONAPIDEVICECERTRESPONSE']._serialized_end = 2419
    _globals['_COMMONAPIGETNETWORKINGSTATUSREQUEST']._serialized_start = 2421
    _globals['_COMMONAPIGETNETWORKINGSTATUSREQUEST']._serialized_end = 2458
    _globals['_COMMONAPIGETNETWORKINGSTATUSRESPONSE']._serialized_start = 2461
    _globals['_COMMONAPIGETNETWORKINGSTATUSRESPONSE']._serialized_end = 2746
    _globals['_COMMONAPIGETCELLULARINFOREQUEST']._serialized_start = 2748
    _globals['_COMMONAPIGETCELLULARINFOREQUEST']._serialized_end = 2781
    _globals['_COMMONAPIGETCELLULARINFORESPONSE']._serialized_start = 2783
    _globals['_COMMONAPIGETCELLULARINFORESPONSE']._serialized_end = 2901
    _globals['_COMMONAPICONFIGUREETHERNETREQUEST']._serialized_start = 2903
    _globals['_COMMONAPICONFIGUREETHERNETREQUEST']._serialized_end = 3017
    _globals['_COMMONAPICONFIGUREETHERNETRESPONSE']._serialized_start = 3019
    _globals['_COMMONAPICONFIGUREETHERNETRESPONSE']._serialized_end = 3116
    _globals['_COMMONAPIFORGETWIFINETWORKREQUEST']._serialized_start = 3118
    _globals['_COMMONAPIFORGETWIFINETWORKREQUEST']._serialized_end = 3167
    _globals['_COMMONAPIFORGETWIFINETWORKRESPONSE']._serialized_start = 3169
    _globals['_COMMONAPIFORGETWIFINETWORKRESPONSE']._serialized_end = 3205
    _globals['_COMMONAPICHECKINTERNETREQUEST']._serialized_start = 3207
    _globals['_COMMONAPICHECKINTERNETREQUEST']._serialized_end = 3238
    _globals['_COMMONAPICHECKINTERNETRESPONSE']._serialized_start = 3241
    _globals['_COMMONAPICHECKINTERNETRESPONSE']._serialized_end = 3457
    _globals['_COMMONAPINEGOTIATEUPDATEWITHLOCALLYAVAILABLEPACKAGESREQUEST']._serialized_start = 3460
    _globals['_COMMONAPINEGOTIATEUPDATEWITHLOCALLYAVAILABLEPACKAGESREQUEST']._serialized_end = 3612
    _globals['_COMMONAPINEGOTIATEUPDATEWITHLOCALLYAVAILABLEPACKAGESRESPONSE']._serialized_start = 3615
    _globals['_COMMONAPINEGOTIATEUPDATEWITHLOCALLYAVAILABLEPACKAGESRESPONSE']._serialized_end = 3751
    _globals['_COMMONAPIPERFORMUPDATEFROMLOCALLYAVAILABLEPACKAGESREQUEST']._serialized_start = 3754
    _globals['_COMMONAPIPERFORMUPDATEFROMLOCALLYAVAILABLEPACKAGESREQUEST']._serialized_end = 3904
    _globals['_COMMONAPIPERFORMUPDATEFROMLOCALLYAVAILABLEPACKAGESRESPONSE']._serialized_start = 3907
    _globals['_COMMONAPIPERFORMUPDATEFROMLOCALLYAVAILABLEPACKAGESRESPONSE']._serialized_end = 4041
    _globals['_COMMONAPIPREPAREREGISTRATIONPAYLOADREQUEST']._serialized_start = 4043
    _globals['_COMMONAPIPREPAREREGISTRATIONPAYLOADREQUEST']._serialized_end = 4123
    _globals['_COMMONAPIPREPAREREGISTRATIONPAYLOADRESPONSE']._serialized_start = 4126
    _globals['_COMMONAPIPREPAREREGISTRATIONPAYLOADRESPONSE']._serialized_end = 4259
    _globals['_TCPDUMPINFO']._serialized_start = 4262
    _globals['_TCPDUMPINFO']._serialized_end = 4467
    _globals['_COMMONAPISTARTTCPDUMPREQUEST']._serialized_start = 4470
    _globals['_COMMONAPISTARTTCPDUMPREQUEST']._serialized_end = 4620
    _globals['_COMMONAPISTARTTCPDUMPRESPONSE']._serialized_start = 4622
    _globals['_COMMONAPISTARTTCPDUMPRESPONSE']._serialized_end = 4653
    _globals['_COMMONAPISTOPTCPDUMPREQUEST']._serialized_start = 4655
    _globals['_COMMONAPISTOPTCPDUMPREQUEST']._serialized_end = 4714
    _globals['_COMMONAPISTOPTCPDUMPRESPONSE']._serialized_start = 4716
    _globals['_COMMONAPISTOPTCPDUMPRESPONSE']._serialized_end = 4746
    _globals['_COMMONAPIGETTCPDUMPINFOREQUEST']._serialized_start = 4748
    _globals['_COMMONAPIGETTCPDUMPINFOREQUEST']._serialized_end = 4780
    _globals['_COMMONAPIGETTCPDUMPINFORESPONSE']._serialized_start = 4782
    _globals['_COMMONAPIGETTCPDUMPINFORESPONSE']._serialized_end = 4892
    _globals['_COMMONMESSAGES']._serialized_start = 4895
    _globals['_COMMONMESSAGES']._serialized_end = 9701