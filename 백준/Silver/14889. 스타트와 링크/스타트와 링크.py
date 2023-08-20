import sys 
input = sys.stdin.readline

def sol(members, cur, current_num):
    global min_diff
    if current_num == N//2:
        start_total = 0
        link_total = 0 
        for i in range(1, N):
            for j in range(i+1, N+1):
                if members[i] == members[j]: 
                    if members[i] == 1: 
                        start_total += (arr[i-1][j-1] + arr[j-1][i-1]) 
                    else: 
                        link_total += (arr[i-1][j-1] + arr[j-1][i-1])

        min_diff = min(min_diff, abs(start_total - link_total))
        
    for i in range(cur, N+1): 
        if members[i] == 0: 
            members[i] = 1 
            sol(members, i + 1, current_num + 1)
            members[i] = 0 
        

N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]
members = [0 for _ in range(N+1)]
min_diff = 40000

sol(members, 1, 0)
print(min_diff)