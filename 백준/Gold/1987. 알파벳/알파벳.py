import sys 
input = sys.stdin.readline


def dfs(start, visited, count):

    global max_count

    max_count = max(count, max_count)  
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    sx, sy = start[0], start[1]
    visited[ord(arr[sx][sy])-65] = 1 

    for k in range(4):
        nx = sx + dx[k]
        ny = sy + dy[k]
        if 0 <= nx < R and 0 <= ny < C: 
            if visited[ord(arr[nx][ny])-65] == 0: 
                visited[ord(arr[nx][ny])-65] = 1
                dfs((nx, ny), visited, count + 1)
                visited[ord(arr[nx][ny])-65] = 0


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

max_count = 0
visited = [0 for _ in range(26)]
dfs((0, 0), visited, 1)
print(max_count)