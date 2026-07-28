from . import authorization_types_pb2 as _authorization_types_pb2
from . import authorization_api_pb2 as _authorization_api_pb2
from . import common_api_pb2 as _common_api_pb2
from . import teg_api_pb2 as _teg_api_pb2
from . import wall_connector_pb2 as _wall_connector_pb2
from . import pvi_api_pb2 as _pvi_api_pb2
from . import local_auth_api_pb2 as _local_auth_api_pb2
from . import neurio_meter_api_pb2 as _neurio_meter_api_pb2
from . import energy_site_net_pb2 as _energy_site_net_pb2
from . import intra_site_api_pb2 as _intra_site_api_pb2
from . import filestore_api_pb2 as _filestore_api_pb2
from . import graphql_api_pb2 as _graphql_api_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

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

class LocalParticipant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCAL_PARTICIPANT_INVALID: _ClassVar[LocalParticipant]
    LOCAL_PARTICIPANT_INSTALLER: _ClassVar[LocalParticipant]
    LOCAL_PARTICIPANT_CUSTOMER: _ClassVar[LocalParticipant]

class ExternalAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXTERNAL_AUTH_TYPE_INVALID: _ClassVar[ExternalAuthType]
    EXTERNAL_AUTH_TYPE_PRESENCE: _ClassVar[ExternalAuthType]
    EXTERNAL_AUTH_TYPE_MTLS: _ClassVar[ExternalAuthType]
    EXTERNAL_AUTH_TYPE_HERMES_COMMAND: _ClassVar[ExternalAuthType]
DELIVERY_CHANNEL_INVALID: DeliveryChannel
DELIVERY_CHANNEL_LOCAL_HTTPS: DeliveryChannel
DELIVERY_CHANNEL_HERMES_COMMAND: DeliveryChannel
DELIVERY_CHANNEL_BLE: DeliveryChannel
TESLA_SERVICE_INVALID: TeslaService
TESLA_SERVICE_COMMAND: TeslaService
LOCAL_PARTICIPANT_INVALID: LocalParticipant
LOCAL_PARTICIPANT_INSTALLER: LocalParticipant
LOCAL_PARTICIPANT_CUSTOMER: LocalParticipant
EXTERNAL_AUTH_TYPE_INVALID: ExternalAuthType
EXTERNAL_AUTH_TYPE_PRESENCE: ExternalAuthType
EXTERNAL_AUTH_TYPE_MTLS: ExternalAuthType
EXTERNAL_AUTH_TYPE_HERMES_COMMAND: ExternalAuthType

class ExternalAuth(_message.Message):
    __slots__ = ('type',)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ExternalAuthType

    def __init__(self, type: _Optional[_Union[ExternalAuthType, str]]=...) -> None:
        ...

class AuthEnvelope(_message.Message):
    __slots__ = ('payload', 'external_auth')
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_AUTH_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    external_auth: ExternalAuth

    def __init__(self, payload: _Optional[bytes]=..., external_auth: _Optional[_Union[ExternalAuth, _Mapping]]=...) -> None:
        ...

class Participant(_message.Message):
    __slots__ = ('din', 'tesla_service', 'local', 'authorized_client')
    DIN_FIELD_NUMBER: _ClassVar[int]
    TESLA_SERVICE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_CLIENT_FIELD_NUMBER: _ClassVar[int]
    din: str
    tesla_service: TeslaService
    local: LocalParticipant
    authorized_client: _authorization_types_pb2.AuthorizedClientType

    def __init__(self, din: _Optional[str]=..., tesla_service: _Optional[_Union[TeslaService, str]]=..., local: _Optional[_Union[LocalParticipant, str]]=..., authorized_client: _Optional[_Union[_authorization_types_pb2.AuthorizedClientType, str]]=...) -> None:
        ...

class RegistrationPayload(_message.Message):
    __slots__ = ('customer_registration_info', 'nonce')
    CUSTOMER_REGISTRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    customer_registration_info: bytes
    nonce: bytes

    def __init__(self, customer_registration_info: _Optional[bytes]=..., nonce: _Optional[bytes]=...) -> None:
        ...

class MessageEnvelope(_message.Message):
    __slots__ = ('delivery_channel', 'sender', 'recipient', 'common', 'teg', 'wc', 'pvi', 'localauth', 'neuriometer', 'energysitenet', 'intrasite', 'authorization', 'filestore', 'graphql')
    DELIVERY_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    COMMON_FIELD_NUMBER: _ClassVar[int]
    TEG_FIELD_NUMBER: _ClassVar[int]
    WC_FIELD_NUMBER: _ClassVar[int]
    PVI_FIELD_NUMBER: _ClassVar[int]
    LOCALAUTH_FIELD_NUMBER: _ClassVar[int]
    NEURIOMETER_FIELD_NUMBER: _ClassVar[int]
    ENERGYSITENET_FIELD_NUMBER: _ClassVar[int]
    INTRASITE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    FILESTORE_FIELD_NUMBER: _ClassVar[int]
    GRAPHQL_FIELD_NUMBER: _ClassVar[int]
    delivery_channel: DeliveryChannel
    sender: Participant
    recipient: Participant
    common: _common_api_pb2.CommonMessages
    teg: _teg_api_pb2.TEGMessages
    wc: _wall_connector_pb2.WCMessages
    pvi: _pvi_api_pb2.PVIMessages
    localauth: _local_auth_api_pb2.LocalAuthMessages
    neuriometer: _neurio_meter_api_pb2.NeurioMeterMessages
    energysitenet: _energy_site_net_pb2.EnergySiteNetMessages
    intrasite: _intra_site_api_pb2.IntraSiteMessages
    authorization: _authorization_api_pb2.AuthorizationMessages
    filestore: _filestore_api_pb2.FileStoreMessages
    graphql: _graphql_api_pb2.GraphQLMessages

    def __init__(self, delivery_channel: _Optional[_Union[DeliveryChannel, str]]=..., sender: _Optional[_Union[Participant, _Mapping]]=..., recipient: _Optional[_Union[Participant, _Mapping]]=..., common: _Optional[_Union[_common_api_pb2.CommonMessages, _Mapping]]=..., teg: _Optional[_Union[_teg_api_pb2.TEGMessages, _Mapping]]=..., wc: _Optional[_Union[_wall_connector_pb2.WCMessages, _Mapping]]=..., pvi: _Optional[_Union[_pvi_api_pb2.PVIMessages, _Mapping]]=..., localauth: _Optional[_Union[_local_auth_api_pb2.LocalAuthMessages, _Mapping]]=..., neuriometer: _Optional[_Union[_neurio_meter_api_pb2.NeurioMeterMessages, _Mapping]]=..., energysitenet: _Optional[_Union[_energy_site_net_pb2.EnergySiteNetMessages, _Mapping]]=..., intrasite: _Optional[_Union[_intra_site_api_pb2.IntraSiteMessages, _Mapping]]=..., authorization: _Optional[_Union[_authorization_api_pb2.AuthorizationMessages, _Mapping]]=..., filestore: _Optional[_Union[_filestore_api_pb2.FileStoreMessages, _Mapping]]=..., graphql: _Optional[_Union[_graphql_api_pb2.GraphQLMessages, _Mapping]]=...) -> None:
        ...