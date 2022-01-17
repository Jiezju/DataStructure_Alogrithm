//
// Created by bright on 2022/1/17.
/* Demo Description: */

#include <iostream>

using namespace std;

bool hasPathSum(TreeNode *root, int targetSum) {
    if (root == nullptr)
        return false;

    if (root->left == nullptr && root->right == nullptr && root->val == targetSum)
        return true;

    return hasPathSum(root->left, targetSum - root->val) && hasPathSum(root->right, targetSum - root->val);
}
