class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        answer = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                top =  stack.pop()
                if not stack:
                    break

                length = i - stack[-1] - 1
                answer += length * (min(height[stack[-1]], h) - height[top])
            stack.append(i)
        return answer
