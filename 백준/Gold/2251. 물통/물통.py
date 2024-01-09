from collections import deque

def check(a, b, c):
    moves = []

    if a > 0 and b < B:
        new_a, new_b = max(a - (B - b), 0), min(b + a, B)
        moves.append((new_a, new_b, c))

    if a > 0 and c < C:
        new_a, new_c = max(a - (C - c), 0), min(c + a, C)
        moves.append((new_a, b, new_c))

    if b > 0 and a < A:
        new_b, new_a = max(b - (A - a), 0), min(a + b, A)
        moves.append((new_a, new_b, c))

    if b > 0 and c < C:
        new_b, new_c = max(b - (C - c), 0), min(c + b, C)
        moves.append((a, new_b, new_c))

    if c > 0 and a < A:
        new_c, new_a = max(c - (A - a), 0), min(a + c, A)
        moves.append((new_a, b, new_c))
        
    if c > 0 and b < B:
        new_c, new_b = max(c - (B - b), 0), min(b + c, B)
        moves.append((a, new_b, new_c))

    return moves
    

def bfs(start): 
    
    q = deque([start])
    visited = [start]

    while q: 
        cur_a, cur_b, cur_c = q.popleft()
        moves = check(cur_a, cur_b, cur_c)

        for move in moves: 
            if move not in visited: 
                visited.append(move)
                q.append(move)
    
    return visited

        
A, B, C = map(int, input().split())
visited = bfs((0, 0, C))
ans = []
for visit in visited: 
    if visit[0] == 0 and visit[2] not in ans: 
        ans.append(visit[2])

ans.sort() 
print(*ans)