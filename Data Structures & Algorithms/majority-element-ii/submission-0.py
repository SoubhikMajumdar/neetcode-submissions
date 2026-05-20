class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        n = len(nums)
        n/=3
        result = []
        for num in nums:
            freq[num] = freq.get(num,0)+1
            if freq[num] > n and num not in result:
                result.append(num)
        return result


        