# BOJ 3055 탈출
import sys 
from collections import deque 

input = sys.stdin.readline 

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

def bfs(si, sj, water):

    q = deque([(si, sj, 0)])
    waterq = deque(water)
    visited = [[0]*C for _ in range(R)]
    visited[si][sj] = 1
    pt = -1

    while q:
        ci, cj, ct = q.popleft()
        if ct > pt:
            pt = ct

            prev_water_len = len(waterq)
            while prev_water_len: 
                wi, wj = waterq.popleft() 
                
                for k in range(4): 
                    wni, wnj = wi+di[k], wj+dj[k]
                    if 0<=wni<R and 0<=wnj<C and arr[wni][wnj] == ".":
                            waterq.append((wni, wnj))
                            arr[wni][wnj] = "*"   

                prev_water_len -= 1     
            
        for k in range(4): 
            ni, nj = ci + di[k], cj + dj[k]
            if 0<=ni<R and 0<=nj<C and visited[ni][nj] == 0: 
                if arr[ni][nj] == "D": 
                    return ct+1 
                if arr[ni][nj] == ".":
                    visited[ni][nj] = 1 
                    q.append((ni, nj, ct+1))
                      
    return 'KAKTUS'

water = []
for i in range(R): 
    for j in range(C):
        if arr[i][j] == "S": 
            si, sj = i, j
            arr[si][sj] = '.'
        elif arr[i][j] == "*": 
            water.append((i, j))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

ans = bfs(si, sj, water)
print(ans)