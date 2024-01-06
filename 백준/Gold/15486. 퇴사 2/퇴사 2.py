# BOJ 15486 퇴사2
import sys 
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
dp = [0]*(N+1)
for i in range(N): 
    T, P = map(int, input().split())
    if i + T < N + 1: 
        arr[i+T].append([i+1, P])

for j in range(1, N+1):
    dp[j] = dp[j-1]
    choices = arr[j]
    if choices: 
        for choice in choices:
            dp[j] = max(dp[choice[0] - 1] + choice[1], dp[j])
            
print(dp[-1])