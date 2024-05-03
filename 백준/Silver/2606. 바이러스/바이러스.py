N = int(input()) 
pairs = int(input())


graph =  [[] for i in range(N)]
for i in range(pairs):
    start, end = map(int, input().split())
    graph[start - 1].append(end - 1)
    graph[end - 1].append(start - 1)

def dfs(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered: 
            discovered = dfs(w, discovered)

    return discovered 

virus = dfs(0)

print(len(virus) - 1)