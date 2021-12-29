//
// Created by bright on 2021/12/29.
/* Demo Description: binary search */

#include "utils.h"

// binary search 闭区间定义下的搜索
int binarySearch(const int arr[], int n, int T) {
    int l = 0, r = n - 1; // [l,r]

    while (l <= r) {
        int mid = l + (r - l) / 2;

        if (arr[mid] == T)
            return mid;
        else if (arr[mid] < T) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    return -1;
}

int binarySearch2(const int arr[], int n, int T) {
    int l = 0, r = n; // [l,r)

    while (l < r) {
        int mid = l + (r - l) / 2;

        if (arr[mid] == T) {
            return mid;
        }
        else if (arr[mid] < T) {
            r = mid;
        }
        else {
            l = mid + 1;
        }
    }

    return -1;
}


int main() {

    int n = pow(10, 7);
    int* data = generateOrderedArray(n);

    int res1 = binarySearch(data, n, 10);
    int res2 = binarySearch2(data, n, 2);

    std::cout << res1 << std::endl;
    std::cout << res2 << std::endl;

    return 0;
}

