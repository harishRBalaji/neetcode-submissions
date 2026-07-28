class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        difference_dict = defaultdict(int)

        for source, destination in trust:
            difference_dict[source] -= 1
            difference_dict[destination] += 1
        
        for i in range(1, n + 1):
            if difference_dict[i] == n - 1:
                return i
        return -1