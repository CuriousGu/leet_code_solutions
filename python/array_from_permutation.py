# https://leetcode.com/problems/build-array-from-permutation/
# Easy

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        final = list()
        for value in nums:
            final.append(nums[value])
        
        return final
