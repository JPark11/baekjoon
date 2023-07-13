# 1717 집합의 표현 
import sys 
input = sys.stdin.readline

def find(x):
    if parent[x] != x: 
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(y)] = find(x)

    

N, M = map(int, input().split())
parent = [ n for n in range(N+1)]

for _ in range(M):
    raw_input = list(map(int, input().split()))
    s, a, b = raw_input  
    if s == 0: 
        union(a, b)
    if s == 1: 
        if find(a) == find(b): 
            print("yes")
        else:
            print("no")