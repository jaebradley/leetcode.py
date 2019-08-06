from unittest import TestCase


from rotate_array import Solution


class TestNoOrbit(TestCase):
    def test_single_step(self):
        values = [1, 2, 3, 4, 5]
        Solution().rotate(values, 1)
        self.assertEqual([5, 1, 2, 3, 4], values)

    def test_two_steps(self):
        values = [1, 2, 3, 4, 5]
        Solution().rotate(values, 2)
        self.assertEqual([4, 5, 1, 2, 3], values)


class TestSingleOrbit(TestCase):
    def test_single_step(self):
        values = [1, 2, 3, 4, 5]
        Solution().rotate(values, 6)
        self.assertEqual([5, 1, 2, 3, 4], values)

    def test_two_steps(self):
        values = [1, 2, 3, 4, 5]
        Solution().rotate(values, 7)
        self.assertEqual([4, 5, 1, 2, 3], values)
