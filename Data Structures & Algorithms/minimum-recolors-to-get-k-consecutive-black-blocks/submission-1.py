class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = k #worst case scenario need to make k consec black
        
        for i in range(len(blocks) - k + 1):
            count = blocks[i:i+k].count("W") #sliding window of size k and we count how many Whites to change to black to make it k consec black
            result = min(result, count) # store min W we need to change across sliding windows
        
        return result