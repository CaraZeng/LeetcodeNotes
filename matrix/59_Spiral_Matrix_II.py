"""
59. Spiral Matrix II
Given a positive integer n, generate an n x n matrix filled with elements from 1
to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
 
Constraints:
1 <= n <= 20
"""

# Key Note:
# 1. for _ in range(n) means do the for loops for n time and if we dont need to
# actually use i, we can just _

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom, left, right = 0, n - 1, 0, n - 1
        nums = [[0] * n for _ in range(n)]
        count = 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                nums[top][j] = count
                count += 1
            top += 1
            for i in range(top, bottom + 1):
                nums[i][right] = count
                count += 1
            right -= 1
            for j in range(right, left - 1, -1):
                nums[bottom][j] = count
                count += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                nums[i][left] = count
                count += 1
            left += 1
        return nums