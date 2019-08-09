from unittest import TestCase


from course_schedule import Solution


class TestNoDependencies(TestCase):
    def test_no_dependencies_can_finish(self):
        self.assertTrue(Solution().canFinish(2, []))


class TestSingleDependency(TestCase):
    def test_single_dependency_can_finish(self):
        self.assertTrue(Solution().canFinish(
            2,
            [
                [1, 0],
            ]
        ))


class TestDoubleDependency(TestCase):
    def test_double_dependency_can_finish_when_do_not_depend_on_each_other(self):
        self.assertTrue(Solution().canFinish(
            3,
            [
                [1, 0],
                [2, 0],
            ]
        ))

    def test_double_dependency_cannot_finish_when_depend_on_each_other(self):
        self.assertFalse(Solution().canFinish(
            2,
            [
                [1, 0],
                [0, 1],
            ]
        ))

    def test_double_dependency_can_finish_when_depend_on_two_separate_dependencies(self):
        self.assertTrue(Solution().canFinish(
            3,
            [
                [0, 1],
                [1, 2],
            ]
        ))


class TestTripleDependency(TestCase):
    def test_triple_dependency_cannot_finish_when_all_three_depend_on_each_other(self):
        self.assertFalse(Solution().canFinish(
            3,
            [
                [0, 1],
                [1, 2],
                [2, 0],
            ]
        ))
