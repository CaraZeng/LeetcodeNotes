"""
2563. Count the Number of Fair Pairs
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
"""

# Key Note:
# 1. use one binary search func to handle both lower and upper
# 2. for this one, we need to find the last element slightly
# smaller than target, then we can use it for lower and + 1
# for upper.
# 3. l should be i + 1 because we are tring to find num to
# pair with i

class Solution:
    def binSearch(self, nums, l, r, target):
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        return r
    
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            low = lower - nums[i]
            upp = upper - nums[i]
            res += self.binSearch(nums, i + 1, len(nums) - 1, upp + 1) - self.binSearch(nums, i + 1, len(nums) - 1, low)
        return res