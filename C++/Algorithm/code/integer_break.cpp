//
// Created by bright on 2022/1/24.
/* Demo Description: */

#include <iostream>

using namespace std;

int max3(int a, int b, int c) {
    return max(a, max(b, c));
}

// recursion 将n进行分割(至少分割两部分), 可以获得的最大乘积
int breakInteger_recursion(int n) {
    if (n == 1)
        return n;

    int res = -1;
    for (int i = 1; i < n; i++)
        // i * (n - i):  n - i 不分割的场景
        res = max3(res, i * (n - i), i * breakInteger(n - i));

    return res;
}

// memo
int breakInteger_memo(int n, vector<int> memo) {
    if (n == 1)
        return 1;

    if (memo[n] != -1)
        return memo[n];

    int res = -1;
    for (int i = 1; i < n; i++)
        res = max3(res, i * (n-i), i * breakInteger_memo(n-i, memo));

    memo[n] = res;

    return res;
}

// dyn
int breakInteger_dyn(int n, vector<int> dp) {
    dp[1] = 1;

    for (int i = 2; i < n; i++) {
        for (int j = 1; j < i; j++)
            dp[j] = max3(dp[j],  i * (i-j), i * dp[i-j]);
    }

    return dp[n];
}
