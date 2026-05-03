class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        ans = [0]*2
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in seen:
                    ans[0] = grid[i][j]
                seen.add(grid[i][j])
        l = sum(seen)
        N = ((len(seen)+1)*(len(seen)+2))/2
        ans[1] = int(abs(N-l))
        return ans
