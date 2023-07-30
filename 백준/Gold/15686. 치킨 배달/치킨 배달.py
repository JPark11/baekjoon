# BOJ 15686 치킨 배달 
import sys 
input = sys.stdin.readline 


def find(chick_num, chick_idx):

    global min_dist 

    if chick_idx > len(chickens): 
        return 

    if chick_num == M:
        total_dist = 0 
        for house in houses:
            house_dist = 10000 
            for idx, chick in enumerate(chickens): 
                if chicken_check[idx] == 1: 
                    house_dist = min(house_dist, abs(house[0]-chick[0])+abs(house[1]-chick[1]))
            
            total_dist += house_dist 
        
        min_dist = min(min_dist, total_dist)
        return
            

    chicken_check[chick_idx] = 1 
    find(chick_num + 1, chick_idx + 1)
    chicken_check[chick_idx] = 0
    find(chick_num, chick_idx + 1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

houses = [] 
chickens = []


for i in range(N): 
    for j in range(N): 
        if arr[i][j] == 1: 
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

chicken_check = [0] * (len(chickens)+1)
min_dist = 100 * 100 

find(0, 0)

print(min_dist)