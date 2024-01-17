# BOJ 2636 
import sys
from collections import deque 

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
melt_time = 0 


def bfs(si, sj):
    q = deque([(si, sj)]) 
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni, nj = ci+di[k], cj+dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj]==0 and air[ni][nj] == 0: 
                    q.append((ni, nj))
                    air[ni][nj] = 1
                elif arr[ni][nj] == 1:
                    melt[ni][nj] = 1 
     
                                            
while True:
    cheese_count = 0
    melt_count = 0
    air = [[0]*M for _ in range(N)]
    melt = [[0]*M for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    bfs(0, 0) 

    for i in range(N):
        for j in range(M): 
            if arr[i][j] == 1: 
                cheese_count += 1 
            
            if melt[i][j] == 1: 
                arr[i][j] = 0
                melt_count += 1 

    if melt_count == cheese_count: 
        print(melt_time+1)
        print(melt_count)
        break
    
    melt_time += 1 
