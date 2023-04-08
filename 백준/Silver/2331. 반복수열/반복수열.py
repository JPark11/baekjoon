A, P = map(int, input().split())

check = {A: 1}
count = 2 
prev = A 

while True:
    cur = 0 
    while prev > 0: 
        cur += (prev % 10) ** P 
        prev //= 10 

    if cur not in check:
        check[cur] = count 
        count += 1 
    else: 
        count_end = check[cur]
        break 
    prev = cur 

print(count_end-1)