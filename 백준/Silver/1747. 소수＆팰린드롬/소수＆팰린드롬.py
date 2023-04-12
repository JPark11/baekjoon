import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False


N = int(input())

x = N

if x == 1: 
    x += 1

while True:
    if is_prime(x) and is_palindrome(x):
        ans = x
        break
    x += 1

print(ans)