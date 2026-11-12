"""
1249. Minimum Remove to Make Valid Parentheses
Medium
Topics
premium lock icon
Companies
Hint
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
"""

# Key Note:
# 1. dont need to keep left_count 0, can use it to skip (
# when forming string
# 2. When forming string, do it backwards cause the
# left parentness in the end is the most needed to
# cut off.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        left_count = 0
        for c in s:
            if c == "(":
                stack.append(c)
                left_count += 1
            elif c == ")" and left_count > 0:
                stack.append(c)
                left_count -= 1
            elif c != ")":
                stack.append(c)
        
        filtered = []
        for c in reversed(stack):
            if c == "(" and left_count > 0:
                left_count -= 1
            else:
                filtered.append(c)
        return "".join(reversed(filtered))