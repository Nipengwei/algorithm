# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if s is None or pattern is None:
            return False
        if s == '' and pattern == '':
            return True
        if s and not pattern:
            return False           
        if len(pattern) > 1 and pattern[1] == '*':
            if s and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s[1:],pattern[2:]) or self.match(s[1:],pattern) or self.match(s,pattern[2:])
            else:
                return self.match(s,pattern[2:])
        if s and (pattern[0] == '.' or s[0] == pattern[0]):
            return self.match(s[1:],pattern[1:])
        return False