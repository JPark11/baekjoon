import sys 
input = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x >= y:
        parent[x] = y
    else:
        parent[y] = x

N, M = map(int, input().split())
school = input().split()
school = ['X'] + school
edges = []
parent = [i for i in range(N+1)]
for _ in range(M):
    u, v, d = map(int, input().split())
    edges.append([d, u, v])

edges.sort()

total = 0
cnt = 0
for edge in edges:
    e, u, v = edge
    if find_parent(u) != find_parent(v):
        if school[u] != school[v]:
            union(u, v)
            total += e
            cnt += 1
    if cnt == N-1:
        break

if cnt < N-1:
    print(-1)
else:
    print(total)