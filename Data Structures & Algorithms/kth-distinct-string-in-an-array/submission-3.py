class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        count=0
        for n in arr:
            freq[n] = freq.get(n,0) +1
        for n in arr:
            if freq[n] == 1:
                count+=1
            if count == k:
                return n
        return ""
