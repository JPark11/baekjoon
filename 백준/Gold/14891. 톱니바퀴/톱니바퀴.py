# BOJ 14891 톱니바퀴 
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, direction):
    q = deque([(start, direction)])
    visited = [0 for _ in range(4)]
    visited[start] = direction 

    while q: 
        cur_cog, cur_dir = q.popleft()
        for k in [-1, 1]:
            next_cog = cur_cog + k
            if 0 <= next_cog < 4 and visited[next_cog] == 0:
                if (k == -1 and cogs[cur_cog][6]+cogs[next_cog][2] == 1) or (k==1 and cogs[cur_cog][2]+cogs[next_cog][6] == 1):
                    q.append((next_cog, -1*cur_dir))
                    visited[next_cog] = -1*cur_dir  
       
    return visited

cogs = [list(map(int, input().rstrip())) for _ in range(4)]
K = int(input().rstrip())
for _ in range(K):
    cog_num, cog_dir = map(int, input().split())
    visited = bfs(cog_num-1, cog_dir)
    for cur_cog, cur_dir in enumerate(visited): 
        if cur_dir == 1: 
            cogs[cur_cog] = [cogs[cur_cog][-1]] + cogs[cur_cog][:-1]
        elif cur_dir == -1:
            cogs[cur_cog] = cogs[cur_cog][1:] + [cogs[cur_cog][0]]

score = cogs[0][0] + cogs[1][0]*2 + cogs[2][0]*4 + cogs[3][0]*8

print(score)
        