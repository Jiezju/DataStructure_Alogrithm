//
// Created by bright on 2022/1/10.
/* Demo Description: swapPairs */

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

ListNode* swapPairs(ListNode* head) {
    ListNode* dummyNode = ListNode(0);
    dummyNode->next = head;

    ListNode* p = dummyNode;

    while (p->next && p->next->next) {
        // 存储中间节点
        ListNode* node1 = p->next;
        ListNode* node2 = node1->next;
        ListNode* next = node2->next;

        // 反转
        node2->next = node1;
        node1->next = next;
        p->next = node2;

        p = node1;
    }

    // 处理哨兵节点
    ListNode* retNode = dummy_node->next;
    delete dummy_node;
    return retNode;
}

