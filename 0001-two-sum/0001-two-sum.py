class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}

        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in nums_hash:
                return [nums_hash[num2], i]
            else:
                nums_hash[num] = i
                