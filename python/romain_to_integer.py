# https://leetcode.com/problems/roman-to-integer/
# Easy

class Solution:
    def __init__(self):
        self.num = {'I':1, 'V':5, 'X':10, 'L':50,'C':100, 'D':500, 'M':1000}
        self.sum = 0
        self.n = 0

    def romanToInt(self, s: str) -> int:     
        while self.n <= len(s) - 1:
            if self.n == len(s) - 1:
                self.sum +=  self.num[s[self.n]]
                self.n += 1
            elif self.num[s[self.n]] >= self.num[s[self.n + 1]]:
                val = self.num[s[self.n]]
                self.sum += val
                self.n += 1
            elif self.num[s[self.n]] < self.num[s[self.n + 1]]:
                val = self.num[s[self.n + 1]] -  self.num[s[self.n]]
                self.sum += val
                self.n += 2

        return self.sum
