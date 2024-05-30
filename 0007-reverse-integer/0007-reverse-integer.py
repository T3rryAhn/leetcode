class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        answer = 0

        if x < 0:
            is_negative = True
            x *= -1

        while x > 0:
            answer = answer * 10 + x % 10
            x //= 10
        
        if answer > 2 ** 31:
            answer = 0
        if is_negative:
            answer *= -1

        return answer