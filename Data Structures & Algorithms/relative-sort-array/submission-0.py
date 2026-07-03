class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = dict()
        for num in arr1:
            count[num] = count.get(num, 0) + 1

        res = []
        for num in arr2:
            res += [num] * count.pop(num)

        for num in sorted(count):
            res += [num] * count[num]

        return res