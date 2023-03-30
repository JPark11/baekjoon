T = int(input())

for tc in range(1, T + 1): 
    command = input()

    l = r = t = b = 0 

    cx, cy = 0, 0 

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direc = 0 

    for c in command:
        if c == "F": 
            cx += dx[direc]
            cy += dy[direc]
        elif c == "B":
            cx -= dx[direc]
            cy -= dy[direc]
        elif c == "L": 
            direc = (direc - 1) % 4 
        elif c == "R":
            direc = (direc + 1) % 4 
        
        l = min(l, cx)
        r = max(r, cx)
        b = min(b, cy)
        t = max(t, cy)
    
    print((r - l) * (t - b)) 