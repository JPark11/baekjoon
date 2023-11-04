def solution(s):
    
    stack = [] 
    
    for p in s: 
        if p == "(": 
            stack.append(p)
        else: 
            if stack: 
                stack.pop() 
            else: 
                return False 

    return not stack