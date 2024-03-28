def solution(n, costs):
    
    parents = [i for i in range(n+1)]
    
    def find_parents(x): 
        if parents[x] != x: 
            parents[x] = find_parents(parents[x])
        return parents[x]

    
    def union(x, y):
        a = find_parents(x)
        b = find_parents(y)
        
        if a < b:
            parents[b] = a 
        else: 
            parents[a] = b
    
    
    costs.sort(key=lambda x: x[2])
    
    total_cost = 0
    
    for cost in costs: 
        i, j, edge = cost 
        if find_parents(i) != find_parents(j): 
            total_cost += edge
            union(i, j)
    
    return total_cost
            
            
        