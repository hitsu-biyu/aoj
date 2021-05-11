import collections


n = int(input())
res = collections.deque()
for i in range(n):
    l = [int(i) for i in input().split()]
    if l[0] == 0:
        if l[1] == 1:
            res.append(l[2])
        if l[1] == 0:
            res.appendleft(l[2])
    if l[0] == 1:
        print(res[l[1]])
    if l[0] == 2:
        if l[1] == 1:
            res.pop()
        if l[1] == 0:
            res.popleft()
