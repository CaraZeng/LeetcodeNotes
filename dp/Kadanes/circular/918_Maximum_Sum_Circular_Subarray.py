"""
918. Maximum Sum Circular Subarray
Given a circular integer array nums of length n, return the maximum 
possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of 
the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and 
the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most 
once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there 
does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.

Constraints:
n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""

# Key Notes:
# 1. we need to use kadane to calculate the max and min sum, the answer
# would be max(max_sum, total_sum - min_sum), because its a circle, so 
# total_sum - min_sum would be the max_sum if it involves with numbers
# across tail and head.
# 2. to get the min_sum, we can calculate the neg_max_sum, then * -1.
# 3. If all numbers are negative, just return max_sum, no need for 
# min_sum calculation because if all numbers are negative, total_sum - 
# min_sum would == 0(cross the whole nums), it would override max_sum
# (the most greatest negative numbers).
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            curr_sum = max_sum = nums[0]
            for i in range(1, len(nums)):
                curr_sum = max(curr_sum + nums[i], nums[i])
                max_sum = max(curr_sum, max_sum)
            return max_sum

        max_sum = kadane(nums)
        
        if max_sum < 0:
            return max_sum
        neg_nums = [-x for x in nums]
        neg_max_sum = kadane(neg_nums)
        min_sum = -1 * neg_max_sum

        total_sum = sum(nums)
        return max(max_sum, total_sum - min_sum)