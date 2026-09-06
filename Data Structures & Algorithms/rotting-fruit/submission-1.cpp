class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int fresh = 0;
        int minutes = 0;
        queue<pair<int, int>> q;
        
        // Directions for moving up, down, left, and right
        vector<pair<int, int>> directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        
        int m = grid.size();
        int n = grid[0].size();
        
        // Find initial rotten oranges and count fresh ones
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 2) {
                    q.push({r, c});
                } else if (grid[r][c] == 1) {
                    fresh++;
                }
            }
        }
        
        // Breadth-First Search (BFS)
        while (!q.empty() && fresh > 0) {
            int q_size = q.size();
            
            for (int i = 0; i < q_size; ++i) {
                auto [r, c] = q.front();
                q.pop();
                
                for (auto& [dr, dc] : directions) {
                    int nr = r + dr;
                    int nc = c + dc;
                    
                    // Check boundaries and if the neighbor orange is fresh
                    if (0 <= nr && nr < m && 0 <= nc && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh--;
                        q.push({nr, nc});
                    }
                }
            }
            minutes++;
        }
        
        return (fresh == 0) ? minutes : -1;
    }
};
