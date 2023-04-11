# BOJ 16234 인구이동 
import sys 
from collections import deque 

input = sys.stdin.readline


def sol(arr, L, R):

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    res = []
    flag = False  
    for i in range(N):
        for j in range(N): 
            if visited[i][j] == 0:
                for k in range(4): 
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N: 
                        if L <= abs(arr[ni][nj] - arr[i][j]) <= R:   
                            start = (i, j)
                            flag = True 
                            bfs_res =  bfs(start, visited)
                            # print(bfs_res)
                            res.append(bfs_res)
                            break
    if not flag: 
        return 'end'
    return res 
  
    
    


def bfs(start, visited):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    visit_bfs = [[0 for _ in range(N)] for _ in range(N)]
    q = deque([start])
    visited[start[0]][start[1]] = 1
    visit_bfs[start[0]][start[1]] = 1 
    total =  arr[start[0]][start[1]]
    cnt = 1 

    while q: 
        ci, cj = q.popleft()
        for k in range(4): 
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N: 
                if visit_bfs[ni][nj] == 0 and L <= abs(arr[ni][nj] - arr[ci][cj]) <= R:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    visit_bfs[ni][nj] = 1 
                    total += arr[ni][nj]
                    cnt += 1  
    
    return visit_bfs, total, cnt 





N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
update = 0 

while True: 
    res = sol(arr, L, R)
    if res == 'end': 
        break
    
    for r in res: 

        visited, total, cnt = r

        newnum = total // cnt 
 

        for i in range(N): 
            for j in range(N): 
                if visited[i][j] == 1:
                    arr[i][j] = newnum
    
    update += 1 

print(update) 




