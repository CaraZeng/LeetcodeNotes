"""
1456. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters 
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""

# Key Note:
# 1. classic sliding window problem.

vowels = {'a', 'e', 'i', 'o', 'u'}
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        max_count = 0
        left = 0
        for right in range(len(s)):
            if s[right] in vowels:
                count += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    count -= 1
                left += 1
            max_count = max(max_count, count)
        return max_count