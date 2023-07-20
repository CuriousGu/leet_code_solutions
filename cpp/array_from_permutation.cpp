//https://leetcode.com/problems/build-array-from-permutation/
// Easy

#include <vector>

class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        int len = nums.size();
        vector<int> arr(len, 0);

        for(int i = 0; i < len; i++){
            arr[i] = nums[nums[i]];
        }
        return arr;
    }
};

