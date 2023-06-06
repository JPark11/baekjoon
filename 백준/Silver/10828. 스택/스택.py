import sys 
input = sys.stdin.readline

N = int(input().rstrip())
s = []

for _ in range(N): 
    raw = input().rstrip()
    if raw[:4] == 'push': 
        push_num = raw.split()[1]
        s.append(push_num)
    elif raw == 'pop': 
        if s:
            print(s.pop())
        else:
            print(-1)
    elif raw == 'size':
        print(len(s))
    elif raw == 'empty':
        res = 0 if s else 1
        print(res)
    elif raw == 'top':
        if s:
            print(s[-1])
        else:
            print(-1)