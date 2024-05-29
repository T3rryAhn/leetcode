class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]

        for i in range(0, len(strs)):
            j = 0
            temp_common = ""

            if common == "":
                return common

            while strs[i] != "" and common[j] == strs[i][j]:
                temp_common += common[j]
                if j + 1 < len(strs[i]) and j + 1< len(common):
                    j += 1
                else:
                    break
                
            common = temp_common
        return common