class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        res = 0
        for n in range(len(heights)):
            if expected[n] != heights[n]:
                res+=1
        return res