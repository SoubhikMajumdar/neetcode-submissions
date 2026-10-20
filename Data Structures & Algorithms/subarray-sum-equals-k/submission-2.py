class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res  = 0
        cur = 0

        prefix = {0: 1}

        for num in nums:
            cur+=num
            diff = cur - k
            res+= prefix.get(diff, 0)
            prefix[cur] = prefix.get(cur, 0) + 1

        return res


