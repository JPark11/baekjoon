# 14502 연구소

from collections import deque
import sys 
import copy 
input = sys.stdin.readline 

def find_viruses(arr):
    viruses = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                viruses.append((i, j))
    return viruses


def count_clean(arr):
    clean = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                clean += 1
    return clean


def transmission(v, tmp):
    si, sj = v
    q = deque([(si, sj)])
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < N and 0 <= nj < M and tmp[ni][nj] == 0:
                tmp[ni][nj] = 2
                q.append((ni, nj))
    
    return tmp


def test_walls(arr, walls, viruses):

    global result

    if walls == 3:
        
        tmp = copy.deepcopy(arr)

        for virus in viruses:
            tmp = transmission(virus, tmp)
        clean = count_clean(tmp)
        result = max(clean, result)
        return 

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                test_walls(arr, walls+1, viruses)
                arr[i][j] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

viruses = find_viruses(arr)
test_walls(arr, 0, viruses)
print(result)