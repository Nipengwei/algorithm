# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return None
        start = 0
        end = 0
        sum_max = array[0]
        sum_now = 0
        for i in range(len(array)):
            sum_now += array[i]
            if sum_now < array[i]:
                start = i
                sum_now = array[i]
            if sum_now > sum_max:
                sum_max = sum_now
                end = i
        return sum_max