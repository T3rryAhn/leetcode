class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if it has loop check True
        loop = False
        def is_loop(start_idx: int, next: int):
            nonlocal loop
            visited[next] = True
            if start_idx == next:
                loop = True
                return
            for n in link[next]:
                if not visited[n]:
                    is_loop(start_idx, n)
            
        link = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            link[pre[0]].append(pre[1])
        print(link)
        
        for i, e in enumerate(link):
            visited = [False] * numCourses
            if not e:
                continue
            for s in e:
                if not visited[s]:
                    is_loop(i, s)

        return not loop
        
            