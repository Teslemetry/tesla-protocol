from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class IdentifierType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDENTIFIER_TYPE_INVALID: _ClassVar[IdentifierType]
    IDENTIFIER_TYPE_GATEWAY_DIN: _ClassVar[IdentifierType]
    IDENTIFIER_TYPE_SITE_UUID: _ClassVar[IdentifierType]
    IDENTIFIER_TYPE_SOLAR_INVERTER_DIN: _ClassVar[IdentifierType]
    IDENTIFIER_TYPE_WALL_CONNECTOR_DIN: _ClassVar[IdentifierType]
IDENTIFIER_TYPE_INVALID: IdentifierType
IDENTIFIER_TYPE_GATEWAY_DIN: IdentifierType
IDENTIFIER_TYPE_SITE_UUID: IdentifierType
IDENTIFIER_TYPE_SOLAR_INVERTER_DIN: IdentifierType
IDENTIFIER_TYPE_WALL_CONNECTOR_DIN: IdentifierType