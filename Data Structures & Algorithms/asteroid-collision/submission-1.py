class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        I: asteroids - List of integers
        O: list of integer(s) - final state of the asteroids
        C:
            2 <= asteroids.length <= 10,000.
            -1000 <= asteroids[i] <= 1000
            asteroids[i] != 0
        E: 1 asteroid
            all asteroids in the same direction
        Plan:
        1. for each asteroid in asteroids array:
            1.1 if empty, push to stack
            1.2 else
                1.2.1 compare the last element in the stack with the current:
                    1.2.1.1 if stack[-1] is of opposite sign to current:
                        if abs(stack[-1]) == abs(current):
                            stack.pop()
                        elif abs(stack[-1]) > abs(current):
                            continue
                        else:
                            stack.pop()
                            stack.append(current)
                    1.2.1.2 else, stack.append(current)

        2. return stack
        '''
        def check_same_sign(a, b):
            if a > 0 and b > 0:
                return True
            elif a < 0 and b < 0:
                return True
            else:
                return False
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = stack[-1] + asteroid
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    asteroid = 0
                else:
                    asteroid = 0
                    stack.pop()
            if asteroid:
                stack.append(asteroid)
        return stack
                

