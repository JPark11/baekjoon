# BOJ 1744 수 묶기 

import sys 
input = sys.stdin.readline 

N = int(input().rstrip())

pos = [] 
neg = [] 
for _ in range(N):
    num_input = int(input().rstrip()) 
    if num_input > 0 : 
        pos.append(num_input)
    else: 
        neg.append(num_input)

pos.sort(reverse=True)
neg.sort()

def add_nums(nums):
    idx = 0
    total = 0 
    while idx < len(nums):
        if idx < len(nums)-1 and nums[idx] * nums[idx+1] > nums[idx] + nums[idx+1]:
            total += (nums[idx] * nums[idx+1])
            idx += 2  
        else:
            total += nums[idx] 
            idx += 1 
    
    return total 
    
print(add_nums(pos) + add_nums(neg))