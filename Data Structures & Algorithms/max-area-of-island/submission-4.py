class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0

        def dfs(r, c):
            if not(0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1

            for dr, dc in directions:
                area+=dfs(r+dr, c+dc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        return max_area