# while True:
#     H, W = map(int, input().split())
#     for i in range(H):
#         if i % 2 != 0:
#             if W % 2 == 0:
#                 print('.#' * (W//2))
#             else:
#                 print('.#' * (W//2) + '.')
#         else:
#             if W % 2 == 0:
#                 print('#.' * (W//2))
#             else:
#                 print('#.' * (W//2) + '#')
#     print()
#     if H == 0 and W == 0:
#         break


while True:
    H, W = map(int, input().split())
    for i in range(H):
        curr = '#' if i % 2 == 0 else '.'
        for _ in range(W):
            print(curr, end='')
            curr = '#' if curr == '.' else '.'
        print()
    print()
    if H == 0 and W == 0:
        break