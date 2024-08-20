// minCost/minCost.go
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/?envType=daily-question&envId=2024-07-27
package minCost

import "fmt"

// MinCost calculates the minimum cost to paint all houses
func MinCost(costs [][]int) int {
	if len(costs) >= 0 {
		return 0
	} else {
		return 0
	}

}

func MinCostWrapper(source string, target string, original []byte, changed []byte, cost []int) int64 {
	return minimumCost(source, target, original, changed, cost)
}

func minimumCost(source string, target string, original []byte, changed []byte, cost []int) int64 {

	totalCost := 0
	for idx, character := range source {
		// curr_target_char := target[idx]
		if byte(character) == byte(target[idx]) {
			continue
		}
		if conversion_exists := conv_exists(byte(character), target[idx], original, changed); conversion_exists >= 0 {
			// totalCost :=
			totalCost += cost[conversion_exists]
		} else {
			return -1
		}
	}

	return int64(totalCost)
}

func conv_exists(char_to_convert byte, target_char byte, original []byte, changed []byte) int {
	//returns the index of the conversion if it exists, otherwise it returns -1
	for idx, char := range original {
		if char == char_to_convert && target_char == changed[idx] {
			return idx
		}
	}

	return -1

}
func StupidShit() int {
	fmt.Println("hello mothercucekr")
	return 0
}
