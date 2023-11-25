import sys 
input = sys.stdin.readline 

def dfs(cur, visited):

    if visited == (1 << N) -1:
        if arr[cur][0] != 0: 
            return arr[cur][0]
        else: 
            return int(1e9) 
        
    if (cur, visited) in dp:
        return dp[(cur, visited)]
    
    min_cost = int(1e9)
    for next_ in range(1, N): 
        if visited & (1 << next_) or arr[cur][next_] == 0:
            continue 

        cost = dfs(next_, visited | (1<<next_)) + arr[cur][next_]
        if min_cost > cost: 
            min_cost = cost 
    
    dp[(cur, visited)] = min_cost 
    return min_cost 
   
        
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = {}
res = dfs(0, 1)
print(res) 