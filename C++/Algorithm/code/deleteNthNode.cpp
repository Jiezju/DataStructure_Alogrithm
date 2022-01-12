//
// Created by bright on 2022/1/11.
/* Demo Description: */

#include <iostream>

ListNode* removeNthFromEnd(ListNode* head, int n) {
    // 设置 dummpy node 方便定位到 第 n-1 个节点
    ListNode* dummy_node = new ListNode(0);
    dummy_node->next = head;

    ListNode* fp,sp; // first, second
    fp = sp = dummy_node;

    for (int i=0; i< n; i++) {
        if (sp == nullptr)
            return;
        sp = sp->next;
    }

    while (sp != nullptr) {
        fp = fp->next;
        sp = sp->next;
    }

    // 删除第 n 个节点
    ListNode* delNode = p->next;
    p->next = delNode->next;
    delete delNode;

    ListNode* retNode = dummyHead->next;
    delete dummyHead;

    return retNode;
}
