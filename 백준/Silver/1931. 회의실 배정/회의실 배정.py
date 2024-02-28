# BOJ 1931 회의실 배정 

import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
times = [list(map(int, input().split())) for _ in range(N)]

times.sort(key=lambda x: (x[1], x[0]))

total = 1 
cur = times[0]

for idx in range(1, len(times)):
    if cur[1] <= times[idx][0]: 
        cur = times[idx]
        total+= 1 

print(total)