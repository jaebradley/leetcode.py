from typing import List
from collections import deque

"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/

Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).



Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]


Constraints:

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
"""


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_edge_adjacency_matrix = {}
        blue_edge_adjacency_matrix = {}

        for red_edge in red_edges:
            starting_node, ending_node = red_edge

            ending_nodes = red_edge_adjacency_matrix.setdefault(starting_node, set([]))
            ending_nodes.add(ending_node)

        for blue_edge in blue_edges:
            starting_node, ending_node = blue_edge

            ending_nodes = blue_edge_adjacency_matrix.setdefault(starting_node, set([]))
            ending_nodes.add(ending_node)

        count = 0
        counts = [-1] * n
        counts[0] = 0

        visited_red_nodes = {0}
        visited_blue_nodes = {0}

        current_red_nodes = deque(red_edge_adjacency_matrix.get(0, set([])))
        current_blue_nodes = deque(blue_edge_adjacency_matrix.get(0, set([])))

        while 0 != len(current_red_nodes) or 0 != len(current_blue_nodes):
            count += 1

            next_red_nodes = deque()
            next_blue_nodes = deque()

            while 0 != len(current_red_nodes):
                current_red_node = current_red_nodes.popleft()

                if current_red_node not in visited_red_nodes:
                    if current_red_node not in visited_blue_nodes:
                        counts[current_red_node] = count

                    for next_blue_node in blue_edge_adjacency_matrix.get(current_red_node, set([])):
                        next_blue_nodes.append(next_blue_node)

                    visited_red_nodes.add(current_red_node)

            while 0 != len(current_blue_nodes):
                current_blue_node = current_blue_nodes.popleft()

                if current_blue_node not in visited_blue_nodes:
                    if current_blue_node not in visited_red_nodes:
                        counts[current_blue_node] = count

                    for next_red_node in red_edge_adjacency_matrix.get(current_blue_node, set([])):
                        next_red_nodes.append(next_red_node)

                    visited_blue_nodes.add(current_blue_node)

            current_red_nodes = next_red_nodes
            current_blue_nodes = next_blue_nodes

        return counts
