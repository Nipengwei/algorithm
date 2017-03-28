class Solution:
    def Fibonacci(self, n, fib1=0, fib2=1):
    	if n == 0:
    		return fib1
    	return self.Fibonacci(n-1,fib2,fib1+fib2)