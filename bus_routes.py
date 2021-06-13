from typing import List
from collections import deque

"""
https://leetcode.com/problems/bus-routes/

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.



Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1


Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106

Solution:

1. Map of stops to list of bus routes that pass through the stop
2. Start with source bus stop
3. Get all bus routes that pass through stop
4. If any bus routes have not yet been "visited" add them to the visited list
5. For each of these newly visited bus routes, iterate over the stops in the bus route - if any of the stops are the 
target stop, return the count, else add the stop to the queue
6. This way, each possible bus route are the "same distance" away from the source
"""

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        next_routes_by_current_stop = {}

        for route_index, route  in enumerate(routes):
            for stop in route:
                if stop in next_routes_by_current_stop:
                    next_routes_by_current_stop[stop].add(route_index)
                else:
                    next_routes_by_current_stop[stop] = {route_index}

        if source == target:
            return 0

        queue = deque([source])
        count = 0
        visited = set([])

        while len(queue) > 0:
            count += 1

            for _ in range(len(queue)):
                current_stop = queue.pop()

                for next_bus_route in next_routes_by_current_stop.get(current_stop):
                    if next_bus_route not in visited:
                        visited.add(next_bus_route)

                        for bus_stop in routes[next_bus_route]:
                            if bus_stop == target:
                                return count

                            queue.appendleft(bus_stop)

        return -1
