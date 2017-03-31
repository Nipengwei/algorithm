# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or not popV:
            return False
        data = []
        index_push = 0
        index_pop = 0
        
        while index_pop < len(popV):
            while not data or data[-1] != popV[index_pop]:
                if index_push >= len(pushV):
                    return False
                data.append(pushV[index_push])
                index_push += 1
            data.pop()
            index_pop += 1
            
        if not data and index_pop == len(popV):
            return True
        return False