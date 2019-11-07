class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,res = 0,0
        l = {}
        for i in range(len(s)):
            if s[i] in l:
                start = max(start, l[s[i]])
            l[s[i]] = i+1
            res = max(res, i-start+1)
        return res