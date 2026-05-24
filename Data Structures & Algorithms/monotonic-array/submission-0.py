class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l,r =0, 1
        dirset = set()
        while r< len(nums): 
            direction = nums[r] - nums[l]
            if direction > 0:
                dirset.add(1)
            elif direction < 0:
                dirset.add(-1)
            else:
                dirset.add(0)

            if 1 in dirset and -1 in dirset:
                return False
            l+=1
            r+=1
        return True