//
// Created by bright on 2022/1/5.
/* Demo Description: 两个数组的交集 */

#include <iostream>
#include <set>
#include <map>

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    std::set<int> records;
    for (auto ele : nums1)
        records.insert(ele);

    set<int> result;
    for (auto ele : nums2) {
        if (records.find(ele) != records.end())
            result.insert(ele);
    }

    return vector<int>(result.begin(), result.end());
}

vector<int> intersection2(vector<int>& nums1, vector<int>& nums2) {
    std::map<int, int> records;
    for (auto ele : nums1)
        if (records.find(ele) == records.end())
            records.insert(make_pair(ele, 1));
        else
            records[ele]++;

    vector<int> result;
    for (auto e : nums2) {
        if (records.find(e) != records.end() && records[e] > 0) {
            result.push_back(e);
            records[e]--;
            if (records[e] == 0)
                records.erase(e);
        }
    }

    return result;
}





