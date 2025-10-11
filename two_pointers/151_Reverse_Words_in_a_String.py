"""
151. Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be 
separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two 
words. The returned string should only have a single space separating the words. 
Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 
Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it 
in-place with O(1) extra space?
"""

# Key Note:
# 1. we can reverse them in place.
# 2. we can write the reverse function by ourselves so we can reverse each single
# word, because we can control the left and right pointer.
# 3. so this question is bacially we reverse the whole string and skip single multiply spaces,
# then we reverse each word separately.

class Solution:
    def reverseWord(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s.reverse()
        fast = 0
        result = ""
        while fast < len(s):
            if s[fast] != " ":
                if len(result) != 0:
                    result += " "
                while fast < len(s) and s[fast] != " ":
                    result += s[fast]
                    fast += 1
            else:
                fast += 1
        
        result = list(result)
        slow = 0
        fast = 0
        while fast <= len(result):
            if fast == len(result) or result[fast] == " ":
                self.reverseWord(result, slow, fast - 1)
                slow = fast + 1
            fast += 1
        return "".join(result)

