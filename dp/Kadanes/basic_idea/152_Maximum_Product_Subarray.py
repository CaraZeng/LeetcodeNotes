"""
152. Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit 
integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit 
integer.
"""
# Key Notes:
# 1. since there will be negative numbers, we need to also track the 
# curr_min because curr_min * a negative number, it might be curr_max.
# 2. so basically we need to track curr_max and curr_min, after each 
# iteration, update curr_max to ans.
# 3. before we calculate curr_max in each iteration, we should record
# curr_max incase we lost it and use the new curr_max to claculate 
# curr_min, it would be wrong, the calculation of curr_max and curr_min
# should be calculate using the same curr_max.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = ans = nums[0]
        for i in range(1, len(nums)):
            prev_max = curr_max
            prev_min = curr_min
            curr_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            curr_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])
            ans = max(ans, curr_max)
        return ans