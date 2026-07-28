"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'energy_site_net.proto')
_sym_db = _symbol_database.Default()
from . import device_pb2 as device__pb2
from . import networking_pb2 as networking__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15energy_site_net.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x0cdevice.proto\x1a\x10networking.proto"\xd2\x01\n\x13EnergySiteNetDevice\x12.\n\x03din\x18\x01 \x01(\x0b2!.tesla.proto.energy_device.v1.Din\x12@\n\x0ewifi_ap_config\x18\x02 \x01(\x0b2(.tesla.proto.energy_device.v1.WifiConfig\x12I\n\rservice_types\x18\x03 \x03(\x0e22.tesla.proto.energy_device.v1.IntraSiteServiceType"\x9d\x01\n EnergySiteNetRecentlyAddedDevice\x12.\n\x03din\x18\x01 \x01(\x0b2!.tesla.proto.energy_device.v1.Din\x12I\n\x06status\x18\x02 \x01(\x0e29.tesla.proto.energy_device.v1.EnergySiteNetAdditionStatus"\x9e\x01\n"EnergySiteNetRecentlyRemovedDevice\x12.\n\x03din\x18\x01 \x01(\x0b2!.tesla.proto.energy_device.v1.Din\x12H\n\x06status\x18\x02 \x01(\x0e28.tesla.proto.energy_device.v1.EnergySiteNetRemovalStatus"\xb8\x02\n\x1bEnergySiteNetUnpairedDevice\x12.\n\x03din\x18\x01 \x01(\x0b2!.tesla.proto.energy_device.v1.Din\x12J\n\x0bpair_status\x18\x02 \x01(\x0e25.tesla.proto.energy_device.v1.EnergySiteNetPairStatus\x12\x18\n\x10firmware_version\x18\x03 \x01(\t\x12=\n\x0bdevice_type\x18\x04 \x01(\x0e2(.tesla.proto.energy_device.v1.DeviceType\x12D\n\x0fteg_device_type\x18d \x01(\x0e2+.tesla.proto.energy_device.v1.TEGDeviceType"\xe2\x02\n\x13EnergySiteNetConfig\x12B\n\x07devices\x18\x01 \x03(\x0b21.tesla.proto.energy_device.v1.EnergySiteNetDevice\x12V\n\x0erecently_added\x18\x02 \x01(\x0b2>.tesla.proto.energy_device.v1.EnergySiteNetRecentlyAddedDevice\x12Z\n\x10recently_removed\x18\x03 \x01(\x0b2@.tesla.proto.energy_device.v1.EnergySiteNetRecentlyRemovedDevice\x12S\n\x10unpaired_devices\x18\x04 \x03(\x0b29.tesla.proto.energy_device.v1.EnergySiteNetUnpairedDevice"\xb3\x01\n EnergySiteNetAPIAddDeviceRequest\x12A\n\x06device\x18\x01 \x01(\x0b21.tesla.proto.energy_device.v1.EnergySiteNetDevice\x12L\n\x0cnetwork_type\x18\x02 \x01(\x0e26.tesla.proto.energy_device.v1.EnergySiteNetNetworkType"{\n!EnergySiteNetAPIAddDeviceResponse\x12V\n\x0erecently_added\x18\x01 \x01(\x0b2>.tesla.proto.energy_device.v1.EnergySiteNetRecentlyAddedDevice"\xed\x01\n#EnergySiteNetAPIRemoveDeviceRequest\x12.\n\x03din\x18\x01 \x01(\x0b2!.tesla.proto.energy_device.v1.Din\x12L\n\x0cnetwork_type\x18\x02 \x01(\x0e26.tesla.proto.energy_device.v1.EnergySiteNetNetworkType\x12H\n\x0cservice_type\x18\x03 \x01(\x0e22.tesla.proto.energy_device.v1.IntraSiteServiceType"\x82\x01\n$EnergySiteNetAPIRemoveDeviceResponse\x12Z\n\x10recently_removed\x18\x01 \x01(\x0b2@.tesla.proto.energy_device.v1.EnergySiteNetRecentlyRemovedDevice"p\n EnergySiteNetAPIGetConfigRequest\x12L\n\x0cnetwork_type\x18\x01 \x01(\x0e26.tesla.proto.energy_device.v1.EnergySiteNetNetworkType"\xb4\x01\n!EnergySiteNetAPIGetConfigResponse\x12A\n\x06config\x18\x01 \x01(\x0b21.tesla.proto.energy_device.v1.EnergySiteNetConfig\x12L\n\x0cnetwork_type\x18\x02 \x01(\x0e26.tesla.proto.energy_device.v1.EnergySiteNetNetworkType"\xe8\x04\n\x15EnergySiteNetMessages\x12\\\n\x12add_device_request\x18\x01 \x01(\x0b2>.tesla.proto.energy_device.v1.EnergySiteNetAPIAddDeviceRequestH\x00\x12^\n\x13add_device_response\x18\x02 \x01(\x0b2?.tesla.proto.energy_device.v1.EnergySiteNetAPIAddDeviceResponseH\x00\x12b\n\x15remove_device_request\x18\x03 \x01(\x0b2A.tesla.proto.energy_device.v1.EnergySiteNetAPIRemoveDeviceRequestH\x00\x12d\n\x16remove_device_response\x18\x04 \x01(\x0b2B.tesla.proto.energy_device.v1.EnergySiteNetAPIRemoveDeviceResponseH\x00\x12\\\n\x12get_config_request\x18\x05 \x01(\x0b2>.tesla.proto.energy_device.v1.EnergySiteNetAPIGetConfigRequestH\x00\x12^\n\x13get_config_response\x18\x06 \x01(\x0b2?.tesla.proto.energy_device.v1.EnergySiteNetAPIGetConfigResponseH\x00B\t\n\x07message*\xdf\x05\n\x1bEnergySiteNetAdditionStatus\x12+\n\'ENERGY_SITE_NET_ADDITION_STATUS_INVALID\x10\x00\x12/\n+ENERGY_SITE_NET_ADDITION_STATUS_IN_PROGRESS\x10\x01\x12)\n%ENERGY_SITE_NET_ADDITION_STATUS_ADDED\x10\x02\x124\n0ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NOT_FOUND\x10\x03\x126\n2ENERGY_SITE_NET_ADDITION_STATUS_FAILED_CANNOT_JOIN\x10\x04\x126\n2ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NO_RESPONSE\x10\x05\x127\n3ENERGY_SITE_NET_ADDITION_STATUS_FAILED_BAD_RESPONSE\x10\x06\x129\n5ENERGY_SITE_NET_ADDITION_STATUS_FAILED_INTERNAL_ERROR\x10\x07\x12=\n9ENERGY_SITE_NET_ADDITION_STATUS_FAILED_CHANGES_PROHIBITED\x10\x08\x126\n2ENERGY_SITE_NET_ADDITION_STATUS_FAILED_MAX_DEVICES\x10\t\x125\n1ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NOT_LEADER\x10\n\x121\n-ENERGY_SITE_NET_ADDITION_STATUS_FAILED_EXISTS\x10\x0b\x12<\n8ENERGY_SITE_NET_ADDITION_STATUS_FAILED_PROOF_OF_PRESENCE\x10\x0c*\xd1\x01\n\x18EnergySiteNetNetworkType\x12(\n$ENERGY_SITE_NET_NETWORK_TYPE_INVALID\x10\x00\x12+\n\'ENERGY_SITE_NET_NETWORK_TYPE_POWERWALL3\x10\x01\x12/\n+ENERGY_SITE_NET_NETWORK_TYPE_SMART_CHARGING\x10\x02\x12-\n)ENERGY_SITE_NET_NETWORK_TYPE_LOAD_SHARING\x10\x03*\xdd\x01\n\x17EnergySiteNetPairStatus\x12\'\n#ENERGY_SITE_NET_PAIR_STATUS_INVALID\x10\x00\x12\'\n#ENERGY_SITE_NET_PAIR_STATUS_PENDING\x10\x01\x125\n1ENERGY_SITE_NET_PAIR_STATUS_FAILED_INTERNAL_ERROR\x10\x02\x129\n5ENERGY_SITE_NET_PAIR_STATUS_PROOF_OF_PRESENCE_TIMEOUT\x10\x03*\xb0\x04\n\x1aEnergySiteNetRemovalStatus\x12*\n&ENERGY_SITE_NET_REMOVAL_STATUS_INVALID\x10\x00\x12.\n*ENERGY_SITE_NET_REMOVAL_STATUS_IN_PROGRESS\x10\x01\x12*\n&ENERGY_SITE_NET_REMOVAL_STATUS_REMOVED\x10\x02\x128\n4ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_NO_SUCH_DEVICE\x10\x03\x128\n4ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_INTERNAL_ERROR\x10\x04\x12<\n8ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_CHANGES_PROHIBITED\x10\x05\x123\n/ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_AM_LEADER\x10\x06\x121\n-ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_AM_SOLO\x10\x07\x124\n0ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_NOT_LEADER\x10\x08\x12:\n6ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_LEADER_AVAILABLE\x10\t*\xd1\x01\n\x14IntraSiteServiceType\x12#\n\x1fINTRA_SITE_SERVICE_TYPE_INVALID\x10\x00\x12.\n*INTRA_SITE_SERVICE_TYPE_MULTI_PW3_FOLLOWER\x10\x01\x124\n0INTRA_SITE_SERVICE_TYPE_WC_LOAD_SHARING_FOLLOWER\x10\x02\x12.\n*INTRA_SITE_SERVICE_TYPE_WC_CURRENT_CONTROL\x10\x03B\x81\x01\n$com.tesla.generated.energy_device.v1B\rEnergySiteNetZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'energy_site_net_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\rEnergySiteNetZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_ENERGYSITENETADDITIONSTATUS']._serialized_start = 2890
    _globals['_ENERGYSITENETADDITIONSTATUS']._serialized_end = 3625
    _globals['_ENERGYSITENETNETWORKTYPE']._serialized_start = 3628
    _globals['_ENERGYSITENETNETWORKTYPE']._serialized_end = 3837
    _globals['_ENERGYSITENETPAIRSTATUS']._serialized_start = 3840
    _globals['_ENERGYSITENETPAIRSTATUS']._serialized_end = 4061
    _globals['_ENERGYSITENETREMOVALSTATUS']._serialized_start = 4064
    _globals['_ENERGYSITENETREMOVALSTATUS']._serialized_end = 4624
    _globals['_INTRASITESERVICETYPE']._serialized_start = 4627
    _globals['_INTRASITESERVICETYPE']._serialized_end = 4836
    _globals['_ENERGYSITENETDEVICE']._serialized_start = 88
    _globals['_ENERGYSITENETDEVICE']._serialized_end = 298
    _globals['_ENERGYSITENETRECENTLYADDEDDEVICE']._serialized_start = 301
    _globals['_ENERGYSITENETRECENTLYADDEDDEVICE']._serialized_end = 458
    _globals['_ENERGYSITENETRECENTLYREMOVEDDEVICE']._serialized_start = 461
    _globals['_ENERGYSITENETRECENTLYREMOVEDDEVICE']._serialized_end = 619
    _globals['_ENERGYSITENETUNPAIREDDEVICE']._serialized_start = 622
    _globals['_ENERGYSITENETUNPAIREDDEVICE']._serialized_end = 934
    _globals['_ENERGYSITENETCONFIG']._serialized_start = 937
    _globals['_ENERGYSITENETCONFIG']._serialized_end = 1291
    _globals['_ENERGYSITENETAPIADDDEVICEREQUEST']._serialized_start = 1294
    _globals['_ENERGYSITENETAPIADDDEVICEREQUEST']._serialized_end = 1473
    _globals['_ENERGYSITENETAPIADDDEVICERESPONSE']._serialized_start = 1475
    _globals['_ENERGYSITENETAPIADDDEVICERESPONSE']._serialized_end = 1598
    _globals['_ENERGYSITENETAPIREMOVEDEVICEREQUEST']._serialized_start = 1601
    _globals['_ENERGYSITENETAPIREMOVEDEVICEREQUEST']._serialized_end = 1838
    _globals['_ENERGYSITENETAPIREMOVEDEVICERESPONSE']._serialized_start = 1841
    _globals['_ENERGYSITENETAPIREMOVEDEVICERESPONSE']._serialized_end = 1971
    _globals['_ENERGYSITENETAPIGETCONFIGREQUEST']._serialized_start = 1973
    _globals['_ENERGYSITENETAPIGETCONFIGREQUEST']._serialized_end = 2085
    _globals['_ENERGYSITENETAPIGETCONFIGRESPONSE']._serialized_start = 2088
    _globals['_ENERGYSITENETAPIGETCONFIGRESPONSE']._serialized_end = 2268
    _globals['_ENERGYSITENETMESSAGES']._serialized_start = 2271
    _globals['_ENERGYSITENETMESSAGES']._serialized_end = 2887