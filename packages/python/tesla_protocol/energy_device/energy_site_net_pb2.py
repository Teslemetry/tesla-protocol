"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'energy_site_net.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b"\n\x15energy_site_net.proto\x12\x1ctesla.proto.energy_device.v1*\xdf\x05\n\x1bEnergySiteNetAdditionStatus\x12+\n'ENERGY_SITE_NET_ADDITION_STATUS_INVALID\x10\x00\x12/\n+ENERGY_SITE_NET_ADDITION_STATUS_IN_PROGRESS\x10\x01\x12)\n%ENERGY_SITE_NET_ADDITION_STATUS_ADDED\x10\x02\x124\n0ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NOT_FOUND\x10\x03\x126\n2ENERGY_SITE_NET_ADDITION_STATUS_FAILED_CANNOT_JOIN\x10\x04\x126\n2ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NO_RESPONSE\x10\x05\x127\n3ENERGY_SITE_NET_ADDITION_STATUS_FAILED_BAD_RESPONSE\x10\x06\x129\n5ENERGY_SITE_NET_ADDITION_STATUS_FAILED_INTERNAL_ERROR\x10\x07\x12=\n9ENERGY_SITE_NET_ADDITION_STATUS_FAILED_CHANGES_PROHIBITED\x10\x08\x126\n2ENERGY_SITE_NET_ADDITION_STATUS_FAILED_MAX_DEVICES\x10\t\x125\n1ENERGY_SITE_NET_ADDITION_STATUS_FAILED_NOT_LEADER\x10\n\x121\n-ENERGY_SITE_NET_ADDITION_STATUS_FAILED_EXISTS\x10\x0b\x12<\n8ENERGY_SITE_NET_ADDITION_STATUS_FAILED_PROOF_OF_PRESENCE\x10\x0c*\xd1\x01\n\x18EnergySiteNetNetworkType\x12(\n$ENERGY_SITE_NET_NETWORK_TYPE_INVALID\x10\x00\x12+\n'ENERGY_SITE_NET_NETWORK_TYPE_POWERWALL3\x10\x01\x12/\n+ENERGY_SITE_NET_NETWORK_TYPE_SMART_CHARGING\x10\x02\x12-\n)ENERGY_SITE_NET_NETWORK_TYPE_LOAD_SHARING\x10\x03*\xdd\x01\n\x17EnergySiteNetPairStatus\x12'\n#ENERGY_SITE_NET_PAIR_STATUS_INVALID\x10\x00\x12'\n#ENERGY_SITE_NET_PAIR_STATUS_PENDING\x10\x01\x125\n1ENERGY_SITE_NET_PAIR_STATUS_FAILED_INTERNAL_ERROR\x10\x02\x129\n5ENERGY_SITE_NET_PAIR_STATUS_PROOF_OF_PRESENCE_TIMEOUT\x10\x03*\xb0\x04\n\x1aEnergySiteNetRemovalStatus\x12*\n&ENERGY_SITE_NET_REMOVAL_STATUS_INVALID\x10\x00\x12.\n*ENERGY_SITE_NET_REMOVAL_STATUS_IN_PROGRESS\x10\x01\x12*\n&ENERGY_SITE_NET_REMOVAL_STATUS_REMOVED\x10\x02\x128\n4ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_NO_SUCH_DEVICE\x10\x03\x128\n4ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_INTERNAL_ERROR\x10\x04\x12<\n8ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_CHANGES_PROHIBITED\x10\x05\x123\n/ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_AM_LEADER\x10\x06\x121\n-ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_AM_SOLO\x10\x07\x124\n0ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_NOT_LEADER\x10\x08\x12:\n6ENERGY_SITE_NET_REMOVAL_STATUS_FAILED_LEADER_AVAILABLE\x10\t*\xd1\x01\n\x14IntraSiteServiceType\x12#\n\x1fINTRA_SITE_SERVICE_TYPE_INVALID\x10\x00\x12.\n*INTRA_SITE_SERVICE_TYPE_MULTI_PW3_FOLLOWER\x10\x01\x124\n0INTRA_SITE_SERVICE_TYPE_WC_LOAD_SHARING_FOLLOWER\x10\x02\x12.\n*INTRA_SITE_SERVICE_TYPE_WC_CURRENT_CONTROL\x10\x03B\x81\x01\n$com.tesla.generated.energy_device.v1B\rEnergySiteNetZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3")
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'energy_site_net_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\rEnergySiteNetZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_ENERGYSITENETADDITIONSTATUS']._serialized_start = 56
    _globals['_ENERGYSITENETADDITIONSTATUS']._serialized_end = 791
    _globals['_ENERGYSITENETNETWORKTYPE']._serialized_start = 794
    _globals['_ENERGYSITENETNETWORKTYPE']._serialized_end = 1003
    _globals['_ENERGYSITENETPAIRSTATUS']._serialized_start = 1006
    _globals['_ENERGYSITENETPAIRSTATUS']._serialized_end = 1227
    _globals['_ENERGYSITENETREMOVALSTATUS']._serialized_start = 1230
    _globals['_ENERGYSITENETREMOVALSTATUS']._serialized_end = 1790
    _globals['_INTRASITESERVICETYPE']._serialized_start = 1793
    _globals['_INTRASITESERVICETYPE']._serialized_end = 2002