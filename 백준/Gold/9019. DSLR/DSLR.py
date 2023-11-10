# 9019 DSLR 
from collections import deque
import sys 
input = sys.stdin.readline


def bfs(start, B):
    
    q = deque([(start, "")])
    visited = [0] * 10000
    visited[start] = 1

    while q:
        cur, letter = q.popleft() 

        if cur == B: 
            return letter 
            
        new1 = (cur * 2) % 10000
        if visited[new1] == 0: 
            visited[new1] = 1
            q.append((new1, letter + "D"))
        
        new2 = (cur - 1) % 10000 
        if visited[new2] == 0:
            visited[new2] = 1
            q.append((new2, letter + "S"))
      
        new3 = (cur % 1000) * 10 + (cur // 1000)
        if visited[new3] == 0:
            visited[new3] = 1 
            q.append((new3, letter + "L"))
        
        new4 = (cur % 10) * 1000 + (cur // 10)
        if visited[new4] == 0:
            visited[new4] = 1
            q.append((new4, letter+"R"))    
    return -1
                  

T = int(input().rstrip())
for tc in range(1, T + 1): 
    A, B = map(int, input().split())
    ans = bfs(A, B)
    print(ans)