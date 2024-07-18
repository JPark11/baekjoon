def solution(a, b):
    
    prod = 0
    
    for i in range(len(a)):
        prod += a[i] * b[i]
        
    return prod