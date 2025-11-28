"""
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

# Key Note:
# 1. None for now

class Solution:
    def substring(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
    def longestPalindrome(self, s: str) -> str:
        max_substring = ""
        for i in range(len(s)):
            s1 = self.substring(s, i, i)
            s2 = self.substring(s, i, i + 1)
            if len(s1) >= len(s2) and len(s1) > len(max_substring):
                max_substring = s1
            elif len(s2) > len(max_substring):
                max_substring = s2
        return max_substring