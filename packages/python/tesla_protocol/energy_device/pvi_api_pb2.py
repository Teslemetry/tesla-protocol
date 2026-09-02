"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 5, '', 'pvi_api.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import device_pb2 as device__pb2
from . import networking_pb2 as networking__pb2
from . import update_pb2 as update__pb2
from . import energy_pb2 as energy__pb2
from . import neurio_meter_api_pb2 as neurio__meter__api__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpvi_api.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0cdevice.proto\x1a\x10networking.proto\x1a\x0cupdate.proto\x1a\x0cenergy.proto\x1a\x16neurio_meter_api.proto"\x93\x01\n\x0ePVStringVitals\x12G\n\x0edc_measurement\x18\x01 \x01(\x0b2/.tesla.proto.energy_device.v1.InstDCMeasurement\x12\x11\n\tstring_id\x18\x02 \x01(\r\x12\x11\n\tconnected\x18\x03 \x01(\x08\x12\x12\n\nlocked_out\x18\x04 \x01(\x08"\xae\x05\n\x10PVInverterVitals\x12\x10\n\x08uptime_s\x18\x01 \x01(\r\x12\x13\n\x0bpvac_faults\x18\x02 \x03(\r\x12\x12\n\npvs_faults\x18\x03 \x03(\r\x12L\n\x13ac_measurement_pvac\x18\x04 \x01(\x0b2/.tesla.proto.energy_device.v1.InstACMeasurement\x12!\n\x19site_shutdown_switch_open\x18\x05 \x01(\x08\x12E\n\x0cenergy_today\x18\x06 \x01(\x0b2/.tesla.proto.energy_device.v1.AccumulatedEnergy\x12F\n\x10pv_string_vitals\x18\x07 \x03(\x0b2,.tesla.proto.energy_device.v1.PVStringVitals\x12L\n\x13ac_measurement_site\x18\x08 \x01(\x0b2/.tesla.proto.energy_device.v1.InstACMeasurement\x12\x16\n\x0epvac_inv_state\x18\t \x01(\r\x12\x12\n\npvac_state\x18\n \x01(\r\x12R\n\x16grid_compliance_status\x18\x0b \x01(\x0b22.tesla.proto.energy_device.v1.GridComplianceStatus\x12\x15\n\rpvac_warnings\x18\x0c \x03(\r\x12\x14\n\x0cpvs_warnings\x18\r \x03(\r\x12\x11\n\tpvs_state\x18\x0e \x01(\r\x12Q\n\x18ac_measurement_solar_rgm\x18\x0f \x01(\x0b2/.tesla.proto.energy_device.v1.InstACMeasurement"\x8a\x01\n\x17PVInverterLifetimeStats\x12\x10\n\x08uptime_s\x18\x01 \x01(\x04\x12\x13\n\x0balert_count\x18\x02 \x01(\r\x12H\n\x0fenergy_lifetime\x18\x03 \x01(\x0b2/.tesla.proto.energy_device.v1.AccumulatedEnergy"V\n\x10PVMeterInterface\x12B\n\x06neurio\x18\x01 \x01(\x0b22.tesla.proto.energy_device.v1.NeurioMeterInterface":\n\x10PVGridCodeConfig\x12\x11\n\tgrid_code\x18\x01 \x01(\t\x12\x13\n\x0bregion_info\x18\x02 \x01(\t"\xb7\x02\n\x12PVInverterSettings\x12A\n\tgrid_code\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.PVGridCodeConfig\x12>\n\x06meters\x18\x02 \x03(\x0b2..tesla.proto.energy_device.v1.PVMeterInterface\x12^\n\x17solar_installation_type\x18\x03 \x01(\x0e2=.tesla.proto.energy_device.v1.PVInverterSolarInstallationType\x12>\n\x19current_rating_override_a\x18\x04 \x01(\x0b2\x1b.google.protobuf.FloatValue";\n\x14PVInverterCanMessage\x12\x0e\n\x06can_id\x18\x01 \x01(\r\x12\x13\n\x0bcan_payload\x18\x02 \x01(\x0c"\x1c\n\x1aPVIAPIGetSystemInfoRequest"\xc9\x02\n\x1bPVIAPIGetSystemInfoResponse\x125\n\x08pvcom_id\x18\x01 \x01(\x0b2#.tesla.proto.energy_device.v1.EcuId\x124\n\x07pvac_id\x18\x02 \x01(\x0b2#.tesla.proto.energy_device.v1.EcuId\x123\n\x06pvs_id\x18\x03 \x01(\x0b2#.tesla.proto.energy_device.v1.EcuId\x12G\n\x10firmware_version\x18\x04 \x01(\x0b2-.tesla.proto.energy_device.v1.FirmwareVersion\x12\x1c\n\x14nominal_current_amps\x18\x05 \x01(\x02\x12!\n\x19nominal_apparent_power_va\x18\x06 \x01(\x02"\x18\n\x16PVIAPIGetVitalsRequest"Y\n\x17PVIAPIGetVitalsResponse\x12>\n\x06vitals\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.PVInverterVitals"\x1f\n\x1dPVIAPIGetLifetimeStatsRequest"o\n\x1ePVIAPIGetLifetimeStatsResponse\x12M\n\x0elifetime_stats\x18\x01 \x01(\x0b25.tesla.proto.energy_device.v1.PVInverterLifetimeStats"\x18\n\x16PVIAPIGetConfigRequest"\x9f\x03\n\x17PVIAPIGetConfigResponse\x12B\n\x08settings\x18\x01 \x01(\x0b20.tesla.proto.energy_device.v1.PVInverterSettings\x12=\n\x0bwifi_config\x18\x02 \x01(\x0b2(.tesla.proto.energy_device.v1.WifiConfig\x12<\n\x04wifi\x18\x03 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12;\n\x03eth\x18\x04 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12;\n\x03gsm\x18\x05 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12I\n\x0cpower_status\x18\x06 \x01(\x0e23.tesla.proto.energy_device.v1.PVInverterPowerStatus"d\n\x1ePVIAPIConfigureSettingsRequest\x12B\n\x08settings\x18\x01 \x01(\x0b20.tesla.proto.energy_device.v1.PVInverterSettings"e\n\x1fPVIAPIConfigureSettingsResponse\x12B\n\x08settings\x18\x01 \x01(\x0b20.tesla.proto.energy_device.v1.PVInverterSettings"n\n\x1ePVIAPIConfigureEthernetRequest\x12L\n\nip4_config\x18\x01 \x01(\x0b28.tesla.proto.energy_device.v1.NetworkInterfaceIPv4Config"^\n\x1fPVIAPIConfigureEthernetResponse\x12;\n\x03eth\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface",\n\x19PVIAPIConfigureGsmRequest\x12\x0f\n\x07enabled\x18\x01 \x01(\x08"Y\n\x1aPVIAPIConfigureGsmResponse\x12;\n\x03gsm\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface"X\n\x1aPVIAPIInverterResetRequest\x12\x13\n\x0breset_pvcom\x18\x01 \x01(\x08\x12\x12\n\nreset_pvac\x18\x02 \x01(\x08\x12\x11\n\treset_pvs\x18\x03 \x01(\x08"\x84\x02\n\x1bPVIAPIInverterResetResponse\x12L\n\x0cpvcom_status\x18\x01 \x01(\x0e26.tesla.proto.energy_device.v1.PVInverterEcuResetStatus\x12K\n\x0bpvac_status\x18\x02 \x01(\x0e26.tesla.proto.energy_device.v1.PVInverterEcuResetStatus\x12J\n\npvs_status\x18\x03 \x01(\x0e26.tesla.proto.energy_device.v1.PVInverterEcuResetStatus"\xa7\x01\n\x1fPVIAPISetOperationParamsRequest\x12I\n\x0cpower_status\x18\x01 \x01(\x0e23.tesla.proto.energy_device.v1.PVInverterPowerStatus\x129\n\x14active_power_limit_w\x18\x02 \x01(\x0b2\x1b.google.protobuf.FloatValue"\xa8\x01\n PVIAPISetOperationParamsResponse\x12I\n\x0cpower_status\x18\x01 \x01(\x0e23.tesla.proto.energy_device.v1.PVInverterPowerStatus\x129\n\x14active_power_limit_w\x18\x02 \x01(\x0b2\x1b.google.protobuf.FloatValue"f\n\x1bPVIAPISendCanMessageRequest\x12G\n\x0bcan_message\x18\x01 \x01(\x0b22.tesla.proto.energy_device.v1.PVInverterCanMessage"\x1e\n\x1cPVIAPISendCanMessageResponse"\x7f\n%PVIAPIUdsWriteDataByIdentifierRequest\x128\n\x03ecu\x18\x01 \x01(\x0e2+.tesla.proto.energy_device.v1.PVInverterEcu\x12\x0b\n\x03did\x18\x02 \x01(\r\x12\x0f\n\x07payload\x18\x03 \x01(\x0c"(\n&PVIAPIUdsWriteDataByIdentifierResponse"\x1c\n\x1aPVIAPICheckInternetRequest"\xd5\x01\n\x1bPVIAPICheckInternetResponse\x12<\n\x04wifi\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12;\n\x03eth\x18\x02 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface\x12;\n\x03gsm\x18\x03 \x01(\x0b2..tesla.proto.energy_device.v1.NetworkInterface"c\n\x1ePVIAPIConfigureGridCodeRequest\x12A\n\tgrid_code\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.PVGridCodeConfig"d\n\x1fPVIAPIConfigureGridCodeResponse\x12A\n\tgrid_code\x18\x01 \x01(\x0b2..tesla.proto.energy_device.v1.PVGridCodeConfig"\x1a\n\x18PVIAPIClearAlertsRequest"\x1b\n\x19PVIAPIClearAlertsResponse"6\n\x19PVIAPITriggerDrLogRequest\x12\x0c\n\x04pvac\x18\x01 \x01(\x08\x12\x0b\n\x03pvs\x18\x02 \x01(\x08"\x1c\n\x1aPVIAPITriggerDrLogResponse"J\n\x16PVIAPIClearLogsRequest\x12\x11\n\ttelemetry\x18\x01 \x01(\x08\x12\x0e\n\x06alerts\x18\x02 \x01(\x08\x12\r\n\x05drlog\x18\x03 \x01(\x08"\xf6\x01\n\x17PVIAPIClearLogsResponse\x12J\n\ttelemetry\x18\x01 \x01(\x0e27.tesla.proto.energy_device.v1.PVInverterClearLogsStatus\x12G\n\x06alerts\x18\x02 \x01(\x0e27.tesla.proto.energy_device.v1.PVInverterClearLogsStatus\x12F\n\x05drlog\x18\x03 \x01(\x0e27.tesla.proto.energy_device.v1.PVInverterClearLogsStatus"\x8d\x01\n+PVIAPIConfigureSolarInstallationTypeRequest\x12^\n\x17solar_installation_type\x18\x01 \x01(\x0e2=.tesla.proto.energy_device.v1.PVInverterSolarInstallationType"\x8e\x01\n,PVIAPIConfigureSolarInstallationTypeResponse\x12^\n\x17solar_installation_type\x18\x01 \x01(\x0e2=.tesla.proto.energy_device.v1.PVInverterSolarInstallationType"P\n+PVIAPIConfigureCurrentRatingOverrideRequest\x12!\n\x19current_rating_override_a\x18\x01 \x01(\x02"Q\n,PVIAPIConfigureCurrentRatingOverrideResponse\x12!\n\x19current_rating_override_a\x18\x01 \x01(\x02"*\n(PVIAPIRemoveCurrentRatingOverrideRequest"+\n)PVIAPIRemoveCurrentRatingOverrideResponse"\x86\x1e\n\x0bPVIMessages\x12[\n\x17get_system_info_request\x18\x01 \x01(\x0b28.tesla.proto.energy_device.v1.PVIAPIGetSystemInfoRequestH\x00\x12]\n\x18get_system_info_response\x18\x02 \x01(\x0b29.tesla.proto.energy_device.v1.PVIAPIGetSystemInfoResponseH\x00\x12R\n\x12get_vitals_request\x18\x03 \x01(\x0b24.tesla.proto.energy_device.v1.PVIAPIGetVitalsRequestH\x00\x12T\n\x13get_vitals_response\x18\x04 \x01(\x0b25.tesla.proto.energy_device.v1.PVIAPIGetVitalsResponseH\x00\x12a\n\x1aget_lifetime_stats_request\x18\x05 \x01(\x0b2;.tesla.proto.energy_device.v1.PVIAPIGetLifetimeStatsRequestH\x00\x12c\n\x1bget_lifetime_stats_response\x18\x06 \x01(\x0b2<.tesla.proto.energy_device.v1.PVIAPIGetLifetimeStatsResponseH\x00\x12R\n\x12get_config_request\x18\x07 \x01(\x0b24.tesla.proto.energy_device.v1.PVIAPIGetConfigRequestH\x00\x12T\n\x13get_config_response\x18\x08 \x01(\x0b25.tesla.proto.energy_device.v1.PVIAPIGetConfigResponseH\x00\x12b\n\x1aconfigure_settings_request\x18\t \x01(\x0b2<.tesla.proto.energy_device.v1.PVIAPIConfigureSettingsRequestH\x00\x12d\n\x1bconfigure_settings_response\x18\n \x01(\x0b2=.tesla.proto.energy_device.v1.PVIAPIConfigureSettingsResponseH\x00\x12b\n\x1aconfigure_ethernet_request\x18\x0b \x01(\x0b2<.tesla.proto.energy_device.v1.PVIAPIConfigureEthernetRequestH\x00\x12d\n\x1bconfigure_ethernet_response\x18\x0c \x01(\x0b2=.tesla.proto.energy_device.v1.PVIAPIConfigureEthernetResponseH\x00\x12X\n\x15configure_gsm_request\x18\r \x01(\x0b27.tesla.proto.energy_device.v1.PVIAPIConfigureGsmRequestH\x00\x12Z\n\x16configure_gsm_response\x18\x0e \x01(\x0b28.tesla.proto.energy_device.v1.PVIAPIConfigureGsmResponseH\x00\x12Z\n\x16inverter_reset_request\x18\x0f \x01(\x0b28.tesla.proto.energy_device.v1.PVIAPIInverterResetRequestH\x00\x12\\\n\x17inverter_reset_response\x18\x10 \x01(\x0b29.tesla.proto.energy_device.v1.PVIAPIInverterResetResponseH\x00\x12e\n\x1cset_operation_params_request\x18\x11 \x01(\x0b2=.tesla.proto.energy_device.v1.PVIAPISetOperationParamsRequestH\x00\x12g\n\x1dset_operation_params_response\x18\x12 \x01(\x0b2>.tesla.proto.energy_device.v1.PVIAPISetOperationParamsResponseH\x00\x12]\n\x18send_can_message_request\x18\x13 \x01(\x0b29.tesla.proto.energy_device.v1.PVIAPISendCanMessageRequestH\x00\x12_\n\x19send_can_message_response\x18\x14 \x01(\x0b2:.tesla.proto.energy_device.v1.PVIAPISendCanMessageResponseH\x00\x12s\n$uds_write_data_by_identifier_request\x18\x15 \x01(\x0b2C.tesla.proto.energy_device.v1.PVIAPIUdsWriteDataByIdentifierRequestH\x00\x12u\n%uds_write_data_by_identifier_response\x18\x16 \x01(\x0b2D.tesla.proto.energy_device.v1.PVIAPIUdsWriteDataByIdentifierResponseH\x00\x12Z\n\x16check_internet_request\x18\x17 \x01(\x0b28.tesla.proto.energy_device.v1.PVIAPICheckInternetRequestH\x00\x12\\\n\x17check_internet_response\x18\x18 \x01(\x0b29.tesla.proto.energy_device.v1.PVIAPICheckInternetResponseH\x00\x12c\n\x1bconfigure_grid_code_request\x18\x19 \x01(\x0b2<.tesla.proto.energy_device.v1.PVIAPIConfigureGridCodeRequestH\x00\x12e\n\x1cconfigure_grid_code_response\x18\x1a \x01(\x0b2=.tesla.proto.energy_device.v1.PVIAPIConfigureGridCodeResponseH\x00\x12V\n\x14clear_alerts_request\x18\x1b \x01(\x0b26.tesla.proto.energy_device.v1.PVIAPIClearAlertsRequestH\x00\x12X\n\x15clear_alerts_response\x18\x1c \x01(\x0b27.tesla.proto.energy_device.v1.PVIAPIClearAlertsResponseH\x00\x12Y\n\x16trigger_dr_log_request\x18\x1d \x01(\x0b27.tesla.proto.energy_device.v1.PVIAPITriggerDrLogRequestH\x00\x12[\n\x17trigger_dr_log_response\x18\x1e \x01(\x0b28.tesla.proto.energy_device.v1.PVIAPITriggerDrLogResponseH\x00\x12R\n\x12clear_logs_request\x18\x1f \x01(\x0b24.tesla.proto.energy_device.v1.PVIAPIClearLogsRequestH\x00\x12T\n\x13clear_logs_response\x18  \x01(\x0b25.tesla.proto.energy_device.v1.PVIAPIClearLogsResponseH\x00\x12~\n)configure_solar_installation_type_request\x18! \x01(\x0b2I.tesla.proto.energy_device.v1.PVIAPIConfigureSolarInstallationTypeRequestH\x00\x12\x80\x01\n*configure_solar_installation_type_response\x18" \x01(\x0b2J.tesla.proto.energy_device.v1.PVIAPIConfigureSolarInstallationTypeResponseH\x00\x12~\n)configure_current_rating_override_request\x18# \x01(\x0b2I.tesla.proto.energy_device.v1.PVIAPIConfigureCurrentRatingOverrideRequestH\x00\x12\x80\x01\n*configure_current_rating_override_response\x18$ \x01(\x0b2J.tesla.proto.energy_device.v1.PVIAPIConfigureCurrentRatingOverrideResponseH\x00\x12x\n&remove_current_rating_override_request\x18% \x01(\x0b2F.tesla.proto.energy_device.v1.PVIAPIRemoveCurrentRatingOverrideRequestH\x00\x12z\n\'remove_current_rating_override_response\x18& \x01(\x0b2G.tesla.proto.energy_device.v1.PVIAPIRemoveCurrentRatingOverrideResponseH\x00B\t\n\x07message*\xb8\x01\n\x1fPVInverterSolarInstallationType\x12/\n+PV_INVERTER_SOLAR_INSTALLATION_TYPE_INVALID\x10\x00\x120\n,PV_INVERTER_SOLAR_INSTALLATION_TYPE_PV_PANEL\x10\x01\x122\n.PV_INVERTER_SOLAR_INSTALLATION_TYPE_SOLARGLASS\x10\x02*\xb5\x01\n\x15PVInverterPowerStatus\x12$\n PV_INVERTER_POWER_STATUS_INVALID\x10\x00\x12 \n\x1cPV_INVERTER_POWER_STATUS_OFF\x10\x01\x12)\n%PV_INVERTER_POWER_STATUS_DC_CONNECTED\x10\x02\x12)\n%PV_INVERTER_POWER_STATUS_AC_PRODUCING\x10\x03*\xf4\x01\n\x18PVInverterEcuResetStatus\x12(\n$PV_INVERTER_ECU_RESET_STATUS_INVALID\x10\x00\x12%\n!PV_INVERTER_ECU_RESET_STATUS_NONE\x10\x01\x12(\n$PV_INVERTER_ECU_RESET_STATUS_SUCCESS\x10\x02\x12+\n\'PV_INVERTER_ECU_RESET_STATUS_PROCESSING\x10\x03\x120\n,PV_INVERTER_ECU_RESET_STATUS_UNKNOWN_FAILURE\x10\x04*z\n\rPVInverterEcu\x12\x1b\n\x17PV_INVERTER_ECU_INVALID\x10\x00\x12\x19\n\x15PV_INVERTER_ECU_PVCOM\x10\x01\x12\x18\n\x14PV_INVERTER_ECU_PVAC\x10\x02\x12\x17\n\x13PV_INVERTER_ECU_PVS\x10\x03*\xf1\x01\n\x19PVInverterClearLogsStatus\x12)\n%PV_INVERTER_CLEAR_LOGS_STATUS_INVALID\x10\x00\x12&\n"PV_INVERTER_CLEAR_LOGS_STATUS_NONE\x10\x01\x12)\n%PV_INVERTER_CLEAR_LOGS_STATUS_FAILURE\x10\x02\x12)\n%PV_INVERTER_CLEAR_LOGS_STATUS_SUCCESS\x10\x03\x12+\n\'PV_INVERTER_CLEAR_LOGS_STATUS_ATTEMPTED\x10\x04Bz\n$com.tesla.generated.energy_device.v1B\x06PviApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pvi_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x06PviApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_PVINVERTERSOLARINSTALLATIONTYPE']._serialized_start = 9596
    _globals['_PVINVERTERSOLARINSTALLATIONTYPE']._serialized_end = 9780
    _globals['_PVINVERTERPOWERSTATUS']._serialized_start = 9783
    _globals['_PVINVERTERPOWERSTATUS']._serialized_end = 9964
    _globals['_PVINVERTERECURESETSTATUS']._serialized_start = 9967
    _globals['_PVINVERTERECURESETSTATUS']._serialized_end = 10211
    _globals['_PVINVERTERECU']._serialized_start = 10213
    _globals['_PVINVERTERECU']._serialized_end = 10335
    _globals['_PVINVERTERCLEARLOGSSTATUS']._serialized_start = 10338
    _globals['_PVINVERTERCLEARLOGSSTATUS']._serialized_end = 10579
    _globals['_PVSTRINGVITALS']._serialized_start = 164
    _globals['_PVSTRINGVITALS']._serialized_end = 311
    _globals['_PVINVERTERVITALS']._serialized_start = 314
    _globals['_PVINVERTERVITALS']._serialized_end = 1000
    _globals['_PVINVERTERLIFETIMESTATS']._serialized_start = 1003
    _globals['_PVINVERTERLIFETIMESTATS']._serialized_end = 1141
    _globals['_PVMETERINTERFACE']._serialized_start = 1143
    _globals['_PVMETERINTERFACE']._serialized_end = 1229
    _globals['_PVGRIDCODECONFIG']._serialized_start = 1231
    _globals['_PVGRIDCODECONFIG']._serialized_end = 1289
    _globals['_PVINVERTERSETTINGS']._serialized_start = 1292
    _globals['_PVINVERTERSETTINGS']._serialized_end = 1603
    _globals['_PVINVERTERCANMESSAGE']._serialized_start = 1605
    _globals['_PVINVERTERCANMESSAGE']._serialized_end = 1664
    _globals['_PVIAPIGETSYSTEMINFOREQUEST']._serialized_start = 1666
    _globals['_PVIAPIGETSYSTEMINFOREQUEST']._serialized_end = 1694
    _globals['_PVIAPIGETSYSTEMINFORESPONSE']._serialized_start = 1697
    _globals['_PVIAPIGETSYSTEMINFORESPONSE']._serialized_end = 2026
    _globals['_PVIAPIGETVITALSREQUEST']._serialized_start = 2028
    _globals['_PVIAPIGETVITALSREQUEST']._serialized_end = 2052
    _globals['_PVIAPIGETVITALSRESPONSE']._serialized_start = 2054
    _globals['_PVIAPIGETVITALSRESPONSE']._serialized_end = 2143
    _globals['_PVIAPIGETLIFETIMESTATSREQUEST']._serialized_start = 2145
    _globals['_PVIAPIGETLIFETIMESTATSREQUEST']._serialized_end = 2176
    _globals['_PVIAPIGETLIFETIMESTATSRESPONSE']._serialized_start = 2178
    _globals['_PVIAPIGETLIFETIMESTATSRESPONSE']._serialized_end = 2289
    _globals['_PVIAPIGETCONFIGREQUEST']._serialized_start = 2291
    _globals['_PVIAPIGETCONFIGREQUEST']._serialized_end = 2315
    _globals['_PVIAPIGETCONFIGRESPONSE']._serialized_start = 2318
    _globals['_PVIAPIGETCONFIGRESPONSE']._serialized_end = 2733
    _globals['_PVIAPICONFIGURESETTINGSREQUEST']._serialized_start = 2735
    _globals['_PVIAPICONFIGURESETTINGSREQUEST']._serialized_end = 2835
    _globals['_PVIAPICONFIGURESETTINGSRESPONSE']._serialized_start = 2837
    _globals['_PVIAPICONFIGURESETTINGSRESPONSE']._serialized_end = 2938
    _globals['_PVIAPICONFIGUREETHERNETREQUEST']._serialized_start = 2940
    _globals['_PVIAPICONFIGUREETHERNETREQUEST']._serialized_end = 3050
    _globals['_PVIAPICONFIGUREETHERNETRESPONSE']._serialized_start = 3052
    _globals['_PVIAPICONFIGUREETHERNETRESPONSE']._serialized_end = 3146
    _globals['_PVIAPICONFIGUREGSMREQUEST']._serialized_start = 3148
    _globals['_PVIAPICONFIGUREGSMREQUEST']._serialized_end = 3192
    _globals['_PVIAPICONFIGUREGSMRESPONSE']._serialized_start = 3194
    _globals['_PVIAPICONFIGUREGSMRESPONSE']._serialized_end = 3283
    _globals['_PVIAPIINVERTERRESETREQUEST']._serialized_start = 3285
    _globals['_PVIAPIINVERTERRESETREQUEST']._serialized_end = 3373
    _globals['_PVIAPIINVERTERRESETRESPONSE']._serialized_start = 3376
    _globals['_PVIAPIINVERTERRESETRESPONSE']._serialized_end = 3636
    _globals['_PVIAPISETOPERATIONPARAMSREQUEST']._serialized_start = 3639
    _globals['_PVIAPISETOPERATIONPARAMSREQUEST']._serialized_end = 3806
    _globals['_PVIAPISETOPERATIONPARAMSRESPONSE']._serialized_start = 3809
    _globals['_PVIAPISETOPERATIONPARAMSRESPONSE']._serialized_end = 3977
    _globals['_PVIAPISENDCANMESSAGEREQUEST']._serialized_start = 3979
    _globals['_PVIAPISENDCANMESSAGEREQUEST']._serialized_end = 4081
    _globals['_PVIAPISENDCANMESSAGERESPONSE']._serialized_start = 4083
    _globals['_PVIAPISENDCANMESSAGERESPONSE']._serialized_end = 4113
    _globals['_PVIAPIUDSWRITEDATABYIDENTIFIERREQUEST']._serialized_start = 4115
    _globals['_PVIAPIUDSWRITEDATABYIDENTIFIERREQUEST']._serialized_end = 4242
    _globals['_PVIAPIUDSWRITEDATABYIDENTIFIERRESPONSE']._serialized_start = 4244
    _globals['_PVIAPIUDSWRITEDATABYIDENTIFIERRESPONSE']._serialized_end = 4284
    _globals['_PVIAPICHECKINTERNETREQUEST']._serialized_start = 4286
    _globals['_PVIAPICHECKINTERNETREQUEST']._serialized_end = 4314
    _globals['_PVIAPICHECKINTERNETRESPONSE']._serialized_start = 4317
    _globals['_PVIAPICHECKINTERNETRESPONSE']._serialized_end = 4530
    _globals['_PVIAPICONFIGUREGRIDCODEREQUEST']._serialized_start = 4532
    _globals['_PVIAPICONFIGUREGRIDCODEREQUEST']._serialized_end = 4631
    _globals['_PVIAPICONFIGUREGRIDCODERESPONSE']._serialized_start = 4633
    _globals['_PVIAPICONFIGUREGRIDCODERESPONSE']._serialized_end = 4733
    _globals['_PVIAPICLEARALERTSREQUEST']._serialized_start = 4735
    _globals['_PVIAPICLEARALERTSREQUEST']._serialized_end = 4761
    _globals['_PVIAPICLEARALERTSRESPONSE']._serialized_start = 4763
    _globals['_PVIAPICLEARALERTSRESPONSE']._serialized_end = 4790
    _globals['_PVIAPITRIGGERDRLOGREQUEST']._serialized_start = 4792
    _globals['_PVIAPITRIGGERDRLOGREQUEST']._serialized_end = 4846
    _globals['_PVIAPITRIGGERDRLOGRESPONSE']._serialized_start = 4848
    _globals['_PVIAPITRIGGERDRLOGRESPONSE']._serialized_end = 4876
    _globals['_PVIAPICLEARLOGSREQUEST']._serialized_start = 4878
    _globals['_PVIAPICLEARLOGSREQUEST']._serialized_end = 4952
    _globals['_PVIAPICLEARLOGSRESPONSE']._serialized_start = 4955
    _globals['_PVIAPICLEARLOGSRESPONSE']._serialized_end = 5201
    _globals['_PVIAPICONFIGURESOLARINSTALLATIONTYPEREQUEST']._serialized_start = 5204
    _globals['_PVIAPICONFIGURESOLARINSTALLATIONTYPEREQUEST']._serialized_end = 5345
    _globals['_PVIAPICONFIGURESOLARINSTALLATIONTYPERESPONSE']._serialized_start = 5348
    _globals['_PVIAPICONFIGURESOLARINSTALLATIONTYPERESPONSE']._serialized_end = 5490
    _globals['_PVIAPICONFIGURECURRENTRATINGOVERRIDEREQUEST']._serialized_start = 5492
    _globals['_PVIAPICONFIGURECURRENTRATINGOVERRIDEREQUEST']._serialized_end = 5572
    _globals['_PVIAPICONFIGURECURRENTRATINGOVERRIDERESPONSE']._serialized_start = 5574
    _globals['_PVIAPICONFIGURECURRENTRATINGOVERRIDERESPONSE']._serialized_end = 5655
    _globals['_PVIAPIREMOVECURRENTRATINGOVERRIDEREQUEST']._serialized_start = 5657
    _globals['_PVIAPIREMOVECURRENTRATINGOVERRIDEREQUEST']._serialized_end = 5699
    _globals['_PVIAPIREMOVECURRENTRATINGOVERRIDERESPONSE']._serialized_start = 5701
    _globals['_PVIAPIREMOVECURRENTRATINGOVERRIDERESPONSE']._serialized_end = 5744
    _globals['_PVIMESSAGES']._serialized_start = 5747
    _globals['_PVIMESSAGES']._serialized_end = 9593