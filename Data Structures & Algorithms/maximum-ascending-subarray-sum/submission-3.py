class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        left = 0
        subsum =nums[left]
        maxsum = nums[left]
        for right in range(1, len(nums)):
            if nums[right] > nums[left]:
                subsum+=nums[right]
                maxsum = max(maxsum, subsum)
                left+=1
            else:
                left = right
                subsum = nums[left]
            right+=1

        return maxsum


