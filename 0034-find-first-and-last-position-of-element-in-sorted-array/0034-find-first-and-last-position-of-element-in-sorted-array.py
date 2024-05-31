class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        answer = [-1, -1]

        if len(nums) < 1:
            if target in nums:
                return [0, 0]
            else:
                return [-1, -1]

        while left <= right:
            if nums[left] == target:
                answer[0] = left
                break
            left += 1

        while right >= left:
            if nums[right] == target:
                answer[1] = right
                break
            right -= 1

        return answer