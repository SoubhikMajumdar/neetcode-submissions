class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i=0
        while i<len(s):
            if s.count(s[i]) != t.count(s[i]):
                    return False
            i+=1
        return True
