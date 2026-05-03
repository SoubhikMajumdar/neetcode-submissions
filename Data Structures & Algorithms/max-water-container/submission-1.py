class Solution(object):
    def maxArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        left, right = 0, len(heights) - 1
        best = 0

        while left < right:
            h = min(heights[left], heights[right])
            area = (right - left) * h
            if area > best:
                best = area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return best
