class Solution(object):
    def maxArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        left, right = 0, len(heights)-1
        maxamt = 0
        currentamt = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    currentamt = abs(i-j)*min(heights[i],heights[j])
                if currentamt > maxamt:
                    maxamt = currentamt
        return maxamt