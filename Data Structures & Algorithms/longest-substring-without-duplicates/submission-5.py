class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l,r=0,1
        longestsubstring =1
        substring =1
        hashset = set()
        while r <len(s):
            hashset.add(s[l])
            if s[r] not in hashset:
                substring+=1
                hashset.add(s[r])
                longestsubstring = max(substring, longestsubstring)
                r+=1
            else:
                hashset = set()
                l+=1
                r=l+1
                substring =1

        return longestsubstring
