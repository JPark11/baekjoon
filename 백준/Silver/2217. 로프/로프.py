import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
weights = [int(input().rstrip()) for _ in range(N)] 

weights.sort()
weight_limit = [weights[idx]*(len(weights)-idx) for idx in range(len(weights))]
print(max(weight_limit))