# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=daily-question&envId=2023-10-13
"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""

# Python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[len(cost) - 1], cost[len(cost) - 2])

# golang
func minCostClimbingStairs(cost []int) int {
    for i:= 2; i < len(cost); i++ {
        cost[i] += min(cost[i-1], cost[i-2])
    }
    return min(cost[len(cost)-1], cost[len(cost)-2])
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

