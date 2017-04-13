# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        
        result_xor = 0
        for i in array:
            result_xor ^= i
        
        index_bit = 0
        while result_xor&1 == 0 and index_bit <= 32:
            result_xor = result_xor >> 1
            index_bit += 1
        
        num1 = num2 = 0 
        for i in array:
            if (i>>index_bit)&1 == 1:
                num1 ^= i
            else:
                num2 ^= i
                
        return [num1,num2]