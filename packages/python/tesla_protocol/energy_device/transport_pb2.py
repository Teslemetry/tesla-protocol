"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'transport.proto')
_sym_db = _symbol_database.Default()
from . import authorization_types_pb2 as authorization__types__pb2
from . import authorization_api_pb2 as authorization__api__pb2
from . import common_api_pb2 as common__api__pb2
from . import teg_api_pb2 as teg__api__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftransport.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x19authorization_types.proto\x1a\x17authorization_api.proto\x1a\x10common_api.proto\x1a\rteg_api.proto"L\n\x0cExternalAuth\x12<\n\x04type\x18\x01 \x01(\x0e2..tesla.proto.energy_device.v1.ExternalAuthType"l\n\x0cAuthEnvelope\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12C\n\rexternal_auth\x18\x02 \x01(\x0b2*.tesla.proto.energy_device.v1.ExternalAuthH\x00B\x06\n\x04auth"\xf9\x01\n\x0bParticipant\x12\r\n\x03din\x18\x01 \x01(\tH\x00\x12C\n\rtesla_service\x18\x02 \x01(\x0e2*.tesla.proto.energy_device.v1.TeslaServiceH\x00\x12?\n\x05local\x18\x03 \x01(\x0e2..tesla.proto.energy_device.v1.LocalParticipantH\x00\x12O\n\x11authorized_client\x18\x04 \x01(\x0e22.tesla.proto.energy_device.v1.AuthorizedClientTypeH\x00B\x04\n\x02id"H\n\x13RegistrationPayload\x12"\n\x1acustomer_registration_info\x18\x01 \x01(\x0c\x12\r\n\x05nonce\x18\x02 \x01(\x0c"\xac\x03\n\x0fMessageEnvelope\x12G\n\x10delivery_channel\x18\x01 \x01(\x0e2-.tesla.proto.energy_device.v1.DeliveryChannel\x129\n\x06sender\x18\x02 \x01(\x0b2).tesla.proto.energy_device.v1.Participant\x12<\n\trecipient\x18\x03 \x01(\x0b2).tesla.proto.energy_device.v1.Participant\x12>\n\x06common\x18\x04 \x01(\x0b2,.tesla.proto.energy_device.v1.CommonMessagesH\x00\x128\n\x03teg\x18\x05 \x01(\x0b2).tesla.proto.energy_device.v1.TEGMessagesH\x00\x12L\n\rauthorization\x18\x0c \x01(\x0b23.tesla.proto.energy_device.v1.AuthorizationMessagesH\x00B\t\n\x07payloadJ\x04\x08\x07\x10\x08*\x90\x01\n\x0fDeliveryChannel\x12\x1c\n\x18DELIVERY_CHANNEL_INVALID\x10\x00\x12 \n\x1cDELIVERY_CHANNEL_LOCAL_HTTPS\x10\x01\x12#\n\x1fDELIVERY_CHANNEL_HERMES_COMMAND\x10\x02\x12\x18\n\x14DELIVERY_CHANNEL_BLE\x10\x03*D\n\x0cTeslaService\x12\x19\n\x15TESLA_SERVICE_INVALID\x10\x00\x12\x19\n\x15TESLA_SERVICE_COMMAND\x10\x01*r\n\x10LocalParticipant\x12\x1d\n\x19LOCAL_PARTICIPANT_INVALID\x10\x00\x12\x1f\n\x1bLOCAL_PARTICIPANT_INSTALLER\x10\x01\x12\x1e\n\x1aLOCAL_PARTICIPANT_CUSTOMER\x10\x02*\x97\x01\n\x10ExternalAuthType\x12\x1e\n\x1aEXTERNAL_AUTH_TYPE_INVALID\x10\x00\x12\x1f\n\x1bEXTERNAL_AUTH_TYPE_PRESENCE\x10\x01\x12\x1b\n\x17EXTERNAL_AUTH_TYPE_MTLS\x10\x02\x12%\n!EXTERNAL_AUTH_TYPE_HERMES_COMMAND\x10\x04B}\n$com.tesla.generated.energy_device.v1B\tTransportZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\tTransportZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_DELIVERYCHANNEL']._serialized_start = 1080
    _globals['_DELIVERYCHANNEL']._serialized_end = 1224
    _globals['_TESLASERVICE']._serialized_start = 1226
    _globals['_TESLASERVICE']._serialized_end = 1294
    _globals['_LOCALPARTICIPANT']._serialized_start = 1296
    _globals['_LOCALPARTICIPANT']._serialized_end = 1410
    _globals['_EXTERNALAUTHTYPE']._serialized_start = 1413
    _globals['_EXTERNALAUTHTYPE']._serialized_end = 1564
    _globals['_EXTERNALAUTH']._serialized_start = 134
    _globals['_EXTERNALAUTH']._serialized_end = 210
    _globals['_AUTHENVELOPE']._serialized_start = 212
    _globals['_AUTHENVELOPE']._serialized_end = 320
    _globals['_PARTICIPANT']._serialized_start = 323
    _globals['_PARTICIPANT']._serialized_end = 572
    _globals['_REGISTRATIONPAYLOAD']._serialized_start = 574
    _globals['_REGISTRATIONPAYLOAD']._serialized_end = 646
    _globals['_MESSAGEENVELOPE']._serialized_start = 649
    _globals['_MESSAGEENVELOPE']._serialized_end = 1077