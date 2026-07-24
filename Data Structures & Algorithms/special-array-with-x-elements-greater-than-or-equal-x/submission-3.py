class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l, r = 1, len(nums)
        while l <= r:
            x = (l + r)//2
            count = sum(1 for num in nums if num >= x)

            if count == x:
                return x

            if count < x:
                r = x - 1
            else:
                l = x + 1

        return -1