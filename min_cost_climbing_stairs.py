"""
https://leetcode.com/problems/min-cost-climbing-stairs/

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the
floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        Need to keep track of cost that needs to be paid in 2 hops or cost that needs to be paid in 1 hop.
        Cost that needs to be paid in 2 hops is stored in 0th index, and paid in 1 hop is stored in 1st index.
        The values that need to be paid in two hops are
        1. The value from previous hop that needs to be paid in 1 hop, plus cost of current index
        2. The value from two hops ago that needs to be paid in 2 hops, plus cost of current index
        3. The value from previous hop that needs to be paid in 2 hops, plus cost of current index (paying early,
           for benefit of being able to "hop" earlier)

        The value that need to be paid in one hop are
        1. The value from previous hop that needs to be paid in 2 hops (no added cost - this is just allowing person
           to take advantage of "second" hop)

        The min of the final values should represent the min cost.
        :type cost: List[int]
        :rtype: int
        """
        stair_costs = [
            [cost[0], cost[0]],
            [cost[1], cost[0]],
        ]
        for index in range(2, len(cost)):
            pay_in_two_hops = min(
                stair_costs[index - 1][1] + cost[index],
                stair_costs[index - 2][0] + cost[index],
                stair_costs[index - 1][0] + cost[index],
            )
            pay_in_one_hop = min(
                stair_costs[index - 1][0],
                pay_in_two_hops,
            )
            stair_costs.append([
                pay_in_two_hops,
                pay_in_one_hop,
            ])

        return min(stair_costs[len(cost) - 1])
