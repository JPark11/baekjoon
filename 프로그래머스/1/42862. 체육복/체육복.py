def solution(n, lost, reserve):
    
    lost.sort() 
    reserve = set(reserve)
    lent = 0 
    
    # 앞 번호 혹은 뒷 번호가 reserve에도 있고 lost에도 있을 가능성 고려 
    
    for idx, lost_stu in enumerate(lost):
        if lost_stu in reserve:
            reserve.remove(lost_stu)
            lent += 1 
            
        elif lost_stu - 1 in reserve:
            reserve.remove(lost_stu-1)
            lent += 1 

        elif lost_stu+1 in reserve and lost_stu+1 not in lost:
            reserve.remove(lost_stu+1)
            lent += 1 
    
    return n - len(lost) + lent 
