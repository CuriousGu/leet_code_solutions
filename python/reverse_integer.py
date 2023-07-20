# https://leetcode.com/problems/reverse-integer/
# Medium    

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            rev = str(x)[::-1]
            rev = int(rev)
            return rev if rev < (2**31) - 1 else 0
        
        else:
            rev = str(x)[:0:-1]
            rev = -int(rev)
            return rev if rev > -2**31 else 0