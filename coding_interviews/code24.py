# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return ss
        l = set()
        for i in range(len(ss)):
            s_left = ss[0:i]+ss[i+1:]
            sss = self.Permutation(s_left)        
            for s in sss:
                l.add(ss[i]+s)
        return sorted(list(l))