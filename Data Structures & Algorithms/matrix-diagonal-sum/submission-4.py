class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagSum = 0
        j = len(mat)-1
        for i in range(len(mat)):
            if i == j:
                diagSum+= mat[i][i]
            else:
                diagSum+=mat[i][i] + mat[i][j]
            j-=1
        return diagSum

# for each row, we take ith, iith (main diagonal) and ith, jth (antidiagonal) where j decreases from len(mat) - 1 to 0