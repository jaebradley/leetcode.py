"""
https://leetcode.com/problems/task-scheduler/

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters
represent different tasks. Tasks could be done without original order.

Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n
intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        There have to be n + 1 intervals between the most common tasks.

        So if there are K greatest task counts, there are (K - 1) x (n + 1) intervals (can put the last most common task
        at the end.

        Need to add the number of tasks that share the number of most common tasks as it'll be the number to "task" on
        to the end.

        Imagine example as ["A", "A", "A", "B", "B"]. The answer would be A -> B -> idle -> A -> B -> idle -> A.
        Note the missing "B" at the end. This is because "B" is no longer tied for longest and won't take up space at
        end.

        So formula is something like (max_task_count - 1) x (n + 1) + most_common_tasks.

        Final thing is that the minimum interval is the number of tasks. So have to take the max of the formula and the
        length of the given tasks.

        This is because the formula could calculate a value that's less than the length of the tasks (like when n is 0).

        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        counts = {}
        for task in tasks:
            if task in counts:
                counts[task] += 1
            else:
                counts[task] = 1

        max_count = max(counts.values())
        most_common_tasks = 0
        for key, value in counts.items():
            if value == max_count:
                most_common_tasks += 1

        return max(len(tasks), (max_count - 1) * (n + 1) + most_common_tasks)
