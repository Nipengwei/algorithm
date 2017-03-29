# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1 and not pHead2:
            return None
        elif not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        
        if pHead1.val < pHead2.val:
            pHead_merge = pHead1
            pHead_merge.next = self.Merge(pHead1.next, pHead2)
        else:
            pHead_merge = pHead2
            pHead_merge.next = self.Merge(pHead1, pHead2.next)
        return pHead_merge