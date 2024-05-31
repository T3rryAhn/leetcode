class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_hash_table = {}
        sum_table = []
        count = 0

        temp_sum = 0
        for i, num in enumerate(nums):
            temp_sum += num
            sum_table.append(temp_sum)
            if temp_sum in sum_hash_table:
                continue
            sum_hash_table[temp_sum] = i


        print(sum_hash_table)
        print(sum_table)
        for i, e in enumerate(sum_table):
            # if e < k:
            #     continue
            if e == k:
                count += 1
            key = e - k
            if key in sum_hash_table and sum_hash_table[key] < i:
                count += 1
                
        return count