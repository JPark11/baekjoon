def solution(numbers):
    
    total = 45
    cnt = [0] * 10
    
    for number in numbers:
        if cnt[number] == 0: 
            total -= number
            cnt[number] = 1
    
    return total