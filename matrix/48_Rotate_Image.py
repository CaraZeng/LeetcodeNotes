"""
48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

# Key Note:
# 1. we need to transpose + reverse each row(for clockwise 90)
# transpose + reverse each col(for reverse clockwise 90)
# reverse each col and row(for reverse 180)
# 2. transpose is just (i, j) = (j, i)
# reverse each row is (j, i) = (j, n - 1 - i)
# so we can just (i, j) = (j, n - 1 - i)
# 3. code part:
# for a matrix, we have three part:
# diagonal: i == j
# upper triangle: i < j
# lower triangle: i > j
# so we dont need to reverse diagonal
# and we swap upper triangle and lower triangle
# since j > i means upper triangle and we only want to do with upper triangle, 
# so we begin j at i + 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()