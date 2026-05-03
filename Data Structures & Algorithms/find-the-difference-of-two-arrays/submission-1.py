class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numset1, numset2 = set(nums1), set(nums2)
        return [list(numset1-numset2), list(numset2-numset1)]