"""
1567. Maximum Length of Subarray With Positive Product
Given an array of integers nums, find the maximum length of a subarray 
where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values 
taken out of that array.

Return the maximum length of a subarray with positive product.

Example 1:
Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Example 2:
Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which
has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the 
product 0 which is not positive.

Example 3:
Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or 
[-2,-3].
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
# KEY NOTE:
# 1. a little similar to 152 because sign tracking. but dont need to 
# actually count.
# 2. three situations:
# if pos, we add 1 to both pos and neg
# if neg, we swap pos and neg, then both add
# if 0, reset to 0
# The POINT is we need to check whether neg is 0:
# if neg > 0 's purpose is not to see if its < 0, it would never be neg in
# this problem, only 0 or pos, but if its 0, that means there is no neg
# before, and we cant do anything to neg because
# if is pos and there was no neg before, neg wont grow, only if there was
# neg, neg * pos, neg will grow
# if is neg, pos * this would be new neg, and new pos would be old neg *
# this neg, and if there are no old neg at all, 0 * neg would be 0, so
# the new pos should be 0
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 1 if nums[0] > 0 else 0
        neg = 1 if nums[0] < 0 else 0
        ans = pos
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos += 1
                neg += 1 if neg > 0 else 0
            elif nums[i] < 0:
                new_pos = neg + 1 if neg > 0 else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)
        return ans