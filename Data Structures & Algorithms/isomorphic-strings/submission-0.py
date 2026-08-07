class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = dict()
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashmap.values():
                    return False
                hashmap[s[i]] = t[i]
            else:
                if hashmap[s[i]] != t[i]:
                    return False
        return True