# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l_data = []
        self.l_min = []
    def push(self, node):
        self.l_data.append(node)
        if not self.l_min or node < self.l_min[-1]:
            self.l_min.append(node)
        else:
            self.l_min.append(self.l_min[-1])
    def pop(self):
        if self.l_data and self.l_min:
            self.l_min.pop()
            return self.l_data.pop()
        else:
            return None
        
    def top(self):
        if self.l_data:
        	return self.l_data[-1]
        else:
            return None
    def min(self):
        if self.l_min:
            return self.l_min[-1]
        else:
            return None