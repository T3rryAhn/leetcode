class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1

        answer = 0

        while left < right:
            answer = max(answer, (right - left) * min(height[right], height[left]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return answer