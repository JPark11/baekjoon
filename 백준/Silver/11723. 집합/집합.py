# BOJ 11723 집합 
import sys 
input = sys.stdin.readline

M = int(input())
nums = 0 
for _ in range(M): 
    op = input().rstrip()
    if op == "all": 
        nums = 2**21 - 1 
    elif op == "empty": 
        nums = 0
    else: 
        o, x = op.split()
        if o == "add": 
            nums |= (1 << int(x))
        elif o == "remove": 
            nums &= ~(1<<int(x))
        elif o == "check":
            if nums & (1 << int(x)): 
                print(1)
            else: 
                print(0) 
        elif o == "toggle": 
            if nums & (1 << int(x)): 
                nums &= ~(1<<int(x))
            else: 
                nums |= (1 << int(x))