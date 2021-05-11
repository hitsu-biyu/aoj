x, y = map(int, input().split())
if x <= y:
    x, y = y, x
while x % y:
    x, y = y, x % y
print(y)