# BOJ 11399 ATM 

N = int(input())
nums = list(map(int, input().split()))

nums.sort() 

total = 0 
for idx, num in enumerate(nums): 
    total += num * (len(nums)-idx)

print(total)