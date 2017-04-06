# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        hash = {}
        for i in s:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i
        return -1