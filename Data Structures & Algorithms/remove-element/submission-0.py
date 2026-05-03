class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        read= 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[read] = nums[i]
                read+=1
            i+=1 
        return read