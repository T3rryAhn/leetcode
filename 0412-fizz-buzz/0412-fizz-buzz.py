class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1, n + 1)]

        for i in range(1, n + 1):
            entry = ""
            if i % 3 == 0:
                entry += "Fizz"
            if i % 5 == 0:
                entry += "Buzz"
            if entry != "":
                answer[i - 1] = entry

        return answer