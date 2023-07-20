# https://leetcode.com/problems/ransom-note/
# Easy

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        b, a = list(magazine), list(ransomNote)

        for element in a:
            try:
                b.remove(element)
            except:
                return False
        
        return True
