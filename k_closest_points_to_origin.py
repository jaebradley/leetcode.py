from typing import List
import heapq
import math

"""
https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

Approach:

* Create a min heap of size of 10
* Calculate euclidean distance for each point
* Negate euclidean distance so that farther points are smaller
* Push to min heap - the tuple pushed to min heap has distance as first value and then point as second value
* When min heap does element comparison, it uses first element in tuple (and then next element)
* If heap is at K elements, add the current distance and then pop to guarantee heap is at K elements
* By popping, this removes the largest current distance
"""


class Solution:
    @staticmethod
    def calculate_distance(x, y):
        return math.sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = -Solution.calculate_distance(point[0], point[1])
            if len(heap) == K:
                heapq.heappushpop(heap, (distance, point))
            else:
                heapq.heappush(heap, (distance, point))

        return [result[1] for result in heap]
