import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)

        for i in range(len(points)):
            distance = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            heapq.heappush(max_heap, [-distance, points[i][0], points[i][1]])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        result = []
        while max_heap:
            distance, x, y = heapq.heappop(max_heap)
            result.append([x, y])
        return result
            


        