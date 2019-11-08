class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        d = [[False for i in range(n)] for i in range(n)]
        res = ''
        maxl = 0
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i == j:
                    d[i][j] = True
                    if maxl < 1:
                        res = s[i]
                        maxl = 1
                if ((j-i) == 1) and (s[i] == s[j]):
                    d[i][j] = True
                    if maxl < 2:
                        maxl = 2
                        res = s[i:j+1]
                if ((j-i) > 1) and (s[i] == s[j]) and (d[i+1][j-1] == True):
                    d[i][j] = True
                    if maxl < j-i+1:
                        maxl = j-i+1
                        res = s[i:j+1]
        return res