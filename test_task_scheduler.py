from unittest import TestCase

from task_scheduler import Solution


class TestTaskScheduler(TestCase):
    def test_double_idle_with_two_max_tasks(self):
        self.assertEqual(8, Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))

    def test_double_idle_with_single_max_task(self):
        self.assertEqual(7, Solution().leastInterval(["A", "A", "A", "B", "B"], 2))

    def test_no_idle(self):
        self.assertEqual(5, Solution().leastInterval(["A", "B", "C", "D", "E"], 1))

    def test_zero_cost_idle(self):
        self.assertEqual(6, Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0))

    def test_single_cost_idle_with_two_max_tasks(self):
        self.assertEqual(6, Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 1))
