"""
https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        When an invalid string is found, some parenthesis in the prefix can be deleted to make the string valid again.
        Use BFS to generate all potential combinations of of these potentially valid strings by removing "(" or ")"
        at various parts of the string.

        Start by adding the initial invalid string to the queue.

        While the queue is not empty process the first element in the queue.

        Check if the element is a valid string by counting the parentheses (can do this by checking the counts, when
        checking the count of ")" need to return False when pair of parentheses starts with ")").

        If the element is invalid, iterate through that string and generate all possible combinations of removing a
        single "(" or ")" character from the string.

        If the generated combination has not been visited (and it's length is not that of the longest max length valid
        string seen) then add it to the visited strings and add it to the queue.
        
        :type s: str
        :rtype: List[str]
        """
        valid_strings = set()
        visited_strings = set()
        queue = [s]
        max_length_valid_string = 0

        while len(queue) > 0:
            next_string = queue.pop(0)

            if self.valid(next_string):
                max_length_valid_string = max(max_length_valid_string, len(next_string))
                valid_strings.add(next_string)
            else:
                for index, c in enumerate(next_string):
                    if c == "(" or c == ")":
                        candidate_string = next_string[:index] + next_string[index + 1:]
                        if candidate_string not in visited_strings and len(candidate_string) >= max_length_valid_string:
                            visited_strings.add(candidate_string)
                            queue.append(candidate_string)

        return list(valid_strings)

    def valid(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    return False

        return count == 0
