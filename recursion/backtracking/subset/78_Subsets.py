"""
78. Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

# Key Note:
# 1. for each num, we can choose to add it or not and keep dfs.

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        sub = []
        def dfs(i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()
            dfs(i + 1)
        dfs(0)
        return res