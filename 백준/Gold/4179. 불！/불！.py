# BOJ 4179 불! 
import sys 
from collections import deque 
input = sys.stdin.readline 

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

fire = deque([])
for i in range(R): 
    for j in range(C):
        if arr[i][j] == "J":  
            si, sj = i, j
            arr[i][j] = "."
        elif arr[i][j] == "F":
            fire.append((i, j))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj):
    q = deque([(si, sj, 0)])
    visited = [[0]*C for _ in range(R)]
    visited[si][sj] = 1 
    pt = -1

    if si == R-1 or sj == C-1 or si == 0 or sj == 0: 
        return 1

    while q: 
        ci, cj, ct = q.popleft() 
        if pt < ct: 
            fire_length = len(fire)
            while fire_length:
                fi, fj = fire.popleft()  
                for k in range(4): 
                    fni, fnj = fi+di[k], fj+dj[k]
                    if 0 <= fni < R and 0<= fnj < C and arr[fni][fnj] == ".":
                        arr[fni][fnj] = "F"
                        fire.append((fni, fnj))
                fire_length -= 1
            
            pt = ct 

           
        for k in range(4): 
            ni, nj = ci+di[k], cj+dj[k]
            if 0<= ni < R and 0<=nj<C and visited[ni][nj] == 0 and arr[ni][nj] == ".":
                if ni == R-1 or nj == C-1 or ni == 0 or nj == 0:
                    return ct+2
                else:
                    q.append((ni, nj, ct+1))
                    visited[ni][nj] = 1 
    return "IMPOSSIBLE"


ans = bfs(si, sj)  
print(ans)