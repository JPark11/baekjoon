# BOJ 11403 경로 찾기 

N = int(input())
adjL = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if adjL[i][j] == 1 or (adjL[i][k] == 1 and adjL[k][j] == 1):
                adjL[i][j] = 1 

for row in adjL:
    for r in row:
        print(r, end=" ")
    print()