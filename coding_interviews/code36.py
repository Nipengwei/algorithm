# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        _,result = self.is_balanced(pRoot)
        return result
    def is_balanced(self, pRoot):
        if not pRoot:
            return 0, True
        left_d, left_isb = self.is_balanced(pRoot.left)
        right_d, right_isb = self.is_balanced(pRoot.right)
        if left_isb and right_isb and left_d - right_d <= 1 and left_d - right_d >= -1:
            return max(left_d, right_d)+1, True
        return 0, False