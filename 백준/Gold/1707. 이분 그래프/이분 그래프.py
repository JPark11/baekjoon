from collections import deque 
import sys 
input = sys.stdin.readline 

def bfs(start):
    global visited
    q = deque([start])
    visited[start] = 1 

    while q: 
        cur = q.popleft() 
        for next_ in adjL[cur]: 
            if visited[next_] == 0:
                if visited[cur] == 1: 
                    visited[next_] = 2
                elif visited[cur] == 2:
                    visited[next_] = 1
                q.append(next_) 
            elif visited[next_] == visited[cur]:
                return "NO"

    return "YES" 
                 
    


T = int(input().rstrip())
for tc in range(1, T + 1): 
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    for _ in range(E): 
        u, v = map(int, input().split())
        adjL[u].append(v)
        adjL[v].append(u)
    
    visited = [0] * (V+1) 
    
    for i in range(1, V+1): 
        if visited[i] == 0: 
            result = bfs(i)
            if result == 'NO':
                print(result)
                break 
    else: 
        print("YES")