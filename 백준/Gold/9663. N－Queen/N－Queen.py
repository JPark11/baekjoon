# BOJ 9663 N-Queen 
N = int(input())
arr = [0] * N 
result = 0 
visit = [False] * N 

def check(row):
    for i in range(row):
      if abs(arr[i] - arr[row]) == abs(i - row):
          return False 
    return True  
         

def sol(row): 
    global result 

    if row == N:
        result += 1 
        return

    for col in range(N):
        
        if visit[col]: 
            continue

        arr[row] = col
        if check(row):
            visit[col] = True 
            sol(row+1)
            visit[col] = False
                       

sol(0)
print(result)