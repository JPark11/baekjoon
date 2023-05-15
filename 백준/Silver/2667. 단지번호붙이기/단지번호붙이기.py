from collections import deque
import sys 

input = sys.stdin.readline

def bfs(start): 
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q = deque([start])
    arr[start[0]][start[1]] = 2 
    cnt = 1 

    while q: 
        ci, cj = q.popleft()
        for k in range(4): 
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N: 
                if arr[ni][nj] == 1: 
                    cnt += 1 
                    arr[ni][nj] = arr[ci][cj] + 1 
                    q.append((ni, nj))

    return cnt 



N = int(input().rstrip())
arr = [list(map(int, input().rstrip())) for _ in range(N)]


total = 0 
nums = [] 
for i in range(N): 
    for j in range(N): 
        if arr[i][j] == 1: 
            num = bfs((i, j))
            nums.append(num)
            total += 1

nums.sort()
print(total)
for num in nums: 
    print(num) 