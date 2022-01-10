//
// Created by bright on 2022/1/10.
/* Demo Description: removeElements */

#include <iostream>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// 哨兵节点
ListNode* removeElements(ListNode* head, int val) {
    ListNode* dummy_node = ListNode(0);
    dummy_node->next = head;

    ListNode* cur = dummy_node;

    while (cur) {
        if (cur->next->val == val) {
            ListNode* delNode = cur->next;
            cur->next = cur->next->next;
            delete ListNode;
        } else {
            cur = cur->next;
        }
    }
    // 处理哨兵节点
    ListNode* retNode = dummy_node->next;
    delete dummy_node;
    return retNode;
}

