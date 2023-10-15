def solution(clothes):
    
    closet = dict() 
    for cl, cltype in clothes:
        if cltype in closet:
            closet[cltype].append(cl)
        else:
            closet[cltype] = [cl]
    
    
    answer = 1 
    for clkey in closet:
        answer *= (len(closet[clkey]) + 1)
    
    return answer-1