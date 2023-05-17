# BOJ 9205 맥주 마시면서 걸어가기 
from collections import deque 

def bfs(start):
    q = deque([start])
    visited[start] = 1 

    while q:
        idx = q.popleft()
        for n_idx in adjL[idx]: 
            if visited[n_idx] == 0: 
                q.append(n_idx)
                visited[n_idx] = 1 
                if n_idx == N+1: 
                    return True 

    return False 


        
     
     



T = int(input())

for tc in range(1, T + 1): 
    N = int(input())
    store  = [] 
    for idx in range(N + 2): 
        i, j = map(int, input().split())
        store.append((idx, i, j))
    si, sj = store[0][1], store[0][2]
    gi, gj = store[-1][1], store[-1][2]

    adjL = [[] for _ in range(N+2)] 
    visited = [0 for _ in range(N+2)]

    for i in range(N+1): 
        for j in range(i+1, N+2):
            if abs(store[i][1] - store[j][1]) + abs(store[i][2]-store[j][2]) <= 1000: 
                adjL[i].append(j)
                adjL[j].append(i)
    
             
    res = bfs(0)

    if res: 
        print('happy')
    else:
        print('sad')

  


         