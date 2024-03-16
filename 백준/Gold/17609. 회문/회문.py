# BOJ 17609 회문 

import sys 
input = sys.stdin.readline

N = int(input().rstrip())
for _ in range(N): 
    word = input().rstrip()
    
    if word == word[::-1]: 
        print(0)
    
    else: 

        l, r = 0, len(word)-1

        while l <= r: 
            if word[l] != word[r]:
                choice_1, choice_2 = word[l:r], word[l+1:r+1]
                if choice_1 == choice_1[::-1] or choice_2 == choice_2[::-1]: 
                    print(1)
                else: 
                    print(2)
                
                break
            
            l += 1 
            r -= 1 