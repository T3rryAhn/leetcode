class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        selections = []
        if len(s) == 1:
            return 1
        for c in s:
            while c in selections:
                length = max(length, len(selections))
                selections.pop(0)
            selections.append(c)
        length = max(length, len(selections))
        return length