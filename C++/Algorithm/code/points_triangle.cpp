//
// Created by bright on 2022/1/5.
/* Demo Description: */

#include <iostream>
#include <vector>
#include <map>

using namespace std;

int numberOfBoomerangs(vector<vector<int>>& points) {
    int res = 0;
    map<int, int> record;

    for (int i=0; i<points.size(); ++i)
        for (int j=0;; j<points.size(); ++j)
            if (i != j) {
                record[dis(points[i], points[j])]++;
            }

    for (auto ele : record)
        res += record[ele] * record[ele] - 1;

    return res;
}

