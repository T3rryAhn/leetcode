class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums) - 1):
            mid = nums[i]
            left = max(nums[:i])
            right = max(nums[i + 1:])

            result = (left - mid) * right
            
            if result > 0:
                answer = max(answer, result)
        return answer
