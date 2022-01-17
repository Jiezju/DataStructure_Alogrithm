//
// Created by bright on 2022/1/17.
/* Demo Description: */

#include <iostream>

using namespace std;

/// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int maxDepth(TreeNode* root) {
    if ( root == nullptr)
        return 0;

    return max(maxDepth(root->left), maxDepth(root->left) + 1;
}


