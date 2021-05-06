while True:
    s = input()
    a, b = map(int, s.split())
    if a > b:
        a, b = b, a
    if a == b == 0:
        break
    print(a, b)
    