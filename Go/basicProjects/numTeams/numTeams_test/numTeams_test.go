package numteams_test

import (
	numteams "basicProjects/numTeams"
	"testing"
)

// TestHelloName calls greetings.Hello with a name, checking
// for a valid return value.
func TestNumTeams(t *testing.T) {
	possible_team := []int{5, 2, 7, 1}
	got := numteams.NumTeams2(possible_team)
	if got != 1 {
		t.Errorf("Abs(-1) = %d; want 1", got)

	}
}

func TestNumTeams2(t *testing.T) {
	possible_team := []int{2, 5, 3, 4, 1}
	got := numteams.NumTeams3(possible_team)
	expect := 3
	if got != expect {
		t.Errorf("Abs(-1) = %d; want %d", got, expect)

	}
}
