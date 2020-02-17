class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_now = res = nums[0]

        for i in range(1,len(nums)):
            sum_now = max(nums[i],sum_now+nums[i])
            res = max(res,sum_now)
        
        return res