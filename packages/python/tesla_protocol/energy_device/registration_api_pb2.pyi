import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from tesla_protocol.energy_device import device_pb2 as _device_pb2
from tesla_protocol.energy_device import update_pb2 as _update_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROJECT_ACCESS_TYPE_INVALID: _ClassVar[ProjectAccessType]
    PROJECT_ACCESS_TYPE_SERVICE: _ClassVar[ProjectAccessType]
    PROJECT_ACCESS_TYPE_MANUFACTURING: _ClassVar[ProjectAccessType]
    PROJECT_ACCESS_TYPE_ENGINEERING: _ClassVar[ProjectAccessType]
    PROJECT_ACCESS_TYPE_PRIVATE: _ClassVar[ProjectAccessType]
    PROJECT_ACCESS_TYPE_PUBLIC: _ClassVar[ProjectAccessType]

class PropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_TYPE_INVALID: _ClassVar[PropertyType]
    PROPERTY_TYPE_SHOPPING_MALL_CENTER: _ClassVar[PropertyType]
    PROPERTY_TYPE_RESTAURANT: _ClassVar[PropertyType]
    PROPERTY_TYPE_GAS_STATION: _ClassVar[PropertyType]
    PROPERTY_TYPE_SERVICE_PLAZA_REST_AREA: _ClassVar[PropertyType]
    PROPERTY_TYPE_HOTEL_RESORT_TOURIST_COMPLEX: _ClassVar[PropertyType]
    PROPERTY_TYPE_GROCERY_STORE: _ClassVar[PropertyType]
    PROPERTY_TYPE_TESLA_STORE_SERVICE_CENTER: _ClassVar[PropertyType]
    PROPERTY_TYPE_OFFICE: _ClassVar[PropertyType]
    PROPERTY_TYPE_RESIDENTIAL_BUILDING: _ClassVar[PropertyType]
    PROPERTY_TYPE_PARKING_GARAGE_PUBLIC_PARKING_LOT: _ClassVar[PropertyType]
    PROPERTY_TYPE_BANK: _ClassVar[PropertyType]
    PROPERTY_TYPE_AIRPORT: _ClassVar[PropertyType]
    PROPERTY_TYPE_CITY_VISITOR_CENTER_CITY_PROPERTY: _ClassVar[PropertyType]
    PROPERTY_TYPE_MUSEUM_AMUSEMENT_ATTRACTION: _ClassVar[PropertyType]
    PROPERTY_TYPE_UNIVERSITY_SCHOOL: _ClassVar[PropertyType]
    PROPERTY_TYPE_WINERY: _ClassVar[PropertyType]
    PROPERTY_TYPE_AUTOMOTIVE: _ClassVar[PropertyType]
    PROPERTY_TYPE_MIXED_USE: _ClassVar[PropertyType]
    PROPERTY_TYPE_RECREATION: _ClassVar[PropertyType]
    PROPERTY_TYPE_RENTAL_PROPERTY: _ClassVar[PropertyType]
    PROPERTY_TYPE_WORKPLACE: _ClassVar[PropertyType]

class RegistrationDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGISTRATION_DEVICE_TYPE_INVALID: _ClassVar[RegistrationDeviceType]
    REGISTRATION_DEVICE_TYPE_POWERWALL: _ClassVar[RegistrationDeviceType]
    REGISTRATION_DEVICE_TYPE_POWERWALL_EXPANSION: _ClassVar[RegistrationDeviceType]
    REGISTRATION_DEVICE_TYPE_PV_INVERTER: _ClassVar[RegistrationDeviceType]
    REGISTRATION_DEVICE_TYPE_WALL_CONNECTOR: _ClassVar[RegistrationDeviceType]
    REGISTRATION_DEVICE_TYPE_POWERWALL_3: _ClassVar[RegistrationDeviceType]
    REGISTRATION_DEVICE_TYPE_POWERWALL_3_EXPANSION: _ClassVar[RegistrationDeviceType]

class RegistrationSiteRelationshipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGISTRATION_SITE_RELATIONSHIP_TYPE_INVALID: _ClassVar[RegistrationSiteRelationshipType]
    REGISTRATION_SITE_RELATIONSHIP_TYPE_OWNER: _ClassVar[RegistrationSiteRelationshipType]
    REGISTRATION_SITE_RELATIONSHIP_TYPE_INSTALLER: _ClassVar[RegistrationSiteRelationshipType]
    REGISTRATION_SITE_RELATIONSHIP_TYPE_FINANCIER: _ClassVar[RegistrationSiteRelationshipType]
    REGISTRATION_SITE_RELATIONSHIP_TYPE_SERVICER: _ClassVar[RegistrationSiteRelationshipType]

class RegistrationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGISTRATION_SOURCE_INVALID: _ClassVar[RegistrationSource]
    REGISTRATION_SOURCE_AUTOCONFIG: _ClassVar[RegistrationSource]
    REGISTRATION_SOURCE_INSTALLER: _ClassVar[RegistrationSource]
    REGISTRATION_SOURCE_CUSTOMER: _ClassVar[RegistrationSource]

class RegistrationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGISTRATION_STATUS_INVALID: _ClassVar[RegistrationStatus]
    REGISTRATION_STATUS_MISSING_INFO: _ClassVar[RegistrationStatus]
    REGISTRATION_STATUS_UNDERWAY: _ClassVar[RegistrationStatus]
    REGISTRATION_STATUS_ALREADY_REGISTERED: _ClassVar[RegistrationStatus]
    REGISTRATION_STATUS_FAILED: _ClassVar[RegistrationStatus]
    REGISTRATION_STATUS_RETRY_WITH_NO_FURTHER_ACTION: _ClassVar[RegistrationStatus]

class WCLoadSharingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WC_LOAD_SHARING_TYPE_INVALID: _ClassVar[WCLoadSharingType]
    WC_LOAD_SHARING_TYPE_LEADER: _ClassVar[WCLoadSharingType]
    WC_LOAD_SHARING_TYPE_FOLLOWER: _ClassVar[WCLoadSharingType]
PROJECT_ACCESS_TYPE_INVALID: ProjectAccessType
PROJECT_ACCESS_TYPE_SERVICE: ProjectAccessType
PROJECT_ACCESS_TYPE_MANUFACTURING: ProjectAccessType
PROJECT_ACCESS_TYPE_ENGINEERING: ProjectAccessType
PROJECT_ACCESS_TYPE_PRIVATE: ProjectAccessType
PROJECT_ACCESS_TYPE_PUBLIC: ProjectAccessType
PROPERTY_TYPE_INVALID: PropertyType
PROPERTY_TYPE_SHOPPING_MALL_CENTER: PropertyType
PROPERTY_TYPE_RESTAURANT: PropertyType
PROPERTY_TYPE_GAS_STATION: PropertyType
PROPERTY_TYPE_SERVICE_PLAZA_REST_AREA: PropertyType
PROPERTY_TYPE_HOTEL_RESORT_TOURIST_COMPLEX: PropertyType
PROPERTY_TYPE_GROCERY_STORE: PropertyType
PROPERTY_TYPE_TESLA_STORE_SERVICE_CENTER: PropertyType
PROPERTY_TYPE_OFFICE: PropertyType
PROPERTY_TYPE_RESIDENTIAL_BUILDING: PropertyType
PROPERTY_TYPE_PARKING_GARAGE_PUBLIC_PARKING_LOT: PropertyType
PROPERTY_TYPE_BANK: PropertyType
PROPERTY_TYPE_AIRPORT: PropertyType
PROPERTY_TYPE_CITY_VISITOR_CENTER_CITY_PROPERTY: PropertyType
PROPERTY_TYPE_MUSEUM_AMUSEMENT_ATTRACTION: PropertyType
PROPERTY_TYPE_UNIVERSITY_SCHOOL: PropertyType
PROPERTY_TYPE_WINERY: PropertyType
PROPERTY_TYPE_AUTOMOTIVE: PropertyType
PROPERTY_TYPE_MIXED_USE: PropertyType
PROPERTY_TYPE_RECREATION: PropertyType
PROPERTY_TYPE_RENTAL_PROPERTY: PropertyType
PROPERTY_TYPE_WORKPLACE: PropertyType
REGISTRATION_DEVICE_TYPE_INVALID: RegistrationDeviceType
REGISTRATION_DEVICE_TYPE_POWERWALL: RegistrationDeviceType
REGISTRATION_DEVICE_TYPE_POWERWALL_EXPANSION: RegistrationDeviceType
REGISTRATION_DEVICE_TYPE_PV_INVERTER: RegistrationDeviceType
REGISTRATION_DEVICE_TYPE_WALL_CONNECTOR: RegistrationDeviceType
REGISTRATION_DEVICE_TYPE_POWERWALL_3: RegistrationDeviceType
REGISTRATION_DEVICE_TYPE_POWERWALL_3_EXPANSION: RegistrationDeviceType
REGISTRATION_SITE_RELATIONSHIP_TYPE_INVALID: RegistrationSiteRelationshipType
REGISTRATION_SITE_RELATIONSHIP_TYPE_OWNER: RegistrationSiteRelationshipType
REGISTRATION_SITE_RELATIONSHIP_TYPE_INSTALLER: RegistrationSiteRelationshipType
REGISTRATION_SITE_RELATIONSHIP_TYPE_FINANCIER: RegistrationSiteRelationshipType
REGISTRATION_SITE_RELATIONSHIP_TYPE_SERVICER: RegistrationSiteRelationshipType
REGISTRATION_SOURCE_INVALID: RegistrationSource
REGISTRATION_SOURCE_AUTOCONFIG: RegistrationSource
REGISTRATION_SOURCE_INSTALLER: RegistrationSource
REGISTRATION_SOURCE_CUSTOMER: RegistrationSource
REGISTRATION_STATUS_INVALID: RegistrationStatus
REGISTRATION_STATUS_MISSING_INFO: RegistrationStatus
REGISTRATION_STATUS_UNDERWAY: RegistrationStatus
REGISTRATION_STATUS_ALREADY_REGISTERED: RegistrationStatus
REGISTRATION_STATUS_FAILED: RegistrationStatus
REGISTRATION_STATUS_RETRY_WITH_NO_FURTHER_ACTION: RegistrationStatus
WC_LOAD_SHARING_TYPE_INVALID: WCLoadSharingType
WC_LOAD_SHARING_TYPE_LEADER: WCLoadSharingType
WC_LOAD_SHARING_TYPE_FOLLOWER: WCLoadSharingType

