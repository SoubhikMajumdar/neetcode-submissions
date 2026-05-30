class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            score += abs(ord(s[i+1]) - ord(s[i]))
        return score