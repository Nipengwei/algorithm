# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if base == 0.0 and exponent < 0:
            return 0.0
        abs_exponent = exponent
        if exponent < 0:
            abs_exponent = -exponent
        result = self.Power_abs(base,abs_exponent)
        if exponent < 0:
            result = 1.0/result
        return result
    
    def Power_abs(self, base, exponent):
        if exponent == 0:
            return 1.0
        if exponent == 1:
            return base
        result = self.Power_abs(base, exponent >> 1)
        result *= result
        if exponent & 0x1 == 1:
            result *= base
        return result