class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        longestSeq = 0

        for n in s:
            if n-1 not in s:
                current = n
                currentSeq = 1

                while current + 1 in s:
                    current+=1
                    currentSeq+=1

                longestSeq = max(longestSeq, currentSeq)

        return longestSeq
