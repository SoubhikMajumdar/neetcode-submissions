class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        ans[0:len(nums)] = nums
        ans[len(nums):2*len(nums)] = nums
        return ans
        