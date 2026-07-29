class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sortedParity = []
        for n in nums:
            if n & 1:
                sortedParity.append(n)

            else:
                sortedParity.insert(0, n)

        return sortedParity
