import sys 
input = sys.stdin.readline

def cal(a, b, sign): 
    if sign == '+': 
        return a+b 
    elif sign == '-': 
        return a-b 
    elif sign == '*': 
        return a*b
    elif sign == '/': 
        if a >= 0:
            return a // b 
        else: 
            return ((-1*a)//b) * (-1)

def sol(cnt, result, equation):
    global max_ans
    global min_ans
    
    if cnt == N:
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)
         

    for sign in signs: 
        if signs[sign] > 0:
            new_result = cal(result, nums[cnt], sign)
            signs[sign] -= 1  
            sol(cnt+1, new_result, equation+sign+str(nums[cnt]))
            signs[sign] += 1 

    
N = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
signs = {'+': plus, '-': minus, '*': multiply, '/': divide}
max_ans = -1000000000
min_ans = 1000000000
sol(1, nums[0], str(nums[0]))
print(max_ans)
print(min_ans)