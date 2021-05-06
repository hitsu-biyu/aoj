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

    def all_patterns(self):
        labels = self.labels
        d1 = Dice(labels).roll('S')
        d2 = Dice(labels)
        d3 = Dice(labels).roll('W').roll('S')
        d4 = Dice(labels).roll('E').roll('S')
        d5 = Dice(labels).roll('S').roll('S')
        d6 = Dice(labels).roll('N')
        d_all = []
        for d in (d1, d2, d3, d4, d5, d6):
            for _ in range(4):
                l = d.labels
                d_all.append(l)
                d.roll('E')
        return d_all




n = int(input())
dices = [Dice(list(map(int, input().split()))) for _ in range(n)]
found = False
for i in range(n - 1):
    if found:
        break
    patterns = dices[i].all_patterns()
    for j in range(i + 1, n):
        if dices[j].labels in patterns:
            print('No')
            found = True
            break
if not found:
    print('Yes')