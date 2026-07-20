class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0: #while stack is not emoty and top of stack and incoming asteriod are +-
                sign = a + stack[-1] #sign < 0 means stack element on top will be reomve and new asteriod takes its place
                if sign < 0:
                    stack.pop()
                elif sign == 0:
                    stack.pop()
                    a = 0 #if sign is +- then incoming asteriod will not survive
                else:
                    a = 0
            if a:
                stack.append(a)
        return stack
