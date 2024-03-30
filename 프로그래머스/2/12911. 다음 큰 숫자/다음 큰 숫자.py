def solution(n):
    ones = bin(n).count('1')
    while True: 
        n += 1
        if bin(n).count('1') == ones:
            return n
        
    
    
    
    