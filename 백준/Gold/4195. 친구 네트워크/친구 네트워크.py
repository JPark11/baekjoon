import sys
input = sys.stdin.readline

def get_direc(person, idx, parent):
    global cnt
    if person in direc:
        num = direc[person]
    else:
        direc[person] = idx
        parent.append(idx)
        cnt.append(1)
        num = idx
        idx += 1
    return num, idx, parent


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x >= y:
        parent[x] = y
        cnt[y], cnt[x] = cnt[x]+cnt[y], 0
    else:
        parent[y] = x
        cnt[x], cnt[y] = cnt[x] + cnt[y], 0


T = int(input())
for tc in range(1, T+1):
    direc = dict()
    d = 0
    parent = []
    cnt = []
    N = int(input())
    for _ in range(N):
        person_a, person_b = input().split()
        a, d, parent = get_direc(person_a, d, parent)
        b, d, parent = get_direc(person_b, d, parent)
        if find_parent(a) != find_parent(b):
            union(a, b)
        print(cnt[find_parent(a)])