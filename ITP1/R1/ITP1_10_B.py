import math


a, b, C = map(float, input().split())
r = math.radians(C)
h = b * math.sin(r)
S = a * h * 0.5
L = a + b + math.sqrt(h**2 + (a - b * math.cos(r))**2)
print(S)
print(L)
print(h)
