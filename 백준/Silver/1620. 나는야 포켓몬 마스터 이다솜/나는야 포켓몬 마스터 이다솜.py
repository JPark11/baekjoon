# BOJ 1620 나는야 포켓몬 마스터 이다솜 
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
po2num = dict()
num2po = ['']
for idx in range(1, N+1): 
    po = input().rstrip()
    num2po.append(po)
    po2num[po] = idx 

for _ in range(M): 
    find = input().rstrip()
    if find.isnumeric():
        print(num2po[int(find)]) 
    else: 
        print(po2num[find])