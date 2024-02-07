import sys 
from collections import deque 

input = sys.stdin.readline

N = int(input().rstrip())
q = deque() 
for _ in range(N):
    raw = input().rstrip()

    if raw[:4] == 'push':
        q.append(raw.split()[1])
    elif raw == 'pop':
        if q: 
            print(q.popleft())
        else:
            print(-1)
    elif raw == 'size':
        print(len(q))
    elif raw == 'empty':
        res = 0 if q else 1 
        print(res)
    elif raw == 'front':
        if q: 
            print(q[0])
        else:
            print(-1)
    elif raw == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)