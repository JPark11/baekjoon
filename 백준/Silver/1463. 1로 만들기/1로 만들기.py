from collections import deque 

def bfs(start): 
    q = deque([start])

    while q: 
        cur = q.popleft()

        if cur == 1:
            return 0

        for i in range(3): 
            if i == 0 and cur % 3 == 0: 
                next_num = cur // 3 
            elif i == 1 and cur % 2 == 0:
                next_num = cur // 2
            else: 
                next_num = cur - 1

            if next_num == 1: 
                return check[cur] + 1 
            
            if check[next_num] == 0: 
                check[next_num] = check[cur] + 1 
                q.append(next_num)

    return -1 

N = int(input())
check = [0] * (N+1)
ans = bfs(N)
print(ans)