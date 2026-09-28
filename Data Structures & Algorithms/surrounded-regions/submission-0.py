class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            board[start_row][start_col] = "T"

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < rows and
                        0 <= new_col < cols and
                        board[new_row][new_col] == "O"
                    ):
                        board[new_row][new_col] = "T"
                        queue.append((new_row, new_col))

        # Check left and right borders
        for row in range(rows):
            if board[row][0] == "O":
                bfs(row, 0)

            if board[row][cols - 1] == "O":
                bfs(row, cols - 1)

        # Check top and bottom borders
        for col in range(cols):
            if board[0][col] == "O":
                bfs(0, col)

            if board[rows - 1][col] == "O":
                bfs(rows - 1, col)

        # Capture surrounded regions and restore safe regions
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"