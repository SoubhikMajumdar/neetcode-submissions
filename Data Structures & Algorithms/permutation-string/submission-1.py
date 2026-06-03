class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        # logic: use sliding window, then check if substrings have same characters with same freq i.e permutation
        for i in range(len(s2) - window + 1):
            if Counter(s1) == Counter(s2[i:i+window]):
                return True

        return False