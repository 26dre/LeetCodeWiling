package minstepscopying

import (
	"errors"
	"fmt"
)

const BaseCaseMax = 3

func minSteps(n int) int {

	curr_steps := 0

	for n > BaseCaseMax {
		curr_max_divisor := get_max_divisor_util(n)
		curr_steps += n / curr_max_divisor // how many times it takes to copy + paste this max divisor
		fmt.Printf("Curr max divisor = %d\t Curr steps = %d", curr_max_divisor, curr_steps)
		n = curr_max_divisor

	}

	if result_int, res_err := get_base_cases_util(n); res_err == nil {
		curr_steps += result_int
	}

	return curr_steps
}

func get_max_divisor_util(n int) int {
	max_divisor := 1
	for i := 1; i < n; i++ {
		if n%i == 0 {
			max_divisor = i
		}
	}
	return max_divisor
}

func get_base_cases_util(base_case int) (int, error) {
	if base_case == 1 {
		return 0, nil
	}
	if base_case <= 3 {
		return base_case, nil
	}

	return -1, errors.New("not a base case as given number > 3")
}

func MinSteps(n int) int {
	return minSteps(n)
}

/// get biggest divisor return those steps +
