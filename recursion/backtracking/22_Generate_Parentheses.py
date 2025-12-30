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
    def backtrack(self, path_list, left, right, n, res):
        if left == n and right == n:
            res.append("".join(path_list))
            return
        if left < n:
            path_list.append('(')
            self.backtrack(path_list, left + 1, right, n, res)
            path_list.pop()
        if right < left:
            path_list.append(')')
            self.backtrack(path_list, left, right + 1, n, res)
            path_list.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path_list = []
        self.backtrack(path_list, 0, 0, n, res)
        return res