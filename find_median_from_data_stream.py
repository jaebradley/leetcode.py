"""
https://leetcode.com/problems/find-median-from-data-stream/

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
import heapq


class MedianFinder(object):

    def __init__(self):
        # small is going to be a max heap which is going to represent the smallest n/2 values
        # it's max value is going to be used to calculate the median
        self.small = []

        # large is going to be a min heap which is going to represent the largest n/2 (or n/2 + 1) values
        # it's min value is going to be used to calculate the median
        self.large = []

    def addNum(self, num):
        """
        When even values, add num (inverted since small is max heap) to small and pop value.
        Push popped value to large, which is min heap.

        When odd values, add num to large min heap, and push smallest value to small max heap
        :param num:
        :return:
        """
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        """
        When even values, sum min value in large (i.e. first element) and max value in small (i.e. first element).
        Since all values in small are negative, to "sum" need to subtract the value in small.
        :return:
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

