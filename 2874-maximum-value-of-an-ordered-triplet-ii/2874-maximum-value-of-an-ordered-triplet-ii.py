class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        back = [e for e in nums]
        front = [e for e in nums]

        answer = 0
        for i in range(1, len(nums)):
            if front[i] < front[i - 1]:
                front[i] = front[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            if back[i] < back[i + 1]:
                back[i] = back[i + 1]

        for i in range(1, len(nums) - 1):
            temp_answer = (front[i - 1] - nums[i]) * back[i + 1]
            print(temp_answer)
            answer = max(answer, temp_answer)
        print(front)
        print(back)

        return answer