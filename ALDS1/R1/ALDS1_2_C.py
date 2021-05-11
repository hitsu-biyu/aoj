def BubbleSort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j][1:] < C[j-1][1:]:
                C[j], C[j-1] = C[j-1], C[j]
    print(' '.join(map(str, C)))
    
def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1:] < C[minj][1:]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    print(' '.join(map(str, C)))

N = int(input())
C = list(map(str, input().split()))
R = C[:]
BubbleSort(C, N)
print('Stable')
SelectionSort(R, N)
if C == R:
    print('Stable')
else:
    print('Not stable')


