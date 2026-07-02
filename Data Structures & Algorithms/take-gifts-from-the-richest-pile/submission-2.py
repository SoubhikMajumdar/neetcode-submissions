class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts) #largest original element now smallest in gifts

        for i in range(k):
            n = -heapq.heappop(gifts) #original largest element
            heapq.heappush(gifts, -floor(sqrt(n)))
        return -sum(gifts)