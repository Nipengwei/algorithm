# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.last = None
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        
        if pRootOfTree.left:
            left = self.Convert(pRootOfTree.left)
            pRootOfTree.left = self.last
            self.last.right = pRootOfTree
            
        self.last = pRootOfTree
        
        if pRootOfTree.right:
            right = self.Convert(pRootOfTree.right)
            pRootOfTree.right = right
            right.left = pRootOfTree
        
        if pRootOfTree.left:
            return left
        else:
            return pRootOfTree