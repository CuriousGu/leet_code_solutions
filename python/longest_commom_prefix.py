# https://leetcode.com/problems/longest-common-prefix/
# Easy

import os

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        return os.path.commonprefix(strs)