# print(input().swapcase())
s = input()
for ch in s:
    if ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch.lower(), end='')
print()
