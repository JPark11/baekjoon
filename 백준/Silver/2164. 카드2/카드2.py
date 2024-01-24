# BOJ 2164 카드2 
from collections import deque 

N = int(input())
q = deque(list(range(1, N+1)))

while q:
    a = q.popleft()

    if len(q) == 0: 
        print(a)
        break 
    else:
        q.append(q.popleft()) 
