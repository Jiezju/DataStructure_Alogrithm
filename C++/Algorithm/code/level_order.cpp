//
// Created by bright on 2022/1/12.
/* Demo Description: */

#include <iostream>
#include <stack>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> levelOrder(TreeNode *root) {
    vector<vector<int>> res;

    if (root == nullptr)
        return res;

    queue<TreeNode *, int> q;
    q.push(make_pair(root, 0))

    while (!q.empty()) {
        TreeNode *nod = q.front().first;
        int level = q.front().second;
        q.pop();

        if (level == res.size())
            res.push_back(vector<int>());

        res[level].push_back(nod->val);

        if (nod->left)
            q.push(make_pair(nod->left, level + 1));

        if (nod->right)
            q.push(make_pair(nod->right, level + 1));

    }
    return res;


}
