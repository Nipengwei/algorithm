class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1: return s

        l = ['' for i in range(numRows)]
        zlen = 2*numRows-2

        for i in range(len(s)):
            pos = i % zlen
            if pos < numRows:
                l[pos] += s[i]
            else:
                l[(numRows-2)-(pos-numRows)] += s[i]
        
        res = ''.join(l)
        return res