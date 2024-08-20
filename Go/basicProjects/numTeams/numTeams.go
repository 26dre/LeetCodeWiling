// https://leetcode.com/problems/count-number-of-teams/?envType=daily-question&envId=2024-07-29
package numteams

import (
	"fmt"
	"os"
)

func NumTeams(rating []int) int {
	return numTeams(rating)
}

func numTeams(rating []int) int {

	num_teams := 0
	for i := range rating {
		smaller := true
		for j := i + 1; j < len(rating); j++ {
			if rating[j] > rating[i] {
				smaller = false
			} else if rating[j] == rating[i] {
				continue
			}
			for z := j + 1; z < len(rating); z++ {
				if smaller {
					if rating[z] < rating[j] {
						num_teams += 1
					}
				} else if rating[z] > rating[j] {
					num_teams += 1
				}
			}
		}
	}
	return num_teams
}

// func numTeams2(rating []int) int {
// 	num_teams := 0
// 	for i := range rating {
// 		smaller := true
// 		for j := i+1; j < len(rating) - 1; j++ {
// 			if rating[j] > rating[i] {
// 				smaller = false;
// 			} else if rating[j] == rating[i] {
// 				continue
// 			}
// 			for k := j + 1; k < len(rating); k++ {
// 				if smaller {
// 					if rating[j] < rating[k] {

// 					}
// 				}
// 			}
// 		}
// 	}
// }

func NumTeams2(rating []int) int {
	return numTeams2(rating)
}
func numTeams2(rating []int) int {
	num_teams := 0

	for i := range rating {

		fmt.Fprintf(os.Stderr, "\n\nCurrently running with i = %d\n", i)
		increasing := true
		for j := i + 1; j < len(rating)-1; j++ {
			if rating[j] < rating[i] {
				increasing = false
				fmt.Fprintf(os.Stderr, "Increasing changed to false\n")
			} else {
				continue
			}

			for z := j + 1; z < len(rating); z++ {
				switch increasing {
				case true:
					fmt.Fprintf(os.Stderr, "Evaluated increasing as true\n")
					if rating[z] > rating[j] {
						num_teams += 1
						fmt.Fprintf(os.Stdout, "Adding team %d %d %d\n", rating[i], rating[j], rating[z])
					}

				default:
					fmt.Fprintf(os.Stderr, "Evaluated increasing as false\n")
					if rating[z] < rating[j] {
						num_teams += 1
						fmt.Fprintf(os.Stderr, "Adding team %d %d %d\n", rating[i], rating[j], rating[z])
					}

				}
			}
		}
	}

	return num_teams
}

func NumTeams3(rating []int) int {
	return numTeams3(rating)
}
func numTeams3(rating []int) int {
	num_teams := 0

	for i := range rating {
		monotonically_increasing := true
		first_val := rating[i]
		for j := range rating[i+1:] {

			second_val := rating[i]
			if first_val < second_val {
				monotonically_increasing = false
			} else if first_val == second_val {
				continue
			}
			for k := range rating[j+i:] {
				if monotonically_increasing {
					if second_val < rating[k] {
						num_teams += 1
					}
				} else {
					if second_val > rating[k] {
						num_teams += 1
					}
				}
			}
		}
	}

	// for i, first_val := range rating {
	// 	increasing := false

	// 	for j, second_val := range rating[i+1:] {
	// 		if second_val > first_val {
	// 			increasing = true
	// 		} else if second_val == first_val {
	// 			continue
	// 		}

	// 		for _, third_val := range rating[j+1:] {
	// 			if increasing {

	// 				if third_val > second_val {
	// 					num_teams += 1
	// 					fmt.Fprintf(os.Stderr, "Adding %d %d %d\n", first_val, second_val, third_val)
	// 				}
	// 			} else if third_val < second_val {
	// 				num_teams += 1
	// 				fmt.Fprintf(os.Stderr, "Adding %d %d %d\n", first_val, second_val, third_val)
	// 			}
	// 		}
	// 	}

	// }

	return num_teams
}
