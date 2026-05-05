class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        
        for item in s:
            freq[item] = freq.get(item, 0) + 1
        
        for i, item in enumerate(s):
            if freq[item] == 1:
                return i
        
        return -1