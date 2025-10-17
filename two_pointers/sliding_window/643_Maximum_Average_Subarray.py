"""
643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum 
average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
 
Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

# Key Note:
# 1. we cant use if and elif here, because if and elif will excute one of them,
# but if we use if and if, after first if, the length might just be k, so we need
# to excute second if too.
# 2. we can also use while and if too, but for this problem, if we enter while
# it will actually excute once, so using if just fine.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        total = 0
        max_total = float('-inf')
        for right in range(len(nums)):
            total += nums[right]
            if right - left + 1 > k:
                total -= nums[left]
                left += 1
            if right - left + 1 == k:
                max_total = max(max_total, total)
        return max_total / k