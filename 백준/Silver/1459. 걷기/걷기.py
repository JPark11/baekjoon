# BOJ 1459 걷기 

X, Y, W, S = map(int, input().split())

if S >= 2 * W: 
    print((X+Y)*W) 
elif W <= S < 2 * W: 
    print(min(X, Y)*S + abs(X-Y)*W)
else: 
    print(min(X, Y)*S + abs(X-Y)//2*2*S + abs(X-Y)%2*W)