class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image    
        rows, cols = len(image), len(image[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        original = image[sr][sc]

        def dfs(r, c):
            if not(0 <= r <rows and 0 <=c < cols) or image[r][c] != original:
                return
            image[r][c] = color
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        dfs(sr, sc)
        return image


