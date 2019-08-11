"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity
O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        Keep track of counts of characters in T - this is used to understand what characters are needed.
        Also keep track of how many characters are missing.

        Starting from beginning of S, expand string until have a string that contains all characters in string T.
        This means need to keep track that all characters in T have at least a 0 count and that characters needed
        is 0 (both are needed in case come across duplicate character that has already been fulfilled but missing
        count for one character that hasn't been fulfilled).

        Remove characters from start of substring until invalid.

        Then add characters from end of substring until valid.

        Continue until end of string.
        :type s: str
        :type t: str
        :rtype: str
        """

        character_counts = {}
        for c in t:
            if c in character_counts:
                character_counts[c] += 1
            else:
                character_counts[c] = 1

        characters_needed = len(t)

        start_index = 0
        end_index = 0

        window_start_index = 0
        for window_end_index, c in enumerate(s, 1):
            if c in character_counts:
                if character_counts[c] > 0:
                    characters_needed -= 1
                character_counts[c] -= 1

            if characters_needed == 0:
                while (s[window_start_index] not in character_counts or character_counts[s[window_start_index]] < 0) \
                        and window_start_index < window_end_index:
                    window_start_character = s[window_start_index]
                    if window_start_character in character_counts:
                        character_counts[window_start_character] += 1
                    window_start_index += 1

                if end_index == 0 or window_end_index - window_start_index <= end_index - start_index:
                    start_index, end_index = window_start_index, window_end_index

        return s[start_index:end_index]
