M, N = map(int, input().split())
check = [False, False] + [True] * (N-1)
n = int(N**0.5)

for num in range(2, n+1):
    if check[num]:
        for j in range(2*num, N+1, num): 
            check[j] = False 

for num in range(M, N+1):
    if check[num]: 
        print(num) 