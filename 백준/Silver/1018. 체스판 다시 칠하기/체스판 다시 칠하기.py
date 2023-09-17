N, M = map(int ,input().split())
arr = [list(input()) for _ in range(N)]
min_count = 64

board = [["W", "B", "W", "B", "W", "B", "W", "B"], 
         ["B", "W", "B", "W", "B", "W", "B", "W"]]

for p in range(N-7):
    for q in range(M-7):
        count = 0
        for i in range(p, p+8): 
            for j in range(q, q+8):
                if i % 2 == 0: 
                    ans = board[0][j-q]
                else:
                    ans = board[1][j-q]
                if arr[i][j] != ans:
                    count += 1


        
        count = min(count, 64-count)
        min_count = min(count, min_count)

print(min_count)
