class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sumsq = n
        seen = set()
        while sumsq not in seen:
            seen.add(sumsq)
            sumsq = sum(int(digit) ** 2 for digit in str(sumsq))
            if sumsq == 1:
                return True
        return False

'''
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
'''