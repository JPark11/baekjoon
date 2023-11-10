# BOJ 1966 프린터 큐
from collections import deque  
import sys 
input = sys.stdin.readline


T = int(input().rstrip())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    imp = [0] * 10
    q_list = [] 
    for idx, doc in enumerate(docs):
        q_list.append((idx, doc))
        imp[doc] += 1 
        

    q = deque(q_list)
    cnt = 0
    while q: 
        idx, doc = q.popleft() 
        for i in range(doc+1, 10):
            if imp[i] > 0: 
                q.append((idx, doc))
                break 
        else:
            cnt += 1 
            imp[doc] -= 1 
            if idx == M: 
                break 
  
    print(cnt)