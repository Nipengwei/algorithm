# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        fib = [0,1,1]
        if n < 3:
            return fib[n]
        fib1 = 1
        fib2 = 0
        for i in range(3,n+1):
            fib1,fib2 = fib1+fib2,fib1
        return fib1 + fib2