class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        x = l
        for i in range(l):
            x ^= i
            x ^= nums[i]
        return x
