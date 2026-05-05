class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = len(nums)
        return nums[l-1]*nums[l-2] - nums[1]*nums[0]