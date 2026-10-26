class Solution:
    def backspaceCompare(self, s, t):
        stack, stack2 = [], []
        for c in s:
            if c == '#' and stack:
                stack.pop()
            elif c != '#':
                stack.append(c)
            continue

        for c in t:
            if c == '#' and stack2:
                stack2.pop()
            elif c != '#':
                stack2.append(c)
            continue

        if len(stack) == len(stack2):
            for i in range(len(stack2)):
                if stack[i] != stack2[i]:
                    return False
        else:
            return False

        return True

            

