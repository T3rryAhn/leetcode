class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            sum = target
            sum -= num
            for j in range(i + 1, len(nums)):
                if sum == nums[j]:
                    return [i, j]

        