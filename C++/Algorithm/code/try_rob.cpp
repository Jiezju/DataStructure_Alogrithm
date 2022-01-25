//
// Created by bright on 2022/1/25.
/* Demo Description: */

#include <iostream>

using namespace std;

// 抢劫 第 index 间 房子
int tryRob_helper(vector<int>& nums, int index) {
    if (index >= nums.size())
        return 0;

    int res = 0;
    for (int i=index; i<nums.size(); i++) {
        res = max(res, nums[i] + tryRob_helper(nums, i+2));
    }

    return res;
}

int rob_recursion(vector<int>& nums) {
    return tryRob_helper(nums, 0);
}

// memo
int tryRob_helper(vector<int>& nums, vector<int>& memo, int index) {
    if (index >= nums.size())
        return 0;

    if (memo[index] != -1)
        return memo[index];

    int res = 0;
    for (int i=index; i < nums.size(); i++) {
        res = max(res, nums[i] + tryRob_helper(nums, memo, i + 2));
    }

    memo[index] = res;
    return res;
}

int rob_recursion(vector<int>& nums) {
    vector<int> memo(n, -1);
    return tryRob_helper(nums, memo, 0);
}

// dynamic
int rob(vector<int>& nums) {
    vector<int> dp(n, -1);

    // init 考虑偷取 [i, ... , n-1] 范围里的房子
    dp[n-1] = nums[n-1];
    dp[n-2] = nums[n-2];

    for (int i = n-3; i >=0; i--) {
        for (int j = i; j < n; j++) {
            dp[i] = max(dp[i], nums[j] + (j + 2 < n ? dp[j + 2] : 0));
        }
    }

    return dp[0];
}
