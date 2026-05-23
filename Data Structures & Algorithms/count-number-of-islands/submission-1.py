class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            # boundary + visited + water checks
            if (
                i < 0 or j < 0 or
                i >= rows or j >= cols or
                grid[i][j] == "0" or
                (i, j) in visited
            ):
                return
            visited.add((i, j))
            # explore neighbors
            for dr, dc in directions:
                dfs(i + dr, j + dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1

        return islands