n = int(input())
hand = set()
for _ in range(n):
    hand.add(input())
suits = ('S', 'H', 'C', 'D')
values = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')
for s in suits:
    for v in values:
        card = (f'{s} {v}')
        if card not in hand:
            print(card)


# num = int(input())
# hand = set()
# for _ in range(num):
#     hand.add(input())
# print('-' * 25)
# suits = ('S', 'H', 'C', 'D')
# values = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')
# for s in suits:
#     for v in values:
#         card = f'{s} {v}'
#         if card not in hand:
#             print(card)