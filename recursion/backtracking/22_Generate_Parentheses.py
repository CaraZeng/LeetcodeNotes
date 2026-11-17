"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8
"""

# Key Note:
# 1. combination of backtracking and parentheses
# 2. notice the rules: left must <= n and right must <= left.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return res
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res