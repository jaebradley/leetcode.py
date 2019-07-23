"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Iterate through string.
        Keep two pointers - one to keep track of start index and one to keep track of current index.
        These pointers are used to measure max length.
        Keep track of character locations.
        If character exists in character mapping, set the start index to max of existing start index value or previous
        character location + 1 (to get to right of character).
        Calculate max length by taking the max of existing max length or current index - start index + 1.

        Runtime: O(n) since need to iterate through entire string
        Memory: O(n) worst-case since could store all characters in memory
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        character_locations = {}
        max_length = 0
        start_index = 0

        for index, character in enumerate(s):
            if character in character_locations:
                start_index = max(start_index, character_locations[character] + 1)

            character_locations[character] = index
            max_length = max(max_length, index - start_index + 1)

        return max_length
