"""
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from heapq import heappush, heappop


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        Get counts, add to max heap (in this case, negated the counts because Python only has min heap), and then popped
        off heap k times.

        Runtime is O(n log n) since each insert is log n and worst-case there are n inserts.
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        heap = []
        for number, count in counts.items():
            heappush(heap, (-count, number))

        return [heappop(heap)[1] for _ in range(k)]

    def bucketSort(self, nums, k):
        """
        Get counts, create buckets where each bucket represents the number of numbers having a given count.
        Walk through the bucket backwards, appending numbers to result list until result list is k.

        This should be O(n).
        :param nums:
        :param k:
        :return:
        """
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        buckets = [[] for _ in range(len(nums))]
        for number, count in counts.items():
            buckets[count - 1].append(number)

        result = []
        for bucket in reversed(buckets):
            for number in bucket:
                result.append(number)
                if len(result) >= k:
                    return result

        return result


