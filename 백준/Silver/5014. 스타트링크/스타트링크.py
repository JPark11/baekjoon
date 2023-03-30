from collections import deque


def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        c = q.popleft()
        if c == G:
            return visited[c]
        for move in [U, -1*D]:
            n = c + move
            if 1 <= n <= F and visited[n]==0:
                q.append(n)
                visited[n] = visited[c] + 1

    return -1


F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)]
res = bfs(S)
if res == -1:
    print("use the stairs")
else:
    print(res-1)