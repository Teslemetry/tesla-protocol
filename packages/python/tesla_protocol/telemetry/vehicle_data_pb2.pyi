import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unknown: _ClassVar[Field]
    DriveRail: _ClassVar[Field]
    ChargeState: _ClassVar[Field]
    BmsFullchargecomplete: _ClassVar[Field]
    VehicleSpeed: _ClassVar[Field]
    Odometer: _ClassVar[Field]
    PackVoltage: _ClassVar[Field]
    PackCurrent: _ClassVar[Field]
    Soc: _ClassVar[Field]
    DCDCEnable: _ClassVar[Field]
    Gear: _ClassVar[Field]
    IsolationResistance: _ClassVar[Field]
    PedalPosition: _ClassVar[Field]
    BrakePedal: _ClassVar[Field]
    DiStateR: _ClassVar[Field]
    DiHeatsinkTR: _ClassVar[Field]
    DiAxleSpeedR: _ClassVar[Field]
    DiTorquemotor: _ClassVar[Field]
    DiStatorTempR: _ClassVar[Field]
    DiVBatR: _ClassVar[Field]
    DiMotorCurrentR: _ClassVar[Field]
    Location: _ClassVar[Field]
    GpsState: _ClassVar[Field]
    GpsHeading: _ClassVar[Field]
    NumBrickVoltageMax: _ClassVar[Field]
    BrickVoltageMax: _ClassVar[Field]
    NumBrickVoltageMin: _ClassVar[Field]
    BrickVoltageMin: _ClassVar[Field]
    NumModuleTempMax: _ClassVar[Field]
    ModuleTempMax: _ClassVar[Field]
    NumModuleTempMin: _ClassVar[Field]
    ModuleTempMin: _ClassVar[Field]
    RatedRange: _ClassVar[Field]
    Hvil: _ClassVar[Field]
    DCChargingEnergyIn: _ClassVar[Field]
    DCChargingPower: _ClassVar[Field]
    ACChargingEnergyIn: _ClassVar[Field]
    ACChargingPower: _ClassVar[Field]
    ChargeLimitSoc: _ClassVar[Field]
    FastChargerPresent: _ClassVar[Field]
    EstBatteryRange: _ClassVar[Field]
    IdealBatteryRange: _ClassVar[Field]
    BatteryLevel: _ClassVar[Field]
    TimeToFullCharge: _ClassVar[Field]
    ScheduledChargingStartTime: _ClassVar[Field]
    ScheduledChargingPending: _ClassVar[Field]
    ScheduledDepartureTime: _ClassVar[Field]
    PreconditioningEnabled: _ClassVar[Field]
    ScheduledChargingMode: _ClassVar[Field]
    ChargeAmps: _ClassVar[Field]
    ChargeEnableRequest: _ClassVar[Field]
    ChargerPhases: _ClassVar[Field]
    ChargePortColdWeatherMode: _ClassVar[Field]
    ChargeCurrentRequest: _ClassVar[Field]
    ChargeCurrentRequestMax: _ClassVar[Field]
    BatteryHeaterOn: _ClassVar[Field]
    NotEnoughPowerToHeat: _ClassVar[Field]
    SuperchargerSessionTripPlanner: _ClassVar[Field]
    DoorState: _ClassVar[Field]
    Locked: _ClassVar[Field]
    FdWindow: _ClassVar[Field]
    FpWindow: _ClassVar[Field]
    RdWindow: _ClassVar[Field]
    RpWindow: _ClassVar[Field]
    VehicleName: _ClassVar[Field]
    SentryMode: _ClassVar[Field]
    SpeedLimitMode: _ClassVar[Field]
    CurrentLimitMph: _ClassVar[Field]
    Version: _ClassVar[Field]
    TpmsPressureFl: _ClassVar[Field]
    TpmsPressureFr: _ClassVar[Field]
    TpmsPressureRl: _ClassVar[Field]
    TpmsPressureRr: _ClassVar[Field]
    SemitruckTpmsPressureRe1L0: _ClassVar[Field]
    SemitruckTpmsPressureRe1L1: _ClassVar[Field]
    SemitruckTpmsPressureRe1R0: _ClassVar[Field]
    SemitruckTpmsPressureRe1R1: _ClassVar[Field]
    SemitruckTpmsPressureRe2L0: _ClassVar[Field]
    SemitruckTpmsPressureRe2L1: _ClassVar[Field]
    SemitruckTpmsPressureRe2R0: _ClassVar[Field]
    SemitruckTpmsPressureRe2R1: _ClassVar[Field]
    TpmsLastSeenPressureTimeFl: _ClassVar[Field]
    TpmsLastSeenPressureTimeFr: _ClassVar[Field]
    TpmsLastSeenPressureTimeRl: _ClassVar[Field]
    TpmsLastSeenPressureTimeRr: _ClassVar[Field]
    InsideTemp: _ClassVar[Field]
    OutsideTemp: _ClassVar[Field]
    SeatHeaterLeft: _ClassVar[Field]
    SeatHeaterRight: _ClassVar[Field]
    SeatHeaterRearLeft: _ClassVar[Field]
    SeatHeaterRearRight: _ClassVar[Field]
    SeatHeaterRearCenter: _ClassVar[Field]
    AutoSeatClimateLeft: _ClassVar[Field]
    AutoSeatClimateRight: _ClassVar[Field]
    DriverSeatBelt: _ClassVar[Field]
    PassengerSeatBelt: _ClassVar[Field]
    DriverSeatOccupied: _ClassVar[Field]
    SemitruckPassengerSeatFoldPosition: _ClassVar[Field]
    LateralAcceleration: _ClassVar[Field]
    LongitudinalAcceleration: _ClassVar[Field]
    Deprecated_2: _ClassVar[Field]
    CruiseSetSpeed: _ClassVar[Field]
    LifetimeEnergyUsed: _ClassVar[Field]
    LifetimeEnergyUsedDrive: _ClassVar[Field]
    SemitruckTractorParkBrakeStatus: _ClassVar[Field]
    SemitruckTrailerParkBrakeStatus: _ClassVar[Field]
    BrakePedalPos: _ClassVar[Field]
    RouteLastUpdated: _ClassVar[Field]
    RouteLine: _ClassVar[Field]
    MilesToArrival: _ClassVar[Field]
    MinutesToArrival: _ClassVar[Field]
    OriginLocation: _ClassVar[Field]
    DestinationLocation: _ClassVar[Field]
    CarType: _ClassVar[Field]
    Trim: _ClassVar[Field]
    ExteriorColor: _ClassVar[Field]
    RoofColor: _ClassVar[Field]
    ChargePort: _ClassVar[Field]
    ChargePortLatch: _ClassVar[Field]
    Experimental_1: _ClassVar[Field]
    Experimental_2: _ClassVar[Field]
    Experimental_3: _ClassVar[Field]
    Experimental_4: _ClassVar[Field]
    GuestModeEnabled: _ClassVar[Field]
    PinToDriveEnabled: _ClassVar[Field]
    PairedPhoneKeyAndKeyFobQty: _ClassVar[Field]
    CruiseFollowDistance: _ClassVar[Field]
    AutomaticBlindSpotCamera: _ClassVar[Field]
    BlindSpotCollisionWarningChime: _ClassVar[Field]
    SpeedLimitWarning: _ClassVar[Field]
    ForwardCollisionWarning: _ClassVar[Field]
    LaneDepartureAvoidance: _ClassVar[Field]
    EmergencyLaneDepartureAvoidance: _ClassVar[Field]
    AutomaticEmergencyBrakingOff: _ClassVar[Field]
    LifetimeEnergyGainedRegen: _ClassVar[Field]
    DiStateF: _ClassVar[Field]
    DiStateREL: _ClassVar[Field]
    DiStateRER: _ClassVar[Field]
    DiHeatsinkTF: _ClassVar[Field]
    DiHeatsinkTREL: _ClassVar[Field]
    DiHeatsinkTRER: _ClassVar[Field]
    DiAxleSpeedF: _ClassVar[Field]
    DiAxleSpeedREL: _ClassVar[Field]
    DiAxleSpeedRER: _ClassVar[Field]
    DiSlaveTorqueCmd: _ClassVar[Field]
    DiTorqueActualR: _ClassVar[Field]
    DiTorqueActualF: _ClassVar[Field]
    DiTorqueActualREL: _ClassVar[Field]
    DiTorqueActualRER: _ClassVar[Field]
    DiStatorTempF: _ClassVar[Field]
    DiStatorTempREL: _ClassVar[Field]
    DiStatorTempRER: _ClassVar[Field]
    DiVBatF: _ClassVar[Field]
    DiVBatREL: _ClassVar[Field]
    DiVBatRER: _ClassVar[Field]
    DiMotorCurrentF: _ClassVar[Field]
    DiMotorCurrentREL: _ClassVar[Field]
    DiMotorCurrentRER: _ClassVar[Field]
    EnergyRemaining: _ClassVar[Field]
    ServiceMode: _ClassVar[Field]
    BMSState: _ClassVar[Field]
    GuestModeMobileAccessState: _ClassVar[Field]
    Deprecated_1: _ClassVar[Field]
    DestinationName: _ClassVar[Field]
    DiInverterTR: _ClassVar[Field]
    DiInverterTF: _ClassVar[Field]
    DiInverterTREL: _ClassVar[Field]
    DiInverterTRER: _ClassVar[Field]
    Experimental_5: _ClassVar[Field]
    Experimental_6: _ClassVar[Field]
    Experimental_7: _ClassVar[Field]
    Experimental_8: _ClassVar[Field]
    Experimental_9: _ClassVar[Field]
    Experimental_10: _ClassVar[Field]
    Experimental_11: _ClassVar[Field]
    Experimental_12: _ClassVar[Field]
    Experimental_13: _ClassVar[Field]
    Experimental_14: _ClassVar[Field]
    Experimental_15: _ClassVar[Field]
    DetailedChargeState: _ClassVar[Field]
    CabinOverheatProtectionMode: _ClassVar[Field]
    CabinOverheatProtectionTemperatureLimit: _ClassVar[Field]
    CenterDisplay: _ClassVar[Field]
    ChargePortDoorOpen: _ClassVar[Field]
    ChargerVoltage: _ClassVar[Field]
    ChargingCableType: _ClassVar[Field]
    ClimateKeeperMode: _ClassVar[Field]
    DefrostForPreconditioning: _ClassVar[Field]
    DefrostMode: _ClassVar[Field]
    EfficiencyPackage: _ClassVar[Field]
    EstimatedHoursToChargeTermination: _ClassVar[Field]
    EuropeVehicle: _ClassVar[Field]
    ExpectedEnergyPercentAtTripArrival: _ClassVar[Field]
    FastChargerType: _ClassVar[Field]
    HomelinkDeviceCount: _ClassVar[Field]
    HomelinkNearby: _ClassVar[Field]
    HvacACEnabled: _ClassVar[Field]
    HvacAutoMode: _ClassVar[Field]
    HvacFanSpeed: _ClassVar[Field]
    HvacFanStatus: _ClassVar[Field]
    HvacLeftTemperatureRequest: _ClassVar[Field]
    HvacPower: _ClassVar[Field]
    HvacRightTemperatureRequest: _ClassVar[Field]
    HvacSteeringWheelHeatAuto: _ClassVar[Field]
    HvacSteeringWheelHeatLevel: _ClassVar[Field]
    OffroadLightbarPresent: _ClassVar[Field]
    PowershareHoursLeft: _ClassVar[Field]
    PowershareInstantaneousPowerKW: _ClassVar[Field]
    PowershareStatus: _ClassVar[Field]
    PowershareStopReason: _ClassVar[Field]
    PowershareType: _ClassVar[Field]
    RearDisplayHvacEnabled: _ClassVar[Field]
    RearSeatHeaters: _ClassVar[Field]
    RemoteStartEnabled: _ClassVar[Field]
    RightHandDrive: _ClassVar[Field]
    RouteTrafficMinutesDelay: _ClassVar[Field]
    SoftwareUpdateDownloadPercentComplete: _ClassVar[Field]
    SoftwareUpdateExpectedDurationMinutes: _ClassVar[Field]
    SoftwareUpdateInstallationPercentComplete: _ClassVar[Field]
    SoftwareUpdateScheduledStartTime: _ClassVar[Field]
    SoftwareUpdateVersion: _ClassVar[Field]
    TonneauOpenPercent: _ClassVar[Field]
    TonneauPosition: _ClassVar[Field]
    TonneauTentMode: _ClassVar[Field]
    TpmsHardWarnings: _ClassVar[Field]
    TpmsSoftWarnings: _ClassVar[Field]
    ValetModeEnabled: _ClassVar[Field]
    WheelType: _ClassVar[Field]
    WiperHeatEnabled: _ClassVar[Field]
    LocatedAtHome: _ClassVar[Field]
    LocatedAtWork: _ClassVar[Field]
    LocatedAtFavorite: _ClassVar[Field]
    SettingDistanceUnit: _ClassVar[Field]
    SettingTemperatureUnit: _ClassVar[Field]
    Setting24HourTime: _ClassVar[Field]
    SettingTirePressureUnit: _ClassVar[Field]
    SettingChargeUnit: _ClassVar[Field]
    ClimateSeatCoolingFrontLeft: _ClassVar[Field]
    ClimateSeatCoolingFrontRight: _ClassVar[Field]
    LightsHazardsActive: _ClassVar[Field]
    LightsTurnSignal: _ClassVar[Field]
    LightsHighBeams: _ClassVar[Field]
    MediaPlaybackStatus: _ClassVar[Field]
    MediaPlaybackSource: _ClassVar[Field]
    MediaAudioVolume: _ClassVar[Field]
    MediaNowPlayingDuration: _ClassVar[Field]
    MediaNowPlayingElapsed: _ClassVar[Field]
    MediaNowPlayingArtist: _ClassVar[Field]
    MediaNowPlayingTitle: _ClassVar[Field]
    MediaNowPlayingAlbum: _ClassVar[Field]
    MediaNowPlayingStation: _ClassVar[Field]
    MediaAudioVolumeIncrement: _ClassVar[Field]
    MediaAudioVolumeMax: _ClassVar[Field]
    SunroofInstalled: _ClassVar[Field]
    SeatVentEnabled: _ClassVar[Field]
    RearDefrostEnabled: _ClassVar[Field]
    ChargeRateMilePerHour: _ClassVar[Field]
    Deprecated_3: _ClassVar[Field]
    MilesSinceReset: _ClassVar[Field]
    SelfDrivingMilesSinceReset: _ClassVar[Field]

class ChargingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChargeStateUnknown: _ClassVar[ChargingState]
    ChargeStateDisconnected: _ClassVar[ChargingState]
    ChargeStateNoPower: _ClassVar[ChargingState]
    ChargeStateStarting: _ClassVar[ChargingState]
    ChargeStateCharging: _ClassVar[ChargingState]
    ChargeStateComplete: _ClassVar[ChargingState]
    ChargeStateStopped: _ClassVar[ChargingState]

class DetailedChargeStateValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DetailedChargeStateUnknown: _ClassVar[DetailedChargeStateValue]
    DetailedChargeStateDisconnected: _ClassVar[DetailedChargeStateValue]
    DetailedChargeStateNoPower: _ClassVar[DetailedChargeStateValue]
    DetailedChargeStateStarting: _ClassVar[DetailedChargeStateValue]
    DetailedChargeStateCharging: _ClassVar[DetailedChargeStateValue]
    DetailedChargeStateComplete: _ClassVar[DetailedChargeStateValue]
    DetailedChargeStateStopped: _ClassVar[DetailedChargeStateValue]

class ShiftState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ShiftStateUnknown: _ClassVar[ShiftState]
    ShiftStateInvalid: _ClassVar[ShiftState]
    ShiftStateP: _ClassVar[ShiftState]
    ShiftStateR: _ClassVar[ShiftState]
    ShiftStateN: _ClassVar[ShiftState]
    ShiftStateD: _ClassVar[ShiftState]
    ShiftStateSNA: _ClassVar[ShiftState]

class FollowDistance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FollowDistanceUnknown: _ClassVar[FollowDistance]
    FollowDistance1: _ClassVar[FollowDistance]
    FollowDistance2: _ClassVar[FollowDistance]
    FollowDistance3: _ClassVar[FollowDistance]
    FollowDistance4: _ClassVar[FollowDistance]
    FollowDistance5: _ClassVar[FollowDistance]
    FollowDistance6: _ClassVar[FollowDistance]
    FollowDistance7: _ClassVar[FollowDistance]

class ForwardCollisionSensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ForwardCollisionSensitivityUnknown: _ClassVar[ForwardCollisionSensitivity]
    ForwardCollisionSensitivityOff: _ClassVar[ForwardCollisionSensitivity]
    ForwardCollisionSensitivityLate: _ClassVar[ForwardCollisionSensitivity]
    ForwardCollisionSensitivityAverage: _ClassVar[ForwardCollisionSensitivity]
    ForwardCollisionSensitivityEarly: _ClassVar[ForwardCollisionSensitivity]

class GuestModeMobileAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GuestModeMobileAccessUnknown: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessInit: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessNotAuthenticated: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAuthenticated: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAbortedDriving: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAbortedUsingRemoteStart: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAbortedUsingBLEKeys: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAbortedValetMode: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAbortedGuestModeOff: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAbortedDriveAuthTimeExceeded: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAbortedNoDataReceived: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessRequestingFromMothership: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessRequestingFromAuthD: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAbortedFetchFailed: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessAbortedBadDataReceived: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessShowingQRCode: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessSwipedAway: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessDismissedQRCodeExpired: _ClassVar[GuestModeMobileAccess]
    GuestModeMobileAccessSucceededPairedNewBLEKey: _ClassVar[GuestModeMobileAccess]

class LaneAssistLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LaneAssistLevelUnknown: _ClassVar[LaneAssistLevel]
    LaneAssistLevelNone: _ClassVar[LaneAssistLevel]
    LaneAssistLevelWarning: _ClassVar[LaneAssistLevel]
    LaneAssistLevelAssist: _ClassVar[LaneAssistLevel]

class ScheduledChargingModeValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ScheduledChargingModeUnknown: _ClassVar[ScheduledChargingModeValue]
    ScheduledChargingModeOff: _ClassVar[ScheduledChargingModeValue]
    ScheduledChargingModeStartAt: _ClassVar[ScheduledChargingModeValue]
    ScheduledChargingModeDepartBy: _ClassVar[ScheduledChargingModeValue]

class SentryModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SentryModeStateUnknown: _ClassVar[SentryModeState]
    SentryModeStateOff: _ClassVar[SentryModeState]
    SentryModeStateIdle: _ClassVar[SentryModeState]
    SentryModeStateArmed: _ClassVar[SentryModeState]
    SentryModeStateAware: _ClassVar[SentryModeState]
    SentryModeStatePanic: _ClassVar[SentryModeState]
    SentryModeStateQuiet: _ClassVar[SentryModeState]

class SpeedAssistLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SpeedAssistLevelUnknown: _ClassVar[SpeedAssistLevel]
    SpeedAssistLevelNone: _ClassVar[SpeedAssistLevel]
    SpeedAssistLevelDisplay: _ClassVar[SpeedAssistLevel]
    SpeedAssistLevelChime: _ClassVar[SpeedAssistLevel]

class BMSStateValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BMSStateUnknown: _ClassVar[BMSStateValue]
    BMSStateStandby: _ClassVar[BMSStateValue]
    BMSStateDrive: _ClassVar[BMSStateValue]
    BMSStateSupport: _ClassVar[BMSStateValue]
    BMSStateCharge: _ClassVar[BMSStateValue]
    BMSStateFEIM: _ClassVar[BMSStateValue]
    BMSStateClearFault: _ClassVar[BMSStateValue]
    BMSStateFault: _ClassVar[BMSStateValue]
    BMSStateWeld: _ClassVar[BMSStateValue]
    BMSStateTest: _ClassVar[BMSStateValue]
    BMSStateSNA: _ClassVar[BMSStateValue]

class BuckleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BuckleStatusUnknown: _ClassVar[BuckleStatus]
    BuckleStatusUnlatched: _ClassVar[BuckleStatus]
    BuckleStatusLatched: _ClassVar[BuckleStatus]
    BuckleStatusFaulted: _ClassVar[BuckleStatus]

class CarTypeValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CarTypeUnknown: _ClassVar[CarTypeValue]
    CarTypeModelS: _ClassVar[CarTypeValue]
    CarTypeModelX: _ClassVar[CarTypeValue]
    CarTypeModel3: _ClassVar[CarTypeValue]
    CarTypeModelY: _ClassVar[CarTypeValue]
    CarTypeSemiTruck: _ClassVar[CarTypeValue]
    CarTypeCybertruck: _ClassVar[CarTypeValue]

class ChargePortValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChargePortUnknown: _ClassVar[ChargePortValue]
    ChargePortUS: _ClassVar[ChargePortValue]
    ChargePortEU: _ClassVar[ChargePortValue]
    ChargePortGB: _ClassVar[ChargePortValue]
    ChargePortCCS: _ClassVar[ChargePortValue]

class ChargePortLatchValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChargePortLatchUnknown: _ClassVar[ChargePortLatchValue]
    ChargePortLatchSNA: _ClassVar[ChargePortLatchValue]
    ChargePortLatchDisengaged: _ClassVar[ChargePortLatchValue]
    ChargePortLatchEngaged: _ClassVar[ChargePortLatchValue]
    ChargePortLatchBlocking: _ClassVar[ChargePortLatchValue]

class DriveInverterState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DriveInverterStateUnknown: _ClassVar[DriveInverterState]
    DriveInverterStateUnavailable: _ClassVar[DriveInverterState]
    DriveInverterStateStandby: _ClassVar[DriveInverterState]
    DriveInverterStateFault: _ClassVar[DriveInverterState]
    DriveInverterStateAbort: _ClassVar[DriveInverterState]
    DriveInverterStateEnable: _ClassVar[DriveInverterState]

class HvilStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HvilStatusUnknown: _ClassVar[HvilStatus]
    HvilStatusFault: _ClassVar[HvilStatus]
    HvilStatusOK: _ClassVar[HvilStatus]

class WindowState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WindowStateUnknown: _ClassVar[WindowState]
    WindowStateClosed: _ClassVar[WindowState]
    WindowStatePartiallyOpen: _ClassVar[WindowState]
    WindowStateOpened: _ClassVar[WindowState]

class SeatFoldPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SeatFoldPositionUnknown: _ClassVar[SeatFoldPosition]
    SeatFoldPositionSNA: _ClassVar[SeatFoldPosition]
    SeatFoldPositionFaulted: _ClassVar[SeatFoldPosition]
    SeatFoldPositionNotConfigured: _ClassVar[SeatFoldPosition]
    SeatFoldPositionFolded: _ClassVar[SeatFoldPosition]
    SeatFoldPositionUnfolded: _ClassVar[SeatFoldPosition]

class TractorAirStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TractorAirStatusUnknown: _ClassVar[TractorAirStatus]
    TractorAirStatusNotAvailable: _ClassVar[TractorAirStatus]
    TractorAirStatusError: _ClassVar[TractorAirStatus]
    TractorAirStatusCharged: _ClassVar[TractorAirStatus]
    TractorAirStatusBuildingPressureIntermediate: _ClassVar[TractorAirStatus]
    TractorAirStatusExhaustingPressureIntermediate: _ClassVar[TractorAirStatus]
    TractorAirStatusExhausted: _ClassVar[TractorAirStatus]

class TrailerAirStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TrailerAirStatusUnknown: _ClassVar[TrailerAirStatus]
    TrailerAirStatusSNA: _ClassVar[TrailerAirStatus]
    TrailerAirStatusInvalid: _ClassVar[TrailerAirStatus]
    TrailerAirStatusBobtailMode: _ClassVar[TrailerAirStatus]
    TrailerAirStatusCharged: _ClassVar[TrailerAirStatus]
    TrailerAirStatusBuildingPressureIntermediate: _ClassVar[TrailerAirStatus]
    TrailerAirStatusExhaustingPressureIntermediate: _ClassVar[TrailerAirStatus]
    TrailerAirStatusExhausted: _ClassVar[TrailerAirStatus]

class HvacAutoModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HvacAutoModeStateUnknown: _ClassVar[HvacAutoModeState]
    HvacAutoModeStateOn: _ClassVar[HvacAutoModeState]
    HvacAutoModeStateOverride: _ClassVar[HvacAutoModeState]

class CabinOverheatProtectionModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CabinOverheatProtectionModeStateUnknown: _ClassVar[CabinOverheatProtectionModeState]
    CabinOverheatProtectionModeStateOff: _ClassVar[CabinOverheatProtectionModeState]
    CabinOverheatProtectionModeStateOn: _ClassVar[CabinOverheatProtectionModeState]
    CabinOverheatProtectionModeStateFanOnly: _ClassVar[CabinOverheatProtectionModeState]

class ClimateOverheatProtectionTempLimit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ClimateOverheatProtectionTempLimitUnknown: _ClassVar[ClimateOverheatProtectionTempLimit]
    ClimateOverheatProtectionTempLimitHigh: _ClassVar[ClimateOverheatProtectionTempLimit]
    ClimateOverheatProtectionTempLimitMedium: _ClassVar[ClimateOverheatProtectionTempLimit]
    ClimateOverheatProtectionTempLimitLow: _ClassVar[ClimateOverheatProtectionTempLimit]

class DefrostModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DefrostModeStateUnknown: _ClassVar[DefrostModeState]
    DefrostModeStateOff: _ClassVar[DefrostModeState]
    DefrostModeStateNormal: _ClassVar[DefrostModeState]
    DefrostModeStateMax: _ClassVar[DefrostModeState]
    DefrostModeStateAutoDefog: _ClassVar[DefrostModeState]

class ClimateKeeperModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ClimateKeeperModeStateUnknown: _ClassVar[ClimateKeeperModeState]
    ClimateKeeperModeStateOff: _ClassVar[ClimateKeeperModeState]
    ClimateKeeperModeStateOn: _ClassVar[ClimateKeeperModeState]
    ClimateKeeperModeStateDog: _ClassVar[ClimateKeeperModeState]
    ClimateKeeperModeStateParty: _ClassVar[ClimateKeeperModeState]

class HvacPowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HvacPowerStateUnknown: _ClassVar[HvacPowerState]
    HvacPowerStateOff: _ClassVar[HvacPowerState]
    HvacPowerStateOn: _ClassVar[HvacPowerState]
    HvacPowerStatePrecondition: _ClassVar[HvacPowerState]
    HvacPowerStateOverheatProtect: _ClassVar[HvacPowerState]

class FastCharger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FastChargerUnknown: _ClassVar[FastCharger]
    FastChargerSupercharger: _ClassVar[FastCharger]
    FastChargerCHAdeMO: _ClassVar[FastCharger]
    FastChargerGB: _ClassVar[FastCharger]
    FastChargerACSingleWireCAN: _ClassVar[FastCharger]
    FastChargerCombo: _ClassVar[FastCharger]
    FastChargerMCSingleWireCAN: _ClassVar[FastCharger]
    FastChargerOther: _ClassVar[FastCharger]
    FastChargerSNA: _ClassVar[FastCharger]

class CableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CableTypeUnknown: _ClassVar[CableType]
    CableTypeIEC: _ClassVar[CableType]
    CableTypeSAE: _ClassVar[CableType]
    CableTypeGB_AC: _ClassVar[CableType]
    CableTypeGB_DC: _ClassVar[CableType]
    CableTypeSNA: _ClassVar[CableType]

class TonneauTentModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TonneauTentModeStateUnknown: _ClassVar[TonneauTentModeState]
    TonneauTentModeStateInactive: _ClassVar[TonneauTentModeState]
    TonneauTentModeStateMoving: _ClassVar[TonneauTentModeState]
    TonneauTentModeStateFailed: _ClassVar[TonneauTentModeState]
    TonneauTentModeStateActive: _ClassVar[TonneauTentModeState]

class TonneauPositionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TonneauPositionStateUnknown: _ClassVar[TonneauPositionState]
    TonneauPositionStateInvalid: _ClassVar[TonneauPositionState]
    TonneauPositionStateClosed: _ClassVar[TonneauPositionState]
    TonneauPositionStatePartiallyOpen: _ClassVar[TonneauPositionState]
    TonneauPositionStateFullyOpen: _ClassVar[TonneauPositionState]

class PowershareState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PowershareStateUnknown: _ClassVar[PowershareState]
    PowershareStateInactive: _ClassVar[PowershareState]
    PowershareStateHandshaking: _ClassVar[PowershareState]
    PowershareStateInit: _ClassVar[PowershareState]
    PowershareStateEnabled: _ClassVar[PowershareState]
    PowershareStateEnabledReconnectingSoon: _ClassVar[PowershareState]
    PowershareStateStopped: _ClassVar[PowershareState]

class PowershareStopReasonStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PowershareStopReasonStatusUnknown: _ClassVar[PowershareStopReasonStatus]
    PowershareStopReasonStatusNone: _ClassVar[PowershareStopReasonStatus]
    PowershareStopReasonStatusSOCTooLow: _ClassVar[PowershareStopReasonStatus]
    PowershareStopReasonStatusRetry: _ClassVar[PowershareStopReasonStatus]
    PowershareStopReasonStatusFault: _ClassVar[PowershareStopReasonStatus]
    PowershareStopReasonStatusUser: _ClassVar[PowershareStopReasonStatus]
    PowershareStopReasonStatusReconnecting: _ClassVar[PowershareStopReasonStatus]
    PowershareStopReasonStatusAuthentication: _ClassVar[PowershareStopReasonStatus]

class PowershareTypeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PowershareTypeStatusUnknown: _ClassVar[PowershareTypeStatus]
    PowershareTypeStatusNone: _ClassVar[PowershareTypeStatus]
    PowershareTypeStatusLoad: _ClassVar[PowershareTypeStatus]
    PowershareTypeStatusHome: _ClassVar[PowershareTypeStatus]

class DisplayState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DisplayStateUnknown: _ClassVar[DisplayState]
    DisplayStateOff: _ClassVar[DisplayState]
    DisplayStateDim: _ClassVar[DisplayState]
    DisplayStateAccessory: _ClassVar[DisplayState]
    DisplayStateOn: _ClassVar[DisplayState]
    DisplayStateDriving: _ClassVar[DisplayState]
    DisplayStateCharging: _ClassVar[DisplayState]
    DisplayStateLock: _ClassVar[DisplayState]
    DisplayStateSentry: _ClassVar[DisplayState]
    DisplayStateDog: _ClassVar[DisplayState]
    DisplayStateEntertainment: _ClassVar[DisplayState]

class DistanceUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DistanceUnitUnknown: _ClassVar[DistanceUnit]
    DistanceUnitMiles: _ClassVar[DistanceUnit]
    DistanceUnitKilometers: _ClassVar[DistanceUnit]

class TemperatureUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TemperatureUnitUnknown: _ClassVar[TemperatureUnit]
    TemperatureUnitFahrenheit: _ClassVar[TemperatureUnit]
    TemperatureUnitCelsius: _ClassVar[TemperatureUnit]

class PressureUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PressureUnitUnknown: _ClassVar[PressureUnit]
    PressureUnitPsi: _ClassVar[PressureUnit]
    PressureUnitBar: _ClassVar[PressureUnit]

class ChargeUnitPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChargeUnitUnknown: _ClassVar[ChargeUnitPreference]
    ChargeUnitDistance: _ClassVar[ChargeUnitPreference]
    ChargeUnitPercent: _ClassVar[ChargeUnitPreference]

class SunroofInstalledState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SunroofInstalledStateUnknown: _ClassVar[SunroofInstalledState]
    SunroofInstalledStateNotInstalled: _ClassVar[SunroofInstalledState]
    SunroofInstalledStateGen1Installed: _ClassVar[SunroofInstalledState]
    SunroofInstalledStateGen2Installed: _ClassVar[SunroofInstalledState]

class TurnSignalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TurnSignalStateUnknown: _ClassVar[TurnSignalState]
    TurnSignalStateOff: _ClassVar[TurnSignalState]
    TurnSignalStateLeft: _ClassVar[TurnSignalState]
    TurnSignalStateRight: _ClassVar[TurnSignalState]
    TurnSignalStateBoth: _ClassVar[TurnSignalState]

class MediaStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MediaStatusUnknown: _ClassVar[MediaStatus]
    MediaStatusStopped: _ClassVar[MediaStatus]
    MediaStatusPlaying: _ClassVar[MediaStatus]
    MediaStatusPaused: _ClassVar[MediaStatus]
