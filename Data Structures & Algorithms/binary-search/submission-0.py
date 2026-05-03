class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0,len(nums)-1
        while left<=right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            left+= 1
            right-= 1
        return -1
        
        