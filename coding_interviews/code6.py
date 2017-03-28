# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray)-1
        mid = left
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                mid = right
                break
            mid = left + (right - left)/2
            if rotateArray[left] == rotateArray[right] and rotateArray[mid] == rotateArray[right]:
                return self.Min(rotateArray[left:right+1])
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid
        return rotateArray[mid]
    def Min(self, Array):
        result = Array[0]
        for t in Array:
            if t < result:
                result = t
        return result