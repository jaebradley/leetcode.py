"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        character_counts = [0] * 26
        for c in s:
            character_index = ord(c) - ord('a')
            character_counts[character_index] += 1

        for c in t:
            character_index = ord(c) - ord('a')
            character_counts[character_index] -= 1

        return min(character_counts) == 0 and max(character_counts) == 0
