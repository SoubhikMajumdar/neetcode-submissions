class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = k
        
        for i in range(len(blocks) - k + 1):
            count = blocks[i:i+k].count("W")
            result = min(result, count)
        
        return result