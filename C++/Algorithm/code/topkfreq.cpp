//
// Created by bright on 2022/1/13.
/* Demo Description: */

#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int,int> freq;

    for (num : nums)
        freq[num]++;

    // 最小堆
    priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int, int>> pq;

    for (auto ele : freq) {
        pq.push(make_pair(ele.second, ele.first));
        if (pq.size() > k)
            pq.pop();
    }

    vector<int> res;

    while (!pq.empty()) {
        res.pop_back(pq.top().second);
        pq.pop();
    }

    return res;
}
