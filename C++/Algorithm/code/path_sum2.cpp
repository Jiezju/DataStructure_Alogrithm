//
// Created by bright on 2022/1/18.
/* Demo Description: */

#include <iostream>

using namespace std;

int findPath(TreeNode* root, int target) {
    if (root == nullptr)
        return 0;

    int res = 0;

    // 不能 return 需要继续向下搜索
    if (root->val == target)
        res += 1;

    res += findPath(root->left, target - root->val);
    res += findPath(root->right, target - root->val);

    return res;
}

// 在以 root 为根节点的二叉树中， 寻找和为 sum 的路径个数
int pathSum(TreeNode* root, int targetSum) {
    if (root == nullptr)
        return 0;

    int res += findPath(root, targetSum);
    res += pathSum(root->left, targetSum);
    res += pathSum(root->right, targetSum);

    return res;
}

