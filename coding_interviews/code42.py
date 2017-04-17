# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        sign = 1
        res = 0
        if s[0] == '-':
            sign = -1
        start = 1 if s[0] == '-' or s[0] == '+' else 0
        for i in range(start,len(s)):
            if '9' < s[i] or s[i] < '0':
                return 0
            res = res*10 + ord(s[i]) - ord('0')
        return res*sign