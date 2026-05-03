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
        print(c)
        print(c.most_common(k))
        for key, value in c.most_common(k):
            print(key, value)
            arr.append(key)
        return arr