'''class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR = Counter(ransomNote)
        countM = Counter(magazine)

        for c in countR:
            if countM[c] < countR[c]:
                return False

        return True'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = Counter(magazine)
        for letter in ransomNote:
            if letter not in mag or mag[letter] == 0:
                return False
            else:
                mag[letter]-=1
        return True
