from collections import defaultdict
def solution(participant, completion):
    part_num = defaultdict(int)
    for name in participant:
        part_num[name] += 1 
    
    for name in completion: 
        part_num[name] -= 1 
    
    for name in part_num: 
        if part_num[name] != 0: 
            return name
        