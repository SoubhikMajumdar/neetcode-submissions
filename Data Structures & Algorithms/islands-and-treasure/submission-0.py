from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 1. Add all treasure chests (0s) to the queue as starting points
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        # 2. Multi-source BFS: expand outward layer by layer
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Only traverse into unvisited land cells (INF)
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))

