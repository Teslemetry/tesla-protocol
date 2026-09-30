"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'intra_site_api.proto')
_sym_db = _symbol_database.Default()
from . import networking_pb2 as networking__pb2
from . import energy_site_net_pb2 as energy__site__net__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14intra_site_api.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x10networking.proto\x1a\x15energy_site_net.proto"\xeb\x03\n\x0fIntraSiteConfig\x12\x1e\n\x16last_changed_timestamp\x18\x01 \x01(\x04\x12F\n\x0bsite_config\x18\x02 \x01(\x0b21.tesla.proto.energy_device.v1.EnergySiteNetConfig\x12]\n\x17backhaul_interface_type\x18\x03 \x01(\x0e2<.tesla.proto.energy_device.v1.IntraSiteBackhaulInterfaceType\x12;\n\tsite_wifi\x18\x04 \x01(\x0b2(.tesla.proto.energy_device.v1.WifiConfig\x12A\n\x06leader\x18\x05 \x01(\x0b21.tesla.proto.energy_device.v1.EnergySiteNetDevice\x12I\n\rservice_types\x18\x07 \x03(\x0e22.tesla.proto.energy_device.v1.IntraSiteServiceType\x12@\n\x08lan_type\x18\x08 \x01(\x0e2..tesla.proto.energy_device.v1.IntraSiteLanTypeJ\x04\x08\x06\x10\x07"V\n\x17IntraSiteAPIPairRequest\x12;\n\x04site\x18\x01 \x01(\x0b2-.tesla.proto.energy_device.v1.IntraSiteConfig"]\n\x18IntraSiteAPIPairResponse\x12A\n\x06result\x18\x01 \x01(\x0e21.tesla.proto.energy_device.v1.IntraSitePairResult"\x1b\n\x19IntraSiteAPIUnpairRequest"a\n\x1aIntraSiteAPIUnpairResponse\x12C\n\x06result\x18\x01 \x01(\x0e23.tesla.proto.energy_device.v1.IntraSiteUnpairResult"]\n\x1eIntraSiteAPIJoinNetworkRequest\x12;\n\x04site\x18\x01 \x01(\x0b2-.tesla.proto.energy_device.v1.IntraSiteConfig"k\n\x1fIntraSiteAPIJoinNetworkResponse\x12H\n\x06result\x18\x01 \x01(\x0e28.tesla.proto.energy_device.v1.IntraSiteJoinNetworkResult"\x9e\x01\n\x1cIntraSiteAPIAddDeviceRequest\x12A\n\x06device\x18\x01 \x01(\x0b21.tesla.proto.energy_device.v1.EnergySiteNetDevice\x12;\n\x04site\x18\x02 \x01(\x0b2-.tesla.proto.energy_device.v1.IntraSiteConfig"j\n\x1dIntraSiteAPIAddDeviceResponse\x12I\n\x06result\x18\x01 \x01(\x0e29.tesla.proto.energy_device.v1.EnergySiteNetAdditionStatus"\xb6\x01\n&IntraSiteAPIPushAddDeviceResultRequest\x12A\n\x06device\x18\x01 \x01(\x0b21.tesla.proto.energy_device.v1.EnergySiteNetDevice\x12I\n\x06result\x18\x02 \x01(\x0e29.tesla.proto.energy_device.v1.EnergySiteNetAdditionStatus")\n\'IntraSiteAPIPushAddDeviceResultResponse"!\n\x1fIntraSiteAPILeaveNetworkRequest""\n IntraSiteAPILeaveNetworkResponse""\n IntraSiteAPIPushHeartbeatRequest"k\n!IntraSiteAPIPushHeartbeatResponse\x12F\n\x06result\x18\x01 \x01(\x0e26.tesla.proto.energy_device.v1.IntraSiteHeartbeatResult"\\\n\x1dIntraSiteAPIPushConfigRequest\x12;\n\x04site\x18\x01 \x01(\x0b2-.tesla.proto.energy_device.v1.IntraSiteConfig" \n\x1eIntraSiteAPIPushConfigResponse"\xd6\x01\n%IntraSiteAPIPushBackhaulStatusRequest\x12]\n\x17backhaul_interface_type\x18\x01 \x01(\x0e2<.tesla.proto.energy_device.v1.IntraSiteBackhaulInterfaceType\x12N\n\x0fbackhaul_status\x18\x02 \x01(\x0e25.tesla.proto.energy_device.v1.IntraSiteBackhaulStatus"(\n&IntraSiteAPIPushBackhaulStatusResponse"\x87\x01\n#IntraSiteAPIPushLeaderStatusRequest\x12C\n\x06status\x18\x01 \x01(\x0e23.tesla.proto.energy_device.v1.IntraSiteLeaderStatus\x12\x1b\n\x13expected_duration_s\x18\x02 \x01(\r"&\n$IntraSiteAPIPushLeaderStatusResponse"/\n IntraSiteAPIRequestUpdateRequest\x12\x0b\n\x03din\x18\x01 \x01(\t"6\n!IntraSiteAPIRequestUpdateResponse\x12\x11\n\tsignature\x18\x01 \x01(\t"}\n!IntraSiteAPICompleteUpdateRequest\x12\x0b\n\x03din\x18\x01 \x01(\t\x12K\n\x06result\x18\x02 \x01(\x0e2;.tesla.proto.energy_device.v1.IntraSiteCompleteUpdateResult"$\n"IntraSiteAPICompleteUpdateResponse"\xbe\x12\n\x11IntraSiteMessages\x12\\\n\x14join_network_request\x18\x01 \x01(\x0b2<.tesla.proto.energy_device.v1.IntraSiteAPIJoinNetworkRequestH\x00\x12^\n\x15join_network_response\x18\x02 \x01(\x0b2=.tesla.proto.energy_device.v1.IntraSiteAPIJoinNetworkResponseH\x00\x12X\n\x12add_device_request\x18\x03 \x01(\x0b2:.tesla.proto.energy_device.v1.IntraSiteAPIAddDeviceRequestH\x00\x12Z\n\x13add_device_response\x18\x04 \x01(\x0b2;.tesla.proto.energy_device.v1.IntraSiteAPIAddDeviceResponseH\x00\x12n\n\x1epush_add_device_result_request\x18\x05 \x01(\x0b2D.tesla.proto.energy_device.v1.IntraSiteAPIPushAddDeviceResultRequestH\x00\x12p\n\x1fpush_add_device_result_response\x18\x06 \x01(\x0b2E.tesla.proto.energy_device.v1.IntraSiteAPIPushAddDeviceResultResponseH\x00\x12^\n\x15leave_network_request\x18\x07 \x01(\x0b2=.tesla.proto.energy_device.v1.IntraSiteAPILeaveNetworkRequestH\x00\x12`\n\x16leave_network_response\x18\x08 \x01(\x0b2>.tesla.proto.energy_device.v1.IntraSiteAPILeaveNetworkResponseH\x00\x12`\n\x16push_heartbeat_request\x18\t \x01(\x0b2>.tesla.proto.energy_device.v1.IntraSiteAPIPushHeartbeatRequestH\x00\x12b\n\x17push_heartbeat_response\x18\n \x01(\x0b2?.tesla.proto.energy_device.v1.IntraSiteAPIPushHeartbeatResponseH\x00\x12Z\n\x13push_config_request\x18\x0b \x01(\x0b2;.tesla.proto.energy_device.v1.IntraSiteAPIPushConfigRequestH\x00\x12\\\n\x14push_config_response\x18\x0c \x01(\x0b2<.tesla.proto.energy_device.v1.IntraSiteAPIPushConfigResponseH\x00\x12k\n\x1cpush_backhaul_status_request\x18\r \x01(\x0b2C.tesla.proto.energy_device.v1.IntraSiteAPIPushBackhaulStatusRequestH\x00\x12m\n\x1dpush_backhaul_status_response\x18\x0e \x01(\x0b2D.tesla.proto.energy_device.v1.IntraSiteAPIPushBackhaulStatusResponseH\x00\x12g\n\x1apush_leader_status_request\x18\x0f \x01(\x0b2A.tesla.proto.energy_device.v1.IntraSiteAPIPushLeaderStatusRequestH\x00\x12i\n\x1bpush_leader_status_response\x18\x10 \x01(\x0b2B.tesla.proto.energy_device.v1.IntraSiteAPIPushLeaderStatusResponseH\x00\x12`\n\x16request_update_request\x18\x11 \x01(\x0b2>.tesla.proto.energy_device.v1.IntraSiteAPIRequestUpdateRequestH\x00\x12b\n\x17request_update_response\x18\x12 \x01(\x0b2?.tesla.proto.energy_device.v1.IntraSiteAPIRequestUpdateResponseH\x00\x12b\n\x17complete_update_request\x18\x13 \x01(\x0b2?.tesla.proto.energy_device.v1.IntraSiteAPICompleteUpdateRequestH\x00\x12d\n\x18complete_update_response\x18\x14 \x01(\x0b2@.tesla.proto.energy_device.v1.IntraSiteAPICompleteUpdateResponseH\x00\x12M\n\x0cpair_request\x18\x15 \x01(\x0b25.tesla.proto.energy_device.v1.IntraSiteAPIPairRequestH\x00\x12O\n\rpair_response\x18\x16 \x01(\x0b26.tesla.proto.energy_device.v1.IntraSiteAPIPairResponseH\x00\x12Q\n\x0eunpair_request\x18\x17 \x01(\x0b27.tesla.proto.energy_device.v1.IntraSiteAPIUnpairRequestH\x00\x12S\n\x0funpair_response\x18\x18 \x01(\x0b28.tesla.proto.energy_device.v1.IntraSiteAPIUnpairResponseH\x00B\t\n\x07message*\xaa\x01\n\x1eIntraSiteBackhaulInterfaceType\x12.\n*INTRA_SITE_BACKHAUL_INTERFACE_TYPE_INVALID\x10\x00\x12+\n\'INTRA_SITE_BACKHAUL_INTERFACE_TYPE_WIFI\x10\x01\x12+\n\'INTRA_SITE_BACKHAUL_INTERFACE_TYPE_CELL\x10\x02*\x90\x01\n\x17IntraSiteBackhaulStatus\x12&\n"INTRA_SITE_BACKHAUL_STATUS_INVALID\x10\x00\x12&\n"INTRA_SITE_BACKHAUL_STATUS_OFFLINE\x10\x01\x12%\n!INTRA_SITE_BACKHAUL_STATUS_ONLINE\x10\x02*\x94\x01\n\x15IntraSiteLeaderStatus\x12$\n INTRA_SITE_LEADER_STATUS_INVALID\x10\x00\x120\n,INTRA_SITE_LEADER_STATUS_TEMPORARILY_OFFLINE\x10\x01\x12#\n\x1fINTRA_SITE_LEADER_STATUS_ONLINE\x10\x02*\xa7\x02\n\x1aIntraSiteJoinNetworkResult\x12*\n&INTRA_SITE_JOIN_NETWORK_RESULT_INVALID\x10\x00\x12+\n\'INTRA_SITE_JOIN_NETWORK_RESULT_ACCEPTED\x10\x01\x12:\n6INTRA_SITE_JOIN_NETWORK_RESULT_REJECTED_ALREADY_JOINED\x10\x02\x128\n4INTRA_SITE_JOIN_NETWORK_RESULT_REJECTED_INCOMPATIBLE\x10\x03\x12:\n6INTRA_SITE_JOIN_NETWORK_RESULT_REJECTED_INTERNAL_ERROR\x10\x04*\x8b\x03\n\x13IntraSitePairResult\x12"\n\x1eINTRA_SITE_PAIR_RESULT_INVALID\x10\x00\x12#\n\x1fINTRA_SITE_PAIR_RESULT_ACCEPTED\x10\x01\x12D\n@INTRA_SITE_PAIR_RESULT_REJECTED_DIFFERENT_NETWORK_ALREADY_JOINED\x10\x02\x122\n.INTRA_SITE_PAIR_RESULT_REJECTED_INTERNAL_ERROR\x10\x03\x12=\n9INTRA_SITE_PAIR_RESULT_REJECTED_UNSUPPORTED_SERVICE_TYPES\x10\x04\x128\n4INTRA_SITE_PAIR_RESULT_REJECTED_UNSUPPORTED_LAN_TYPE\x10\x05\x128\n4INTRA_SITE_PAIR_RESULT_REJECTED_NO_PROOF_OF_PRESENCE\x10\x06*\xa0\x02\n\x15IntraSiteUnpairResult\x12$\n INTRA_SITE_UNPAIR_RESULT_INVALID\x10\x00\x12%\n!INTRA_SITE_UNPAIR_RESULT_ACCEPTED\x10\x01\x12E\nAINTRA_SITE_UNPAIR_RESULT_REJECTED_NETWORK_LED_BY_DIFFERENT_LEADER\x10\x02\x126\n2INTRA_SITE_UNPAIR_RESULT_REJECTED_DEVICE_IS_LEADER\x10\x03\x12;\n7INTRA_SITE_UNPAIR_RESULT_REJECTED_UNSUPPORTED_OPERATION\x10\x04*\xe8\x02\n\x1dIntraSiteCompleteUpdateResult\x12-\n)INTRA_SITE_COMPLETE_UPDATE_RESULT_INVALID\x10\x00\x126\n2INTRA_SITE_COMPLETE_UPDATE_RESULT_FIRMWARE_MATCHES\x10\x01\x127\n3INTRA_SITE_COMPLETE_UPDATE_RESULT_TERMINATE_SUCCESS\x10\x02\x127\n3INTRA_SITE_COMPLETE_UPDATE_RESULT_TERMINATE_FAILURE\x10\x03\x127\n3INTRA_SITE_COMPLETE_UPDATE_RESULT_HANDSHAKE_FAILURE\x10\x04\x125\n1INTRA_SITE_COMPLETE_UPDATE_RESULT_UNKNOWN_FAILURE\x10\x05*\x9e\x01\n\x18IntraSiteHeartbeatResult\x12\'\n#INTRA_SITE_HEARTBEAT_RESULT_INVALID\x10\x00\x12(\n$INTRA_SITE_HEARTBEAT_RESULT_ACCEPTED\x10\x01\x12/\n+INTRA_SITE_HEARTBEAT_RESULT_NOT_ON_MANIFEST\x10\x02*y\n\x10IntraSiteLanType\x12\x1f\n\x1bINTRA_SITE_LAN_TYPE_INVALID\x10\x00\x12\x1f\n\x1bINTRA_SITE_LAN_TYPE_SOFT_AP\x10\x01\x12#\n\x1fINTRA_SITE_LAN_TYPE_PRE_DEFINED\x10\x02B\x80\x01\n$com.tesla.generated.energy_device.v1B\x0cIntraSiteApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'intra_site_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x0cIntraSiteApiZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_INTRASITEBACKHAULINTERFACETYPE']._serialized_start = 5022
    _globals['_INTRASITEBACKHAULINTERFACETYPE']._serialized_end = 5192
    _globals['_INTRASITEBACKHAULSTATUS']._serialized_start = 5195
    _globals['_INTRASITEBACKHAULSTATUS']._serialized_end = 5339
    _globals['_INTRASITELEADERSTATUS']._serialized_start = 5342
    _globals['_INTRASITELEADERSTATUS']._serialized_end = 5490
    _globals['_INTRASITEJOINNETWORKRESULT']._serialized_start = 5493
    _globals['_INTRASITEJOINNETWORKRESULT']._serialized_end = 5788
    _globals['_INTRASITEPAIRRESULT']._serialized_start = 5791
    _globals['_INTRASITEPAIRRESULT']._serialized_end = 6186
    _globals['_INTRASITEUNPAIRRESULT']._serialized_start = 6189
    _globals['_INTRASITEUNPAIRRESULT']._serialized_end = 6477
    _globals['_INTRASITECOMPLETEUPDATERESULT']._serialized_start = 6480
    _globals['_INTRASITECOMPLETEUPDATERESULT']._serialized_end = 6840
    _globals['_INTRASITEHEARTBEATRESULT']._serialized_start = 6843
    _globals['_INTRASITEHEARTBEATRESULT']._serialized_end = 7001
    _globals['_INTRASITELANTYPE']._serialized_start = 7003
    _globals['_INTRASITELANTYPE']._serialized_end = 7124
    _globals['_INTRASITECONFIG']._serialized_start = 96
    _globals['_INTRASITECONFIG']._serialized_end = 587
    _globals['_INTRASITEAPIPAIRREQUEST']._serialized_start = 589
    _globals['_INTRASITEAPIPAIRREQUEST']._serialized_end = 675
    _globals['_INTRASITEAPIPAIRRESPONSE']._serialized_start = 677
    _globals['_INTRASITEAPIPAIRRESPONSE']._serialized_end = 770
    _globals['_INTRASITEAPIUNPAIRREQUEST']._serialized_start = 772
    _globals['_INTRASITEAPIUNPAIRREQUEST']._serialized_end = 799
    _globals['_INTRASITEAPIUNPAIRRESPONSE']._serialized_start = 801
    _globals['_INTRASITEAPIUNPAIRRESPONSE']._serialized_end = 898
    _globals['_INTRASITEAPIJOINNETWORKREQUEST']._serialized_start = 900
    _globals['_INTRASITEAPIJOINNETWORKREQUEST']._serialized_end = 993
    _globals['_INTRASITEAPIJOINNETWORKRESPONSE']._serialized_start = 995
    _globals['_INTRASITEAPIJOINNETWORKRESPONSE']._serialized_end = 1102
    _globals['_INTRASITEAPIADDDEVICEREQUEST']._serialized_start = 1105
    _globals['_INTRASITEAPIADDDEVICEREQUEST']._serialized_end = 1263
    _globals['_INTRASITEAPIADDDEVICERESPONSE']._serialized_start = 1265
    _globals['_INTRASITEAPIADDDEVICERESPONSE']._serialized_end = 1371
    _globals['_INTRASITEAPIPUSHADDDEVICERESULTREQUEST']._serialized_start = 1374
    _globals['_INTRASITEAPIPUSHADDDEVICERESULTREQUEST']._serialized_end = 1556
    _globals['_INTRASITEAPIPUSHADDDEVICERESULTRESPONSE']._serialized_start = 1558
    _globals['_INTRASITEAPIPUSHADDDEVICERESULTRESPONSE']._serialized_end = 1599
    _globals['_INTRASITEAPILEAVENETWORKREQUEST']._serialized_start = 1601
    _globals['_INTRASITEAPILEAVENETWORKREQUEST']._serialized_end = 1634
    _globals['_INTRASITEAPILEAVENETWORKRESPONSE']._serialized_start = 1636
    _globals['_INTRASITEAPILEAVENETWORKRESPONSE']._serialized_end = 1670
    _globals['_INTRASITEAPIPUSHHEARTBEATREQUEST']._serialized_start = 1672
    _globals['_INTRASITEAPIPUSHHEARTBEATREQUEST']._serialized_end = 1706
    _globals['_INTRASITEAPIPUSHHEARTBEATRESPONSE']._serialized_start = 1708
    _globals['_INTRASITEAPIPUSHHEARTBEATRESPONSE']._serialized_end = 1815
    _globals['_INTRASITEAPIPUSHCONFIGREQUEST']._serialized_start = 1817
    _globals['_INTRASITEAPIPUSHCONFIGREQUEST']._serialized_end = 1909
    _globals['_INTRASITEAPIPUSHCONFIGRESPONSE']._serialized_start = 1911
    _globals['_INTRASITEAPIPUSHCONFIGRESPONSE']._serialized_end = 1943
    _globals['_INTRASITEAPIPUSHBACKHAULSTATUSREQUEST']._serialized_start = 1946
    _globals['_INTRASITEAPIPUSHBACKHAULSTATUSREQUEST']._serialized_end = 2160
    _globals['_INTRASITEAPIPUSHBACKHAULSTATUSRESPONSE']._serialized_start = 2162
    _globals['_INTRASITEAPIPUSHBACKHAULSTATUSRESPONSE']._serialized_end = 2202
    _globals['_INTRASITEAPIPUSHLEADERSTATUSREQUEST']._serialized_start = 2205
    _globals['_INTRASITEAPIPUSHLEADERSTATUSREQUEST']._serialized_end = 2340
    _globals['_INTRASITEAPIPUSHLEADERSTATUSRESPONSE']._serialized_start = 2342
    _globals['_INTRASITEAPIPUSHLEADERSTATUSRESPONSE']._serialized_end = 2380
    _globals['_INTRASITEAPIREQUESTUPDATEREQUEST']._serialized_start = 2382
    _globals['_INTRASITEAPIREQUESTUPDATEREQUEST']._serialized_end = 2429
    _globals['_INTRASITEAPIREQUESTUPDATERESPONSE']._serialized_start = 2431
    _globals['_INTRASITEAPIREQUESTUPDATERESPONSE']._serialized_end = 2485
    _globals['_INTRASITEAPICOMPLETEUPDATEREQUEST']._serialized_start = 2487
    _globals['_INTRASITEAPICOMPLETEUPDATEREQUEST']._serialized_end = 2612
    _globals['_INTRASITEAPICOMPLETEUPDATERESPONSE']._serialized_start = 2614
    _globals['_INTRASITEAPICOMPLETEUPDATERESPONSE']._serialized_end = 2650
    _globals['_INTRASITEMESSAGES']._serialized_start = 2653
    _globals['_INTRASITEMESSAGES']._serialized_end = 5019