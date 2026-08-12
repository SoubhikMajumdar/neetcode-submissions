class Solution:
    def check(self, nums: List[int]) -> bool:
        for k in range(0, len(nums)+1):
            rotatednums = nums[-k % len(nums):] + nums[:-k % len(nums)]
            if rotatednums == sorted(nums):
                return True
        return False