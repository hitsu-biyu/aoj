n = int(input())
tp = 0
hp = 0
for i in range (n):
    t, h = input().split()
    if t == h:
        tp += 1
        hp += 1
    elif t > h:
        tp += 3
    else:
        hp += 3
print(tp, hp)
