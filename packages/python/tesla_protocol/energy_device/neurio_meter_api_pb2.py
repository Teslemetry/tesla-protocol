"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'neurio_meter_api.proto')
_sym_db = _symbol_database.Default()
from . import networking_pb2 as networking__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16neurio_meter_api.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x10networking.proto"C\n\x0eNeurioCTConfig\x12\x10\n\x08location\x18\x01 \x01(\x05\x12\x1f\n\x17real_power_scale_factor\x18\x02 \x01(\x02"Z\n\x0fNeurioCTReading\x12\x14\n\x0creal_power_w\x18\x01 \x01(\x02\x12\x1b\n\x13scaled_real_power_w\x18\x02 \x01(\x02\x12\x14\n\x0ccurrent_amps\x18\x03 \x01(\x02"Y\n\x13NeurioMeterReadings\x12B\n\x0bct_readings\x18\x01 \x03(\x0b2-.tesla.proto.energy_device.v1.NeurioCTReading"\xce\x02\n\x15NeurioMeterConnection\x12O\n\x11connection_status\x18\x01 \x01(\x0e24.tesla.proto.energy_device.v1.NeurioConnectionStatus\x12M\n\x10connection_error\x18\x02 \x01(\x0e23.tesla.proto.energy_device.v1.NeurioConnectionError\x120\n\x04rssi\x18\x03 \x01(\x0b2".tesla.proto.energy_device.v1.Rssi\x12\x18\n\x10firmware_version\x18\x04 \x01(\t\x12I\n\x0emeter_readings\x18\x05 \x01(\x0b21.tesla.proto.energy_device.v1.NeurioMeterReadings"\xc3\x01\n\x11NeurioMeterConfig\x12\x10\n\x08short_id\x18\x01 \x01(\t\x12\x0e\n\x06serial\x18\x02 \x01(\t\x12?\n\tct_config\x18\x03 \x03(\x0b2,.tesla.proto.energy_device.v1.NeurioCTConfig\x12K\n\nmeter_type\x18\x04 \x01(\x0e27.tesla.proto.energy_device.v1.NeurioCompatibleMeterType"\xa0\x01\n\x14NeurioMeterInterface\x12?\n\x06config\x18\x01 \x01(\x0b2/.tesla.proto.energy_device.v1.NeurioMeterConfig\x12G\n\nconnection\x18\x02 \x01(\x0b23.tesla.proto.energy_device.v1.NeurioMeterConnection"`\n\x1dNeurioMeterAPIAddMeterRequest\x12?\n\x06config\x18\x01 \x01(\x0b2/.tesla.proto.energy_device.v1.NeurioMeterConfig"a\n\x1eNeurioMeterAPIAddMeterResponse\x12?\n\x06config\x18\x01 \x01(\x0b2/.tesla.proto.energy_device.v1.NeurioMeterConfig"2\n NeurioMeterAPIRemoveMeterRequest\x12\x0e\n\x06serial\x18\x01 \x01(\t"#\n!NeurioMeterAPIRemoveMeterResponse"t\n!NeurioMeterAPIConfigureCtsRequest\x12\x0e\n\x06serial\x18\x01 \x01(\t\x12?\n\tct_config\x18\x02 \x03(\x0b2,.tesla.proto.energy_device.v1.NeurioCTConfig"e\n"NeurioMeterAPIConfigureCtsResponse\x12?\n\tct_config\x18\x01 \x03(\x0b2,.tesla.proto.energy_device.v1.NeurioCTConfig""\n NeurioMeterAPIDetectWiredRequest"#\n!NeurioMeterAPIDetectWiredResponse"6\n$NeurioMeterAPIGetNeurioCtTypeRequest\x12\x0e\n\x06serial\x18\x01 \x01(\t"\xfa\x02\n%NeurioMeterAPIGetNeurioCtTypeResponse\x12\x0e\n\x06serial\x18\x01 \x01(\t\x12I\n\x06status\x18\x02 \x01(\x0e29.tesla.proto.energy_device.v1.NeurioCtConfigRequestStatus\x12<\n\x08ct1_type\x18\x03 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType\x12<\n\x08ct2_type\x18\x04 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType\x12<\n\x08ct3_type\x18\x05 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType\x12<\n\x08ct4_type\x18\x06 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType"\xb4\x02\n$NeurioMeterAPISetNeurioCtTypeRequest\x12\x0e\n\x06serial\x18\x01 \x01(\t\x12<\n\x08ct1_type\x18\x03 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType\x12<\n\x08ct2_type\x18\x04 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType\x12<\n\x08ct3_type\x18\x05 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType\x12<\n\x08ct4_type\x18\x06 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtTypeJ\x04\x08\x02\x10\x03"\xfa\x02\n%NeurioMeterAPISetNeurioCtTypeResponse\x12\x0e\n\x06serial\x18\x01 \x01(\t\x12I\n\x06status\x18\x02 \x01(\x0e29.tesla.proto.energy_device.v1.NeurioCtConfigRequestStatus\x12<\n\x08ct1_type\x18\x03 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType\x12<\n\x08ct2_type\x18\x04 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType\x12<\n\x08ct3_type\x18\x05 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType\x12<\n\x08ct4_type\x18\x06 \x01(\x0e2*.tesla.proto.energy_device.v1.NeurioCtType"\xcc\t\n\x13NeurioMeterMessages\x12X\n\x11add_meter_request\x18\x01 \x01(\x0b2;.tesla.proto.energy_device.v1.NeurioMeterAPIAddMeterRequestH\x00\x12Z\n\x12add_meter_response\x18\x02 \x01(\x0b2<.tesla.proto.energy_device.v1.NeurioMeterAPIAddMeterResponseH\x00\x12^\n\x14remove_meter_request\x18\x03 \x01(\x0b2>.tesla.proto.energy_device.v1.NeurioMeterAPIRemoveMeterRequestH\x00\x12`\n\x15remove_meter_response\x18\x04 \x01(\x0b2?.tesla.proto.energy_device.v1.NeurioMeterAPIRemoveMeterResponseH\x00\x12`\n\x15configure_cts_request\x18\x05 \x01(\x0b2?.tesla.proto.energy_device.v1.NeurioMeterAPIConfigureCtsRequestH\x00\x12b\n\x16configure_cts_response\x18\x06 \x01(\x0b2@.tesla.proto.energy_device.v1.NeurioMeterAPIConfigureCtsResponseH\x00\x12^\n\x14detect_wired_request\x18\x07 \x01(\x0b2>.tesla.proto.energy_device.v1.NeurioMeterAPIDetectWiredRequestH\x00\x12`\n\x15detect_wired_response\x18\x08 \x01(\x0b2?.tesla.proto.energy_device.v1.NeurioMeterAPIDetectWiredResponseH\x00\x12h\n\x1aget_neurio_ct_type_request\x18\t \x01(\x0b2B.tesla.proto.energy_device.v1.NeurioMeterAPIGetNeurioCtTypeRequestH\x00\x12j\n\x1bget_neurio_ct_type_response\x18\n \x01(\x0b2C.tesla.proto.energy_device.v1.NeurioMeterAPIGetNeurioCtTypeResponseH\x00\x12h\n\x1aset_neurio_ct_type_request\x18\x0b \x01(\x0b2B.tesla.proto.energy_device.v1.NeurioMeterAPISetNeurioCtTypeRequestH\x00\x12j\n\x1bset_neurio_ct_type_response\x18\x0c \x01(\x0b2C.tesla.proto.energy_device.v1.NeurioMeterAPISetNeurioCtTypeResponseH\x00B\t\n\x07message*l\n\tPowerType\x12\x16\n\x12POWER_TYPE_INVALID\x10\x00\x12\x19\n\x15POWER_TYPE_AC_1_PHASE\x10\x01\x12\x19\n\x15POWER_TYPE_AC_3_PHASE\x10\x02\x12\x11\n\rPOWER_TYPE_DC\x10\x03*\xa6\x02\n\rConnectorType\x12\x1a\n\x16CONNECTOR_TYPE_INVALID\x10\x00\x12\x17\n\x13CONNECTOR_TYPE_CCS1\x10\x01\x12\x17\n\x13CONNECTOR_TYPE_CCS2\x10\x02\x12\x15\n\x11CONNECTOR_TYPE_GB\x10\x03\x12\x15\n\x11CONNECTOR_TYPE_NA\x10\x04\x12\x19\n\x15CONNECTOR_TYPE_TYPE_2\x10\x05\x12\x18\n\x14CONNECTOR_TYPE_J1772\x10\x06\x120\n,CONNECTOR_TYPE_INDISTINGUISHABLE_DUAL_HANDLE\x10\x07\x12\x1a\n\x16CONNECTOR_TYPE_UNKNOWN\x10\x08\x12\x16\n\x12CONNECTOR_TYPE_MCS\x10\t*\xe8\x01\n\x16NeurioConnectionStatus\x12$\n NEURIO_CONNECTION_STATUS_INVALID\x10\x00\x12%\n!NEURIO_CONNECTION_STATUS_NO_COMMS\x10\x01\x12$\n NEURIO_CONNECTION_STATUS_PAIRING\x10\x02\x12&\n"NEURIO_CONNECTION_STATUS_CONNECTED\x10\x03\x123\n/NEURIO_CONNECTION_STATUS_CONFIG_CHANGE_UNDERWAY\x10\x04*\x81\x02\n\x15NeurioConnectionError\x12#\n\x1fNEURIO_CONNECTION_ERROR_INVALID\x10\x00\x12 \n\x1cNEURIO_CONNECTION_ERROR_NONE\x10\x01\x12#\n\x1fNEURIO_CONNECTION_ERROR_UNKNOWN\x10\x02\x12#\n\x1fNEURIO_CONNECTION_ERROR_WIFI_AP\x10\x03\x12+\n\'NEURIO_CONNECTION_ERROR_PAIRING_COMMAND\x10\x04\x12*\n&NEURIO_CONNECTION_ERROR_REBOOT_COMMAND\x10\x05*\x96\x01\n\x0cNeurioCtType\x12\x1a\n\x16NEURIO_CT_TYPE_INVALID\x10\x00\x12\x1a\n\x16NEURIO_CT_TYPE_MISSING\x10\x01\x12\x17\n\x13NEURIO_CT_TYPE_200A\x10\x02\x12\x17\n\x13NEURIO_CT_TYPE_800A\x10\x03\x12\x1c\n\x18NEURIO_CT_TYPE_UNIVERSAL\x10\x04*\xdc\x01\n\x1bNeurioCtConfigRequestStatus\x12+\n\'NEURIO_CT_CONFIG_REQUEST_STATUS_INVALID\x10\x00\x12+\n\'NEURIO_CT_CONFIG_REQUEST_STATUS_SUCCESS\x10\x01\x122\n.NEURIO_CT_CONFIG_REQUEST_STATUS_FAILED_NETWORK\x10\x02\x12/\n+NEURIO_CT_CONFIG_REQUEST_STATUS_FAILED_HTTP\x10\x03*\x94\x01\n\x19NeurioCompatibleMeterType\x12(\n$NEURIO_COMPATIBLE_METER_TYPE_INVALID\x10\x00\x12\'\n#NEURIO_COMPATIBLE_METER_TYPE_NEURIO\x10\x01\x12$\n NEURIO_COMPATIBLE_METER_TYPE_TRM\x10\x02B\x82\x01\n$com.tesla.generated.energy_device.v1B\x0eNeurioMeterApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'neurio_meter_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x0eNeurioMeterApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_POWERTYPE']._serialized_start = 3964
    _globals['_POWERTYPE']._serialized_end = 4072
    _globals['_CONNECTORTYPE']._serialized_start = 4075
    _globals['_CONNECTORTYPE']._serialized_end = 4369
    _globals['_NEURIOCONNECTIONSTATUS']._serialized_start = 4372
    _globals['_NEURIOCONNECTIONSTATUS']._serialized_end = 4604
    _globals['_NEURIOCONNECTIONERROR']._serialized_start = 4607
    _globals['_NEURIOCONNECTIONERROR']._serialized_end = 4864
    _globals['_NEURIOCTTYPE']._serialized_start = 4867
    _globals['_NEURIOCTTYPE']._serialized_end = 5017
    _globals['_NEURIOCTCONFIGREQUESTSTATUS']._serialized_start = 5020
    _globals['_NEURIOCTCONFIGREQUESTSTATUS']._serialized_end = 5240
    _globals['_NEURIOCOMPATIBLEMETERTYPE']._serialized_start = 5243
    _globals['_NEURIOCOMPATIBLEMETERTYPE']._serialized_end = 5391
    _globals['_NEURIOCTCONFIG']._serialized_start = 74
    _globals['_NEURIOCTCONFIG']._serialized_end = 141
    _globals['_NEURIOCTREADING']._serialized_start = 143
    _globals['_NEURIOCTREADING']._serialized_end = 233
    _globals['_NEURIOMETERREADINGS']._serialized_start = 235
    _globals['_NEURIOMETERREADINGS']._serialized_end = 324
    _globals['_NEURIOMETERCONNECTION']._serialized_start = 327
    _globals['_NEURIOMETERCONNECTION']._serialized_end = 661
    _globals['_NEURIOMETERCONFIG']._serialized_start = 664
    _globals['_NEURIOMETERCONFIG']._serialized_end = 859
    _globals['_NEURIOMETERINTERFACE']._serialized_start = 862
    _globals['_NEURIOMETERINTERFACE']._serialized_end = 1022
    _globals['_NEURIOMETERAPIADDMETERREQUEST']._serialized_start = 1024
    _globals['_NEURIOMETERAPIADDMETERREQUEST']._serialized_end = 1120
    _globals['_NEURIOMETERAPIADDMETERRESPONSE']._serialized_start = 1122
    _globals['_NEURIOMETERAPIADDMETERRESPONSE']._serialized_end = 1219
    _globals['_NEURIOMETERAPIREMOVEMETERREQUEST']._serialized_start = 1221
    _globals['_NEURIOMETERAPIREMOVEMETERREQUEST']._serialized_end = 1271
    _globals['_NEURIOMETERAPIREMOVEMETERRESPONSE']._serialized_start = 1273
    _globals['_NEURIOMETERAPIREMOVEMETERRESPONSE']._serialized_end = 1308
    _globals['_NEURIOMETERAPICONFIGURECTSREQUEST']._serialized_start = 1310
    _globals['_NEURIOMETERAPICONFIGURECTSREQUEST']._serialized_end = 1426
    _globals['_NEURIOMETERAPICONFIGURECTSRESPONSE']._serialized_start = 1428
    _globals['_NEURIOMETERAPICONFIGURECTSRESPONSE']._serialized_end = 1529
    _globals['_NEURIOMETERAPIDETECTWIREDREQUEST']._serialized_start = 1531
    _globals['_NEURIOMETERAPIDETECTWIREDREQUEST']._serialized_end = 1565
    _globals['_NEURIOMETERAPIDETECTWIREDRESPONSE']._serialized_start = 1567
    _globals['_NEURIOMETERAPIDETECTWIREDRESPONSE']._serialized_end = 1602
    _globals['_NEURIOMETERAPIGETNEURIOCTTYPEREQUEST']._serialized_start = 1604
    _globals['_NEURIOMETERAPIGETNEURIOCTTYPEREQUEST']._serialized_end = 1658
    _globals['_NEURIOMETERAPIGETNEURIOCTTYPERESPONSE']._serialized_start = 1661
    _globals['_NEURIOMETERAPIGETNEURIOCTTYPERESPONSE']._serialized_end = 2039
    _globals['_NEURIOMETERAPISETNEURIOCTTYPEREQUEST']._serialized_start = 2042
    _globals['_NEURIOMETERAPISETNEURIOCTTYPEREQUEST']._serialized_end = 2350
    _globals['_NEURIOMETERAPISETNEURIOCTTYPERESPONSE']._serialized_start = 2353
    _globals['_NEURIOMETERAPISETNEURIOCTTYPERESPONSE']._serialized_end = 2731
    _globals['_NEURIOMETERMESSAGES']._serialized_start = 2734
    _globals['_NEURIOMETERMESSAGES']._serialized_end = 3962