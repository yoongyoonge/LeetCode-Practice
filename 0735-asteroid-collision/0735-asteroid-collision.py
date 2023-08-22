class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # 문제 이해 miss...
        # 소행성이 궤도를 도는 걸로 생각했는데...
        # 소행성이 일직선 상에 있다고 생각해야한다..

        # 예제 1
        # 가장 이해가 잘되는 코드
        stack = []
        for a in asteroids:
            #print(stack)
            while stack and stack[-1] > 0 > a:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                break # this means asteroid must be destroyed (not add to stack in else statement below)
            else:
                stack.append(a)
        
        return stack