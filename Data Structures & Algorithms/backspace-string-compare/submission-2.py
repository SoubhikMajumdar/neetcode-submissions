class Solution:
    def backspaceCompare(self, s, t):
        stack, stack2 = [], []
        for c in s:
            if c == '#' and stack:
                stack.pop()
            elif c != '#':
                stack.append(c)

        for c in t:
            if c == '#' and stack2:
                stack2.pop()
            elif c != '#':
                stack2.append(c)

        return stack == stack2

            

