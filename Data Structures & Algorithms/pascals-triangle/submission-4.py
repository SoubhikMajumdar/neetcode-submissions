class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            newrow = [1]*i
            res.append(newrow)
            if len(newrow) > 2:
                for j in range(1, len(newrow)-1):
                    newrow[j] = res[i-2][j-1] + res[i-2][j] 
        
        return res