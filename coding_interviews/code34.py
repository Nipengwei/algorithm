# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        
        first = Solution.get_first(data, k, 0, len(data)-1)
        last = Solution.get_last(data, k, 0, len(data)-1)
        if first >= 0 and last >=0:
            return last-first+1
        return 0
    
    @classmethod
    def get_first(cls,data,k,start,end):
        if start > end:
            return -1
        mid = start + (end-start)/2
        if data[mid] == k:
            if mid == 0 or data[mid-1] != k:
                return mid
            else:
                end = mid-1
        elif data[mid] > k:
            end = mid-1
        else:
            start = mid+1
        return cls.get_first(data, k, start, end)
    
    @classmethod
    def get_last(cls,data,k,start,end):
        if start > end:
            return -1
        mid = start + (end-start)/2
        if data[mid] == k:
            if mid == len(data)-1 or data[mid+1] != k:
                return mid
            else:
                start = mid+1
        elif data[mid] > k:
            end = mid-1
        else:
            start = mid+1
        return cls.get_last(data, k, start, end)