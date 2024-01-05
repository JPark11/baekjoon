# BoJ 1436 영화감독 숌 

N = int(input())
num = 666 
idx = 1 

while idx <= 10000:
    if "666" in str(num): 
        if idx == N: 
            print(num)
            break
        else:
            idx += 1 
    num += 1 