class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            entry = ""
            if i % 3 == 0:
                entry += "Fizz"
            if i % 5 == 0:
                entry += "Buzz"
            if i % 3 and i % 5:
                entry += str(i)
            answer.append(entry)

        return answer