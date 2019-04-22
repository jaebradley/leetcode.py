"""
https://leetcode.com/problems/word-break/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Store the values of the words at various indices as True or False.

        The only way a word is True is if
        1. It exists as a word in the dictionary
        2. The state of the word at the index preceding the current word is True
           OR it's at the start of the entire word
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        valid_word_indices = [False] * len(s)
        for index in range(len(s)):
            for word in wordDict:
                previous_word_with_identical_length = s[index - len(word) + 1:index + 1]
                state_before_previous_word = valid_word_indices[index - len(word)]
                no_state_before_previous_word = index - len(word) == -1
                if word == previous_word_with_identical_length and (
                        state_before_previous_word is True
                        or no_state_before_previous_word
                ):
                    valid_word_indices[index] = True

        return valid_word_indices[len(s) - 1]
