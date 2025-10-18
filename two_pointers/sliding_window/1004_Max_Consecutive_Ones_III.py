"""
1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum 
number of consecutive 1's in the array if you can flip at most k 
0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is 
underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is 
underlined.
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

# Key Note:
# 1. we need to calculate max_number and number while k >= 0, 
# not only k == 0, because
# nums = [1, 1, 0, 1, 1, 1], k = 1
# if we calculate max_number and number only when k == 0, we will
# miss a lot.
# so we should make calculation as a uncondition statement in loop
# and use a if to handle k < 0(that's the special treated part).