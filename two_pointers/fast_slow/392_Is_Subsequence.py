"""
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or 
false otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a 
subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk 
where k >= 109, and you want to check one by one to see if t has its 
subsequence. In this scenario, how would you change your code?
"""

# Key Note:
# 1. slow and fast pointers for two strings perspectively.
# 2. need to handle the length of i, since if all the chars in s are matched,
# i would be exactly == to length, and that's out of index, so we need to out
# of loop.
# 3. Because before we enter the while loop, i within index range, during the
# loop, i exceed index range, but at the same time, loop is illegal, so it ends
# so we will not encounter errors.