class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distanceOrigin(x,y):
            return x**2 + y**2

        result = []

        heap = []

        for x, y in points:
            heapq.heappush(heap, (-distanceOrigin(x,y), [x,y]))

            if len(heap) > k:
                heapq.heappop(heap)

        for _, coord in heap:
            result.append(coord)

        return result
