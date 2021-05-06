n, m = map(int, input().split())
A = []
b = []
for i in range(n):
    A.append([int(x) for x in input().split()])
for j in range(m):
    num = int(input())
    b.append(num)
for i in range(n):
    sum = 0
    for j in range(m):
        sum += A[i][j] * b[j]
    print(sum)
