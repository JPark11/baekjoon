# BOJ 14499 주사위굴리기 
import sys 
input = sys.stdin.readline

def move_dice(d): 
    if d == 1: 
        dice[2], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[2]
    elif d == 2: 
        dice[2], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[2], dice[3]
    elif d == 3: 
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    elif d == 4:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]


N, M, x, y, K  = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice = [0] * 6

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cx, cy = x, y

for command in commands:
    nx, ny = cx + dx[command-1], cy + dy[command-1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M: 
        continue 
    move_dice(command)
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[3]
    else:
        dice[3] = arr[nx][ny]
        arr[nx][ny] = 0
    cx, cy = nx, ny
    print(dice[2])