class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                sign+=1
        if sign & 1:
            return -1
        else:
            return 1