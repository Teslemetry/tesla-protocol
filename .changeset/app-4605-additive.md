---
"@teslemetry/tesla-protocol": minor
---

Wire-compatible additions to the command protocol. Every new field is marked `UNCONFIRMED` (not yet confirmed on a live vehicle), and placeholder names are marked "name not recovered".

- `VehicleAction`: wire the existing `PrepareMobileUploadAction` (177), `PutMobileUploadChunkAction` (178) and `DisplayStateAction` (180) messages, and add `SetUpkeepUsernameAction` (147), `DrivingSetCruiseSpeedLimitAction` (694177) and `SetDeckLightAction` (698038). Fill in `PrepareMobileUploadAction` tag 3, `MediaPlayAction.media_playback_status`, `SetPhoneSettingPreferencesAction` tag 2, the remaining `DestinationCharging` fields and `DogModeLiveActivityData` tags 2-4, and reserve `Action` tags 6-8.
