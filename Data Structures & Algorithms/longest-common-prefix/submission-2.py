class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort(key=len)
        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if char != s[i]:
                    return prefix
            prefix+=char
        return prefix