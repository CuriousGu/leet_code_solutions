# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Medium

class Solution:
    def letterCombinations(self, digits: str):
        if not digits: return []
        p = {
            "2": "abc", "3": "def", "4": "ghi",
             "5": "jkl", "6": "mno", "7": "pqrs",
             "8": "tuv", "9": "wxyz"
            }    
        l = [list(p[n]) for n in digits]
        idxs = [0 for _ in enumerate(l)]     
        
        t, poss = 1, 0
        for p in l:
            t *= len(p)
        
        combs = []
        while poss != t:
            poss += 1
            temp = []
            for i, v in enumerate(idxs):
                temp.append(l[i][v])
            temp = "".join(temp)
            combs.append(temp)

            for i, n in enumerate(idxs[::-1]):
                fix_i = (i - len(idxs) + 1) * -1
                if n != len(l[fix_i]) - 1:
                    idxs[fix_i] = n+1
                    idxs = [0 if q > fix_i else k for q, k in enumerate(idxs)]    
                    break
        

        return combs