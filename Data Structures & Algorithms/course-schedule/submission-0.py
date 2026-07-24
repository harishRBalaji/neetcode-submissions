class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prerequisites = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            course_to_prerequisites[c].append(p)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if course_to_prerequisites[course] == []:
                return True
            
            visiting.add(course)
            for pre in course_to_prerequisites[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            course_to_prerequisites[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True