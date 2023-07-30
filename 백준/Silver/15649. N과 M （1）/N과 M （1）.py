# BOJ 15649 N과M (1)

def sol(cnt, check, ans):

    if cnt == M:
        for a in ans: 
            print(a, end=' ')
        print()
        return
        

    for idx in range(1, N+1):
        if check[idx] == 0:
            check[idx] = 1 
            sol(cnt+1, check, ans+[idx])
            check[idx] = 0
         


N, M = map(int, input().split())
check = [0] * (N+1)

sol(0, check, [])