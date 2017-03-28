# -*- coding:utf-8 -*-
class Solution:
    def Find(self, target, array):
        if not array:
            return False
        m=len(array)
        n=len(array[1])
        i=0
        j=m-1
        while(i<n and j>=0):
            if array[i][j]<target:
                i+=1
            elif array[i][j]>target:
                j-=1
            else:
                return True
        return False