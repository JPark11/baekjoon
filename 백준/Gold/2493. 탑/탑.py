N = int(input())
nums = list(map(int, input().split()))
tmp = []
res = [0 for _ in range(N)]

for idx in range(N-1, -1, -1):
    while tmp: 
        if tmp[-1][0] < nums[idx]:
            res[tmp[-1][1]] = idx+1 
            tmp.pop()
        else:
            break 

    tmp.append((nums[idx], idx))

print(*res)