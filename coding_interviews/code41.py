# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        return n and self.Sum_Solution(n-1)+n