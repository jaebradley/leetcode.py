from unittest import TestCase

from jump_game import Solution


class TestJumpGame(TestCase):
    def test_able_to_reach_end(self):
        self.assertTrue(Solution().canJump([2, 3, 1, 1, 4]))

    def test_unable_to_reach_end(self):
        self.assertFalse(Solution().canJump([3, 2, 1, 0, 4]))
