class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev = 0

        if x < 0:
            return False

        while x:
            rev = rev * 10 + x % 10
            x //= 10

        return original == rev