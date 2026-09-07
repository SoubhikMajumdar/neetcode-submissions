class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            # add element at idx i

            subset.append(nums[i])
            dfs(i+1, subset)

            # exclude that same element idx i  
            subset.pop()
            dfs(i+1, subset)

        dfs(0,[])

        return res