class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visit):
            if (r,c) in visit:
                return

            visit.add((r,c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visit):
                    dfs(nr, nc, visit)

        for c in range(COLS): # top row pacific, bottom row atlantic
            dfs(0, c, pac)
            dfs(ROWS-1, c, atl)

        for r in range(ROWS): #first column pacific, last column atlantic
            dfs(r, 0, pac)
            dfs(r, COLS-1, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res