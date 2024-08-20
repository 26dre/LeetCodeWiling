package minclimbingcost

func MinCostClimbingStairs(cost []int) int {
	return minCostClimbingStairs(cost)
}
func minCostClimbingStairs(cost []int) int {
	cost_len := len(cost)
	dp := make([]int, cost_len)

	dp[cost_len-1] = cost[cost_len-1]
	dp[cost_len-2] = cost[cost_len-2]
	for i := cost_len - 3; i >= 0; i-- {
		minclimbingcost_util(cost, dp, i)
	}

	return min(dp[0], dp[1])

}

func min(a int, b int) int {
	if b < a {
		return b
	}
	return a
}

func minclimbingcost_util(cost []int, dp_costs []int, curr_pos int) int {

	cost_comp1 := dp_costs[curr_pos+1] + cost[curr_pos]
	cost_comp2 := dp_costs[curr_pos+2] + cost[curr_pos]
	dp_costs[curr_pos] = cost_comp1
	if cost_comp2 < cost_comp1 {
		dp_costs[curr_pos] = cost_comp2
	}

	return dp_costs[curr_pos]

}
