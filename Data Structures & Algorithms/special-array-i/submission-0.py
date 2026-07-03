class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if (sum(nums[i:i+2]))%2 == 0: # when numbers are both odd or even then sum is even
                return False
        return True