//
// Created by bright on 2022/1/24.
/* Demo Description: */

#include <iostream>
#include <vector>

using namespace std;

// recursion
int calcWays(int n) {
    if (n == 0 || n == 1)
        return n;

    return calcWays(n - 1) + calcWays(n - 2);
}

// memo
int calcWays_memo_helper(int n, vector<int> memo) {
    if (n == 0 || n == 1)
        return n;

    if (memo[n] == -1)
        memo[n] = memo[n - 1] + memo[n - 2];

    return memo[n];
}

int calcWays_memo(int n) {
    vector<int> memo(n + 1, -1);

    return calcWays_memo_helper(n, memo);
}

// dynamic program
int climbStairs_dyn(int n) {
    vector<int> memo(n + 1, -1);

    memo[0] = 0;
    memo[1] = 1;

    for (int i = 0; i < n + 1; i++) {
        memo[n] = memo[n - 1] + memo[n - 2];
    }

    return memo[n];
}
