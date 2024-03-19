# BOJ 2212 센서 
import sys 
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
sensors = list(map(int, input().split()))

if len(sensors) == 1 or K >= N: 
    print(0)

elif K == 1: 
    print(max(sensors) - min(sensors))

else: 
    distance = [] 
    sensors.sort() 

    for idx in range(1, len(sensors)): 
        distance.append(sensors[idx] - sensors[idx-1])

    distance.sort()

    print(sum(distance[:-(K-1)]))
