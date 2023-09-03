N, X = map(int, input().split())
arr = list(map(int, input().split()))

freq = dict() 

cur_sum = sum(arr[:X])
if cur_sum in freq: 
    freq[cur_sum] += 1
else:
    freq[cur_sum] = 1

for i in range(1, N-X+1): 
    cur_sum = cur_sum - arr[i-1] + arr[i+X-1]
    if cur_sum in freq: 
        freq[cur_sum] += 1
    else:
        freq[cur_sum] = 1

max_freq = max(freq)
if max_freq == 0:
    print("SAD")
else:
    print(max_freq)
    print(freq[max_freq])