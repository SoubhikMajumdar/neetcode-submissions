'''class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = 0
        for x in range(len(nums)+1):
            count = 0
            for n in nums:
                if n >= x:
                    count+=1
            if count == x:
                return x
        return -1 #not optimal yet'''
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l, r = 1, len(nums)
        while l <= r:
            mid = (l + r)//2
            cnt = sum(1 for num in nums if num >= mid)

            if cnt == mid:
                return mid

            if cnt < mid:
                r = mid - 1
            else:
                l = mid + 1

        return -1