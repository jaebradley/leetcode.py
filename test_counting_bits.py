from unittest import TestCase

from counting_bits import Solution


class TestCountingBits(TestCase):
    def test_zero_is_zero(self):
        self.assertEqual([0], Solution().countBits(0))

    def test_one_is_one(self):
        self.assertEqual([0, 1], Solution().countBits(1))

    def test_two(self):
        self.assertEqual([0, 1, 1], Solution().countBits(2))

    def test_three(self):
        self.assertEqual([0, 1, 1, 2], Solution().countBits(3))

    def test_ten(self):
        self.assertEqual([0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2], Solution().countBits(10))
