class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        nums.sort()
        ans = float('inf')

        for i in range(len(nums)- k + 1):
            ans = min(ans, nums[i+k-1] - nums[i])

        return ans