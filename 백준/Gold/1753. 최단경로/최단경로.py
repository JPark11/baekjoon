# BOJ 1753 최단경로
import heapq 
import sys 
input = sys.stdin.readline  

def dijkstra(start):
    heap = [] 
    heapq.heappush(heap, [0, start])
     
    
    weights = [INF] * (V+1)
    weights[start] = 0

    while heap: 
        weight, node = heapq.heappop(heap)
        if weight > weights[node]: 
            continue 
        
        for v, w in graph[node]: 
            if w + weight < weights[v]: 
                weights[v] = w + weight 
                heapq.heappush(heap, [w + weight, v])
        
    return weights 
          

V, E = map(int, input().split())
start = int(input().rstrip())
graph = [[] for _ in range(V+1)]
for _ in range(E): 
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
INF = float('inf')
weights = dijkstra(start)

for idx in range(1, V+1): 
    if weights[idx] == INF: 
        print('INF')
    else:
        print(weights[idx]) 