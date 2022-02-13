//
// Created by bright on 2022/2/13.
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<bool> col, dia1, dia2;
vector<vector<string>> res;

void putQueen(vector<vector<int>>& res, index, vector<int> row) {
    if (index == n) {
        res.push_back(row);
        return;
    }

    // 处理 第 index 个皇后，一一遍历
    for (int i=0; i<n; i++) {
        // 放入 queen 的条件
        if (!col[i] && !dia1[index + i] && !dia2[index - i + n - 1]) {
            col[i] = true;
            dia1[index + i] = true;
            dia2[index - i + n - 1] = true;
            row.push_back(i);

            putQueen(res, index + 1, row);

            col[i] = true;
            dia1[index + i] = true;
            dia2[index - i + n - 1] = true;
            row.pop_back();
        }
    }
}

vector<vector<int>> solveNQueens(int n) {
    res.clear();

    col = vector<bool>(n, false);
    dia1 = vector<bool>(2*n-1, false);
    dia2 = vector<bool>(2*n-1, true);

    vector<int> row;

    putQueen(res, 0, row);

    return res;
}