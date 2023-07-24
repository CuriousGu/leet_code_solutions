# https://leetcode.com/problems/remove-element/
# Easy


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0

        for i, _ in enumerate(nums):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index

