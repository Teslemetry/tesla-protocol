---
"@teslemetry/tesla-protocol": minor
---

Wire-compatible additions to the command protocol. Every new field is marked `UNCONFIRMED` (not yet confirmed on a live vehicle), and placeholder names are marked "name not recovered".

- `VehicleAction`: wire the existing `PrepareMobileUploadAction` (177), `PutMobileUploadChunkAction` (178) and `DisplayStateAction` (180) messages, and add `SetUpkeepUsernameAction` (147), `DrivingSetCruiseSpeedLimitAction` (694177) and `SetDeckLightAction` (698038). Fill in `PrepareMobileUploadAction` tag 3, `MediaPlayAction.media_playback_status`, `SetPhoneSettingPreferencesAction` tag 2, the remaining `DestinationCharging` fields and `DogModeLiveActivityData` tags 2-4, and reserve `Action` tags 6-8.
- Add the `MobileAppFeature` enum (the capability bits a vehicle advertises, with how to test them against the vehicle-state feature bitmask), `VehicleConfig.wheel_caps_on` (200), the `VehicleDataFields` enum that `EncryptedData.field_number` holds, the PII vehicle-data fields `VehicleData.encrypted_data` (11), `pii_key_responses` (900) and `wrapped_key` (901), and `SohState.SohResult` tag 3.
