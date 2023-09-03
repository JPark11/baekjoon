def sol(k, parents):
    parents[k] = -2 

    for i, p in enumerate(parents): 
        if p == k: 
            sol(i, parents)

    return parents
    

N = int(input())
parents = list(map(int, input().split()))
X = int(input())

parents= sol(X, parents)

ans = 0
for i in range(N): 
    if parents[i] != -2 and i not in parents: 
        ans += 1 

print(ans)