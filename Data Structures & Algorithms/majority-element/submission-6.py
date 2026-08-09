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
'''
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
'''

# using Boyer-Moore Voting Algorithm, we keep candidate and increment count, if different number then decrement, if count is 0 new candidate, majority element survives as candidate

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count+=1
            else:
                count-=1
        return candidate

















        