class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {}

        for p in paths:
            dic[p[0]] = p[1]

        target = dic[paths[0][0]]

        while True:
            if target in dic:
                target = dic[target]
            else:
                return target