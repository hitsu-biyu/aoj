class Dice:
    def __init__(self, labels) -> None:
        self.labels = labels[:]
    
    def roll(self, op):
        labels = self.labels
        if op == 'E':
            self.labels = [labels[3], labels[1], labels[0], labels[5], labels[4], labels[2]]
        if op == 'W':
            self.labels = [labels[2], labels[1], labels[5], labels[0], labels[4], labels[3]]
        if op == 'N':
            self.labels = [labels[1], labels[5], labels[2], labels[3], labels[0], labels[4]]
        if op == 'S':
            self.labels = [labels[4], labels[0], labels[2], labels[3], labels[5], labels[1]]
        return self


labels = list(map(int, input().split()))
d1 = Dice(labels).roll('S')
d2 = Dice(labels)
d3 = Dice(labels).roll('W').roll('S')
d4 = Dice(labels).roll('E').roll('S')
d5 = Dice(labels).roll('S').roll('S')
d6 = Dice(labels).roll('N')
d_2 = list(map(int, input().split()))
found = False
for d in (d1, d2, d3, d4, d5, d6):
    if found:
        break
    for _ in range(4):
        l = d.labels
        if l == d_2:
            print('Yes')
            found = True
            break
        d.roll('E')

if not found:
    print('No')
    
# d_all = []
# for d in (d1, d2, d3, d4, d5, d6):
#     for _ in range(4):
#         l = d.labels
#         d_all.append(l)
#         d.roll('E')
# if d_2 in d_all:
#     print('Yes')
# else:
#     print('No')

