class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = 0
        for x in range(len(nums)+1):
            count = 0
            for n in nums:
                if n >= x:
                    count+=1
            if count == x:
                return x
        return -1 