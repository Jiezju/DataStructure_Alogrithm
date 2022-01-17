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

TreeNode* invertTree(TreeNode* root) {
    if (root == nullptr)
        return root;

    invertTree(root->left);
    invertTree(root->right);

    swap(root->left->val, root->right->val);

    return root;
}

