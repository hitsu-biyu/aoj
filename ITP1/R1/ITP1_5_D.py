n = int(input())
l = []
for i in range(3, n + 1):
    if i % 3 == 0:
        l.append(i)
    else:
        x = i
        while x :
            if x % 10 == 3:
                l.append(i)
                break
            else:
                x //= 10
print(' '.join(str(j) for j in l))