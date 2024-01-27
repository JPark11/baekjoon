# BOJ 1158 요세푸스 문제 

N, K = map(int, input().split())
nums = [n for n in range(1, N+1)]

idx = 0
ans = []
while nums:
    idx = (idx+K-1)%len(nums)
    ans.append(str(nums.pop(idx)))

ans = ', '.join(ans)
print("<"+ans+">")