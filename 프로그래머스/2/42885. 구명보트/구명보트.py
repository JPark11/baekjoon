def solution(people, limit):
    
    people.sort(reverse=True)
    
    boats = 0
    i, j = 0, len(people)-1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1 
            j -= 1 
        else: 
            i += 1
        boats += 1 
    
    return boats