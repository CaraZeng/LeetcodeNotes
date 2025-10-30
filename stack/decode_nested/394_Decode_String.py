"""
394. Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside
the square brackets is being repeated exactly k times. Note that k is 
guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra
white spaces, square brackets are well-formed, etc. Furthermore, you may
assume that the original data does not contain any digits and that 
digits are only for those repeat numbers, k. For example, there will not
be input like 3a or 2[4].

The test cases are generated so that the length of the output will never
exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 
Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

# Key Note:
# 1. c.isdigit() is just to check if its a int character, like "1", but
# its not 1 the digit
# 2. its basiclly when we meet a [, we use curr to record the items inside
# [, until we meet ], we take out prev and prev num inside stack and calculate
# them use the new curr inside new [], so the curr is updated.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append([curr, num])
                curr = ""
                num = 0
            elif c == ']':
                prev, k = stack.pop()
                curr = prev + curr * k
            else:
                curr += c
        return curr