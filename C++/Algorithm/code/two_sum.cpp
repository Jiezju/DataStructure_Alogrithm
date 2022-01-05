//
// Created by bright on 2022/1/5.
/* Demo Description: 乱序数组的两数之和 */

#include <iostream>
#include <map>
#include <vector>

vector<int> twoSum(vector<int>& nums, int target) {

    std::map<int, int> records;

    std::vector<int> res(2);
    for (int i=0; i<nums.size(); ++i) {
        if (records.find(nums[i]) != records.end()) {
            res[0] = i;
            res[1] = records[nums[i]];
        } else {
            records[nums[i]] = i;
        }
    }

    return res;
}


