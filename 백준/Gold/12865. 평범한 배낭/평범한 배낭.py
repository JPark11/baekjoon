import sys 
input = sys.stdin.readline 

N, K = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)] 
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = things[i-1] 
    for j in range(1, K+1):
        if W > j: 
            dp[i][j] = dp[i-1][j]
        else: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V)

print(dp[-1][-1]) 