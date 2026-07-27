class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque()
        time=0
        for i in range(n):
            q.append(i)
        while q:
            time+=1
            cur = q.popleft()
            tickets[cur]-=1
            
            if tickets[cur] == 0: 
                if cur == k:
                    return time
            
            if tickets[cur] > 0:
                q.append(cur)



        
