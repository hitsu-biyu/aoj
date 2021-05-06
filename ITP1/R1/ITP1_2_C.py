l: str = input()
a, b, c = map(int, l.split())
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(a, b, c)


# s = input()
# l = list(map(int, s.split()))
# l.sort()
# print(' '.join(str(i) for i in l))