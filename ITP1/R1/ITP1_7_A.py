
while True:
    m, f, r = map(int, input().split())
    total = m + f
    if m == -1 and f == -1 and r == -1:
        break
    elif m == -1 or f == -1:
        print('F')
    elif total >= 80:
        print('A')
    elif 65 <= total < 80:
        print('B')
    elif 50 <= total < 65:
        print('C')
    elif 30 <= total < 50:
        if r >= 50:
            print('C')
        else:
            print('D')
    else:
        print('F')

