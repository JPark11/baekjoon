from itertools import permutations

def solution(picks, minerals):
    
    mat = {'dia': {'diamond': 1, 'iron': 1, 'stone': 1},
           'iron': {'diamond': 5, 'iron': 1, 'stone': 1},
          'stone': {'diamond': 25, 'iron': 5, 'stone': 1}}
    
    pick_list = ['dia']*picks[0] + ['iron']*picks[1] + ['stone']*picks[2]
    
    mineral_list = [minerals[5*i:5*i+5] for i in range(len(minerals))][:len(pick_list)]
    mineral_list.sort(key=lambda x: (x.count("diamond"), x.count("iron"), x.count("stone")), reverse=True)
    
    fatigue = 0 
    
    for i, pick in enumerate(pick_list):
        for mineral in mineral_list[i]:
            fatigue += mat[pick][mineral]
    
    return fatigue 

        