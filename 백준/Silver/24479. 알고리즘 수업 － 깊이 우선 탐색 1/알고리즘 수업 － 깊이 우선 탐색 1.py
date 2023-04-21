import sys 
sys.setrecursionlimit(10000000)
input = sys.stdin.readline


def dfs(now, visited):
    global cnt 
    visited[now] = cnt 
    cnt += 1 
    for new in adjL[now]: 
        if visited[new]==0:
            dfs(new, visited)

    return visited  


N, M, R = map(int, input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adjL[u].append(v)
    adjL[v].append(u)

for l in adjL: 
    l.sort() 

visited = [0 for _ in range(N+1)]

cnt = 1 
ans = dfs(R, visited)

for idx in range(1, N+1): 
    print(visited[idx])