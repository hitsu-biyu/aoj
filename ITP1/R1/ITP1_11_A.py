class Dice:
    def __init__(self, labels) -> None:
        self.labels = labels
    
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

labels = list(map(int, input().split()))
op_list = list(input())
dice = Dice(labels)
for op in op_list:
    dice.roll(op)
print(dice.labels[0])