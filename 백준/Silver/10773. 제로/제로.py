# BOJ 10773 제로 

import sys 
input = sys.stdin.readline 

K = int(input().rstrip())
s = [] 

for _ in range(K):
    num = input().rstrip()
    if num == '0':
        s.pop()
    else:
        s.append(int(num))
    
print(sum(s))