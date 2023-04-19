import heapq 

def bfs(start):
    q = []
    heapq.heappush(q, (0,start))
    visited[start] = 0 

    while q: 
        now_t, now = heapq.heappop(q)
        if now == K:
            return now_t 

        for k in range(3):
            if k == 0: 
                new = 2 * now 
                new_t = now_t 
            elif k == 1: 
                new = now + 1 
                new_t = now_t + 1 
            else: 
                new = now - 1 
                new_t = now_t + 1 

            if 0 <= new < 100001 and visited[new] == -1: 
                visited[new] = new_t 
                heapq.heappush(q, (new_t, new))
    return -1 
        

N, K = map(int, input().split())
visited = [-1 for _ in range(100001)]
res = bfs(N)
print(res)