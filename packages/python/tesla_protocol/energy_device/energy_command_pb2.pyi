from tesla_protocol.energy_device import common_api_pb2 as _common_api_pb2
from tesla_protocol.energy_device import teg_api_pb2 as _teg_api_pb2
from tesla_protocol.energy_device import wall_connector_pb2 as _wall_connector_pb2
from tesla_protocol.energy_device import pvi_api_pb2 as _pvi_api_pb2
from tesla_protocol.energy_device import neurio_meter_api_pb2 as _neurio_meter_api_pb2
from tesla_protocol.energy_device import energy_site_net_pb2 as _energy_site_net_pb2
from tesla_protocol.energy_device import authorization_api_pb2 as _authorization_api_pb2
from tesla_protocol.energy_device import filestore_api_pb2 as _filestore_api_pb2
from tesla_protocol.energy_device import graphql_api_pb2 as _graphql_api_pb2
from tesla_protocol.energy_device import supercharger_api_pb2 as _supercharger_api_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceResponseTimeout(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class EnergyDeviceMessage(_message.Message):
    __slots__ = ("common", "teg", "wc", "pvi", "neuriometer", "energysitenet", "authorization", "filestore", "server", "graphql", "supercharger")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    TEG_FIELD_NUMBER: _ClassVar[int]
    WC_FIELD_NUMBER: _ClassVar[int]
    PVI_FIELD_NUMBER: _ClassVar[int]
    NEURIOMETER_FIELD_NUMBER: _ClassVar[int]
    ENERGYSITENET_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    FILESTORE_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    GRAPHQL_FIELD_NUMBER: _ClassVar[int]
    SUPERCHARGER_FIELD_NUMBER: _ClassVar[int]
    common: _common_api_pb2.CommonMessages
    teg: _teg_api_pb2.TEGMessages
    wc: _wall_connector_pb2.WCMessages
    pvi: _pvi_api_pb2.PVIMessages
    neuriometer: _neurio_meter_api_pb2.NeurioMeterMessages
    energysitenet: _energy_site_net_pb2.EnergySiteNetMessages
    authorization: _authorization_api_pb2.AuthorizationMessages
    filestore: _filestore_api_pb2.FileStoreMessages
    server: ServerMessages
    graphql: _graphql_api_pb2.GraphQLMessages
    supercharger: _supercharger_api_pb2.SuperchargerMessages
    def __init__(self, common: _Optional[_Union[_common_api_pb2.CommonMessages, _Mapping]] = ..., teg: _Optional[_Union[_teg_api_pb2.TEGMessages, _Mapping]] = ..., wc: _Optional[_Union[_wall_connector_pb2.WCMessages, _Mapping]] = ..., pvi: _Optional[_Union[_pvi_api_pb2.PVIMessages, _Mapping]] = ..., neuriometer: _Optional[_Union[_neurio_meter_api_pb2.NeurioMeterMessages, _Mapping]] = ..., energysitenet: _Optional[_Union[_energy_site_net_pb2.EnergySiteNetMessages, _Mapping]] = ..., authorization: _Optional[_Union[_authorization_api_pb2.AuthorizationMessages, _Mapping]] = ..., filestore: _Optional[_Union[_filestore_api_pb2.FileStoreMessages, _Mapping]] = ..., server: _Optional[_Union[ServerMessages, _Mapping]] = ..., graphql: _Optional[_Union[_graphql_api_pb2.GraphQLMessages, _Mapping]] = ..., supercharger: _Optional[_Union[_supercharger_api_pb2.SuperchargerMessages, _Mapping]] = ...) -> None: ...

class ServerMessages(_message.Message):
    __slots__ = ("timeout",)
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    timeout: DeviceResponseTimeout
    def __init__(self, timeout: _Optional[_Union[DeviceResponseTimeout, _Mapping]] = ...) -> None: ...
