class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def addOne(digits, i):
            if i == 0 and digits[i] == 9:
                digits[i] = 0
                arr = [1]
                arr.extend(digits)
                return arr

            if digits[i] < 9:
                digits[i] += 1
                return digits

            if digits[i] == 9:
                digits[i] = 0
                return addOne(digits, i - 1)

        return addOne(digits, len(digits) - 1)