class AnonymizedSiteDetails(_message.Message):
    __slots__ = ("device_details", "city", "zip")
    DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    device_details: _containers.RepeatedCompositeFieldContainer[DeviceDetail]
    city: _wrappers_pb2.StringValue
    zip: _wrappers_pb2.StringValue
    def __init__(self, device_details: _Optional[_Iterable[_Union[DeviceDetail, _Mapping]]] = ..., city: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., zip: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class AssetSiteDetailsResponse(_message.Message):
    __slots__ = ("devices",)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[DeviceDetail]
    def __init__(self, devices: _Optional[_Iterable[_Union[DeviceDetail, _Mapping]]] = ...) -> None: ...

class AssetSiteUuidOfDeviceResponse(_message.Message):
    __slots__ = ("asset_site_uuid",)
    ASSET_SITE_UUID_FIELD_NUMBER: _ClassVar[int]
    asset_site_uuid: _wrappers_pb2.StringValue
    def __init__(self, asset_site_uuid: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class CommercialChargingDetails(_message.Message):
    __slots__ = ("property_type", "project_access_type", "destination_phone_number", "destination_website")
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_WEBSITE_FIELD_NUMBER: _ClassVar[int]
    property_type: PropertyType
    project_access_type: ProjectAccessType
    destination_phone_number: _wrappers_pb2.StringValue
    destination_website: _wrappers_pb2.StringValue
    def __init__(self, property_type: _Optional[_Union[PropertyType, str]] = ..., project_access_type: _Optional[_Union[ProjectAccessType, str]] = ..., destination_phone_number: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., destination_website: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class CommercialChargingDeviceProperties(_message.Message):
    __slots__ = ("main_service_size", "nominal_voltage", "load_sharing", "max_output", "latitude", "longitude", "label", "rssi", "power_type", "connector_type", "load_sharing_type")
    MAIN_SERVICE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    LOAD_SHARING_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    POWER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOAD_SHARING_TYPE_FIELD_NUMBER: _ClassVar[int]
    main_service_size: int
    nominal_voltage: int
    load_sharing: bool
    max_output: int
    latitude: _wrappers_pb2.FloatValue
    longitude: _wrappers_pb2.FloatValue
    label: _wrappers_pb2.Int32Value
    rssi: _wrappers_pb2.Int32Value
    power_type: int
    connector_type: int
    load_sharing_type: WCLoadSharingType
    def __init__(self, main_service_size: _Optional[int] = ..., nominal_voltage: _Optional[int] = ..., load_sharing: _Optional[bool] = ..., max_output: _Optional[int] = ..., latitude: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., longitude: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., label: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., rssi: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., power_type: _Optional[int] = ..., connector_type: _Optional[int] = ..., load_sharing_type: _Optional[_Union[WCLoadSharingType, str]] = ...) -> None: ...

class CommercialChargingSiteInfo(_message.Message):
    __slots__ = ("site_address", "warp_site_name", "commercial_charging_details", "site_owner_email")
    SITE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WARP_SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMERCIAL_CHARGING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SITE_OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    site_address: CustomerSiteAddress
    warp_site_name: _wrappers_pb2.StringValue
    commercial_charging_details: CommercialChargingDetails
    site_owner_email: str
    def __init__(self, site_address: _Optional[_Union[CustomerSiteAddress, _Mapping]] = ..., warp_site_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., commercial_charging_details: _Optional[_Union[CommercialChargingDetails, _Mapping]] = ..., site_owner_email: _Optional[str] = ...) -> None: ...

class CustomerInfo(_message.Message):
    __slots__ = ("sso_id", "email", "given_name", "family_name")
    SSO_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    sso_id: _device_pb2.UUIDv4
    email: str
    given_name: str
    family_name: str
    def __init__(self, sso_id: _Optional[_Union[_device_pb2.UUIDv4, _Mapping]] = ..., email: _Optional[str] = ..., given_name: _Optional[str] = ..., family_name: _Optional[str] = ...) -> None: ...

class CustomerLegalConsent(_message.Message):
    __slots__ = ("privacy_notice", "limited_warranty", "grid_services", "marketing")
    PRIVACY_NOTICE_FIELD_NUMBER: _ClassVar[int]
    LIMITED_WARRANTY_FIELD_NUMBER: _ClassVar[int]
    GRID_SERVICES_FIELD_NUMBER: _ClassVar[int]
    MARKETING_FIELD_NUMBER: _ClassVar[int]
    privacy_notice: _wrappers_pb2.BoolValue
    limited_warranty: _wrappers_pb2.BoolValue
    grid_services: _wrappers_pb2.BoolValue
    marketing: _wrappers_pb2.BoolValue
    def __init__(self, privacy_notice: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., limited_warranty: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., grid_services: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., marketing: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class CustomerSiteAddress(_message.Message):
    __slots__ = ("street", "city", "state", "zip", "country", "phone")
    STREET_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    street: str
    city: str
    state: str
    zip: str
    country: str
    phone: str
    def __init__(self, street: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., zip: _Optional[str] = ..., country: _Optional[str] = ..., phone: _Optional[str] = ...) -> None: ...

class DeactivateDeviceRequest(_message.Message):
    __slots__ = ("dins", "installer_tesla_auth_bearer_token")
    DINS_FIELD_NUMBER: _ClassVar[int]
    INSTALLER_TESLA_AUTH_BEARER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    dins: _containers.RepeatedScalarFieldContainer[str]
    installer_tesla_auth_bearer_token: str
    def __init__(self, dins: _Optional[_Iterable[str]] = ..., installer_tesla_auth_bearer_token: _Optional[str] = ...) -> None: ...

class DeviceDetail(_message.Message):
    __slots__ = ("device_type", "fallback_description", "din")
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIN_FIELD_NUMBER: _ClassVar[int]
    device_type: RegistrationDeviceType
    fallback_description: str
    din: str
    def __init__(self, device_type: _Optional[_Union[RegistrationDeviceType, str]] = ..., fallback_description: _Optional[str] = ..., din: _Optional[str] = ...) -> None: ...

class InstallationInfo(_message.Message):
    __slots__ = ("installation_guid",)
    INSTALLATION_GUID_FIELD_NUMBER: _ClassVar[int]
    installation_guid: str
    def __init__(self, installation_guid: _Optional[str] = ...) -> None: ...

class InstallerInfo(_message.Message):
    __slots__ = ("email", "account_master_id", "company_name", "phone")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_MASTER_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    email: str
    account_master_id: _device_pb2.UUIDv4
    company_name: _wrappers_pb2.StringValue
    phone: _wrappers_pb2.StringValue
    def __init__(self, email: _Optional[str] = ..., account_master_id: _Optional[_Union[_device_pb2.UUIDv4, _Mapping]] = ..., company_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., phone: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class InstallerLocation(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class PartDetail(_message.Message):
    __slots__ = ("part_number", "serial_number", "part_type", "manufacturer")
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PART_TYPE_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    part_number: str
    serial_number: str
    part_type: str
    manufacturer: _wrappers_pb2.StringValue
    def __init__(self, part_number: _Optional[str] = ..., serial_number: _Optional[str] = ..., part_type: _Optional[str] = ..., manufacturer: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class PartnerInfo(_message.Message):
    __slots__ = ("account_master_id", "site_relationship_type")
    ACCOUNT_MASTER_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    account_master_id: _device_pb2.UUIDv4
    site_relationship_type: RegistrationSiteRelationshipType
    def __init__(self, account_master_id: _Optional[_Union[_device_pb2.UUIDv4, _Mapping]] = ..., site_relationship_type: _Optional[_Union[RegistrationSiteRelationshipType, str]] = ...) -> None: ...

class RegistrationAPIDeactivateDeviceRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: DeactivateDeviceRequest
    def __init__(self, request: _Optional[_Union[DeactivateDeviceRequest, _Mapping]] = ...) -> None: ...

class RegistrationAPIDeactivateDeviceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegistrationAPIPrepareRegistrationPayloadRequest(_message.Message):
    __slots__ = ("customer_registration_info",)
    CUSTOMER_REGISTRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_registration_info: bytes
    def __init__(self, customer_registration_info: _Optional[bytes] = ...) -> None: ...

class RegistrationAPIPrepareRegistrationPayloadResponse(_message.Message):
    __slots__ = ("signed_registration_payload",)
    SIGNED_REGISTRATION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    signed_registration_payload: _device_pb2.DeviceSignedPayload
    def __init__(self, signed_registration_payload: _Optional[_Union[_device_pb2.DeviceSignedPayload, _Mapping]] = ...) -> None: ...

class RegistrationAPIRegisterRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: RegistrationRequest
    def __init__(self, request: _Optional[_Union[RegistrationRequest, _Mapping]] = ...) -> None: ...

class RegistrationAPIRegisterResponse(_message.Message):
    __slots__ = ("failure", "response")
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    failure: int
    response: RegistrationResponse
    def __init__(self, failure: _Optional[int] = ..., response: _Optional[_Union[RegistrationResponse, _Mapping]] = ...) -> None: ...

class RegistrationAPIRetrieveAssetSiteDetailsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegistrationAPIRetrieveAssetSiteDetailsResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: AssetSiteDetailsResponse
    def __init__(self, response: _Optional[_Union[AssetSiteDetailsResponse, _Mapping]] = ...) -> None: ...

class RegistrationAPIRetrieveSiteSuggestionRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: SiteSuggestionRequest
    def __init__(self, request: _Optional[_Union[SiteSuggestionRequest, _Mapping]] = ...) -> None: ...

class RegistrationAPIRetrieveSiteSuggestionResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: SiteSuggestionResponse
    def __init__(self, response: _Optional[_Union[SiteSuggestionResponse, _Mapping]] = ...) -> None: ...

class RegistrationAPIRetrieveSiteUuidRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegistrationAPIRetrieveSiteUuidResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: AssetSiteUuidOfDeviceResponse
    def __init__(self, response: _Optional[_Union[AssetSiteUuidOfDeviceResponse, _Mapping]] = ...) -> None: ...

class RegistrationMessages(_message.Message):
    __slots__ = ("prepare_registration_payload_request", "prepare_registration_payload_response", "register_request", "register_response", "retrieve_site_uuid_request", "retrieve_site_uuid_response", "retrieve_site_suggestion_request", "retrieve_site_suggestion_response", "retrieve_asset_site_details_request", "retrieve_asset_site_details_response", "deactivate_device_request", "deactivate_device_response")
    PREPARE_REGISTRATION_PAYLOAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PREPARE_REGISTRATION_PAYLOAD_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REGISTER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REGISTER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_SITE_UUID_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_SITE_UUID_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_SITE_SUGGESTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_SITE_SUGGESTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ASSET_SITE_DETAILS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_ASSET_SITE_DETAILS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_DEVICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_DEVICE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    prepare_registration_payload_request: RegistrationAPIPrepareRegistrationPayloadRequest
    prepare_registration_payload_response: RegistrationAPIPrepareRegistrationPayloadResponse
    register_request: RegistrationAPIRegisterRequest
    register_response: RegistrationAPIRegisterResponse
    retrieve_site_uuid_request: RegistrationAPIRetrieveSiteUuidRequest
    retrieve_site_uuid_response: RegistrationAPIRetrieveSiteUuidResponse
    retrieve_site_suggestion_request: RegistrationAPIRetrieveSiteSuggestionRequest
    retrieve_site_suggestion_response: RegistrationAPIRetrieveSiteSuggestionResponse
    retrieve_asset_site_details_request: RegistrationAPIRetrieveAssetSiteDetailsRequest
    retrieve_asset_site_details_response: RegistrationAPIRetrieveAssetSiteDetailsResponse
    deactivate_device_request: RegistrationAPIDeactivateDeviceRequest
    deactivate_device_response: RegistrationAPIDeactivateDeviceResponse
    def __init__(self, prepare_registration_payload_request: _Optional[_Union[RegistrationAPIPrepareRegistrationPayloadRequest, _Mapping]] = ..., prepare_registration_payload_response: _Optional[_Union[RegistrationAPIPrepareRegistrationPayloadResponse, _Mapping]] = ..., register_request: _Optional[_Union[RegistrationAPIRegisterRequest, _Mapping]] = ..., register_response: _Optional[_Union[RegistrationAPIRegisterResponse, _Mapping]] = ..., retrieve_site_uuid_request: _Optional[_Union[RegistrationAPIRetrieveSiteUuidRequest, _Mapping]] = ..., retrieve_site_uuid_response: _Optional[_Union[RegistrationAPIRetrieveSiteUuidResponse, _Mapping]] = ..., retrieve_site_suggestion_request: _Optional[_Union[RegistrationAPIRetrieveSiteSuggestionRequest, _Mapping]] = ..., retrieve_site_suggestion_response: _Optional[_Union[RegistrationAPIRetrieveSiteSuggestionResponse, _Mapping]] = ..., retrieve_asset_site_details_request: _Optional[_Union[RegistrationAPIRetrieveAssetSiteDetailsRequest, _Mapping]] = ..., retrieve_asset_site_details_response: _Optional[_Union[RegistrationAPIRetrieveAssetSiteDetailsResponse, _Mapping]] = ..., deactivate_device_request: _Optional[_Union[RegistrationAPIDeactivateDeviceRequest, _Mapping]] = ..., deactivate_device_response: _Optional[_Union[RegistrationAPIDeactivateDeviceResponse, _Mapping]] = ...) -> None: ...

class RegistrationRequest(_message.Message):
    __slots__ = ("version", "part_details", "attempt", "registration_source", "installer", "customer", "site_address", "legal_consent", "installation_info", "asset_site_id", "additional_partners")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PART_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    INSTALLER_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    SITE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LEGAL_CONSENT_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_INFO_FIELD_NUMBER: _ClassVar[int]
    ASSET_SITE_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARTNERS_FIELD_NUMBER: _ClassVar[int]
    version: _update_pb2.FirmwareVersion
    part_details: _containers.RepeatedCompositeFieldContainer[PartDetail]
    attempt: int
    registration_source: RegistrationSource
    installer: InstallerInfo
    customer: CustomerInfo
    site_address: CustomerSiteAddress
    legal_consent: CustomerLegalConsent
    installation_info: InstallationInfo
    asset_site_id: _wrappers_pb2.StringValue
    additional_partners: _containers.RepeatedCompositeFieldContainer[PartnerInfo]
    def __init__(self, version: _Optional[_Union[_update_pb2.FirmwareVersion, _Mapping]] = ..., part_details: _Optional[_Iterable[_Union[PartDetail, _Mapping]]] = ..., attempt: _Optional[int] = ..., registration_source: _Optional[_Union[RegistrationSource, str]] = ..., installer: _Optional[_Union[InstallerInfo, _Mapping]] = ..., customer: _Optional[_Union[CustomerInfo, _Mapping]] = ..., site_address: _Optional[_Union[CustomerSiteAddress, _Mapping]] = ..., legal_consent: _Optional[_Union[CustomerLegalConsent, _Mapping]] = ..., installation_info: _Optional[_Union[InstallationInfo, _Mapping]] = ..., asset_site_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., additional_partners: _Optional[_Iterable[_Union[PartnerInfo, _Mapping]]] = ...) -> None: ...

class RegistrationResponse(_message.Message):
    __slots__ = ("status", "retry_delay_s", "status_time", "asset_site_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_S_FIELD_NUMBER: _ClassVar[int]
    STATUS_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSET_SITE_ID_FIELD_NUMBER: _ClassVar[int]
    status: RegistrationStatus
    retry_delay_s: int
    status_time: _timestamp_pb2.Timestamp
    asset_site_id: _wrappers_pb2.StringValue
    def __init__(self, status: _Optional[_Union[RegistrationStatus, str]] = ..., retry_delay_s: _Optional[int] = ..., status_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., asset_site_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class SiteSuggestion(_message.Message):
    __slots__ = ("asset_site_uuid", "anonymized_site_details")
    ASSET_SITE_UUID_FIELD_NUMBER: _ClassVar[int]
    ANONYMIZED_SITE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    asset_site_uuid: str
    anonymized_site_details: AnonymizedSiteDetails
    def __init__(self, asset_site_uuid: _Optional[str] = ..., anonymized_site_details: _Optional[_Union[AnonymizedSiteDetails, _Mapping]] = ...) -> None: ...

class SiteSuggestionRequest(_message.Message):
    __slots__ = ("lookup", "installer_location", "installer_tesla_auth_bearer_token")
    LOOKUP_FIELD_NUMBER: _ClassVar[int]
    INSTALLER_LOCATION_FIELD_NUMBER: _ClassVar[int]
    INSTALLER_TESLA_AUTH_BEARER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    lookup: str
    installer_location: InstallerLocation
    installer_tesla_auth_bearer_token: str
    def __init__(self, lookup: _Optional[str] = ..., installer_location: _Optional[_Union[InstallerLocation, _Mapping]] = ..., installer_tesla_auth_bearer_token: _Optional[str] = ...) -> None: ...

class SiteSuggestionResponse(_message.Message):
    __slots__ = ("site_suggestions",)
    SITE_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    site_suggestions: _containers.RepeatedCompositeFieldContainer[SiteSuggestion]
    def __init__(self, site_suggestions: _Optional[_Iterable[_Union[SiteSuggestion, _Mapping]]] = ...) -> None: ...

class WCCommercialRegistrationRequest(_message.Message):
    __slots__ = ("device_properties", "asset_site_id", "site_info", "installer_info", "installation_completed", "site_owner_email")
    DEVICE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ASSET_SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_INFO_FIELD_NUMBER: _ClassVar[int]
    INSTALLER_INFO_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    SITE_OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    device_properties: CommercialChargingDeviceProperties
    asset_site_id: _device_pb2.UUIDv4
    site_info: CommercialChargingSiteInfo
    installer_info: InstallerInfo
    installation_completed: bool
    site_owner_email: _wrappers_pb2.StringValue
    def __init__(self, device_properties: _Optional[_Union[CommercialChargingDeviceProperties, _Mapping]] = ..., asset_site_id: _Optional[_Union[_device_pb2.UUIDv4, _Mapping]] = ..., site_info: _Optional[_Union[CommercialChargingSiteInfo, _Mapping]] = ..., installer_info: _Optional[_Union[InstallerInfo, _Mapping]] = ..., installation_completed: _Optional[bool] = ..., site_owner_email: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
