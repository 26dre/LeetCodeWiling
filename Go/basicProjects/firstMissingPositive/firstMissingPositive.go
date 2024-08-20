package firstmissingpositive

import "fmt"

func firstMissingPositive2(nums []int) int {
	for idx, number := range nums {
		if number <= 0 || number > len(nums) {
			nums[idx] = -1
		}
	}

	for _, number := range nums {
		nums[number-1] = 1
	}

	for _, number := range nums {
		if number != -1 {
		}

	}

	return -1
}

func firstMissingPositive(nums []int) int {
	nums_len := len(nums)
	num_positives := 0
	for idx, value := range nums {
		if value > 0 {
			num_positives += 1

			if value <= nums_len && idx != (value-1) {
				current := value
				for current > 0 && current >= value {

				}
			}
		}
	}

	for _, v := range nums {
		fmt.Printf("%d\t", v)
	}
	fmt.Println()
	for idx, value := range nums {

		if idx != (value - 1) {
			return idx + 1
		}
	}

	return num_positives + 1
}

func put_in_right_place(nums []int, idx, replacement int) int {
	tmp := nums[idx]
	nums[idx] = replacement
	return tmp
}

func FirstMissingPositive(nums []int) int {
	return firstMissingPositive(nums)
}
