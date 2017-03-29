# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k == 0:
            return None
        first = head
        second = head
        for i in range(k-1):
            if first.next:
                first = first.next
            else:
                return None
        while first.next:
            first = first.next
            second = second.next
        return second