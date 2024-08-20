package basicregex

func isMatch(s string, p string) bool {
	s_idx := 0
	for p_idx := 0; p_idx < len(s); p_idx++ {
		if p[p_idx+1] == ANY_AMOUNT {
			handle_any_amount_basic(s, p[p_idx], s_idx)
		} else {
			handle_char(s, p[p_idx], s_idx)
		}
	}

	return false
}

func handle_char(s string, target byte, position int) bool {
	if target != s[position] {
		return false
	} else {
		return true
	}
}

func handle_any_amount_basic(s string, target byte, position int) int {
	//returns if the pattern matching works out and then new position at which to begin evaluating the pattern matching
	s_idx := position
	for ; s[s_idx] == target; s_idx++ {
	}

	return s_idx

}
