class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        # sum incl ith to jth index = prefix[j+1] - prefix[i]; prefix[0] always 0
        for i in range(n):
            leftSum = prefixSum[i]
            rightSum = prefixSum[n] - prefixSum[i+1]
            if leftSum == rightSum:
                return i
        return -1