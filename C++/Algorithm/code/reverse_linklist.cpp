//
// Created by bright on 2022/1/10.
/* Demo Description: reverse link list */

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

ListNode* reverseList(ListNode* head) {
    ListNode* pre = nullptr;
    ListNode* cur = head;
    ListNode* nxt = nullptr;

    while(cur) {
        // 保存中间指针
        nxt = cur->next;
        // 反转
        cur->next = pre;
        // 更新指针
        pre = cur;
        cur = nxt;
    }

    return pre;
}
