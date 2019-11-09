class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        num = x if x>=0 else -x
        while num != 0:
            res = res * 10 + num % 10
            if res > 2**31-1: return 0
            num = num // 10
        return res if x>=0 else -res