class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = "0"
        for r in range(len(num) - 2):
            if num[r] == num[r+1] == num[r+2]:
                ans = max(ans, num[r:r+3])
        
        return "" if ans == "0" else ans

