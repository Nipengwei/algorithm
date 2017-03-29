# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pHead_reverse = None
        pNode = pHead
        pPrev = None
        while pNode:
            pNext = pNode.next
            if not pNext:
                pHead_reverse = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pHead_reverse