//
// Created by bright on 2021/12/29.
/* Demo Description: */

#include <iostream>

// 保持 [0,k) 区间 非 0
void moveZeroes(vector<int>& nums) {
    int k = 0; // 保证区间为 空

    for (int i=0; i< nums.size(); ++i)
        if (nums[i]) {
            nums[k] = nums[i];
            k++;
        }

    for (int i=k; i<nums.size(); ++i)
        nums[i] = 0;
}

// 交换 代替赋值
void moveZeroes2(vector<int>& nums) {
    int k = 0; // 保证区间为 空

    for (int i=0; i< nums.size(); ++i)
        // 第一次进入  nums[i] 不为 0，k一定在之前的 0 元素位置上
        if (nums[i]) {
            // 如果全不为 0
            if (i != k) {
                std::swap(nums[k], nums[i]);
                k++;
            }
            else {
                k++;
            }
        }
}

int main() {

    return 0;
}

