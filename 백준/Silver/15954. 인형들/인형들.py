import math

N, K = map(int, input().split())
nums = list(map(int, input().split()))

min_var = float('inf')

for i in range(K, N+1):
    for start in range(N-i+1):

        nums_now = nums[start:start+i]
        mean = sum(nums_now) / i 
        var = sum([(a-mean)**2 for a in nums_now])/ i
        if var < min_var: 
            min_var = var

print(math.sqrt(min_var))