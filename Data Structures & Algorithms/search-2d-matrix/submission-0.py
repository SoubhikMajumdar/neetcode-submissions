class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i=0
        m = len(matrix)
        n = len(matrix[i])
        for j in range(m):
            if target in matrix[j]:
                return True
        return False