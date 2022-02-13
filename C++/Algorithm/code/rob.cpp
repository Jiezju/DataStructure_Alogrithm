//
// Created by bright on 2022/2/13.
//

#include <iostream>
#include <vector>

using namespace std;

// 考虑抢劫 [index， n-1] 的房子
int tryRob(vector<int>& nums, int index) {
    if (index > nums.size())
        return 0;

    int res = -1;
    for (int i=index; i<nums.size(); i++) {
        res = max(res, nums[i] + tryRob(nums, i + 2));
    }

    return res;
}