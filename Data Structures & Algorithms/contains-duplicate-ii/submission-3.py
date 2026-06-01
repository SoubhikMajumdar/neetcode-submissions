class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            # If nums[right] already exists in current window,
            # then distance between duplicate indices is <= k
            if nums[right] in window:
                return True

            window.add(nums[right])

            # Keep window size at most k
            if right - left + 1 > k:
                window.remove(nums[left])
                left += 1

        return False