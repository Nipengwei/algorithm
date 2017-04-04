# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n < 0:
            return None
        count = 0
        i = 1
        while i <= n:
            a = n/i
            b = n%i
            count += (a+8)/10*i + (a%10==1)*(b+1)
            i *= 10
        return count