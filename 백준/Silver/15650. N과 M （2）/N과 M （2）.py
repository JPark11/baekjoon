def sol(cur, cnt, nums):
    if cnt == M: 
        print(*nums)
        return 

    if cur > N: 
        return

    sol(cur+1, cnt+1, nums + [cur])
    sol(cur+1, cnt, nums)
         

N, M = map(int, input().split())
sol(1, 0, [])