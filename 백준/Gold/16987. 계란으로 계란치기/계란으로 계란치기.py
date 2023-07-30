import sys 
input = sys.stdin.readline 

def sol(cnt):
    
    global max_total
    
    if cnt == len(eggs): 
        total = sum(check)
        max_total = max(total, max_total)
        return
  
    if sum(check) >= len(eggs)-1:
        max_total = max(sum(check), max_total)
        return

    if check[cnt] == 1: 
        sol(cnt+1)
        return 
    
    for idx in range(len(eggs)):
        if idx != cnt and check[idx] == 0:
            eggs[idx][0] -= eggs[cnt][1]
            eggs[cnt][0] -= eggs[idx][1]

            if eggs[idx][0] <= 0: 
                check[idx] = 1 
            if eggs[cnt][0] <= 0:
                check[cnt] = 1
            
            sol(cnt+1)

            eggs[idx][0] += eggs[cnt][1]
            eggs[cnt][0] += eggs[idx][1]

            check[idx] = 0 
            check[cnt] = 0

N = int(input().rstrip())
eggs = []
for _ in range(N):
    s, w = map(int, input().split())
    eggs.append([s, w]) 

check = [0] * len(eggs)

max_total = 0 
sol(0)

print(max_total)