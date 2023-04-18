from collections import deque 
import sys 
input = sys.stdin.readline


def bfs(si, sj): 
    q = deque([(si, sj)])
    arr[si][sj] = 0
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    while q: 
        ci, cj = q.popleft()
        for k in range(8):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == 1: 
                q.append((ni, nj))
                arr[ni][nj] = 0 


while True: 
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break 
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0 
    for i in range(h): 
        for j in range(w):
            if arr[i][j] == 1:  
                bfs(i, j)
                cnt += 1 

    print(cnt)