class Solution(object):
    def numEnclaves(self, grid):
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        stack = []

        # Add all boundary land cells
        for r in range(rows):
            if grid[r][0] == 1:
                stack.append((r, 0))
            if grid[r][cols - 1] == 1:
                stack.append((r, cols - 1))

        for c in range(cols):
            if grid[0][c] == 1:
                stack.append((0, c))
            if grid[rows - 1][c] == 1:
                stack.append((rows - 1, c))

        # Remove all land connected to the boundary
        while stack:
            r, c = stack.pop()

            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            if grid[r][c] == 0:
                continue

            grid[r][c] = 0

            for dr, dc in directions:
                stack.append((r + dr, c + dc))

        # Remaining land = enclaves
        return sum(row.count(1) for row in grid)