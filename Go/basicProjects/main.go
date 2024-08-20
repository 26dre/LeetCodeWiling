package main

import (
	"basicProjects/maxcost"
	minclimbingcost "basicProjects/minClimbingCost"
	"basicProjects/minCost"
	numteams "basicProjects/numTeams"
	"basicProjects/pow"
	"basicProjects/stupidshit"
	"fmt"
)

func main() {
	// stupidshit.stupid_shit()

	mcc := []int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
	fmt.Println(minclimbingcost.MinCostClimbingStairs(mcc))
	costs := [][]int{{1, 100, 100}, {1, 100, 100}, {100, 1, 100}}

	possible_team := []int{5, 2, 7, 1}
	fmt.Println(numteams.NumTeams2(possible_team))
	pow := pow.Pow(10, 2)
	fmt.Println(pow)

	x := minCost.MinCost(costs)
	minCost.StupidShit()
	fmt.Println(x)
	result := minCost.MinCost(costs)
	// stupidshit.stupid_shit()
	j := maxcost.MaxCost()
	fmt.Println("J = ", j)
	stupidshit.StupidShit()
	fmt.Println("The minimum cost is:", result)
}
