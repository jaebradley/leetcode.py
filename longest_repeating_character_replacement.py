"""
https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        Since we are only interested in the longest valid substring, our sliding windows need not shrink, even if a
        window may cover an invalid substring. We either grow the window by appending one char on the right, or shift
        the whole window to the right by one. And we only grow the window when the count of the new char exceeds the
        historical max count (from a previous window that covers a valid substring).

        That is, we do not need the accurate max count of the current window; we only care if the max count exceeds the
        historical max count; and that can only happen because of the new char.

        :type s: str
        :type k: int
        :rtype: int
        """

        max_length = 0
        start_index = 0
        end_index = 0
        max_count = 0
        uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        character_counts = dict((character, 0) for character in uppercase_letters)

        while end_index < len(s):
            character = s[end_index]
            # Increment character counts to take into account current character
            character_count = character_counts[character] + 1

            max_count = max(max_count, character_count)

            # If the number of non-max character counts are greater than the total number of operations
            # start closing window by incrementing start index and removing character counts.
            while end_index - start_index + 1 - max_count > k:
                character_counts[character] -= 1
                start_index += 1

            end_index += 1
            max_length = max(max_length, end_index - start_index + 1)

        return max_length
