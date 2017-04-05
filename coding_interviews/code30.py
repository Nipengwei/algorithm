# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        res = [1]
        num_2 = num_3 = num_5 = 0
        while len(res) < index:
            result = min(res[num_2]*2, res[num_3]*3, res[num_5]*5)
            res.append(result)
            while res[num_2]*2 <= result:
                num_2 += 1
            while res[num_3]*3 <= result:
                num_3 += 1
            while res[num_5]*5 <= result:
                num_5 += 1
        return res[-1]