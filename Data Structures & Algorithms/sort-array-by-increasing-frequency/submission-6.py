
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # 1. Build the frequency map
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # 2. Sort the keys
        # Primary key: frequency (counts.get)
        # Secondary key: the number itself (descending) 
        # Note: LeetCode usually asks for descending order if frequencies match
        sorted_keys = sorted(counts.keys(), key=lambda x: (counts[x], -x))
        
        # 3. Build the result list
        result = []
        for key in sorted_keys:
            result.extend([key] * counts[key])
            
        return result