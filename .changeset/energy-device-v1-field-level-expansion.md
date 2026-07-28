---
"@teslemetry/tesla-protocol": minor
---

Model field-level definitions for the `energy_device.v1` local-Powerwall/Wall-Connector/PV-inverter API - Wall Connector (`WCAPI`), TEG/Powerwall (`TEGAPI`, controllable-device-program scheduling, OCPP/CSMS config), PV inverter (`PVIAPI`, new `pvi_api.proto`), CT metering (`NeurioMeterAPI`, new `neurio_meter_api.proto`), local login (`LocalAuthAPI`, new `local_auth_api.proto`), site device pairing (`EnergySiteNetAPI`, `IntraSiteAPI`, new `intra_site_api.proto`), on-gateway file storage (`FileStoreAPI`, new `filestore_api.proto`), and the GraphQL-over-protobuf sub-channel (`GraphQLAPI`, new `graphql_api.proto`) - completing each service's request/response bodies and its `*Messages` oneof envelope, based on our own observations and contributions from the community.
