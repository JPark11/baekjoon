# BOJ 2839 설탕 배달 

N = int(input())

a = N // 3 + 1 
b = N // 5 + 1 
min_num = 5000

for i in range(a+1):
    for j in range(b+1): 
        if i*3 + j*5 == N:
            min_num = min(min_num, i+j) 

if min_num == 5000: 
    print(-1)
else: 
    print(min_num)