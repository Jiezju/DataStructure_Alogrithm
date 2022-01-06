//
// Created by bright on 2022/1/6.
/* Demo Description: */

#include <iostream>
#include <set>

using namespace std;

bool containsNearbyAlmostDuplicate(vector<int> &nums, int k, int t) {
    set<int> record;

    for (int i = 0; i < nums.size(); i++) {
        if (record.lower_bound(nums[i] - t) != record.end() && *record.lower_bound(nums[i] - t) <= (nums[i] + t))
            return true;

        record.erase(nums[i]);

        if (record.size() == k + 1)
            record.erase(nums[i - k]);
    }

    return false;
}