Unknown: Field
DriveRail: Field
ChargeState: Field
BmsFullchargecomplete: Field
VehicleSpeed: Field
Odometer: Field
PackVoltage: Field
PackCurrent: Field
Soc: Field
DCDCEnable: Field
Gear: Field
IsolationResistance: Field
PedalPosition: Field
BrakePedal: Field
DiStateR: Field
DiHeatsinkTR: Field
DiAxleSpeedR: Field
DiTorquemotor: Field
DiStatorTempR: Field
DiVBatR: Field
DiMotorCurrentR: Field
Location: Field
GpsState: Field
GpsHeading: Field
NumBrickVoltageMax: Field
BrickVoltageMax: Field
NumBrickVoltageMin: Field
BrickVoltageMin: Field
NumModuleTempMax: Field
ModuleTempMax: Field
NumModuleTempMin: Field
ModuleTempMin: Field
RatedRange: Field
Hvil: Field
DCChargingEnergyIn: Field
DCChargingPower: Field
ACChargingEnergyIn: Field
ACChargingPower: Field
ChargeLimitSoc: Field
FastChargerPresent: Field
EstBatteryRange: Field
IdealBatteryRange: Field
BatteryLevel: Field
TimeToFullCharge: Field
ScheduledChargingStartTime: Field
ScheduledChargingPending: Field
ScheduledDepartureTime: Field
PreconditioningEnabled: Field
ScheduledChargingMode: Field
ChargeAmps: Field
ChargeEnableRequest: Field
ChargerPhases: Field
ChargePortColdWeatherMode: Field
ChargeCurrentRequest: Field
ChargeCurrentRequestMax: Field
BatteryHeaterOn: Field
NotEnoughPowerToHeat: Field
SuperchargerSessionTripPlanner: Field
DoorState: Field
Locked: Field
FdWindow: Field
FpWindow: Field
RdWindow: Field
RpWindow: Field
VehicleName: Field
SentryMode: Field
SpeedLimitMode: Field
CurrentLimitMph: Field
Version: Field
TpmsPressureFl: Field
TpmsPressureFr: Field
TpmsPressureRl: Field
TpmsPressureRr: Field
SemitruckTpmsPressureRe1L0: Field
SemitruckTpmsPressureRe1L1: Field
SemitruckTpmsPressureRe1R0: Field
SemitruckTpmsPressureRe1R1: Field
SemitruckTpmsPressureRe2L0: Field
SemitruckTpmsPressureRe2L1: Field
SemitruckTpmsPressureRe2R0: Field
SemitruckTpmsPressureRe2R1: Field
TpmsLastSeenPressureTimeFl: Field
TpmsLastSeenPressureTimeFr: Field
TpmsLastSeenPressureTimeRl: Field
TpmsLastSeenPressureTimeRr: Field
InsideTemp: Field
OutsideTemp: Field
SeatHeaterLeft: Field
SeatHeaterRight: Field
SeatHeaterRearLeft: Field
SeatHeaterRearRight: Field
SeatHeaterRearCenter: Field
AutoSeatClimateLeft: Field
AutoSeatClimateRight: Field
DriverSeatBelt: Field
PassengerSeatBelt: Field
DriverSeatOccupied: Field
SemitruckPassengerSeatFoldPosition: Field
LateralAcceleration: Field
LongitudinalAcceleration: Field
Deprecated_2: Field
CruiseSetSpeed: Field
LifetimeEnergyUsed: Field
LifetimeEnergyUsedDrive: Field
SemitruckTractorParkBrakeStatus: Field
SemitruckTrailerParkBrakeStatus: Field
BrakePedalPos: Field
RouteLastUpdated: Field
RouteLine: Field
MilesToArrival: Field
MinutesToArrival: Field
OriginLocation: Field
DestinationLocation: Field
CarType: Field
Trim: Field
ExteriorColor: Field
RoofColor: Field
ChargePort: Field
ChargePortLatch: Field
Experimental_1: Field
Experimental_2: Field
Experimental_3: Field
Experimental_4: Field
GuestModeEnabled: Field
PinToDriveEnabled: Field
PairedPhoneKeyAndKeyFobQty: Field
CruiseFollowDistance: Field
AutomaticBlindSpotCamera: Field
BlindSpotCollisionWarningChime: Field
SpeedLimitWarning: Field
ForwardCollisionWarning: Field
LaneDepartureAvoidance: Field
EmergencyLaneDepartureAvoidance: Field
AutomaticEmergencyBrakingOff: Field
LifetimeEnergyGainedRegen: Field
DiStateF: Field
DiStateREL: Field
DiStateRER: Field
DiHeatsinkTF: Field
DiHeatsinkTREL: Field
DiHeatsinkTRER: Field
DiAxleSpeedF: Field
DiAxleSpeedREL: Field
DiAxleSpeedRER: Field
DiSlaveTorqueCmd: Field
DiTorqueActualR: Field
DiTorqueActualF: Field
DiTorqueActualREL: Field
DiTorqueActualRER: Field
DiStatorTempF: Field
DiStatorTempREL: Field
DiStatorTempRER: Field
DiVBatF: Field
DiVBatREL: Field
DiVBatRER: Field
DiMotorCurrentF: Field
DiMotorCurrentREL: Field
DiMotorCurrentRER: Field
EnergyRemaining: Field
ServiceMode: Field
BMSState: Field
GuestModeMobileAccessState: Field
Deprecated_1: Field
DestinationName: Field
DiInverterTR: Field
DiInverterTF: Field
DiInverterTREL: Field
DiInverterTRER: Field
Experimental_5: Field
Experimental_6: Field
Experimental_7: Field
Experimental_8: Field
Experimental_9: Field
Experimental_10: Field
Experimental_11: Field
Experimental_12: Field
Experimental_13: Field
Experimental_14: Field
Experimental_15: Field
DetailedChargeState: Field
CabinOverheatProtectionMode: Field
CabinOverheatProtectionTemperatureLimit: Field
CenterDisplay: Field
ChargePortDoorOpen: Field
ChargerVoltage: Field
ChargingCableType: Field
ClimateKeeperMode: Field
DefrostForPreconditioning: Field
DefrostMode: Field
EfficiencyPackage: Field
EstimatedHoursToChargeTermination: Field
EuropeVehicle: Field
ExpectedEnergyPercentAtTripArrival: Field
FastChargerType: Field
HomelinkDeviceCount: Field
HomelinkNearby: Field
HvacACEnabled: Field
HvacAutoMode: Field
HvacFanSpeed: Field
HvacFanStatus: Field
HvacLeftTemperatureRequest: Field
HvacPower: Field
HvacRightTemperatureRequest: Field
HvacSteeringWheelHeatAuto: Field
HvacSteeringWheelHeatLevel: Field
OffroadLightbarPresent: Field
PowershareHoursLeft: Field
PowershareInstantaneousPowerKW: Field
PowershareStatus: Field
PowershareStopReason: Field
PowershareType: Field
RearDisplayHvacEnabled: Field
RearSeatHeaters: Field
RemoteStartEnabled: Field
RightHandDrive: Field
RouteTrafficMinutesDelay: Field
SoftwareUpdateDownloadPercentComplete: Field
SoftwareUpdateExpectedDurationMinutes: Field
SoftwareUpdateInstallationPercentComplete: Field
SoftwareUpdateScheduledStartTime: Field
SoftwareUpdateVersion: Field
TonneauOpenPercent: Field
TonneauPosition: Field
TonneauTentMode: Field
TpmsHardWarnings: Field
TpmsSoftWarnings: Field
ValetModeEnabled: Field
WheelType: Field
WiperHeatEnabled: Field
LocatedAtHome: Field
LocatedAtWork: Field
LocatedAtFavorite: Field
SettingDistanceUnit: Field
SettingTemperatureUnit: Field
Setting24HourTime: Field
SettingTirePressureUnit: Field
SettingChargeUnit: Field
ClimateSeatCoolingFrontLeft: Field
ClimateSeatCoolingFrontRight: Field
LightsHazardsActive: Field
LightsTurnSignal: Field
LightsHighBeams: Field
MediaPlaybackStatus: Field
MediaPlaybackSource: Field
MediaAudioVolume: Field
MediaNowPlayingDuration: Field
MediaNowPlayingElapsed: Field
MediaNowPlayingArtist: Field
MediaNowPlayingTitle: Field
MediaNowPlayingAlbum: Field
MediaNowPlayingStation: Field
MediaAudioVolumeIncrement: Field
MediaAudioVolumeMax: Field
SunroofInstalled: Field
SeatVentEnabled: Field
RearDefrostEnabled: Field
ChargeRateMilePerHour: Field
Deprecated_3: Field
MilesSinceReset: Field
SelfDrivingMilesSinceReset: Field
ChargeStateUnknown: ChargingState
ChargeStateDisconnected: ChargingState
ChargeStateNoPower: ChargingState
ChargeStateStarting: ChargingState
ChargeStateCharging: ChargingState
ChargeStateComplete: ChargingState
ChargeStateStopped: ChargingState
DetailedChargeStateUnknown: DetailedChargeStateValue
DetailedChargeStateDisconnected: DetailedChargeStateValue
DetailedChargeStateNoPower: DetailedChargeStateValue
DetailedChargeStateStarting: DetailedChargeStateValue
DetailedChargeStateCharging: DetailedChargeStateValue
DetailedChargeStateComplete: DetailedChargeStateValue
DetailedChargeStateStopped: DetailedChargeStateValue
ShiftStateUnknown: ShiftState
ShiftStateInvalid: ShiftState
ShiftStateP: ShiftState
ShiftStateR: ShiftState
ShiftStateN: ShiftState
ShiftStateD: ShiftState
ShiftStateSNA: ShiftState
FollowDistanceUnknown: FollowDistance
FollowDistance1: FollowDistance
FollowDistance2: FollowDistance
FollowDistance3: FollowDistance
FollowDistance4: FollowDistance
FollowDistance5: FollowDistance
FollowDistance6: FollowDistance
FollowDistance7: FollowDistance
ForwardCollisionSensitivityUnknown: ForwardCollisionSensitivity
ForwardCollisionSensitivityOff: ForwardCollisionSensitivity
ForwardCollisionSensitivityLate: ForwardCollisionSensitivity
ForwardCollisionSensitivityAverage: ForwardCollisionSensitivity
ForwardCollisionSensitivityEarly: ForwardCollisionSensitivity
GuestModeMobileAccessUnknown: GuestModeMobileAccess
GuestModeMobileAccessInit: GuestModeMobileAccess
GuestModeMobileAccessNotAuthenticated: GuestModeMobileAccess
GuestModeMobileAccessAuthenticated: GuestModeMobileAccess
GuestModeMobileAccessAbortedDriving: GuestModeMobileAccess
GuestModeMobileAccessAbortedUsingRemoteStart: GuestModeMobileAccess
GuestModeMobileAccessAbortedUsingBLEKeys: GuestModeMobileAccess
GuestModeMobileAccessAbortedValetMode: GuestModeMobileAccess
GuestModeMobileAccessAbortedGuestModeOff: GuestModeMobileAccess
GuestModeMobileAccessAbortedDriveAuthTimeExceeded: GuestModeMobileAccess
GuestModeMobileAccessAbortedNoDataReceived: GuestModeMobileAccess
GuestModeMobileAccessRequestingFromMothership: GuestModeMobileAccess
GuestModeMobileAccessRequestingFromAuthD: GuestModeMobileAccess
GuestModeMobileAccessAbortedFetchFailed: GuestModeMobileAccess
GuestModeMobileAccessAbortedBadDataReceived: GuestModeMobileAccess
GuestModeMobileAccessShowingQRCode: GuestModeMobileAccess
GuestModeMobileAccessSwipedAway: GuestModeMobileAccess
GuestModeMobileAccessDismissedQRCodeExpired: GuestModeMobileAccess
GuestModeMobileAccessSucceededPairedNewBLEKey: GuestModeMobileAccess
LaneAssistLevelUnknown: LaneAssistLevel
LaneAssistLevelNone: LaneAssistLevel
LaneAssistLevelWarning: LaneAssistLevel
LaneAssistLevelAssist: LaneAssistLevel
ScheduledChargingModeUnknown: ScheduledChargingModeValue
ScheduledChargingModeOff: ScheduledChargingModeValue
ScheduledChargingModeStartAt: ScheduledChargingModeValue
ScheduledChargingModeDepartBy: ScheduledChargingModeValue
SentryModeStateUnknown: SentryModeState
SentryModeStateOff: SentryModeState
SentryModeStateIdle: SentryModeState
SentryModeStateArmed: SentryModeState
SentryModeStateAware: SentryModeState
SentryModeStatePanic: SentryModeState
SentryModeStateQuiet: SentryModeState
SpeedAssistLevelUnknown: SpeedAssistLevel
SpeedAssistLevelNone: SpeedAssistLevel
SpeedAssistLevelDisplay: SpeedAssistLevel
SpeedAssistLevelChime: SpeedAssistLevel
BMSStateUnknown: BMSStateValue
BMSStateStandby: BMSStateValue
BMSStateDrive: BMSStateValue
BMSStateSupport: BMSStateValue
BMSStateCharge: BMSStateValue
BMSStateFEIM: BMSStateValue
BMSStateClearFault: BMSStateValue
BMSStateFault: BMSStateValue
BMSStateWeld: BMSStateValue
BMSStateTest: BMSStateValue
BMSStateSNA: BMSStateValue
BuckleStatusUnknown: BuckleStatus
BuckleStatusUnlatched: BuckleStatus
BuckleStatusLatched: BuckleStatus
BuckleStatusFaulted: BuckleStatus
CarTypeUnknown: CarTypeValue
CarTypeModelS: CarTypeValue
CarTypeModelX: CarTypeValue
CarTypeModel3: CarTypeValue
CarTypeModelY: CarTypeValue
CarTypeSemiTruck: CarTypeValue
CarTypeCybertruck: CarTypeValue
ChargePortUnknown: ChargePortValue
ChargePortUS: ChargePortValue
ChargePortEU: ChargePortValue
ChargePortGB: ChargePortValue
ChargePortCCS: ChargePortValue
ChargePortLatchUnknown: ChargePortLatchValue
ChargePortLatchSNA: ChargePortLatchValue
ChargePortLatchDisengaged: ChargePortLatchValue
ChargePortLatchEngaged: ChargePortLatchValue
ChargePortLatchBlocking: ChargePortLatchValue
DriveInverterStateUnknown: DriveInverterState
DriveInverterStateUnavailable: DriveInverterState
DriveInverterStateStandby: DriveInverterState
DriveInverterStateFault: DriveInverterState
DriveInverterStateAbort: DriveInverterState
DriveInverterStateEnable: DriveInverterState
HvilStatusUnknown: HvilStatus
HvilStatusFault: HvilStatus
HvilStatusOK: HvilStatus
WindowStateUnknown: WindowState
WindowStateClosed: WindowState
WindowStatePartiallyOpen: WindowState
WindowStateOpened: WindowState
SeatFoldPositionUnknown: SeatFoldPosition
SeatFoldPositionSNA: SeatFoldPosition
SeatFoldPositionFaulted: SeatFoldPosition
SeatFoldPositionNotConfigured: SeatFoldPosition
SeatFoldPositionFolded: SeatFoldPosition
SeatFoldPositionUnfolded: SeatFoldPosition
TractorAirStatusUnknown: TractorAirStatus
TractorAirStatusNotAvailable: TractorAirStatus
TractorAirStatusError: TractorAirStatus
TractorAirStatusCharged: TractorAirStatus
TractorAirStatusBuildingPressureIntermediate: TractorAirStatus
TractorAirStatusExhaustingPressureIntermediate: TractorAirStatus
TractorAirStatusExhausted: TractorAirStatus
TrailerAirStatusUnknown: TrailerAirStatus
TrailerAirStatusSNA: TrailerAirStatus
TrailerAirStatusInvalid: TrailerAirStatus
TrailerAirStatusBobtailMode: TrailerAirStatus
TrailerAirStatusCharged: TrailerAirStatus
TrailerAirStatusBuildingPressureIntermediate: TrailerAirStatus
TrailerAirStatusExhaustingPressureIntermediate: TrailerAirStatus
TrailerAirStatusExhausted: TrailerAirStatus
HvacAutoModeStateUnknown: HvacAutoModeState
HvacAutoModeStateOn: HvacAutoModeState
HvacAutoModeStateOverride: HvacAutoModeState
CabinOverheatProtectionModeStateUnknown: CabinOverheatProtectionModeState
CabinOverheatProtectionModeStateOff: CabinOverheatProtectionModeState
CabinOverheatProtectionModeStateOn: CabinOverheatProtectionModeState
CabinOverheatProtectionModeStateFanOnly: CabinOverheatProtectionModeState
ClimateOverheatProtectionTempLimitUnknown: ClimateOverheatProtectionTempLimit
ClimateOverheatProtectionTempLimitHigh: ClimateOverheatProtectionTempLimit
ClimateOverheatProtectionTempLimitMedium: ClimateOverheatProtectionTempLimit
ClimateOverheatProtectionTempLimitLow: ClimateOverheatProtectionTempLimit
DefrostModeStateUnknown: DefrostModeState
DefrostModeStateOff: DefrostModeState
DefrostModeStateNormal: DefrostModeState
DefrostModeStateMax: DefrostModeState
DefrostModeStateAutoDefog: DefrostModeState
ClimateKeeperModeStateUnknown: ClimateKeeperModeState
ClimateKeeperModeStateOff: ClimateKeeperModeState
ClimateKeeperModeStateOn: ClimateKeeperModeState
ClimateKeeperModeStateDog: ClimateKeeperModeState
ClimateKeeperModeStateParty: ClimateKeeperModeState
HvacPowerStateUnknown: HvacPowerState
HvacPowerStateOff: HvacPowerState
HvacPowerStateOn: HvacPowerState
HvacPowerStatePrecondition: HvacPowerState
HvacPowerStateOverheatProtect: HvacPowerState
FastChargerUnknown: FastCharger
FastChargerSupercharger: FastCharger
FastChargerCHAdeMO: FastCharger
FastChargerGB: FastCharger
FastChargerACSingleWireCAN: FastCharger
FastChargerCombo: FastCharger
FastChargerMCSingleWireCAN: FastCharger
FastChargerOther: FastCharger
FastChargerSNA: FastCharger
CableTypeUnknown: CableType
CableTypeIEC: CableType
CableTypeSAE: CableType
CableTypeGB_AC: CableType
CableTypeGB_DC: CableType
CableTypeSNA: CableType
TonneauTentModeStateUnknown: TonneauTentModeState
TonneauTentModeStateInactive: TonneauTentModeState
TonneauTentModeStateMoving: TonneauTentModeState
TonneauTentModeStateFailed: TonneauTentModeState
TonneauTentModeStateActive: TonneauTentModeState
TonneauPositionStateUnknown: TonneauPositionState
TonneauPositionStateInvalid: TonneauPositionState
TonneauPositionStateClosed: TonneauPositionState
TonneauPositionStatePartiallyOpen: TonneauPositionState
TonneauPositionStateFullyOpen: TonneauPositionState
PowershareStateUnknown: PowershareState
PowershareStateInactive: PowershareState
PowershareStateHandshaking: PowershareState
PowershareStateInit: PowershareState
PowershareStateEnabled: PowershareState
PowershareStateEnabledReconnectingSoon: PowershareState
PowershareStateStopped: PowershareState
PowershareStopReasonStatusUnknown: PowershareStopReasonStatus
PowershareStopReasonStatusNone: PowershareStopReasonStatus
PowershareStopReasonStatusSOCTooLow: PowershareStopReasonStatus
PowershareStopReasonStatusRetry: PowershareStopReasonStatus
PowershareStopReasonStatusFault: PowershareStopReasonStatus
PowershareStopReasonStatusUser: PowershareStopReasonStatus
PowershareStopReasonStatusReconnecting: PowershareStopReasonStatus
PowershareStopReasonStatusAuthentication: PowershareStopReasonStatus
PowershareTypeStatusUnknown: PowershareTypeStatus
PowershareTypeStatusNone: PowershareTypeStatus
PowershareTypeStatusLoad: PowershareTypeStatus
PowershareTypeStatusHome: PowershareTypeStatus
DisplayStateUnknown: DisplayState
DisplayStateOff: DisplayState
DisplayStateDim: DisplayState
DisplayStateAccessory: DisplayState
DisplayStateOn: DisplayState
DisplayStateDriving: DisplayState
DisplayStateCharging: DisplayState
DisplayStateLock: DisplayState
DisplayStateSentry: DisplayState
DisplayStateDog: DisplayState
DisplayStateEntertainment: DisplayState
DistanceUnitUnknown: DistanceUnit
DistanceUnitMiles: DistanceUnit
DistanceUnitKilometers: DistanceUnit
TemperatureUnitUnknown: TemperatureUnit
TemperatureUnitFahrenheit: TemperatureUnit
TemperatureUnitCelsius: TemperatureUnit
PressureUnitUnknown: PressureUnit
PressureUnitPsi: PressureUnit
PressureUnitBar: PressureUnit
ChargeUnitUnknown: ChargeUnitPreference
ChargeUnitDistance: ChargeUnitPreference
ChargeUnitPercent: ChargeUnitPreference
SunroofInstalledStateUnknown: SunroofInstalledState
SunroofInstalledStateNotInstalled: SunroofInstalledState
SunroofInstalledStateGen1Installed: SunroofInstalledState
SunroofInstalledStateGen2Installed: SunroofInstalledState
TurnSignalStateUnknown: TurnSignalState
TurnSignalStateOff: TurnSignalState
TurnSignalStateLeft: TurnSignalState
TurnSignalStateRight: TurnSignalState
TurnSignalStateBoth: TurnSignalState
MediaStatusUnknown: MediaStatus
MediaStatusStopped: MediaStatus
MediaStatusPlaying: MediaStatus
MediaStatusPaused: MediaStatus

