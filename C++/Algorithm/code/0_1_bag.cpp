//
// Created by bright on 2022/1/25.
/* Demo Description: */

#include <iostream>

using namespace std;

//  recursion
int bestValue(const vector<int> &w, const vector<int> &v, int index, int c) {
    if (c <= 0 || index > v.size())
        return 0;

    int res = bestValue(w, v, index + 1, c);
    if (c >= w[index + 1])
        res = max(res, v[index + 1] + bestValue(w, v, index + 1, c - w[index + 1]));

    return res;
}

int knapsack01(const vector<int> &w, const vector<int> &v, int C){
    assert(w.size() == v.size() && C >= 0);
    int n = w.size();
    if(n == 0 || C == 0)
        return 0;
    return bestValue(w, v, 0, C);
}

// memo
int bestValue(const vector<int> &w, const vector<int> &v, vector<vector<int>>& memo, int index, int c) {
    if (c <= 0 || index > v.size())
        return 0;

    if (memo[index][c] != -1)
        return memo[index][c];

    int res = bestValue(w, v, index + 1, c);
    if (c >= w[index + 1])
        res = max(res, v[index + 1] + bestValue(w, v, index + 1, c - w[index + 1]));

    memo[index][c] = res;

    return res;
}

int knapsack01(const vector<int> &w, const vector<int> &v, int C){
    assert(w.size() == v.size() && C >= 0);
    int n = w.size();
    vector<vector<int>> memo(n, vector<C+1, -1>);
    if(n == 0 || C == 0)
        return 0;
    return bestValue(w, v, memo, 0, C);
}

// dynamic
int knapsack01(const vector<int> &w, const vector<int> &v, int C) {
    assert(w.size() == v.size() && C >= 0);
    int n = w.size();
    if(n == 0 || C == 0)
        return 0;

    vector<vector<int>> memo(n, vector<int>(C+1, -1));

    for (int j =0;j<=C; j++)
        memo[0][j] = j > w[0] ? v[0] : 0;

    for (int i = 1; i<n; i++)
        for (int j = 0; j<=C; j++) {
            memo[i][j] = memo[i-1][j];
            if ( j >= w[i])
                memo[i][j] = max(memo[i][j], v[i] + memo[i - 1][j - w[i]]);
        }

    return memo[n-1][C];
}
