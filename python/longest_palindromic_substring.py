# https://leetcode.com/problems/longest-palindromic-substring/
# Medium

class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        big = ""
        while len(s):
            t = s
            while len(t):
                try:
                    x = len(t) - t[:i:-1].index(t[i]) 
                    if t[i: x][::-1] == t[i: x] and len(t[i:x]) > len(big):
                        big = t[i: x]
                        s = s[i+1:]
                        t = ""
                    else:
                        t = t[:x-1]
                except:
                    r = s
                    s = s[i+1: ]
                    t = ""

        return big if big != "" else r
    