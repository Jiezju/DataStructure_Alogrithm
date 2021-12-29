//
// Created by bright on 2021/12/29.
/* Demo Description: */

#ifndef ALGORITHM_UTILS_H
#define ALGORITHM_UTILS_H

#include <iostream>
#include <cmath>
#include <cassert>

int *generateRandomArray(int n, int rangeL, int rangeR) {

    assert(n > 0 && rangeL <= rangeR);

    int *arr = new int[n];

    srand(time(NULL));
    for (int i = 0; i < n; i++)
        arr[i] = rand() % (rangeR - rangeL + 1) + rangeL;
    return arr;
}

int *generateOrderedArray(int n) {

    assert(n > 0);

    int *arr = new int[n];
    for (int i = 0; i < n; i++)
        arr[i] = i;
    return arr;
}

#endif //ALGORITHM_UTILS_H
