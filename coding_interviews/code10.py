# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        if not array:
            return array
        left = 0
        while left < len(array) and array[left] & 1:
            left += 1
        right = left + 1
        while right < len(array):
            while right < len(array) and not(array[right] & 1):
                right += 1
            if right == len(array):
                break
            temp = array[right]
            for i in range(right,left,-1):
                array[i] = array[i-1]
            array[left] = temp
            left += 1
            right += 1
        return array