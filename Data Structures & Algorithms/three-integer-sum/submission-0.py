class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        for i, a in enumerate(nums):

            if i> 0 and nums[i-1] == a:
                continue

            l, r = i+1, len(nums) - 1

            while l< r:
                threesum = a + nums[l] + nums[r]

                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else: # to avoid duplicates we move 2nd number pointer and check if same as prev, keep shifting if so
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while l <r and nums[l] == nums[l-1]:
                        l+=1
        return res