class Solution:
    def is_palindrome(self, string):
        left = 0
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1

        return True

    def firstPalindrome(self, words):
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""

    


        
