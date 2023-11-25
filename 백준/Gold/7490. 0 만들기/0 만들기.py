import sys
input = sys.stdin.readline 

def sol(num, prev, eq, cal, sign):
    if num == N:
        if sign == "+": 
            res = cal+num 
        elif sign == "-":
            res = cal-num 
        else: 
            res = cal-prev+int(str(prev)+str(num))
        # print(eq+str(num), res)
        if res == 0:
            ans.append(eq+str(num))
        return
    

    next_nums = int("123456789"[num-1: N])
    if (cal > 0 and cal - next_nums > 0) or (cal < 0 and cal + next_nums < 0):
        return


    for choice in " +-": 
        new_eq = str(num) + choice
        if sign == "+": 
            sol(num+1, num, eq + new_eq, cal+num, choice)
        elif sign == "-": 
            sol(num+1, -1*num, eq + new_eq, cal-num, choice)
        else:
            cur = int(str(prev)+str(num))
            sol(num+1, cur, eq + new_eq, cal-prev+cur, choice) 
         


T = int(input())

for tc in range(1, T + 1): 
    N = int(input())

    nums = "123456789"[:N]
    choice = "+- "

    ans = [] 
    sol(1, 0, "", 0, "+")
    for ans_eq in ans: 
        print(ans_eq)

    print()