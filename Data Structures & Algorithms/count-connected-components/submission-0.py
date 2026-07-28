class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for i in range(n)]
        for source, destination in edges:
            adj_list[source].append(destination)
            adj_list[destination].append(source)
    
        visit = set()
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for neighbor in adj_list[i]:
                dfs(neighbor)

        connected_components = 0
        for i in range(n):
            if i not in visit:
                connected_components += 1
                dfs(i)
        return connected_components