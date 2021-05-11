n = int(input())
res = []
for i in range(n):
    l = [int(i) for i in input().split()]
    if l[0] == 0:
        res.append(l[1])
    elif l[0] == 1:
        print(res[l[1]])
    elif l[0] == 2:
        res.pop()