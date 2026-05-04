class Solution:
    def findLucky(self, arr: List[int]) -> int:
        largen = -1
        for n in arr:
            if arr.count(n) == n and n > largen:
                largen = n
        return largen