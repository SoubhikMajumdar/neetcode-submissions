class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec =1,1
        res =1
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                inc, dec = 1, dec+1
            elif nums[i] < nums[i+1]:
                inc, dec = inc+1, 1
            else:
                inc, dec = 1,1
            
            res = max(inc, dec, res)
        return res