# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Hard

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()

        m = (len(nums1) - 1)/ 2

        if len(nums1) % 2 != 0:
            return nums1[int(m)]
        else:
            a, b = int(m), int(m)+1
            return (nums1[a]+nums1[b])/2