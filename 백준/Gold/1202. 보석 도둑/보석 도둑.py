# BOJ 1202 보석도둑 

import heapq 
import sys 
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
for _ in range(N): 
    M, V = map(int, input().split())
    heapq.heappush(jewels, (M, V))

bags = [int(input().rstrip()) for _ in range(K)]
check_bags = [0] * (K)
 
bags.sort()
total_value = 0
bag_jewels = [] 
for bag in bags: 
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(bag_jewels, -jewels[0][1]) 
        heapq.heappop(jewels)
    
    if bag_jewels: 
        total_value += -heapq.heappop(bag_jewels)
        
print(total_value)