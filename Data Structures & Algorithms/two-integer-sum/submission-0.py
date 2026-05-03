class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment],i]
            seen[num] = i
        