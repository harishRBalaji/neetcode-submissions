class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque()

        for i in range(n):
            q.append(i)
        
        time = 0
        while q:
            time += 1
            current = q.popleft()
            tickets[current] -= 1
            if tickets[current] == 0:
                if current == k:
                    return time
            else:
                q.append(current)
        return time
