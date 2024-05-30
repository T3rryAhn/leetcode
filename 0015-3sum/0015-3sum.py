class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 투 포인터와 중복을 피하기 위해 정렬하기
        nums.sort()
        answer = []

        for i in range(len(nums)):
            # 중복된 값 피하기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 투 포인터로 풀기
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    # 중복 피하기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return answer