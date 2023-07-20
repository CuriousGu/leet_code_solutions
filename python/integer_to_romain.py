# https://leetcode.com/problems/integer-to-roman/
# Medium

class Solution:
    def intToRoman(self, num: int) -> str:

        va = {
            1000: "M", 500: "D",
            100: "C",  50: "L",
            10: "X", 5: "V", 1: "I"
            }

        sol = ""
        num = str(num)
        s, c = 0, 0

        while c <= len(num) - 1:
            n = str(num)[c]
            n = int(n) * 10**(len(num) - 1 - c)

            for y, z in va.items():
                if n%y == 0 and n/y <= 3:
                    sol += z * int(n/y)
                    break
                elif n%y > 0 and n%y <= 3*10**(len(num) - 1 - c) and n/y > 1:
                    sol += z
                    for re, ro in va.items():
                        if re <= n%y:
                            sol += ro * int(n%y/re)
                            break
                    break
                elif n-y == -10**(len(num) - 1 - c):
                    sol += va[y-n] + z
                    break

            c += 1

        return sol