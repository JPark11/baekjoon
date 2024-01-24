
N = int(input())
nums = [int(input()) for _ in range(N)]

check = [0] * (N+1)
stack = [0] * N  
ops = []
top = -1 
no = False 


for num in nums:
    if top == -1 or stack[top] < num:
        
        if top == -1: 
            cur = 1
        else: 
            cur = stack[top] + 1

        while cur < num+1:
            
            if check[cur] == 0:
                top += 1  
                stack[top] = cur
                check[cur] = 1 
                ops.append("+")
            cur += 1 

        stack[top] = 0 
        top -= 1 
        ops.append("-")
        

    elif stack[top] == num:
        stack[top] = 0 
        top -= 1 
        ops.append("-")
    
    else: 
        no = True 
        break 
         
if no: 
    print("NO")
else: 
    for op in ops: 
        print(op) 