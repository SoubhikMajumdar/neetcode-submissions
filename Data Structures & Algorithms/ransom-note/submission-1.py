class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR = Counter(ransomNote)
        countM = Counter(magazine)

        for c in countR:
            if countM[c] < countR[c]:
                return False

        return True