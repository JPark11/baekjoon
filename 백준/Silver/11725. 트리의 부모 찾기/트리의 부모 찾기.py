# BOJ 11725 트리의 부모 찾기 

from collections import deque 
import sys 
input = sys.stdin.readline 

def bfs(start): 
    
    q = deque([start])
    visited = [0 for _ in range(N+1)]
    visited[start] = 1

    while q:
        c = q.popleft()

        for n in adjL[c]: 
            if visited[n] == 0:
                visited[n] = c 
                q.append(n)

    return visited  


N = int(input().rstrip())

adjL = [[] for _ in range(N+1)]
for _ in range(N-1): 
    a, b = map(int, input().split())
    adjL[a].append(b)
    adjL[b].append(a)

parents = bfs(1)

for i in range(2, N+1): 
    print(parents[i])