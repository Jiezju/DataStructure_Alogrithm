//
// Created by bright on 2022/1/24.
/* Demo Description: */

#include <iostream>
#include <vector>

using namespace std;

// recursion
int fib( int n ) {
    if (n == 0 || n == 1)
        return n;

    return fib(n-1) + fib(n-2);
}

int fib_memo_helper(int n, vector<int> memo) {
    if (n == 0 || n ==1)
        return n;

    if (memo[n] == -1)
        memo[n] = fib(n-1, memo) + fib(n-2, memo);

    return memo[n];
}

int fib_memo(int n) {
    vector<int> memo(n+1, -1);
    return fib_memo_helper(int n, vector<int> memo);
}

int fib_dyn(int n) {
    vector<int> memo(n+1, -1);

    // init
    memo[0] = 0;
    memo[1] = 1;

    // dynamic program
    for (int i = 2; i < n + 1; i++)
        memo[i] = memo[i-1] + memo[i-2];

    return memo[n];
}

