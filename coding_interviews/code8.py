# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        return sum([(n>>i & 1) for i in range(0,32)])