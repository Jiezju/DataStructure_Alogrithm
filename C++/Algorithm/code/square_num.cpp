//
// Created by bright on 2022/1/13.
/* Demo Description: */

#include <iostream>
#include <queue>

using namespace std;

int numSquares(int n) {
    // 第一个 int 表示 数值， 第二个 int 表示 step （经过step 到达 0）
    queue<pair<int, int>> q;
    q.push(make_pair(n, 0));
    vector<bool> visited(n + 1, false);
    visited[n] = true;

    while (!q.empty()) {
        int num = q.front().first;
        int step = q.front().second;
        q.pop();

        if (num == 0)
            return step;

        // bfs
        for (int i = 0; n - i * i > 0; i++) {
            if (!visited[n - i*i]) {
                q.push(make_pair(n - i*i, step + 1));
                visited[n - i*i] = true;
            }
        }
    }
}
