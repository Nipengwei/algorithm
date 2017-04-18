# -*- coding:utf-8 -*-
class Solution:
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                tmp=numbers[i]
                numbers[i]=numbers[tmp]
                numbers[tmp]=tmp
        return False