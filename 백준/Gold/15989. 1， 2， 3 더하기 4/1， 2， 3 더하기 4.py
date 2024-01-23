# BOJ 15989 1, 2, 3 더하기 4 
import sys
input = sys.stdin.readline

T = int(input().rstrip())
nums = []
for tc in range(1, T + 1): 
      nums.append(int(input().rstrip())) 

max_num = max(nums)
dp = [[0, 0, 0] for _ in range(max_num + 1)] 

for i in range(1, max_num+1):
    if i == 1: 
          dp[1] = [1, 0, 0]
    elif i == 2: 
          dp[2] = [1, 1, 0]
    elif i == 3: 
          dp[3] = [2, 0, 1] 
    else: 
          dp[i] = [sum(dp[i-1]), sum(dp[i-2][1:]), dp[i-3][2]]

for num in nums: 
      print(sum(dp[num]))  