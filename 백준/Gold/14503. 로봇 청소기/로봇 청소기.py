N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cleaned = [[0 for _ in range(M)] for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

ci, cj, cd = r, c, d 
count = 0 
while True:
    if cleaned[ci][cj] == 0:
        cleaned[ci][cj] = 1
        count += 1 
    flag = False 
    for k in range(4): 
        ni, nj = ci + di[k], cj+dj[k]
        if 0<= ni < N and 0 <= nj < M: 
            if arr[ni][nj] == 0 and cleaned[ni][nj] == 0: 
                flag = True 
    if flag:
        for _ in range(4): 
            cd = (cd -1) % 4
            if arr[ci+di[cd]][cj+dj[cd]] == 0 and cleaned[ci+di[cd]][cj+dj[cd]] == 0: 
                ci = ci+di[cd]
                cj = cj+dj[cd]
                break 

    else:
        if arr[ci-di[cd]][cj-dj[cd]] == 0: 
            ci, cj =  ci-di[cd], cj-dj[cd]
        else: 
            break 

print(count)