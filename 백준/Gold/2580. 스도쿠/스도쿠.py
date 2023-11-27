def find_blank():
    blanks = []
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                blanks.append((i, j))
    
    return blanks


def sol(cnt):
    global done

    if cnt == len(blanks):
        done = True 
        for i in range(9): 
            print(*arr[i])
        print()
        return

    if done: 
        return   
    
    i, j = blanks[cnt]
    for k in range(1, 10):
        candidate = True 
        for num in range(9): 
            if arr[i][num] == k or arr[num][j] == k:
                candidate = False
                break   
        if candidate:          
            for p in range(3): 
                for q in range(3): 
                    if arr[i//3*3+p][j//3*3+q] == k: 
                        candidate = False
                        break 
        
        if candidate:    
            arr[i][j] = k
            sol(cnt+1)
            arr[i][j] = 0

            
arr = [list(map(int, input().split())) for _ in range(9)]
blanks = find_blank()
done = False 
ans = [] 
sol(0)