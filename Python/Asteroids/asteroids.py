from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroid_stack = list()
        for asteroid in asteroids:
            asteroid_stack.append(asteroid)
            # print(f' before: {asteroid_stack}')

            while len(asteroid_stack) >= 2 and self.willCollide(asteroid_stack[-2], asteroid_stack[-1]):
                # print(f'Gets to here')
                curr_ast = asteroid_stack.pop(-1)
                asteroid_stack[-1] = self.handleCollision(
                    asteroid_stack[-1], curr_ast)

            if asteroid_stack[-1] == 0:
                asteroid_stack.pop(-1)

            # print(f' after {asteroid_stack}')

        return asteroid_stack

    def willCollide(self, num1: int, num2: int) -> bool:
        return (num1 > 0 and num2 < 0)

    def handleCollision(self, num1: int, num2: int) -> int:
        if abs(num1) > abs(num2):
            return num1
        elif abs(num2) > abs(num1):
            return num2
        else:
            return 0
