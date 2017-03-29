# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if (not pHead) or (not pHead.next):
            return pHead
        else:
            pHead_reverse = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return pHead_reverse