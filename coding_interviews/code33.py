# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        count1 = count2 = 0
        node1 = pHead1
        node2 = pHead2
        while node1:
            node1 = node1.next
            count1 += 1
        while node2:
            node2 = node2.next
            count2 += 1
        node_l = pHead1
        node_s = pHead2
        k = count1 - count2
        if count1 < count2:
            node_l = pHead2
            node_s = pHead1
            k = count2 - count1
        for i in range(k):
            node_l = node_l.next
        while node_l != node_s and node_l and node_s:
            node_l = node_l.next
            node_s = node_s.next
        return node_l