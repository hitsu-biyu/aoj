while True:
    H, W = map(int, input().split())
    for i in range(H):
        if i == 0 or i == H - 1:
            print('#' * W)
        else:
            print('#{}#'.format('.' * (W-2)))
    print()
    if H == 0 and W == 0:
        break

# Not using: *