"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can 
return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to 
form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be 
rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

# Key Note:
# 1. the values of dict is lists.
# 2. we need to count the freqs of chars in each string, then append
# the string to the same freqs of chars's values

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord("a")] += 1
            string_dict[tuple(count)].append(string)
        return list(string_dict.values())