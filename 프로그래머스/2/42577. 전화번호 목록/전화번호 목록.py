def solution(phone_book):
    
    trie = dict() 
    
    for phone_num in phone_book:
        
        t = trie 
        for c in phone_num:
            if c not in t: 
                t[c] = {}
            t = t[c]
        
        t["*"] = True 
        
    prefix = True
    for phone_num in phone_book:
        
        t = trie 
        for num in phone_num: 
            t = t[num]
        if len(t) != 1:
            prefix = False
    
    return prefix
            
            
            
            
    