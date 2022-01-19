//
// Created by bright on 2022/1/19.
/* Demo Description: */

#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> res;
vector<bool> used; // 筛选元素

void generatePermutation(const vector<int> &nums, int index, vector<int> &p) {
    if (index == nums.size()) {
        res.push_back(p);
        return;
    }

    for (int i = 0; i < nums.size(); i++) {
        if (!used[i]) {
            used[i] = true;
            p.push_back(nums[i])
            generatePermutation(nums, index + 1, p);
            used[i] = false;
            p.pop_back();
        }
    }

    return;
}

vector<vector<int>> permute(vector<int> &nums) {
    res.clear();

    if (nums.size() == 0)
        return res;

    used = vector<bool>(nums.size, false);
    vector<int> p;
    generatePermutation(nums, 0, p);

    return res;
}