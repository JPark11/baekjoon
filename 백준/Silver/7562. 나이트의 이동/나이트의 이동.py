# BOJ 7562 나이트의 이동 
from collections import deque
import sys 
input = sys.stdin.readline

def bfs(start):

    q = deque([start])
    visited = [[0]*l for _ in range(l)]
    visited[start[0]][start[1]] = 1 
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1] 

    if start[0] == x and start[1] == y:
        return 0

    while q: 
        cx, cy = q.popleft() 
        for k in range(8):
            nx = cx + dx[k]
            ny = cy + dy[k] 
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                if nx == x and ny == y: 
                    return visited[cx][cy]
                visited[nx][ny] = visited[cx][cy] + 1 
                q.append((nx, ny))

    return -1  
                 

T = int(input())
for tc in range(1, T + 1): 
    l = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())

    num_of_moves = bfs((a, b))
    
    print(num_of_moves)
