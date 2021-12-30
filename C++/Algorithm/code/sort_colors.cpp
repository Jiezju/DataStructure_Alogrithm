//
// Created by bright on 2021/12/30.
/* Demo Description: sort colors */

#include <iostream>
#include <vector>

using namespace std;

// 计数排序
void sortColors(vector<int>& nums) {
    vector<int> count(3, 0);

    for (auto elem : nums)
        count[ele]++;

    int count = 0;

    for (int i = 0; i < 3; i++) {
        for(int c=0; c<count[i]; c++) {
            nums[count] = i;
            count++;
        }
    }
}

// 三路快排：
// [0,zero] 表示 0 [zero+1, i-1] 表示 1  [two, n-1] 表示 2
void sortColors(vector<int>& nums) {
    int zero = -1;
    int two = nums.size();

    int i = 0;

    while (i<nums.size()-1) {
        if (0 == nums[i]) {
            swap(nums[i], nums[++zero]);
            i++;
        } else if (2 == nums[i])
            swap(nums[i], nums[--two]);
        else
            i++;
    }
}

int main() {

    return 0;
}

