class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 1
            is_closed = True

            while stack:
                row, col = stack.pop()

                if row == 0 or row == m - 1 or col == 0 or col == n - 1:
                    is_closed = False

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (0 <= nr < m and 0 <= nc < n
                            and grid[nr][nc] == 0):
                        grid[nr][nc] = 1
                        stack.append((nr, nc))

            return is_closed

        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1

        return count