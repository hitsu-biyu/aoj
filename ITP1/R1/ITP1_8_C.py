c = 'abcdefghijklmnopqrstuvwxyz'
s = ''
while True:
    try:
        s += input().lower()
    except EOFError:
        break
for ch in c:
    print(f'{ch} : {s.count(ch)}')


# c = 'abcdefghijklmnopqrstuvwxyz'
# s = input().lower()
# for ch in c:
#     print(f'{ch} : {s.count(ch)}')