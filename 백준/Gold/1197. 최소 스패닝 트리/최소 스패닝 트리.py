def find_parent(v): 
    if v!=parent[v]: 
        parent[v] = find_parent(parent[v])
    return parent[v]


def union(a, b): 
    a = find_parent(a)
    b = find_parent(b)
    if a >= b: 
        parent[a] = b
    else: 
        parent[b] = a



V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c,a,b)) 
edges.sort() 

parent = [i for i in range(V+1)]

total = 0
cnt = 0 
for edge in edges: 
    c, a, b = edge 
    if find_parent(a) != find_parent(b):
        union(a, b)
        total += c 
        cnt += 1 
        if cnt == V-1: 
            break 

print(total)