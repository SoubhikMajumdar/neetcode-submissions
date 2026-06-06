class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
       Spointer = 0
       Tpointer = 0
       toAppend = len(t)
       while Spointer < len(s) and Tpointer < len(t):
        if s[Spointer] == t[Tpointer]:
            Tpointer+=1
            toAppend-=1 
        Spointer+=1
       return toAppend