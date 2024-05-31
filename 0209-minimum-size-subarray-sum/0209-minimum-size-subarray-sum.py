class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        answer = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                answer = min(answer, right - left + 1)
                total -= nums[left]
                left += 1

        return answer if answer != float('inf') else 0


            
