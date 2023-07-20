# https://leetcode.com/problems/fizz-buzz/
# Easy

class Solution:
    def __init__(self):
        self.l = list()

    def fizzBuzz(self, n: int) -> List[str]:
        for x in range(1, n+1):
            if x%3==0 and x%5==0:
                self.l.append("FizzBuzz")
            elif x%3==0:
                self.l.append("Fizz")
            elif x%5==0:
                self.l.append("Buzz")
            else:
                self.l.append(f"{x}")
        
        return self.l