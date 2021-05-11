n = int(input())
R = []
for i in range(n):
    R.append(int(input()))
minv = R[0]
maxv = -(10**9)
for j in range(1, n):
    maxv = max(maxv,R[j]-minv)
    minv = min(minv, R[j])
print(maxv)
