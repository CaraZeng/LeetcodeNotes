Step1:
contiguous subarray
 - dp/prefix sums/sliding window
maximum or minimum
 - Kadanes dp

Step2:
brute force
 - enumerate all subarrays, compute their sum/product
 O(n**2) or worse
Can I derive the current best answer using only the previous subarray's info?

Step3:
since the subarray must be contiguous, the best subarray ending at index i
must be either:
1. start fresh with nums[i]
2. entend the previous subarray
For 53:
curr_sum = max(nums[i], curr_sum + nums[i])
For 152:
curr_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
curr_min = max(nums[i], prev_max * nums[i], prev_min * nums[i])

Before code:
1. Is it a subarray problem?
2. Is it contiguous? - Maintain local and global states.
3. What's the operation?
 - Addition: track only the max
 - Multiplication: track both max and min
4. Complexity:
O(n) and O(1)