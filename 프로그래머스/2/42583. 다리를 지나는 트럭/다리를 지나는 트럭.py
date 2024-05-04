from collections import deque 

def solution(bridge_length, weight, truck_weights):
    
    q = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    
    t = 0  
    total_weight = 0 
    
    while q:
        t += 1
        w = bridge.popleft() 
        total_weight -= w 
        
        if total_weight + q[0] <= weight:
            truck = q.popleft() 
            bridge.append(truck)
            total_weight += truck
        else: 
            bridge.append(0)
    
    t += bridge_length
    
    return t
        
            
            
        
        