# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        depth_l = self.TreeDepth(pRoot.left)
        depth_r = self.TreeDepth(pRoot.right)
        
        if depth_l >= depth_r:
            return depth_l+1
        else:
            return depth_r+1