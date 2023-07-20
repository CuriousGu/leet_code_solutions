# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Medium 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = ''
        b = c = 0

        while len(s) > c:
            if s[c] not in r:
                r += s[c]
                c += 1
            else:
                b = len(r) if len(r) > b else b
                i = r.index(s[c])
                r = r[i+1:] + s[c]
                c += 1
        b = len(r) if len(r) > b else b

        return b