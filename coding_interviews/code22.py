# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        self.CloneNodes(pHead)
        self.CloneRandom(pHead)
        return self.Reconnect(pHead)
    
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pNew = RandomListNode(pNode.label)
            pNew.next = pNode.next
            pNode.next = pNew
            pNode = pNode.next.next
            
    def CloneRandom(self, pHead):
        pNode = pHead
        while pNode:
            if pNode.random:
            	pNode.next.random = pNode.random.next
            pNode = pNode.next.next
            
    def Reconnect(self, pHead):
        pNode = pHead
        pnewHead = pnewNode = pHead.next
        pNode.next = pnewNode.next
        pNode = pNode.next
        while pNode:
            pnewNode.next = pnewNode.next.next
            pNode.next = pNode.next.next
            pnewNode = pnewNode.next
            pNode = pNode.next            
        return pnewHead