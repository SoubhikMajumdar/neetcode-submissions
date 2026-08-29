from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()

        # Find and mark the complete first island
        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] != 1
            ):
                return

            # 2 means this belongs to the first island
            grid[r][c] = 2
            queue.append((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Locate any cell belonging to the first island
        found = False

        for r in range(rows):
            if found:
                break

            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        # Expand from the entire first island simultaneously
        distance = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        # We reached the second island
                        if grid[nr][nc] == 1:
                            return distance

                        # Expand through unvisited water
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))

            distance += 1

        return -1