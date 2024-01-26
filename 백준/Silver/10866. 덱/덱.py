# BOJ 10866 덱 
import sys
from collections import deque 
input = sys.stdin.readline

def sol(op, deq): 
    if "push_front" in op:
        deq.appendleft(int(op.split()[1])) 
    elif "push_back" in op: 
        deq.append(int(op.split()[1]))
    elif op == "pop_front":
        if len(deq): 
            print(deq.popleft()) 
        else:
            print(-1)
    elif op == "pop_back":
        if len(deq): 
          print(deq.pop())
        else: 
            print(-1)
    elif op == "size": 
        print(len(deq))
    elif op == "empty": 
        print(int(len(deq)==0))
    elif op == "front": 
        if len(deq): 
            print(deq[0])
        else: 
            print(-1)
    elif op == "back": 
        if len(deq):
            print(deq[-1])
        else: 
            print(-1)
    


N = int(input().rstrip())
deq = deque([])

for _ in range(N): 
    operation = input().rstrip()
    sol(operation, deq)