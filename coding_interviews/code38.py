# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        mid = (1+tsum)>>1
        cursum = small + big
        sum_total = []
        while small < mid:
            if cursum == tsum:
                sum_total.append(range(small,big+1))
                big += 1
                cursum += big
            elif cursum < tsum:
                big += 1
                cursum += big
            else:
                cursum -= small
                small += 1
        return sum_total