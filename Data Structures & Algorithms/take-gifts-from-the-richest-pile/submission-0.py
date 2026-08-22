import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        heapq.heapify(max_heap)

        for gift in gifts:
            heapq.heappush(max_heap, -gift)
        
        while k:
            gift = -1 * heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(math.floor(math.sqrt(gift))))
            k -= 1
        
        result = 0
        for gift in max_heap:
            result += -gift
        
        return result