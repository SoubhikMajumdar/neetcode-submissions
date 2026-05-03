class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        longestseqlen = 0 
        for n in s:
            if (n-1) not in s:
                current = n
                currentseq = 1
                while current + 1 in s:
                    current+=1
                    currentseq+=1
                longestseqlen = max(longestseqlen,currentseq)
        return longestseqlen
        