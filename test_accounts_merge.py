from unittest import TestCase

from accounts_merge import Solution


class TestAccountsMerge(TestCase):
    def test_account_merging(self):
        merged_accounts = Solution().accountsMerge(
            [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
             ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
        )
        self.assertTrue(["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'] in merged_accounts)
        self.assertTrue(["John", "johnnybravo@mail.com"] in merged_accounts)
        self.assertTrue(["Mary", "mary@mail.com"] in merged_accounts)