class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dict1, dict2 = {}, {}
        for c in s1:
            dict1[c] = dict1.get(c, 0) + 1

        l, r = 0, len(s1) - 1

        for c in s2[l:r + 1]:
            dict2[c] = dict2.get(c, 0) + 1

        while r < len(s2):
            if dict1 == dict2:
                return True
            dict2[s2[l]] -= 1
            
            if dict2[s2[l]] == 0:
                del dict2[s2[l]]

            l += 1
            r += 1

            if r < len(s2):
                dict2[s2[r]] = dict2.get(s2[r], 0) + 1

        return False