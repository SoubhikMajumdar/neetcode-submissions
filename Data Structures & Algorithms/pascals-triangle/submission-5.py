class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        for i in range(numRows):
            newRow = [1] * (i + 1)
            # fill middle values
            for j in range(1, i):
                newRow[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(newRow)
        return res