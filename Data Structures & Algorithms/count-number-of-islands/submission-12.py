class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r,c):
            stack = [(r,c)]
            grid[r][c] = "0"

            while stack:
                r,c = stack.pop()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c +dc
                    if 0<= nr < rows and 0<= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands+=1

        return islands