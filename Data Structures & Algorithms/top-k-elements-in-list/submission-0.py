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
        count = 0
        print(c)
        for key, value in c.most_common():
            if count < k:
                print(key, value)
                count+=1
                arr.append(key)
            else:
                break
        return arr