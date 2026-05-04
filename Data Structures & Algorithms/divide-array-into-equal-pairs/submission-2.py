class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set(nums)
        for i in s:
            if nums.count(i) % 2 !=0:
                return False 
        return True