class Solution:
    def validPalindrome(self, s: str) -> bool:
        condition1 = (s == s[::-1])
        condition2 = False
        for i in range(len(s)):
            newS = s[0:i] + s[i+1:len(s)]
            if newS == newS[::-1]:
                condition2 = True

        return condition1 or condition2