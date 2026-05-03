class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()#character set
        l = 0 #left pointer
        res = 0
        for r in range(len(s)): #right pointer traverse through string
            while s[r] in charSet: #if right pointer in subset that left pointer changes till
                charSet.remove(s[l]) # set is valid subset again
                l+=1
            charSet.add(s[r]) #if not then add to subset
            res = max(res, r-l+1)
        return(res)
