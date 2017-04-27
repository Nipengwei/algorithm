# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if not A:
            return []
        n = len(A)
        B = [1]*n
        temp = 1
        for i in range(1,n):
            B[i] = B[i-1]*A[i-1]
        for i in range(n-2,-1,-1):
            temp *= A[i+1]
            B[i] *= temp
        return B