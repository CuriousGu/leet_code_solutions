# https://leetcode.com/problems/buddy-strings/
# Easy

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        i = 0 
        d_change = {}
        while i < len(s):
            if s[i] != goal[i]:
                new_index = goal.find(s[i])
                d_change[i] = goal[new_index]
            i += 1
        

        if s == goal: return True
        else: return False 

a = Solution().buddyStrings("ab", "ba")
print(a)