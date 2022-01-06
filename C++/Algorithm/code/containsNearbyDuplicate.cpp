//
// Created by bright on 2022/1/6.
/* Demo Description: */

#include <iostream>
#include <vector>
#include <set>

using namespace std;

// 固定窗口
bool containsNearbyDuplicate(vector<int> &nums, int k) {

    set<int> records;

    int l = 0;
    int n = nums.size();
    for (; l < k; l++)
        if (records.find(nums[l]) == records.end())
            records.insert(nums[l]);
        else
            return true;

    while (l + k + 1 < n) {
        records.erase(nums[l]);
        l += 1;
        if (records.find(nums[l + k + 1]) == records.end())
            records.insert(nums[l + k + 1]);
        else
            return true;
    }
    return false;
}
