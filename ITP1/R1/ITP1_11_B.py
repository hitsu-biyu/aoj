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
upfront_to_right = {}
for d in (d1, d2, d3, d4, d5, d6):
    for _ in range(4):
        l = d.labels
        upfront_to_right[l[0], l[1]] = l[2]
        d.roll('E')
q = int(input())
for _ in range(q):
    up, front = map(int, input().split())
    print(upfront_to_right[up, front])