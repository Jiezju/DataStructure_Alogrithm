//
// Created by bright on 2022/1/19.
/* Demo Description: */

#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> res;

void generateCombinations(int n, int k, int start, vector<int> &c) {
    if (c.size() == k) {
        res.push_back(c);
        return;
    }

    for (int i = start; i <= n; i++) {
        c.push_back(i);
        generateCombinations(n, k, i + 1, c);
        c.pop_back();
    }

    return;
}

vector<vector<int>> combine(int n, int k) {
    res.clear();

    if (n <= 0 || k <= 0 || k > n)
        return res;

    vector<int> c;
    generateCombinations(n, k, 1, c);
    return res;
}

