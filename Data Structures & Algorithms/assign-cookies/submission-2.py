class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gpointer = spointer = 0
        while gpointer < len(g) and spointer <len(s):
            if s[spointer] >= g[gpointer]:
                spointer+=1
                gpointer+=1
            else:
                spointer+=1
            
        return gpointer