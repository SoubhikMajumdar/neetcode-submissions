from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = []
        c = Counter(nums)
        for key, value in c.most_common(k):
            arr.append(key)
        return arr