from math import inf

"""
https://leetcode.com/problems/maximum-length-of-pair-chain/

You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.



Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].


Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti < 1000

Strategy:

Another way of thinking of the problem is the longest sequence of non-overlapping monotonically increasing intervals.

For each given pair, can make the decision to add it to the existing chain or to skip it.
max(chain_length) = existing_chain_length + max(chain_length_if_take_current_pair, chain_length_if_skip_current_pair)

1. Sort array by right value in pair (O(n log n))
2. DP array of length n, with 2 rows.
   First row has cells that represent max values if pair is taken at the index.
   Second row has cells that represent max values if pair is skipped at the index.
3. Initial starting values are 0 and 0 for first cells
4. Need to check that current index pair's left value is less than previous pair's right value.
   If it's not, then set max for both rows as previous max and move on to next index
"""


class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])

        counts = 0

        current_tail = -inf

        for start, end in pairs:
            if start > current_tail:
                counts += 1
                current_tail = end

        return counts
