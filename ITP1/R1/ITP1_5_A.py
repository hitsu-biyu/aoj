while True:
    H, W = map(int, input().split())
    for i in range(H):
        print('#' * W)
    print()
    if H == 0 and W == 0:
        break

# Not using "*":
