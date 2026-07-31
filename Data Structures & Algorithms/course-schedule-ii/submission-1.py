class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #dfs approach
        adj_list = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj_list[course].append(pre)
        
        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for pre in adj_list[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)            
            visit.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return output
        