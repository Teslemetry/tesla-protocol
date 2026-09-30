from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SeiMetadata(_message.Message):
    __slots__ = ('field_1', 'gearState', 'frameSeqNo', 'vehicleSpeedMps', 'acceleratorPedalPosition', 'steeringWheelAngle', 'blinkerOnLeft', 'blinkerOnRight', 'brakeApplied', 'autopilotState', 'latitudeDeg', 'longitudeDeg', 'headingDeg', 'linearAccelerationMps2X', 'linearAccelerationMps2Y', 'linearAccelerationMps2Z')

    class Gear(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GEAR_PARK: _ClassVar[SeiMetadata.Gear]
        GEAR_DRIVE: _ClassVar[SeiMetadata.Gear]
        GEAR_REVERSE: _ClassVar[SeiMetadata.Gear]
        GEAR_NEUTRAL: _ClassVar[SeiMetadata.Gear]
    GEAR_PARK: SeiMetadata.Gear
    GEAR_DRIVE: SeiMetadata.Gear
    GEAR_REVERSE: SeiMetadata.Gear
    GEAR_NEUTRAL: SeiMetadata.Gear

    class AutopilotState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[SeiMetadata.AutopilotState]
        SELF_DRIVING: _ClassVar[SeiMetadata.AutopilotState]
        AUTOSTEER: _ClassVar[SeiMetadata.AutopilotState]
        TACC: _ClassVar[SeiMetadata.AutopilotState]
    NONE: SeiMetadata.AutopilotState
    SELF_DRIVING: SeiMetadata.AutopilotState
    AUTOSTEER: SeiMetadata.AutopilotState
    TACC: SeiMetadata.AutopilotState
    FIELD_1_FIELD_NUMBER: _ClassVar[int]
    GEARSTATE_FIELD_NUMBER: _ClassVar[int]
    FRAMESEQNO_FIELD_NUMBER: _ClassVar[int]
    VEHICLESPEEDMPS_FIELD_NUMBER: _ClassVar[int]
    ACCELERATORPEDALPOSITION_FIELD_NUMBER: _ClassVar[int]
    STEERINGWHEELANGLE_FIELD_NUMBER: _ClassVar[int]
    BLINKERONLEFT_FIELD_NUMBER: _ClassVar[int]
    BLINKERONRIGHT_FIELD_NUMBER: _ClassVar[int]
    BRAKEAPPLIED_FIELD_NUMBER: _ClassVar[int]
    AUTOPILOTSTATE_FIELD_NUMBER: _ClassVar[int]
    LATITUDEDEG_FIELD_NUMBER: _ClassVar[int]
    LONGITUDEDEG_FIELD_NUMBER: _ClassVar[int]
    HEADINGDEG_FIELD_NUMBER: _ClassVar[int]
    LINEARACCELERATIONMPS2X_FIELD_NUMBER: _ClassVar[int]
    LINEARACCELERATIONMPS2Y_FIELD_NUMBER: _ClassVar[int]
    LINEARACCELERATIONMPS2Z_FIELD_NUMBER: _ClassVar[int]
    field_1: int
    gearState: SeiMetadata.Gear
    frameSeqNo: int
    vehicleSpeedMps: float
    acceleratorPedalPosition: float
    steeringWheelAngle: float
    blinkerOnLeft: bool
    blinkerOnRight: bool
    brakeApplied: bool
    autopilotState: SeiMetadata.AutopilotState
    latitudeDeg: float
    longitudeDeg: float
    headingDeg: float
    linearAccelerationMps2X: float
    linearAccelerationMps2Y: float
    linearAccelerationMps2Z: float

    def __init__(self, field_1: _Optional[int]=..., gearState: _Optional[_Union[SeiMetadata.Gear, str]]=..., frameSeqNo: _Optional[int]=..., vehicleSpeedMps: _Optional[float]=..., acceleratorPedalPosition: _Optional[float]=..., steeringWheelAngle: _Optional[float]=..., blinkerOnLeft: bool=..., blinkerOnRight: bool=..., brakeApplied: bool=..., autopilotState: _Optional[_Union[SeiMetadata.AutopilotState, str]]=..., latitudeDeg: _Optional[float]=..., longitudeDeg: _Optional[float]=..., headingDeg: _Optional[float]=..., linearAccelerationMps2X: _Optional[float]=..., linearAccelerationMps2Y: _Optional[float]=..., linearAccelerationMps2Z: _Optional[float]=...) -> None:
        ...