class LocationValue(_message.Message):
    __slots__ = ('latitude', 'longitude')
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float

    def __init__(self, latitude: _Optional[float]=..., longitude: _Optional[float]=...) -> None:
        ...

class Doors(_message.Message):
    __slots__ = ('DriverFront', 'DriverRear', 'PassengerFront', 'PassengerRear', 'TrunkFront', 'TrunkRear')
    DRIVERFRONT_FIELD_NUMBER: _ClassVar[int]
    DRIVERREAR_FIELD_NUMBER: _ClassVar[int]
    PASSENGERFRONT_FIELD_NUMBER: _ClassVar[int]
    PASSENGERREAR_FIELD_NUMBER: _ClassVar[int]
    TRUNKFRONT_FIELD_NUMBER: _ClassVar[int]
    TRUNKREAR_FIELD_NUMBER: _ClassVar[int]
    DriverFront: bool
    DriverRear: bool
    PassengerFront: bool
    PassengerRear: bool
    TrunkFront: bool
    TrunkRear: bool

    def __init__(self, DriverFront: bool=..., DriverRear: bool=..., PassengerFront: bool=..., PassengerRear: bool=..., TrunkFront: bool=..., TrunkRear: bool=...) -> None:
        ...

class TireLocation(_message.Message):
    __slots__ = ('front_left', 'front_right', 'rear_left', 'rear_right', 'semi_middle_axle_left_2', 'semi_middle_axle_right_2', 'semi_rear_axle_left', 'semi_rear_axle_right', 'semi_rear_axle_left_2', 'semi_rear_axle_right_2')
    FRONT_LEFT_FIELD_NUMBER: _ClassVar[int]
    FRONT_RIGHT_FIELD_NUMBER: _ClassVar[int]
    REAR_LEFT_FIELD_NUMBER: _ClassVar[int]
    REAR_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEMI_MIDDLE_AXLE_LEFT_2_FIELD_NUMBER: _ClassVar[int]
    SEMI_MIDDLE_AXLE_RIGHT_2_FIELD_NUMBER: _ClassVar[int]
    SEMI_REAR_AXLE_LEFT_FIELD_NUMBER: _ClassVar[int]
    SEMI_REAR_AXLE_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEMI_REAR_AXLE_LEFT_2_FIELD_NUMBER: _ClassVar[int]
    SEMI_REAR_AXLE_RIGHT_2_FIELD_NUMBER: _ClassVar[int]
    front_left: bool
    front_right: bool
    rear_left: bool
    rear_right: bool
    semi_middle_axle_left_2: bool
    semi_middle_axle_right_2: bool
    semi_rear_axle_left: bool
    semi_rear_axle_right: bool
    semi_rear_axle_left_2: bool
    semi_rear_axle_right_2: bool

    def __init__(self, front_left: bool=..., front_right: bool=..., rear_left: bool=..., rear_right: bool=..., semi_middle_axle_left_2: bool=..., semi_middle_axle_right_2: bool=..., semi_rear_axle_left: bool=..., semi_rear_axle_right: bool=..., semi_rear_axle_left_2: bool=..., semi_rear_axle_right_2: bool=...) -> None:
        ...

