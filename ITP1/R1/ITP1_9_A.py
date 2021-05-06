W = input()
text = []
count = 0
while True:
    T = input()
    if T == 'END_OF_TEXT':
        break
    text += T.lower().split()
for i in text:
    if W == i:
        count += 1
print(count)


