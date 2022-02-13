//
// Created by bright on 2022/2/13.
//

#include <iostream>

// 用 [0...index]的物品,填充容积为c的背包的最大价值
int bestValue(const vector<int> &w, const vector<int> &v, int index, int c) {
    if (index < 0 || c < 0)
        return 0;

    // 不选择 index 物品
    int res = bestValue(w, v, index - 1, c);

    // 选择
    if (c >= w[index]) {
        res = max(res, v[index] + bestvalue(w, v, index - 1, c - w[index]));
    }

    return bestvalue;
}