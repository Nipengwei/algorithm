# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        data = []
        node = []
        node.append(root)
        while node:
            node_now = node.pop()
            data.append(node_now.val)
            if node_now.left:
                node.insert(0,node_now.left)
            if node_now.right:
                node.insert(0,node_now.right)
        return data