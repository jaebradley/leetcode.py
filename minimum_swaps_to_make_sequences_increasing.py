"""
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation:
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].
"""


class Solution(object):
    def minSwap(self, A, B):
        """
        Values at index 0 represent the minimum number of swaps to make A and B increasing if swap at index.
        Values at index 1 represent the minimum number of swaps to make A and B increasing if do not swap at index.

        Two cases:
        1. Sorted (previous A < A, previous B < B) AND previous B < A AND previous A < B
           Swapping doesn't do anything, so just take min of swapping or not swapping up to that point.
           In case of swapping, still need to add 1 since there's technically still a swap.
        2. Should swap (previous A >= A OR previous B >= B)
           Swapping means that minimum of swapping at that index is not swapping at previous index + 1.
           Not swapping means that minimum of not swapping at index is swapping at previous index (since swapping at
           previous index would resolve previous A >= A OR previous B >= B)

        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        min_swap = 1
        min_no_swap = 0

        for index in range(1, len(A)):
            a = A[index]
            prev_a = A[index - 1]

            b = B[index]
            prev_b = B[index - 1]

            if prev_a < a and prev_b < b and prev_b < a and prev_a < b:
                min_swap = min_no_swap = min(min_swap, min_no_swap)
            elif prev_a >= a or prev_b >= b:
                min_swap, min_no_swap = min_no_swap, min_swap

            min_swap += 1

        return min(min_swap, min_no_swap)

