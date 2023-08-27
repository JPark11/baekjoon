def sol(): 
    up = 0 
    down = N-1
    total = 2*N 
    turn = 1
    robots = []

    while True:
        up = (up - 1) % total 
        down = (down - 1) % total

        for idx, robot in enumerate(robots):
            if robot != -1: 
                next_robot = (robot + 1) % total
                if next_robot not in robots and arr[next_robot] >= 1:
                    arr[next_robot] -= 1 
                    if next_robot != down:
                        robots[idx] = next_robot
                    else: 
                        robots[idx] = -1 
    
        if arr[up] != 0: 
            robots.append(up)
            arr[up] -= 1

        new_robots = [] 
        for robot in robots: 
            if robot != (down-1)%total and robot != -1:
                new_robots.append(robot)  
        
        if arr.count(0) >= K: 
            break 

        turn += 1
        robots = new_robots 
    
    return turn 
        

N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = sol() 

print(ans)
