# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        
        root = sequence[-1]
        index = 0
        while index < len(sequence)-1 and sequence[index] < root:
            index += 1
            
        seq_left = sequence[0:index]
        seq_right = sequence[index:len(sequence)-1]
        
        for i in seq_right:
            if i < root:
                return False
        if not seq_left:
            left = True
        else:
            left = self.VerifySquenceOfBST(seq_left)
        if not seq_right:
            right = True
        else:
            right = self.VerifySquenceOfBST(seq_right)
        return left and right