class Time(_message.Message):
    __slots__ = ('hour', 'minute', 'second')
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    hour: int
    minute: int
    second: int

    def __init__(self, hour: _Optional[int]=..., minute: _Optional[int]=..., second: _Optional[int]=...) -> None:
        ...

class Value(_message.Message):
    __slots__ = ('string_value', 'int_value', 'long_value', 'float_value', 'double_value', 'boolean_value', 'location_value', 'charging_value', 'shift_state_value', 'invalid', 'lane_assist_level_value', 'scheduled_charging_mode_value', 'sentry_mode_state_value', 'speed_assist_level_value', 'bms_state_value', 'buckle_status_value', 'car_type_value', 'charge_port_value', 'charge_port_latch_value', 'door_value', 'drive_inverter_state_value', 'hvil_status_value', 'window_state_value', 'seat_fold_position_value', 'tractor_air_status_value', 'follow_distance_value', 'forward_collision_sensitivity_value', 'guest_mode_mobile_access_value', 'trailer_air_status_value', 'time_value', 'detailed_charge_state_value', 'hvac_auto_mode_value', 'cabin_overheat_protection_mode_value', 'cabin_overheat_protection_temperature_limit_value', 'defrost_mode_value', 'climate_keeper_mode_value', 'hvac_power_value', 'tire_location_value', 'fast_charger_value', 'cable_type_value', 'tonneau_tent_mode_value', 'tonneau_position_value', 'powershare_type_value', 'powershare_state_value', 'powershare_stop_reason_value', 'display_state_value', 'distance_unit_value', 'temperature_unit_value', 'pressure_unit_value', 'charge_unit_preference_value', 'turn_signal_state_value', 'media_status_value', 'sunroof_installed_state_value')
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    LONG_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHARGING_VALUE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    INVALID_FIELD_NUMBER: _ClassVar[int]
    LANE_ASSIST_LEVEL_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_MODE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SENTRY_MODE_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SPEED_ASSIST_LEVEL_VALUE_FIELD_NUMBER: _ClassVar[int]
    BMS_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BUCKLE_STATUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    CAR_TYPE_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_LATCH_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOOR_VALUE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_INVERTER_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    HVIL_STATUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SEAT_FOLD_POSITION_VALUE_FIELD_NUMBER: _ClassVar[int]
    TRACTOR_AIR_STATUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_DISTANCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    FORWARD_COLLISION_SENSITIVITY_VALUE_FIELD_NUMBER: _ClassVar[int]
    GUEST_MODE_MOBILE_ACCESS_VALUE_FIELD_NUMBER: _ClassVar[int]
    TRAILER_AIR_STATUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    DETAILED_CHARGE_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    HVAC_AUTO_MODE_VALUE_FIELD_NUMBER: _ClassVar[int]
    CABIN_OVERHEAT_PROTECTION_MODE_VALUE_FIELD_NUMBER: _ClassVar[int]
    CABIN_OVERHEAT_PROTECTION_TEMPERATURE_LIMIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEFROST_MODE_VALUE_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_KEEPER_MODE_VALUE_FIELD_NUMBER: _ClassVar[int]
    HVAC_POWER_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIRE_LOCATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    FAST_CHARGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    CABLE_TYPE_VALUE_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_TENT_MODE_VALUE_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_POSITION_VALUE_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_TYPE_VALUE_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_STOP_REASON_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_UNIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_UNIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_UNIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_UNIT_PREFERENCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    TURN_SIGNAL_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_STATUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    SUNROOF_INSTALLED_STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    int_value: int
    long_value: int
    float_value: float
    double_value: float
    boolean_value: bool
    location_value: LocationValue
    charging_value: ChargingState
    shift_state_value: ShiftState
    invalid: bool
    lane_assist_level_value: LaneAssistLevel
    scheduled_charging_mode_value: ScheduledChargingModeValue
    sentry_mode_state_value: SentryModeState
    speed_assist_level_value: SpeedAssistLevel
    bms_state_value: BMSStateValue
    buckle_status_value: BuckleStatus
    car_type_value: CarTypeValue
    charge_port_value: ChargePortValue
    charge_port_latch_value: ChargePortLatchValue
    door_value: Doors
    drive_inverter_state_value: DriveInverterState
    hvil_status_value: HvilStatus
    window_state_value: WindowState
    seat_fold_position_value: SeatFoldPosition
    tractor_air_status_value: TractorAirStatus
    follow_distance_value: FollowDistance
    forward_collision_sensitivity_value: ForwardCollisionSensitivity
    guest_mode_mobile_access_value: GuestModeMobileAccess
    trailer_air_status_value: TrailerAirStatus
    time_value: Time
    detailed_charge_state_value: DetailedChargeStateValue
    hvac_auto_mode_value: HvacAutoModeState
    cabin_overheat_protection_mode_value: CabinOverheatProtectionModeState
    cabin_overheat_protection_temperature_limit_value: ClimateOverheatProtectionTempLimit
    defrost_mode_value: DefrostModeState
    climate_keeper_mode_value: ClimateKeeperModeState
    hvac_power_value: HvacPowerState
    tire_location_value: TireLocation
    fast_charger_value: FastCharger
    cable_type_value: CableType
    tonneau_tent_mode_value: TonneauTentModeState
    tonneau_position_value: TonneauPositionState
    powershare_type_value: PowershareTypeStatus
    powershare_state_value: PowershareState
    powershare_stop_reason_value: PowershareStopReasonStatus
    display_state_value: DisplayState
    distance_unit_value: DistanceUnit
    temperature_unit_value: TemperatureUnit
    pressure_unit_value: PressureUnit
    charge_unit_preference_value: ChargeUnitPreference
    turn_signal_state_value: TurnSignalState
    media_status_value: MediaStatus
    sunroof_installed_state_value: SunroofInstalledState

    def __init__(self, string_value: _Optional[str]=..., int_value: _Optional[int]=..., long_value: _Optional[int]=..., float_value: _Optional[float]=..., double_value: _Optional[float]=..., boolean_value: bool=..., location_value: _Optional[_Union[LocationValue, _Mapping]]=..., charging_value: _Optional[_Union[ChargingState, str]]=..., shift_state_value: _Optional[_Union[ShiftState, str]]=..., invalid: bool=..., lane_assist_level_value: _Optional[_Union[LaneAssistLevel, str]]=..., scheduled_charging_mode_value: _Optional[_Union[ScheduledChargingModeValue, str]]=..., sentry_mode_state_value: _Optional[_Union[SentryModeState, str]]=..., speed_assist_level_value: _Optional[_Union[SpeedAssistLevel, str]]=..., bms_state_value: _Optional[_Union[BMSStateValue, str]]=..., buckle_status_value: _Optional[_Union[BuckleStatus, str]]=..., car_type_value: _Optional[_Union[CarTypeValue, str]]=..., charge_port_value: _Optional[_Union[ChargePortValue, str]]=..., charge_port_latch_value: _Optional[_Union[ChargePortLatchValue, str]]=..., door_value: _Optional[_Union[Doors, _Mapping]]=..., drive_inverter_state_value: _Optional[_Union[DriveInverterState, str]]=..., hvil_status_value: _Optional[_Union[HvilStatus, str]]=..., window_state_value: _Optional[_Union[WindowState, str]]=..., seat_fold_position_value: _Optional[_Union[SeatFoldPosition, str]]=..., tractor_air_status_value: _Optional[_Union[TractorAirStatus, str]]=..., follow_distance_value: _Optional[_Union[FollowDistance, str]]=..., forward_collision_sensitivity_value: _Optional[_Union[ForwardCollisionSensitivity, str]]=..., guest_mode_mobile_access_value: _Optional[_Union[GuestModeMobileAccess, str]]=..., trailer_air_status_value: _Optional[_Union[TrailerAirStatus, str]]=..., time_value: _Optional[_Union[Time, _Mapping]]=..., detailed_charge_state_value: _Optional[_Union[DetailedChargeStateValue, str]]=..., hvac_auto_mode_value: _Optional[_Union[HvacAutoModeState, str]]=..., cabin_overheat_protection_mode_value: _Optional[_Union[CabinOverheatProtectionModeState, str]]=..., cabin_overheat_protection_temperature_limit_value: _Optional[_Union[ClimateOverheatProtectionTempLimit, str]]=..., defrost_mode_value: _Optional[_Union[DefrostModeState, str]]=..., climate_keeper_mode_value: _Optional[_Union[ClimateKeeperModeState, str]]=..., hvac_power_value: _Optional[_Union[HvacPowerState, str]]=..., tire_location_value: _Optional[_Union[TireLocation, _Mapping]]=..., fast_charger_value: _Optional[_Union[FastCharger, str]]=..., cable_type_value: _Optional[_Union[CableType, str]]=..., tonneau_tent_mode_value: _Optional[_Union[TonneauTentModeState, str]]=..., tonneau_position_value: _Optional[_Union[TonneauPositionState, str]]=..., powershare_type_value: _Optional[_Union[PowershareTypeStatus, str]]=..., powershare_state_value: _Optional[_Union[PowershareState, str]]=..., powershare_stop_reason_value: _Optional[_Union[PowershareStopReasonStatus, str]]=..., display_state_value: _Optional[_Union[DisplayState, str]]=..., distance_unit_value: _Optional[_Union[DistanceUnit, str]]=..., temperature_unit_value: _Optional[_Union[TemperatureUnit, str]]=..., pressure_unit_value: _Optional[_Union[PressureUnit, str]]=..., charge_unit_preference_value: _Optional[_Union[ChargeUnitPreference, str]]=..., turn_signal_state_value: _Optional[_Union[TurnSignalState, str]]=..., media_status_value: _Optional[_Union[MediaStatus, str]]=..., sunroof_installed_state_value: _Optional[_Union[SunroofInstalledState, str]]=...) -> None:
        ...

class Datum(_message.Message):
    __slots__ = ('key', 'value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: Field
    value: Value

    def __init__(self, key: _Optional[_Union[Field, str]]=..., value: _Optional[_Union[Value, _Mapping]]=...) -> None:
        ...

class Payload(_message.Message):
    __slots__ = ('data', 'created_at', 'vin', 'is_resend')
    DATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    IS_RESEND_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Datum]
    created_at: _timestamp_pb2.Timestamp
    vin: str
    is_resend: bool

    def __init__(self, data: _Optional[_Iterable[_Union[Datum, _Mapping]]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., vin: _Optional[str]=..., is_resend: bool=...) -> None:
        ...