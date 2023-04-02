N = int(input())
nums = list(map(int, input().split()))
tmp = [] 
res = [-1 for _ in range(N)]

for idx in range(N-1, -1, -1): 
    while tmp:
        if tmp[-1] > nums[idx]: 
            res[idx] = tmp[-1]
            break 
        else: 
            tmp.pop() 
    if not tmp: 
        res[idx] = -1
    tmp.append(nums[idx]) 

print(*res)