from collections import deque 

def bfs(si, sj): 
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    q = deque([(si, sj)])
    while q: 
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:  # (0,0)이 방문처리되지 않으므로 (0,0) 정보를 얻고 싶으면 좀 바꿔야한다,, 
                    arr[ni][nj] = arr[ci][cj] + 1 
                    if ni == N-1 and nj == M-1:
                        return arr[ni][nj]
                    q.append((ni, nj))
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
res = bfs(0, 0)
print(res)