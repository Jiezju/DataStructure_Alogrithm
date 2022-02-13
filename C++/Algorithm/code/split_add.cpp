//
// Created by bright on 2022/2/13.
//

#include <iostream>

using namespace std;

// 将n进行分割(至少分割两部分), 可以获得的最大乘积
int breakInteger(int n) {
    // teminal
    if (n == 1)
        return 1;

    int res = -1;
    for (int i=1; i<n; i++) {
        res = max(res, max(i * (n-i), i * breakInteger(n-i)));
    }

    return res;
}