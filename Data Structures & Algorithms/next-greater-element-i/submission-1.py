class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for i in nums1:
            j = nums2.index(i)
            found = -1
            for k in range(j + 1, len(nums2)):
                if nums2[k] > i:
                    found = nums2[k]
                    break
            ans.append(found)
        return ans