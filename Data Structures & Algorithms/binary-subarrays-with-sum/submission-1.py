# similar to subarray sum equals K
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curr = 0
        prefix = {0:1}
        res = 0

        for num in nums:
            curr+= num
            res+=prefix.get(curr - goal, 0)
            prefix[curr] = prefix.get(curr, 0) + 1

        return res