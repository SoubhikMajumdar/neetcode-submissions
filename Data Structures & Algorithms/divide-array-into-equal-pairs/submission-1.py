class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set(nums)
        ans = True
        for i in s:
            if nums.count(i) % 2 !=0:
                ans = False

        return ans