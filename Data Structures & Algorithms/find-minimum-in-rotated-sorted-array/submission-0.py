class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # Minimum is to the right of mid
                left = mid + 1
            else:
                # Minimum is at mid or to the left
                right = mid

        return nums[left]