# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        else:
        	root = TreeNode(pre[0])
        root_index = tin.index(root.val)
        pre_left = pre[1:root_index+1]
        pre_right = pre[root_index+1:]
        tin_left = tin[:root_index]
        tin_right = tin[root_index+1:]
        root.left = self.reConstructBinaryTree(pre_left,tin_left)
        root.right = self.reConstructBinaryTree(pre_right,tin_right)
        return root