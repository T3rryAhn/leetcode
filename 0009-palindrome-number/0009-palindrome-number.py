class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x != 0 and not x % 10):
            return False

        origin_x = x
        reverse = 0

        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //=10
        
        return x == reverse or x == reverse // 10