def check_paren(paren):
    level = 0
    stack = []
    cal = [0] * len(paren)
    check = {')': '(', ']': '['}
    for p in paren:
        if p == '(':
            stack.append(p)
            level += 1
        elif p == '[':
            stack.append(p)
            level += 1
        elif p == ')':
            if stack and check[p] == stack.pop():
                if cal[level]:
                    cal[level-1] += cal[level] * 2
                else:
                    cal[level-1] += 2
                cal[level] = 0
                level -= 1
            else:
                return 0
        elif p == ']':
            if stack and check[p] == stack.pop():
                if cal[level]:
                    cal[level-1] += cal[level] * 3
                else:
                    cal[level-1] += 3
                cal[level] = 0
                level -= 1
            else:
                return 0

    if stack:
        return 0
    else:
        return cal[0]


paren = input()
print(check_paren(paren))