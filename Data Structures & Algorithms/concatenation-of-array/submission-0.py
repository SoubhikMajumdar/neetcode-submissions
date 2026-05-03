class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        arr[0:len(nums)] = nums
        arr[len(nums):2*len(nums)] = nums
        return arr
        