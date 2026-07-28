class Solution:
    def minEatingSpeed(self, piles: List[int], h: int):
        left, right = 1, max(piles)

        while left < right:
            rate = (left + right) // 2

            total = 0
            for pile in piles:
                total += pile//rate
                if pile%rate != 0:
                    total+=1

            if total <= h:
                right = rate
            else:
                left = rate + 1

        return left