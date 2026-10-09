class Solution:
    def minSwaps(self, s):
        close, maxClose = 0,0

        for c in s:
            if c == '[':
                close-=1
            if c == ']':
                close+=1
            maxClose = max(maxClose, close)

        return (maxClose + 1)//2

        
        