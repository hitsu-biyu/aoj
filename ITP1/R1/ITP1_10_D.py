import math


n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
d1, d2, d3, d4 = 0, 0, 0, 0
sum_2, sum_3 = 0, 0
l = []
for i in range(n):
    abs_d = abs(x[i] - y[i])
    l.append(abs_d)
    sum_2 += abs_d**2
    sum_3 += abs_d**3
    d1 += abs_d
    d2 = math.sqrt(sum_2)
    d3 = sum_3**(1/3)
    d4 = max(l)

print(d1)
print(d2)
print(d3)
print(d4)