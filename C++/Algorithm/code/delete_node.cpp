//
// Created by bright on 2022/1/11.
/* Demo Description: */

#include <iostream>

// 通过 当前节点进行删除
void deleteNode(ListNode* node) {
    if (node == nullptr)
        return;

    if (node->next == nullptr) {
        delete node;
        node = nullptr;
        return;
    }

    node->val = node->next->val;
    ListNode* delNode = node->next;
    node->next = delNode->next;
    delete delNode;

    return;
}

