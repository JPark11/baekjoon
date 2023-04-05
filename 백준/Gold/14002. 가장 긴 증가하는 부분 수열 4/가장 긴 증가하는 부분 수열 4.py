N = int(input())
arr = list(map(int, input().split()))

LIS = [arr[0]]
res_l = [] # res_l 리스트에 arr 각 원소의 idx를 저장해줌 

def binary(e):  # LIS 내 위치를 찾아줘서 원소 바꿈 
    start = 0
    end = len(LIS) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

for item in arr:
    if LIS[-1] < item:
        LIS.append(item)  # item이 LIS 마지막 원소보다 크면 수열 연장 
        res_l.append((item, len(LIS)))
    else:
        idx = binary(item) 
        LIS[idx] = item # 마지막 원소가 대치되는 경우 원래보다 작은 것으로 바뀌게 된다,
        res_l.append((item, idx+1))


prev = len(LIS)
res = [] 
for idx in range(len(res_l)-1, -1, -1):
    if res_l[idx][1] == prev: 
        res.append(res_l[idx][0])
        prev -= 1 


print(len(LIS))
print(*res[::-1])