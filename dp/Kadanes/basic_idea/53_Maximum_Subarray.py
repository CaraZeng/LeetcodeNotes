"""
53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and 
return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another 
solution using the divide and conquer approach, which is more subtle.
"""

# Key Notes:
# 1. We need to keep tracking of the curr_subarray and max_subarray,
# 2. since we have negative numbers, so the curr_subarray may be 
# negative, in that way, if we iterate to a number that is greater than
# curr_subarray + that number(since curr_subarray way be negative), we
# can just make curr_subarray to be that number(start from it now).
# 3. then we just need to compare curr_array to max_subarray(since we 
# will iterate though many numbers that the curr_subarray might not be
# as big as some old max_subarray)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            max_sum = max(curr, max_sum)
        return max_sum