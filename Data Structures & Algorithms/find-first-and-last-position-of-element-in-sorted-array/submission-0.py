class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # First occurrence:
        # Find first index where nums[index] >= target
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                # Valid, but an earlier valid index may exist
                right = mid - 1
            else:
                left = mid + 1

        first = left

        # Make sure target exists
        if first == n or nums[first] != target:
            return [-1, -1]

        # Last occurrence:
        # Find last index where nums[index] <= target
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                # Valid, but a later valid index may exist
                left = mid + 1
            else:
                right = mid - 1

        last = right

        return [first, last]