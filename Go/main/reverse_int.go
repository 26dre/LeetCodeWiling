package main

// "fmt"
// "strconv"

func reverse_i32(x int) int {
	const max_size = 10
	stack := make([]int, max_size)
	curr_pos := max_size - 1

	for ; x > 0; curr_pos-- {
		curr_num := x % 10
		stack[curr_pos] = curr_num
	}

	accumulator := 0
	for ; curr_pos < max_size; curr_pos++ {
		accumulator *= 10
		accumulator += stack[curr_pos]
	}

	return 0

}
