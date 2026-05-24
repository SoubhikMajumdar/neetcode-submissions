class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        l = len(nums)
        result = []
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                result.append(n)
        result.append(int((l*(l+1)/2)-sum(s)))
        return result