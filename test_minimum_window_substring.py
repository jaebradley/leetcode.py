from unittest import TestCase

from minimum_window_substring import Solution


class TestMinimumWindowSubstring(TestCase):
    def test_valid_window_at_end(self):
        self.assertEqual(
            "BANC",
            Solution().minWindow("ADOBECODEBANC", "ABC")
        )

    def test_valid_window_at_start(self):
        self.assertEqual(
            "BANC",
            Solution().minWindow("BANCADOBECODE", "ABC")
        )

    def test_invalid_window_where_target_string_greater_than_input_string(self):
        self.assertEqual(
            "",
            Solution().minWindow("A", "AA")
        )
