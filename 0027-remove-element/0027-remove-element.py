class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            n = nums.pop(0)
            if n == val:
                k += 1
            else:
                nums.append(n)

