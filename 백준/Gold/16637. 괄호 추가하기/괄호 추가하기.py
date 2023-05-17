# BOJ 16637 괄호 추가하기

def cal(num1, num2, op): 
    if op == '+': 
        return num1 + num2 
    elif op == '-': 
        return num1 - num2 
    elif op == '*': 
        return num1 * num2  
    

def choose(idx, prev): 
    global result 
    if idx >= N: 
        result = max(result, prev)
        return 
    if idx + 3 < N: 
        choose(idx + 4, cal(prev, cal(int(exp[idx+1]), int(exp[idx+3]), exp[idx+2]), exp[idx]))
    choose(idx + 2, cal(prev, int(exp[idx+1]), exp[idx]))



N = int(input())
exp = list(input())
result = -9**10

if N == 1: 
    print(exp[0])
else:
    choose(1, int(exp[0]))
    print(result)
    