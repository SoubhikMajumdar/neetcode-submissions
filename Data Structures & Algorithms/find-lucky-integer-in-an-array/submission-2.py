class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for n in arr:
            if arr.count(n) == n and n > ans:
                ans = n
        return ans