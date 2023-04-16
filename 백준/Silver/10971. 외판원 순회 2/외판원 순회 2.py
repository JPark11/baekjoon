def sol(cnt, total, prev, start):
    global min_total
    if total >= min_total: 
        return  
    if cnt == N-1:
        if arr[prev][start]:
            total += arr[prev][start]
            min_total = min(min_total, total)
        return 
    else:
        for k in range(N):
            if arr[prev][k] > 0 and visited[k] == 0:
                visited[k] = 1  
                sol(cnt+1, total+arr[prev][k], k, start)
                visited[k] = 0  


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_total = 100000000
visited = [0 for _ in range(N)]
for k in range(N):
    visited[k] = 1
    sol(0, 0, k, k)
    visited[k] = 0 
print(min_total)