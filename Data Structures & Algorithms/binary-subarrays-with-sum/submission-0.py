# similar to subarray sum equals K
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = 0
        count = { 0 : 1 }
        res = 0

        for num in nums:
            prefixSum += num
            res += count.get(prefixSum - goal, 0)
            count[prefixSum] = count.get(prefixSum, 0) + 1

        return res