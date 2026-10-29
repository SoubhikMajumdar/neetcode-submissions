class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l =0
        r =1
        maxPrice = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxPrice = max(maxPrice, profit)
            else:
                l =r
            r+=1
        return maxPrice