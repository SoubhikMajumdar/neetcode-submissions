class Solution:
    def longestCommonPrefix(self, strs):
        
        prefix = 0 #index prefix stops
        for i in zip(*strs): #groups letters of strings by index 
            if len(set(i)) > 1: #if set length > 1 then not common letter at that index so exit loop
                break
            prefix+=1
        return strs[0][:prefix]