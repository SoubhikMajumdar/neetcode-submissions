class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = float("inf")
        left = 0
        subsum = 0
        for right in range(len(nums)):
            subsum+=nums[right]
            while subsum >= target:
                res = min(res, right - left + 1)
                subsum-= nums[left]
                left+=1
        if res == float("inf"):
            return 0
        else:
            return res
        
        

