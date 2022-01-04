//
// Created by bright on 2022/1/4.
/* Demo Description: */

#include <iostream>
#include <string>

int lengthOfLongestSubstring(string s) {
    int i = 0;
    int j = -1;
    // 词频率统计
    int freq[256] = {0};
    int n = s.size();
    int res = 0;

    while (i < n) {
        if (j + 1 < n && freq[s[j + 1]] == 0) {
            j++;
            freq[s[j]] += 1;
        } else {
            freq[s[i]]--;
            i++;
        }

        res = std::max(res, j - i + 1);
    }

    return res;
}
