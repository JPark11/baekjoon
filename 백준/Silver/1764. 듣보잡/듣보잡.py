# BOJ 1764 듣보잡 
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
hear = set([input().rstrip() for _ in range(N)])
see = set([input().rstrip() for _ in range(M)])

both = list(hear.intersection(see))
both.sort()
print(len(both))
for b in both: 
    print(b)