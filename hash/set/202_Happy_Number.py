"""
202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares
of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops 
endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 231 - 1
"""

# Key Note:
# 1. as long as n == 1, we can return true
# 2. to avoid a ifinite loop, we can create a visited set to record the n we been
# to, because if we encounter a num for the second time, the rest of the calculation
# just would be the same as we calculate it before.
# 3. for after calculation each n, we should add it to n and reset the total.

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            total = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                total += digit * digit
            n = total
        return True