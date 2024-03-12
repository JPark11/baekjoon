# BOJ 2170 선 긋기 

import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
lines = []
dots = []
for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort(key=lambda x: (x[0], -x[1]))
for x, y in dots: 
    for idx in range(len(lines)): 
        if lines[idx][0] <= x <= lines[idx][1]: 
            if y > lines[idx][1]: 
                lines[idx][1] = y 
            break 
        
        if lines[idx][0] <= y <= lines[idx][1]: 
            if x < lines[idx][0]: 
                lines[idx][0] = x
            break 

    else: 
        lines.append([x, y])

total = 0
for line in lines:
    total += (line[1] - line[0])
print(total)