def InsertionSort(A, N):
    for i in range(N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print(' '.join(map(str, A)))

N = int(input())
A = list(map(int, input().split()))
InsertionSort(A, N)