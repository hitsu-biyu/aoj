while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == '+':
        print(a + b)
    if op == '-': # elif is also acceptable
        print(a - b)
    if op == '*':
        print(a * b)
    if op == '/':
        print(a // b)
    if op == '?':
        break
