# BOJ 2573 빙산 
import sys 
input = sys.stdin.readline
from collections import deque 


def bfs(si, sj):
    
    q = deque([(si, sj)])
    visited[si][sj] = 1 

    while q: 
        ci, cj = q.popleft() 
        for k in range(4): 
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if arr[ni][nj] > 0:  
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                elif arr[ni][nj] == 0:
                    count[ci][cj] += 1  
    
    return 1
                    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]
melt_time = 0

while True: 
    visited = [[0]*M for _ in range(N)]
    count = [[0]*M for _ in range(N)]
    icebergs = 0 
 
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and visited[i][j] == 0:
                icebergs += bfs(i, j)
    if icebergs > 1:
        print(melt_time)
        break
    if icebergs == 0:
        print(0)
        break

    melt_time += 1
    for i in range(N): 
        for j in range(M):
            arr[i][j] = max(arr[i][j]-count[i][j], 0)
