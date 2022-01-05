//
// Created by bright on 2022/1/5.
/* Demo Description: four sum */

#include <iostream>
#include <map>

int fourSumCount(vector<int> &nums1, vector<int> &nums2, vector<int> &nums3, vector<int> &nums4) {
    std::map<int, int> record;

    for (auto ele1: nums1)
        for (auto ele2: nums2)
            record[ele1 + ele2]++;

    int res = 0;

    for (auto ele3 : nums3)
        for (auto ele4 : nums4)
            if (record.find(0 - ele3 - ele4) != record.end())
                res += record[0 - ele3 - ele4];
    return res;
}



