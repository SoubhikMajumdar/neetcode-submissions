class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros+=1
            #shrink window is zeros more than allowed in window    
            while zeros > k:
                if nums[left] == 0:
                    zeros-=1
                left+=1

            result = max(result, right - left +1) #only maximum valid subwindow length kept
        return result