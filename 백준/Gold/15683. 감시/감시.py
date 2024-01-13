# BOJ 15683 감시 
import sys 
input = sys.stdin.readline

def sol(cnt):
    
    global min_no_surveillance 
    
    if cnt == len(cctv):
        checked = [[0]*M for _ in range(N)]
        for idx in range(len(cctv)):
            si, sj = cctv[idx]

            check_type = [[[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [0, 3]], [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]], [[0, 1, 2, 3]]]
            current_type = check_type[arr[si][sj]-1][directions[idx]]
            for k in current_type:
                l = 1
                while True:
                    ni, nj = si + di[k]*l, sj + dj[k]*l 
                    if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] == 6: 
                        break
                    checked[ni][nj] = 1                         
                    l += 1
        
        no_surveillance = 0 
        for n in range(N):
            for m in range(M): 
                if checked[n][m] == 0 and arr[n][m] == 0:
                    no_surveillance += 1 
        
        min_no_surveillance = min(min_no_surveillance, no_surveillance)
        return
             

    ci, cj = cctv[cnt]
    if arr[ci][cj] in [1, 3, 4]: 
        for i in range(4): 
            directions[cnt] = i 
            sol(cnt+1)
            directions[cnt] = -1 

    elif arr[ci][cj] == 2:
        for j in range(2): 
            directions[cnt] = j
            sol(cnt+1)
            directions[cnt] = -1 
    
    else:
        directions[cnt] = 0 
        sol(cnt+1)
        directions[cnt] = -1 


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctv = []
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
min_no_surveillance = N*M

for i in range(N): 
    for j in range(M): 
        if arr[i][j] in [1, 2, 3, 4, 5]:
            cctv.append((i, j))

directions = [-1] * len(cctv)
sol(0)
print(min_no_surveillance)