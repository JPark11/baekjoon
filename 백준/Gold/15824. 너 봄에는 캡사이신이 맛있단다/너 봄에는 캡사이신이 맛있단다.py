def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    
    half = pow(a, b//2)
    return half * half % 1000000007 if b % 2 == 0 else half * half * a % 1000000007

N = int(input())
arr = list(map(int, input().split()))
arr.sort() 
 
answer = 0
 
for i in range(N):
    answer += arr[i] * (pow(2, i) - pow(2, N - i - 1))
print(answer % 1000000007)