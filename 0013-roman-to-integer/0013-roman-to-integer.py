class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        prev = 0
        for c in s:
            curr = roman_to_integer[c]
            if curr > prev:
                result += curr - 2 * prev
            else:
                result += curr
            prev = curr
        return result


roman_to_integer = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000
}