class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make hash table
        num_to_index = {}

        # search hash table
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
