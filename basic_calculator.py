"""
https://leetcode.com/problems/basic-calculator/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution(object):
    def calculate(self, s):
        """
        Keep track of the signs in a Stack.

        Iterate through all characters in the string.

        If character is a digit, need to get all digits in number if it's more than one digit long.
        Once entire number is identified, pop last sign and multiply by number and add it to total sum.

        If character is the plus sign or an open parenthesis, add the last sign to the stack of signs.
        Idea is that when expression wrapped by parentheses, each addition operation (as well as the first value in
        the expression) will reflect the sign preceding the expression.

        If character is the negative sign, the next sign will be the opposite of the last sign.

        If a closed parenthesis is identified, pop the last sign (which would the sign preceding the expression).

        Increment the index to ensure looping through characters in string.
        :type s: str
        :rtype: int
        """
        sum = 0
        index = 0
        signs = [1, 1]

        while index < len(s):
            c = s[index]

            if c.isdigit():
                end_index = index
                while end_index < len(s) and s[end_index].isdigit():
                    end_index += 1
                sum += signs.pop() * int(s[index:end_index])
                index = end_index - 1
            elif c == "+" or c == "(":
                signs.append(signs[-1])
            elif c == "-":
                signs.append(-signs[-1])
            elif c == ")":
                signs.pop()

            index += 1

        return sum
