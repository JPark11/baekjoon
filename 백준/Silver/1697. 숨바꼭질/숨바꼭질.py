from collections import deque 

def bfs(start): 
    q = deque([start])
    loc[start] = 1 
    if start == K: 
        return 0
    while q: 
        now = q.popleft()
        for k in range(3):
            if k == 0: 
                new = now - 1 
            elif k == 1: 
                new = now + 1 
            else:
                new = now * 2 
            if 0 <= new < 100001 and loc[new] == 0:
                if new == K: 
                    return loc[now]
                loc[new] = loc[now] + 1
                q.append(new) 
    return -1  


N, K = map(int, input().split())
loc = [0 for _ in range(100001)]
res = bfs(N)
print(res)