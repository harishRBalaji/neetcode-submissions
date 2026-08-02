class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        is_pre_req = [set() for _ in range(numCourses)]

        for pre, course in prerequisites:
            adj_list[pre].add(course)
            indegree[course] += 1            
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            for neighbor in adj_list[course]:
                is_pre_req[neighbor].add(course)
                is_pre_req[neighbor].update(is_pre_req[course])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        result = []
        for pre, course in queries:
            if pre in is_pre_req[course]:
                result.append(True)
            else:
                result.append(False)
        
        return result

        