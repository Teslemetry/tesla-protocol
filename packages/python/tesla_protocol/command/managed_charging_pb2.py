"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'managed_charging.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16managed_charging.proto\x12\x0fManagedCharging\x1a\x1egoogle/protobuf/wrappers.proto"7\n\x13ChargeOnSolarLimits\x12 \n\x18max_excess_solar_power_w\x18\x01 \x01(\x02"`\n ChargeOnSolarNoChargeRecommended\x12<\n\x06reason\x18\x01 \x01(\x0e2,.ManagedCharging.ChargeOnSolarNoChargeReason"\xa5\x01\n\x15ChargeOnSolarResponse\x12:\n\x0csolar_limits\x18\x01 \x01(\x0b2$.ManagedCharging.ChargeOnSolarLimits\x12P\n\x15no_charge_recommended\x18\x02 \x01(\x0b21.ManagedCharging.ChargeOnSolarNoChargeRecommended"?\n\rErrorResponse\x12.\n\nerror_code\x18\x01 \x01(\x0e2\x1a.ManagedCharging.ErrorCode"G\n\x0eSessionConfigs\x125\n\x10poll_interval_ms\x18\x01 \x01(\x0b2\x1b.google.protobuf.Int32Value"\x9a\x01\n\x1dManageVehicleChargingResponse\x128\n\x0fsession_configs\x18\x01 \x01(\x0b2\x1f.ManagedCharging.SessionConfigs\x12?\n\x0fcharge_on_solar\x18\x02 \x01(\x0b2&.ManagedCharging.ChargeOnSolarResponse"\xa9\x01\n\x15ManagedChargingAction\x126\n\x0eerror_response\x18\x01 \x01(\x0b2\x1e.ManagedCharging.ErrorResponse\x12X\n manage_vehicle_charging_response\x18\x02 \x01(\x0b2..ManagedCharging.ManageVehicleChargingResponse*\xc7\x02\n\x1bChargeOnSolarNoChargeReason\x12,\n(CHARGE_ON_SOLAR_NO_CHARGE_REASON_INVALID\x10\x00\x12>\n:CHARGE_ON_SOLAR_NO_CHARGE_REASON_POWERWALL_CHARGE_PRIORITY\x10\x01\x127\n3CHARGE_ON_SOLAR_NO_CHARGE_REASON_INSUFFICIENT_SOLAR\x10\x02\x129\n5CHARGE_ON_SOLAR_NO_CHARGE_REASON_GRID_EXPORT_PRIORITY\x10\x03\x12F\nBCHARGE_ON_SOLAR_NO_CHARGE_REASON_ALTERNATE_VEHICLE_CHARGE_PRIORITY\x10\x04*b\n\tErrorCode\x12\x16\n\x12ERROR_CODE_INVALID\x10\x00\x12$\n ERROR_CODE_FEATURE_NOT_SUPPORTED\x10\x01\x12\x17\n\x13ERROR_CODE_INTERNAL\x10\x02BNZLgithub.com/teslamotors/vehicle-command/pkg/protocol/protobuf/managedchargingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'managed_charging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/teslamotors/vehicle-command/pkg/protocol/protobuf/managedcharging'
    _globals['_CHARGEONSOLARNOCHARGEREASON']._serialized_start = 866
    _globals['_CHARGEONSOLARNOCHARGEREASON']._serialized_end = 1193
    _globals['_ERRORCODE']._serialized_start = 1195
    _globals['_ERRORCODE']._serialized_end = 1293
    _globals['_CHARGEONSOLARLIMITS']._serialized_start = 75
    _globals['_CHARGEONSOLARLIMITS']._serialized_end = 130
    _globals['_CHARGEONSOLARNOCHARGERECOMMENDED']._serialized_start = 132
    _globals['_CHARGEONSOLARNOCHARGERECOMMENDED']._serialized_end = 228
    _globals['_CHARGEONSOLARRESPONSE']._serialized_start = 231
    _globals['_CHARGEONSOLARRESPONSE']._serialized_end = 396
    _globals['_ERRORRESPONSE']._serialized_start = 398
    _globals['_ERRORRESPONSE']._serialized_end = 461
    _globals['_SESSIONCONFIGS']._serialized_start = 463
    _globals['_SESSIONCONFIGS']._serialized_end = 534
    _globals['_MANAGEVEHICLECHARGINGRESPONSE']._serialized_start = 537
    _globals['_MANAGEVEHICLECHARGINGRESPONSE']._serialized_end = 691
    _globals['_MANAGEDCHARGINGACTION']._serialized_start = 694
    _globals['_MANAGEDCHARGINGACTION']._serialized_end = 863