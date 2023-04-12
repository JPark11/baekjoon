
def select(cx, cy, cnt, total):
    global prob

    if cnt == N:
        prob += total 
        return

    else:
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                select(nx, ny, cnt+1, total*direc[d]*0.01)
                visited[nx][ny] = 0


N, east, west, south, north = map(int, input().split())
visited = [[0 for _ in range(29)] for _ in range(29)]
direc = [east, west, south, north]
visited[14][14] = 1
prob = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
select(14, 14, 0, 1)

print(prob)