# BOJ 3967 매직스타 

def check_sum():
    lines = [[(1, 1), (1, 3), (1, 5), (1, 7)],
             [(3, 1), (3, 3), (3, 5), (3, 7)],
             [(0, 4), (1, 3), (2, 2), (3, 1)],
             [(0, 4), (1, 5), (2, 6), (3, 7)],
             [(4, 4), (3, 3), (2, 2), (1, 1)], 
             [(4, 4), (3, 5), (2, 6), (1, 7)]]
    
    for line in lines:
        total = 0
        completed = True 
        for a, b in line: 
            if arr[a][b] == "x": 
                completed = False 
                break
            total += ord(arr[a][b]) - 64 
        
        if completed: 
            if total != 26: 
                return False 
    
    return True 
            

def sol(cnt):
    
    if not check_sum():
        return
    
    if cnt == len(check_space):
        ans = ''.join([''.join(line) for line in arr])
        res.append(ans)
        return 
            
    cx, cy = check_space[cnt]
    for i in range(1, 13):
        if check_num[i-1] == 0: 
            check_num[i-1] = 1
            arr[cx][cy] = chr(i+64) 
            sol(cnt+1)
            check_num[i-1] = 0
            arr[cx][cy] = "x"
    

arr = [list(input()) for _ in range(5)]
check_num = [0] * 12
check_space = []
res = []

for i in range(5):
    for j in range(9): 
        if arr[i][j] in "ABCDEFGHIJKL":
            check_num[ord(arr[i][j])-65] = 1 
        elif arr[i][j] == "x": 
            check_space.append((i, j))

sol(0)
res.sort()
for i in range(5):
    print(res[0][9*i:9*i+9])