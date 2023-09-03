import heapq
import sys


input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start): 
    q = [] 
    heapq.heappush(q, (0, start))
    distance = [INF] * (N+1)

    while q: 
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue 
        
        for i in graph[now]: 
            cost = dist + i[1]

            if cost < distance[i[0]]: 
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))
    
    return distance


N, M, X = map(int, input().split()) 
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

ans = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if i == X: 
        distance = dijkstra(i)
        for j in range(1, N+1): 
            ans[j] += distance[j]
    
    else: 
        distance = dijkstra(i)
        ans[i] += distance[X]

print(max(ans))