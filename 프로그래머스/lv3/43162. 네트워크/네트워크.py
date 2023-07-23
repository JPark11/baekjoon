from collections import deque 

def bfs(start, visited, computers, n):
    q = deque([start])
    visited[start] = 1 
    
    while q: 
        cur = q.popleft()
        for i in range(n): 
            if computers[cur][i] == 1 and visited[i] == 0: 
                q.append(i)
                visited[i] = 1
    return visited
    


def solution(n, computers):
    
    visited = [0] * n
    answer = 0
    
    for comp in range(n): 
        if visited[comp] == 0:
            visited =  bfs(comp, visited, computers, n)
            answer += 1 
    
            
    
    return answer