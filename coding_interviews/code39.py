# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array or not tsum:
            return []
        small = 0
        big = len(array)-1
        while small < big:
            cursum = array[small] + array[big]
            if cursum == tsum:
                return [array[small],array[big]]
            elif cursum < tsum:
                small += 1
            else:
                big -= 1
        return []