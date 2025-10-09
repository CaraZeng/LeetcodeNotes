"""
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

# Key Note:
# 1. count the freq of c in ransom note and iterate though magazine to subtract c
# in ransom note, if the len(note_dict) == 0 that means all the elements has been
# delete.
# 2. we dont need to worry about the note_dict[c] value to be NEGATIVE, since once
# it reach 0, we delete it, and since we delete it, we can find c in note_dict,
# so its no chance to be NEGATIVE.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_dict = defaultdict(int)
        for c in ransomNote:
            note_dict[c] += 1
        for c in magazine:
            if c in note_dict:
                note_dict[c] -= 1
                if note_dict[c] == 0:
                    del note_dict[c]
        return len(note_dict) == 0