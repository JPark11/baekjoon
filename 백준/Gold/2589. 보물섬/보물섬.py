# BOJ 2589 보물섬
from collections import deque

def bfs(si, sj):
    q = deque([(si, sj)])
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    visited = [[0]*M for _ in range(N)]
    visited[si][sj] = 1
    cnt = 1  

    while q:
        ci, cj = q.popleft()
        for k in range(4): 
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == "L": 
                visited[ni][nj] = visited[ci][cj] + 1 
                cnt = visited[ni][nj]
                q.append((ni, nj))
        
    return cnt - 1
    

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

max_dist = 0
for i in range(N): 
    for j in range(M): 
        if arr[i][j] == "L": 
            dist = bfs(i, j)
            max_dist = max(max_dist, dist)

print(max_dist)