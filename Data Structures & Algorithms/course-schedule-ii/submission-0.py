class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            indegree[prerequisite] += 1
            adj_list[course].append(prerequisite)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        output = []
        finish = 0
        while q:
            course = q.popleft()
            output.append(course)
            finish += 1
            for neighbor in adj_list[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if finish != numCourses:
            return []
        return output[::-1]
        
# [1,2,0]
# [0,1,2]


        