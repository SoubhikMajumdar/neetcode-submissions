class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if y!=x:
                stones.append(y-x)

        if len(stones) ==1:
            return stones[0]
        else:
            return 0    
'''import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, -(first - second))

        if stones:
            return -stones[0]
        return 0'''