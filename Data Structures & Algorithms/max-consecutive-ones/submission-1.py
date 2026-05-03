class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 # count instances
        res = 0 # final result
        for i in range(len(nums)):
                if nums[i] == 1:
                    count+=1
                else:
                    count = 0
                if count > res:
                    res = count
        return res