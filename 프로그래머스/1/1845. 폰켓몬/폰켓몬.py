from collections import defaultdict
def solution(nums):
    
    po = defaultdict(int)
    
    for num in nums:
        po[num] += 1 
    
    return min(len(po.keys()), len(nums)//2)