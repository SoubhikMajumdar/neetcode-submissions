from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        print(c.most_common())
        return c.most_common()[len(set(nums))-1][0]