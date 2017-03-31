# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return matrix
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        l = []
        while col > 2*start and row > 2*start:
            endx = col - start - 1
            endy = row - start - 1
            for i in range(start,endx+1):
                l.append(matrix[start][i])
            if start < endy:
                for i in range(start+1,endy+1):
                    l.append(matrix[i][endx])
            if start < endy and start < endx:
                for i in range(endx-1,start-1,-1):
                    l.append(matrix[endy][i])
            if start+1<endy and start < endx:
                for i in range(endy-1,start,-1):
                    l.append(matrix[i][start])
            start += 1
        return l