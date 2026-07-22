"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'energy.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cenergy.proto\x12\x1ctesla.proto.energy_device.v1\x1a\x1egoogle/protobuf/wrappers.proto"\xa7\x01\n\x11AccumulatedEnergy\x12\x11\n\tenergy_wh\x18\x01 \x01(\x02\x12O\n\x11accumulation_type\x18\x02 \x01(\x0e24.tesla.proto.energy_device.v1.EnergyAccumulationType\x12.\n\x08period_s\x18\x03 \x01(\x0b2\x1c.google.protobuf.UInt64Value"\x96\x01\n\x14GridComplianceStatus\x12;\n\ngrid_state\x18\x01 \x01(\x0e2\'.tesla.proto.energy_device.v1.GridState\x12A\n\x1cqualifiying_time_remaining_s\x18\x02 \x01(\x0b2\x1b.google.protobuf.FloatValue"\x96\x02\n\x11InstACMeasurement\x12\x14\n\x0cvoltage_vrms\x18\x01 \x01(\x02\x12\x14\n\x0cfrequency_hz\x18\x02 \x01(\x02\x121\n\x0ccurrent_arms\x18\x03 \x01(\x0b2\x1b.google.protobuf.FloatValue\x121\n\x0creal_power_w\x18\x04 \x01(\x0b2\x1b.google.protobuf.FloatValue\x127\n\x12reactive_power_var\x18\x05 \x01(\x0b2\x1b.google.protobuf.FloatValue\x126\n\x11apparent_power_va\x18\x06 \x01(\x0b2\x1b.google.protobuf.FloatValue"V\n\x11InstDCMeasurement\x12\x11\n\tvoltage_v\x18\x01 \x01(\x02\x12.\n\tcurrent_a\x18\x02 \x01(\x0b2\x1b.google.protobuf.FloatValue"&\n\x08AlertLog\x12\x11\n\x04data\x18\x01 \x01(\x04H\x00\x88\x01\x01B\x07\n\x05_data")\n\x0bAlertMatrix\x12\x11\n\x04data\x18\x01 \x01(\x04H\x00\x88\x01\x01B\x07\n\x05_data*\xaf\x01\n\x16EnergyAccumulationType\x12$\n ENERGY_ACCUMULATION_TYPE_INVALID\x10\x00\x12%\n!ENERGY_ACCUMULATION_TYPE_LIFETIME\x10\x01\x12"\n\x1eENERGY_ACCUMULATION_TYPE_TODAY\x10\x02\x12$\n ENERGY_ACCUMULATION_TYPE_SESSION\x10\x03*t\n\tGridState\x12\x16\n\x12GRID_STATE_INVALID\x10\x00\x12\x1a\n\x16GRID_STATE_UNCOMPLIANT\x10\x01\x12\x19\n\x15GRID_STATE_QUALIFYING\x10\x02\x12\x18\n\x14GRID_STATE_COMPLIANT\x10\x03Bz\n$com.tesla.generated.energy_device.v1B\x06EnergyZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'energy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.tesla.generated.energy_device.v1B\x06EnergyZJgithub.com/teslamotors/energy_device/pkg/protocol/protobuf/energydevice/v1'
    _globals['_ENERGYACCUMULATIONTYPE']._serialized_start = 854
    _globals['_ENERGYACCUMULATIONTYPE']._serialized_end = 1029
    _globals['_GRIDSTATE']._serialized_start = 1031
    _globals['_GRIDSTATE']._serialized_end = 1147
    _globals['_ACCUMULATEDENERGY']._serialized_start = 79
    _globals['_ACCUMULATEDENERGY']._serialized_end = 246
    _globals['_GRIDCOMPLIANCESTATUS']._serialized_start = 249
    _globals['_GRIDCOMPLIANCESTATUS']._serialized_end = 399
    _globals['_INSTACMEASUREMENT']._serialized_start = 402
    _globals['_INSTACMEASUREMENT']._serialized_end = 680
    _globals['_INSTDCMEASUREMENT']._serialized_start = 682
    _globals['_INSTDCMEASUREMENT']._serialized_end = 768
    _globals['_ALERTLOG']._serialized_start = 770
    _globals['_ALERTLOG']._serialized_end = 808
    _globals['_ALERTMATRIX']._serialized_start = 810
    _globals['_ALERTMATRIX']._serialized_end = 851