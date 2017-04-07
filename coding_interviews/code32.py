# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        if not data:
            return 0
        copy,count = self.merge_count(data)
        return count
    
    def merge_count(self, data):
        if len(data) == 1:
            return data,0
        mid = len(data)/2
        left,count_left = self.merge_count(data[:mid])
        right,count_right = self.merge_count(data[mid:])
        i = j = count = 0
        copy = []
        while i<len(left) and j<len(right):
            if left[i] > right[j]:
                count += len(right)-j
                if count >= 1000000007:
                    count %= 1000000007
                copy.append(left[i])
                i += 1
            else:
                copy.append(right[j])
                j += 1
        while i < len(left):
            copy.append(left[i])
            i += 1
        while j < len(right):
            copy.append(right[j])
            j += 1
        return copy, (count_left+count_right+count)%1000000007