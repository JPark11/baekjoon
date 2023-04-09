import sys
input = sys.stdin.readline

def binary(arr, M):
    l = 0 
    r = max(arr)
    res = 0 
    while l <= r: 
        mid = (l + r) // 2 
        wood = 0 
        for item in arr:
            if item > mid: 
                wood += (item-mid) 
        if wood == M: 
            return mid
        
        elif wood > M:
            res = mid
            l = mid + 1 
        else: 
            r = mid - 1 
    return res  



N, M = map(int, input().split())
trees = list(map(int, input().split()))
ans = binary(trees, M)
print(ans)