//
// Created by bright on 2021/12/30.
/* Demo Description: sort array two sum */

#include <iostream>
#include <vector>

using namespace std;

// two pointers
vector<int> twoSum_sort(vector<int>& nums, int T) {
    int l = 0;
    int r = nums.size() -  1;
    vector<int> res;
    while(l<=r) {
        if (nums[l] + nums[r] == T) {
            res.push_back(l);
            res.push_back(r);
            return res;
        } else if (nums[l] + nums[r] < T)
            l++;
        else
            r--;
    }
    throw invalid_argument("Error!");
}

int main() {

    return 0;
}

