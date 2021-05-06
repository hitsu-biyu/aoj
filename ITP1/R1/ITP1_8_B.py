# while True:
#     x = input()
#     sum = 0
#     for c in x:
#         sum += int(c)
#     if x == '0':
#         break
#     print(sum)

# Not using str (only int):
while True:
    x = int(input())
    sum = 0
    if x == 0:
        break
    while x > 0:
        remainder = x % 10
        sum += remainder
        x //= 10
    print(sum)