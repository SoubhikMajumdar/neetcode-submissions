class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sortedParity = []
        for n in nums:
            if n%2 == 0:
                sortedParity.insert(0, n)
            else:
                sortedParity.append(n)
        return sortedParity
