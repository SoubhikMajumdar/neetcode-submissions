class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count =0
        for i in range(len(nums)):
            count+=nums[i+1:len(nums)].count(nums[i])
        return count