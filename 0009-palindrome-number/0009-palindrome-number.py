class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_list = []

        if x < 0:
            return False
        
        while x > 0:
            num_list.append(x % 10)
            x //= 10

        for i in range(len(num_list) // 2):
            if num_list[i] != num_list[-(1 + i)]:
                return False
        return True