N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(N)] for _ in range(N)]

visited[0][0] = 1 

for i in range(N): 
    for j in range(N):
        if visited[i][j] != 0 and arr[i][j]!=0: 
            d = arr[i][j]
            if i+d < N: 
                visited[i+d][j] += visited[i][j]
            if j+d < N:
                visited[i][j+d] += visited[i][j]



print(visited[N-1][N-1]) 