class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        result = []
        for i in range(3):
            result += [i] * freq.get(i, 0)

        nums[:] = result