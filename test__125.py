from unittest import TestCase

from _125 import RecursiveSolution,NonRecursiveSolution


class TestSolution(TestCase):
    def test_is_palindrome(self):
        self.assertTrue(RecursiveSolution().isPalindrome("a"))
        self.assertFalse(RecursiveSolution().isPalindrome("ab"))
        self.assertTrue(RecursiveSolution().isPalindrome("aa"))
        self.assertTrue(RecursiveSolution().isPalindrome("aba"))
        self.assertFalse(RecursiveSolution().isPalindrome("abab"))
        self.assertTrue(RecursiveSolution().isPalindrome("abba"))
        self.assertTrue(RecursiveSolution().isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(RecursiveSolution().isPalindrome("race a car"))
        self.assertTrue(NonRecursiveSolution().isPalindrome("a"))
        self.assertFalse(NonRecursiveSolution().isPalindrome("ab"))
        self.assertTrue(NonRecursiveSolution().isPalindrome("aa"))
        self.assertTrue(NonRecursiveSolution().isPalindrome("aba"))
        self.assertFalse(NonRecursiveSolution().isPalindrome("abab"))
        self.assertTrue(NonRecursiveSolution().isPalindrome("abba"))
        self.assertTrue(NonRecursiveSolution().isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(NonRecursiveSolution().isPalindrome("race a car"))
