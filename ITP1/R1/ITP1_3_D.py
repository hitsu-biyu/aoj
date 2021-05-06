res = 0
s = input()
a, b, c = map(int, s.split())
for i in range(a, b + 1):
    if c % i == 0:
        res = res + 1 # res += 1
print(res)
