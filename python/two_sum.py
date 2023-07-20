# https://leetcode.com/problems/two-sum/
# Easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            dif = target - v
            if dif in nums and nums.index(dif) != i:
                return i, nums.index(dif)
