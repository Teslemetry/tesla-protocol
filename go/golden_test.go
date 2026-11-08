package tesla_protocol_test

// Round-trips the language-neutral fixtures in fixtures/golden through the
// generated Go code: decoding each golden hex and re-encoding it must give the
// same bytes the TypeScript and Python suites assert.

import (
	"encoding/hex"
	"encoding/json"
	"os"
	"path/filepath"
	"strings"
	"testing"

	"github.com/Teslemetry/tesla-protocol/go/v6/command/carserver"
	"github.com/Teslemetry/tesla-protocol/go/v6/energy_device"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/reflect/protoreflect"

	// Every package, so the test binary also proves they all register in
	// one process without a global registry conflict.
	_ "github.com/Teslemetry/tesla-protocol/go/v6/charging"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/command/errors"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/command/keys"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/command/managedcharging"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/command/session"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/command/signatures"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/command/universalmessage"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/command/vcsec"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/dashcam"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/telemetry"
	_ "github.com/Teslemetry/tesla-protocol/go/v6/teslapower"
)

func readFixture(t *testing.T, name string, v any) {
	t.Helper()
	data, err := os.ReadFile(filepath.Join("..", "fixtures", "golden", name))
	if err != nil {
		t.Fatal(err)
	}
	if err := json.Unmarshal(data, v); err != nil {
		t.Fatal(err)
	}
}

// roundTrip decodes hexIn into msg and checks that re-encoding gives hexOut.
func roundTrip(t *testing.T, msg proto.Message, hexIn, hexOut string) {
	t.Helper()
	raw, err := hex.DecodeString(hexIn)
	if err != nil {
		t.Fatal(err)
	}
	if err := proto.Unmarshal(raw, msg); err != nil {
		t.Fatal(err)
	}
	if len(msg.ProtoReflect().GetUnknown()) != 0 {
		t.Errorf("decoded with unknown fields: %x", msg.ProtoReflect().GetUnknown())
	}
	encoded, err := proto.Marshal(msg)
	if err != nil {
		t.Fatal(err)
	}
	if got := hex.EncodeToString(encoded); got != hexOut {
		t.Errorf("re-encoded %s, want %s", got, hexOut)
	}
}

func TestCommandGoldenFixtures(t *testing.T) {
	files, err := filepath.Glob(filepath.Join("..", "fixtures", "golden", "*.json"))
	if err != nil {
		t.Fatal(err)
	}
	for _, file := range files {
		var fixture struct {
			OuterMessage string `json:"outer_message"`
			Cases        []struct {
				Name  string `json:"name"`
				Field struct {
					Tag protoreflect.FieldNumber `json:"tag"`
				} `json:"vehicle_action_field"`
				Hex string `json:"hex"`
			} `json:"cases"`
		}
		readFixture(t, filepath.Base(file), &fixture)
		if fixture.OuterMessage != "CarServer.Action" {
			continue
		}
		for _, c := range fixture.Cases {
			t.Run(c.Name, func(t *testing.T) {
				action := &carserver.Action{}
				roundTrip(t, action, c.Hex, c.Hex)
				var set []protoreflect.FieldNumber
				action.GetVehicleAction().ProtoReflect().Range(func(fd protoreflect.FieldDescriptor, _ protoreflect.Value) bool {
					set = append(set, fd.Number())
					return true
				})
				if len(set) != 1 || set[0] != c.Field.Tag {
					t.Errorf("VehicleAction fields set %v, want [%d]", set, c.Field.Tag)
				}
			})
		}
	}
}

func TestEnergyDeviceGoldenFixtures(t *testing.T) {
	var envelopes struct {
		Cases []struct {
			Name     string `json:"name"`
			Messages []struct {
				Hex          string `json:"hex"`
				CanonicalHex string `json:"canonical_hex"`
				PayloadCase  string `json:"payload_case"`
			} `json:"messages"`
		} `json:"cases"`
	}
	readFixture(t, "energy_v1r_envelopes.json", &envelopes)
	for _, c := range envelopes.Cases {
		for _, m := range c.Messages {
			t.Run(c.Name+"/"+m.PayloadCase, func(t *testing.T) {
				want := m.CanonicalHex
				if want == "" {
					want = m.Hex
				}
				envelope := &energy_device.MessageEnvelope{}
				roundTrip(t, envelope, m.Hex, want)

				outer, inner, _ := strings.Cut(m.PayloadCase, ".")
				r := envelope.ProtoReflect()
				fd := r.WhichOneof(r.Descriptor().Oneofs().ByName("payload"))
				if fd == nil || string(fd.Name()) != outer {
					t.Fatalf("payload oneof is %v, want %s", fd, outer)
				}
				group := r.Get(fd).Message()
				if !group.Has(group.Descriptor().Fields().ByName(protoreflect.Name(inner))) {
					t.Errorf("%s.%s is not set", outer, inner)
				}
			})
		}
	}

	var systemInfo struct {
		ModelledHex string `json:"modelled_hex"`
	}
	readFixture(t, "get_system_info_response.json", &systemInfo)
	t.Run("get_system_info_response", func(t *testing.T) {
		envelope := &energy_device.MessageEnvelope{}
		roundTrip(t, envelope, systemInfo.ModelledHex, systemInfo.ModelledHex)
		if envelope.GetCommon().GetGetSystemInfoResponse() == nil {
			t.Error("common.get_system_info_response is not set")
		}
	})
}
