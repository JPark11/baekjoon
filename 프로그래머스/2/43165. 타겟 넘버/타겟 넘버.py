def solution(numbers, target):
    
    def dfs(idx, total):
        
        nonlocal ans
        
        if idx == len(numbers):
            if total == target:
                ans += 1 
            return 
        
        
        for i in range(2): 
            if i == 0:
                num = numbers[idx]
            else: 
                num = numbers[idx] * (-1)
            
            dfs(idx+1, total+num)
        
    ans = 0 
    dfs(0, 0)
    return ans

            
            
        