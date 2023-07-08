def cal(ilist, jlist):
    maxsum = 0  

    for i in range(N): 
        for j in range(M):
            tempsum = 0 
            for k in range(4):
                ni = i + ilist[k]
                nj = j + jlist[k]

                if 0 <= ni < N and 0 <= nj < M:
                    tempsum += arr[ni][nj] 
                
                else: 
                    break
            
            if tempsum > maxsum: 
                maxsum = tempsum 
    
    return maxsum 

def cal_set(ilist, jlist):
     return max(cal(ilist, jlist), cal(jlist, ilist))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ai = [0, 0, 0, 0]
aj = [0, 1, 2, 3]

bi = [0, 0, 1, 1]
bj = [0, 1, 0, 1]

ci1 = [0, 0, 0, 1]
cj1 = [0, 1, 2, 1]

ci2 = [0, 1, 2, 1]
cj2 = [1, 1, 1, 0]

di1 = [0, 1, 1, 2]
dj1 = [0, 0, 1, 1]

di2 = [0, 0, 1, 1]
dj2 = [1, 2, 0, 1]

ei1 = [0, 1, 2, 2]
ej1 = [0, 0, 0, 1]

ei2 = [0, 0, 0, 1]
ej2 = [0, 1, 2, 0]

ei3 = [0, 1, 2, 0]
ej3 = [1, 1, 1, 0]

ei4 = [1, 1, 1, 0]
ej4 = [0, 1, 2, 2]

test = [(ai, aj), (bi, bj), (ci1, cj1), (ci2, cj2), (di1, dj1), (di2, dj2),
        (ei1, ej1), (ei2, ej2), (ei3, ej3), (ei4, ej4)]

ans = 0 

for ti, tj in test: 
    ans = max(ans, cal_set(ti, tj))

print(ans)