
import sys 
input = sys.stdin.readline

def sol(cnt, total, sub):

    global ans
 
    if total == S:
        if sum(sub) > 0 and tuple(sub) not in sub_list:
            sub_list.add(tuple(sub))
            ans += 1 

    if cnt == N: 
        return  

    sub[cnt] = 1 
    sol(cnt+1, total+arr[cnt], sub)
    sub[cnt] = 0
    sol(cnt+1, total, sub)



N, S = map(int, input().split())
arr = list(map(int, input().split()))
sub_list = set()
ans = 0
sol(0, 0, [0]*N)
print(ans)