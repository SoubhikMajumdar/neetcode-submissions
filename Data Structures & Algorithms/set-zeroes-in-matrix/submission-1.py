class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])

        marked_rows = set()
        marked_cols = set()

        # Pass 1: collect information
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    marked_rows.add(row)
                    marked_cols.add(col)

        # Pass 2: modify
        for row in range(rows):
            for col in range(cols):
                if row in marked_rows or col in marked_cols:
                    matrix[row][col] = 0