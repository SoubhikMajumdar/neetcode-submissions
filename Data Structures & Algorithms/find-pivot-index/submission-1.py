class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            leftsum = sum(nums[0:index])
            rightsum = sum(nums[index+1:len(nums)])
            if leftsum == rightsum:
                return index
        return -1