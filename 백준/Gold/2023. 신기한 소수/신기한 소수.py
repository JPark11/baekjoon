import math 

def is_prime(n):
    if n < 2:
        return False 
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False 
    return True

def sol(cnt, num):
    if cnt == N: 
        if is_prime(int(num)): 
            print(num)
        return
    
    for digit in '123579':
        new_num = int(num+digit)
        if is_prime(new_num): 
            sol(cnt+1, str(new_num))
     
    
N= int(input())
sol(0, '')