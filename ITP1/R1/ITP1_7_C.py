r, c = map(int, input().split())
l = []
l2 = []
for i in range(r):
    l1 = [int(x) for x in input().split()]
    l1.append(sum(l1))
    l.append(l1)
for j in range(c+1):
    sum = 0
    for i in range(r):
        sum += l[i][j]
    l2.append(sum)
l.append(l2)
for i in range(r+1):
    print(' '.join(map(str, l[i])))