"""
912. Sort an Array
Given an array of integers nums, sort the array in ascending order and 
return it.

You must solve the problem without using any built-in functions in 
O(nlog(n)) time complexity and with the smallest space complexity 
possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are 
not changed (for example, 2 and 3), while the positions of other numbers 
are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
 
Constraints:
1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""

# Key Note:
# 1. basically we keep dividing everything into one num, then we merge 
# these two nums, then we merge these two nums with other two nums, and
# we get four nums, then we merge these four nums with other four nums 
# that's also merged at the same time at other places.
# 2. merge should takes one temp array to store the new array, then we use
# mid to start the second part of array.
# notice that start will change(wont always be 0), so when we copy the 
# temp back to nums, nums's index should not start from 0 but start.
# 3. every time k reset to 0, because we not only use it for one time,
# we use it to update current nums we are dealing with(the divided nums)
class Solution:
    def mergeSort(self, nums, start, end, temp):
        if start == end:
            return nums
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid, temp)
        self.mergeSort(nums, mid + 1, end, temp)
        return self.merge(nums, start, mid, end, temp)
    def merge(self, nums, start, mid, end, temp):
        i = start
        j = mid + 1
        k = 0
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1
        while j <= end:
            temp[k] = nums[j]
            j += 1
            k += 1
        for i in range(k):
            nums[start + i] = temp[i]
        return nums
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1, temp)
        return nums
        