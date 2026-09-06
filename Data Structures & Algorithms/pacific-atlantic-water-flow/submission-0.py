class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit):
            if (r, c) in visit:
                return

            visit.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    (nr, nc) in visit or
                    heights[nr][nc] < heights[r][c]):
                    continue

                dfs(nr, nc, visit)

        # Pacific: top and left borders
        for c in range(COLS):
            dfs(0, c, pac)

        for r in range(ROWS):
            dfs(r, 0, pac)

        # Atlantic: bottom and right borders
        for c in range(COLS):
            dfs(ROWS - 1, c, atl)

        for r in range(ROWS):
            dfs(r, COLS - 1, atl)

        return [[r, c] for r in range(ROWS) for c in range(COLS)
                if (r, c) in pac and (r, c) in atl]
