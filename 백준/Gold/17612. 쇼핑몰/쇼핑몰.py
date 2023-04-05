import heapq
import sys
input = sys.stdin.readline

# 고객 N명, # 계산대 K개
N, K = map(int, input().split())
cashier = []
for c_id in range(1, K+1):
    heapq.heappush(cashier, [c_id*0.0000001, c_id, []])


for idx in range(N):
    i, w = map(int, input().split())
    now = heapq.heappop(cashier)
    now[0] += w
    now[2].append((i, w))
    heapq.heappush(cashier, now)


out = []
for cash in cashier:
    c_id = ((K+1) - cash[1]) * 0.0000001
    prev = 0
    for customer in cash[2]:
        heapq.heappush(out, ((customer[1]+prev)+c_id, customer[0]))
        prev += customer[1]

total = 0
for idx in range(1, N+1):
    c_out = heapq.heappop(out)
    total += idx * c_out[1]


print(total)