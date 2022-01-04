//
// Created by bright on 2022/1/4.
/* Demo Description: */

#include <iostream>
#include <vector>

/*
 * 涉及到连续子数组一般采用滑动窗口
 * */

int minSubArrayLen(int s, vector<int>& nums) {
    // define window
    int i = 0;
    int j = 0;
    int sum = nums[0];
    int res = nums.size();

    while (i < nums.size()) {

        // 窗口调节
        if (sum < s && j + 1 < nums.size()) {
            j++;
            sum += nums[j];
        } else {
            sum -= nums[i];
            i++;
        }

        // 保存结果
        if (sum >= T)
            res = std::min(res, j - i + 1);
    }

    if (res == nums.size())
        return 0;

    return res;
}