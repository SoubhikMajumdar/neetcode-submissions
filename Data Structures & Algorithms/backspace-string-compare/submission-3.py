class Solution:
    def backspaceCompare(self, s, t):
        def postBackspace(string):
            stack = []
            for c in string:
                if c == '#' and stack:
                    stack.pop()
                elif c != '#':
                    stack.append(c)
            return stack

        return postBackspace(s) == postBackspace(t)

            

