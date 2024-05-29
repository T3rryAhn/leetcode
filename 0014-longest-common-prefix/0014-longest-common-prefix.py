class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word1 = min(strs)
        word2 = max(strs)
        common = ""
        for i in range(min(len(word1), len(word2))):
            if word1[i] == word2[i]:
                common += word1[i]
            else:
                break
        return common
