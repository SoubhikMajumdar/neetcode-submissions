class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            return sum(int(x) ** 2 for x in str(number))

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1
