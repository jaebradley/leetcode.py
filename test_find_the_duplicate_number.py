from unittest import TestCase


from find_the_duplicate_number import Solution


class TestFindingDuplicate(TestCase):
    def test_single_duplicate(self):
        self.assertEqual(2, Solution().findDuplicate([1, 3, 4, 2, 2]))

    def test_multiple_duplicates(self):
        self.assertEqual(2, Solution().findDuplicate([1, 3, 2, 4, 2, 2]))

    def test_only_duplicates(self):
        self.assertEqual(2, Solution().findDuplicate([2, 2, 2, 2, 2, 2]))
