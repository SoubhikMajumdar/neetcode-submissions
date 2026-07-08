'''from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table= Counter(nums)
        for key, value in hash_table.items():
            if value == max(hash_table.values()):
                return key'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = dict()
        for n in nums:
            freq[n] = freq.get(n,0) +1
            if freq[n] > len(nums)/2:
                return n
        