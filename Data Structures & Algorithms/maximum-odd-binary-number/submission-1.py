class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted(s)
        s.reverse()

        i = len(s) - 1
        while i>= 0 and s[i] == '0':
            i-=1
        s[i], s[len(s)-1] = s[len(s)-1], s[i]

        return ''.join(s)