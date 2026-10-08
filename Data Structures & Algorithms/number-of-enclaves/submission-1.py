class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0
            ):
                return

            # Mark this land cell visited
            grid[r][c] = 0

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Remove land connected to left and right borders
        for r in range(rows):
            if grid[r][0] == 1:
                dfs(r, 0)

            if grid[r][cols - 1] == 1:
                dfs(r, cols - 1)

        # Remove land connected to top and bottom borders
        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0, c)

            if grid[rows - 1][c] == 1:
                dfs(rows - 1, c)

        # Remaining land cells are enclaves
        enclaves = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    enclaves += 1

        return enclaves