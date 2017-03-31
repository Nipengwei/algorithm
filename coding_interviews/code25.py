# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        times = 0
        for i in numbers:
            if times == 0:
                res = i
                times = 1
            elif res == i:
                times += 1
            else:
                times -= 1
        count = 0
        for j in numbers:
            if j == res:
                count += 1
        if count*2 > len(numbers):
        	return res
        return 0