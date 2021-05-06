n, m, l = map(int, input().split())
A = []
B = []
C = [[0]*l for _ in range(n)]
for i in range(n):
    A.append([int(x) for x in input().split()])
for j in range(m):
    B.append([int(y) for y in input().split()])
for i in range(n):
    for j in range(m):
        for k in range(l):
            C[i][k] += A[i][j] * B[j][k]
for i in range(n):
    print(' '.join(map(str, C[i])))