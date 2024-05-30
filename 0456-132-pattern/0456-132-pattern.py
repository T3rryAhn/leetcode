class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # s1 s3 s2

        s3_stack = []
        s2 = -10 ** 10

        for s1 in reversed(nums):
            if s1 < s2:
                return True
            
            while s3_stack and s3_stack[-1] < s1:
                s2 = s3_stack.pop()
            s3_stack.append(s1)
        return False