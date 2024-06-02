class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        max_h = 0
        answer = 0
        for h in height:
            if max_h > h:
                stack.append(h)
            else:
                while stack:
                    answer += max_h - stack.pop()
                max_h = h

        max_h = 0
        while stack:
            pop = stack.pop()
            temp = max_h - pop
            if temp < 0:
                max_h = pop
                continue
            answer += temp

        return answer
